#!/usr/bin/env python3
"""Extract a local PDF reading unit while preserving one-based source-page identity."""
import argparse, hashlib, json, re, subprocess, tempfile
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--pages', required=True, help='One-based inclusive ranges, e.g. 50-72,141')
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    pdf = args.pdf.resolve(strict=True)
    info = subprocess.check_output(['pdfinfo', str(pdf)], text=True)
    page_count = int(re.search(r'^Pages:\s*(\d+)', info, re.M)[1])
    intervals, pages = [], []
    for chunk in args.pages.split(','):
        match = re.fullmatch(r'(\d+)(?:-(\d+))?', chunk.strip())
        if not match:
            parser.error('Invalid page range: ' + chunk)
        first, last = int(match[1]), int(match[2] or match[1])
        if not 1 <= first <= last <= page_count:
            parser.error(f'Range {chunk} outside PDF pages 1-{page_count}')
        intervals.append((first, last)); pages.extend(range(first, last + 1))
    if len(pages) != len(set(pages)):
        parser.error('Overlapping page ranges would duplicate reading evidence')
    if args.output.exists() and any(args.output.iterdir()):
        parser.error('Output directory must be new or empty; preserve prior runs separately')
    extracted = []
    for first, last in intervals:
        # A temporary file is read only after the subprocess has completed successfully.
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'unit.txt'
            subprocess.run(['pdftotext', '-f', str(first), '-l', str(last), '-layout', str(pdf), str(target)], check=True)
            units = target.read_text().split('\f')
            if units and not units[-1].strip():
                units.pop()
            if len(units) != last - first + 1:
                raise RuntimeError('Text page count does not match selected PDF range; inspect source')
            extracted.extend((first + offset, text) for offset, text in enumerate(units))
    digest = hashlib.sha256()
    with pdf.open('rb') as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b''):
            digest.update(block)
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'pages.txt').write_text(''.join(f'\n=== PDF页 {page} ===\n{text}\n' for page, text in extracted))
    (args.output / 'unit.json').write_text(json.dumps({
        'source_pdf': str(pdf), 'source_sha256': digest.hexdigest(),
        'pdf_total_pages': page_count, 'selected_pdf_pages': pages,
        'printed_page_mapping': 'Must be checked against rendered original; no inferred offset',
        'reading_status': 'Text extracted; not proof of complete reading or visual verification',
        'text_extraction_warnings': ['Formulae, diagrams, tables, superscripts and omitted words require source inspection'],
        'blank_or_short_text_pages': [page for page, text in extracted if len(text.strip()) < 100]
    }, ensure_ascii=False, indent=2) + '\n')
    print(f'Extracted {len(extracted)} of {page_count} PDF pages; source hash recorded.')

if __name__ == '__main__':
    main()
