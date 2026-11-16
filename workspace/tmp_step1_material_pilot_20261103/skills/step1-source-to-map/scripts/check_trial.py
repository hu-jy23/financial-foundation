#!/usr/bin/env python3
"""Check pilot artifact navigation and source-page coordinates, not economic correctness."""
import argparse, hashlib, json, re, subprocess
from pathlib import Path
from urllib.parse import unquote

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('trial', type=Path)
    parser.add_argument('--workspace', type=Path, help='Explicit base when evidence source.path_base is pilot_workspace')
    args = parser.parse_args()
    trial = args.trial.resolve(strict=True)
    errors, warnings, checked_claims = [], [], 0
    cache = {}
    for name in ['reading_map.md', 'change_proposal.md', 'evidence.json']:
        if not (trial / name).is_file():
            errors.append('Missing delivery: ' + name)
    evidence_path = trial / 'evidence.json'
    if evidence_path.exists():
        evidence = json.loads(evidence_path.read_text())
        claims = evidence.get('claims', []) if isinstance(evidence, dict) else evidence
        source_meta = evidence.get('source', {}) if isinstance(evidence, dict) else {}
        if not isinstance(source_meta, dict):
            source_meta = {}
        declared_base = source_meta.get('path_base')
        source_base = evidence_path.parent
        if declared_base == 'pilot_workspace':
            if args.workspace is None:
                errors.append('Evidence declares pilot_workspace; supply --workspace explicitly')
                claims = []
            else:
                source_base = args.workspace.resolve(strict=True)
        for claim in claims:
            file = claim.get('source_file')
            pages = claim.get('pdf_pages')
            if not isinstance(file, str) or not file:
                errors.append(f'Claim {claim.get("id")} needs source_file'); continue
            source = Path(file) if Path(file).is_absolute() else source_base / file
            source = source.resolve()
            if not source.is_file():
                errors.append(f'Claim {claim.get("id")} source missing: {source}'); continue
            if source not in cache:
                count = None
                if source.suffix.lower() == '.pdf':
                    info = subprocess.check_output(['pdfinfo', str(source)], text=True)
                    count = int(re.search(r'^Pages:\s*(\d+)', info, re.M)[1])
                digest = hashlib.sha256()
                with source.open('rb') as handle:
                    for block in iter(lambda: handle.read(1024 * 1024), b''):
                        digest.update(block)
                cache[source] = (count, digest.hexdigest())
            count, digest = cache[source]
            if count is not None:
                if not isinstance(pages, list) or not pages:
                    errors.append(f'Claim {claim.get("id")} needs explicit pdf_pages')
                elif any(not isinstance(p, int) or isinstance(p, bool) or not 1 <= p <= count for p in pages):
                    errors.append(f'Claim {claim.get("id")} has pages outside PDF range')
            elif not claim.get('original_locator') and not claim.get('source_lines'):
                errors.append(f'Claim {claim.get("id")} non-PDF source needs section or line locator')
            expected_hash = claim.get('source_sha256')
            if not expected_hash and file == source_meta.get('file'):
                expected_hash = source_meta.get('sha256')
            if expected_hash and expected_hash != digest:
                errors.append(f'Claim {claim.get("id")} source changed since evidence capture')
            if not (claim.get('claim_type') or claim.get('attribution') or claim.get('attribute')):
                errors.append(f'Claim {claim.get("id")} lacks attribution')
            checked_claims += 1
    for md in trial.rglob('*.md'):
        text = re.sub(r'```.*?```', '', md.read_text(), flags=re.S)
        for target in re.findall(r'!?\[[^\]\n]*\]\((<[^>\n]+>|[^)\n]+)\)', text):
            target = target.strip('<>')
            if target.startswith(('https:', 'http:', 'mailto:', 'data:')):
                continue
            path, _, anchor = target.partition('#')
            linked = (md.parent / unquote(path)).resolve() if path else md
            if not linked.exists():
                errors.append(f'Broken link in {md.relative_to(trial)}: {target}')
            elif linked.suffix == '.pdf' and anchor.startswith('page='):
                try:
                    page = int(anchor[5:])
                    info = subprocess.check_output(['pdfinfo', str(linked)], text=True)
                    count = int(re.search(r'^Pages:\s*(\d+)', info, re.M)[1])
                    if not 1 <= page <= count:
                        errors.append(f'PDF link outside source range: {target}')
                except (ValueError, TypeError):
                    errors.append('Invalid PDF page anchor: ' + target)
    result = {'trial': str(trial), 'checked_claims': checked_claims, 'checked_sources': len(cache),
              'mechanical_pass': not errors, 'errors': errors, 'warnings': warnings,
              'limitation': 'File/link/page/hash checks do not validate semantic support, reading claims or explanation quality.'}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(1 if errors else 0)

if __name__ == '__main__':
    main()
