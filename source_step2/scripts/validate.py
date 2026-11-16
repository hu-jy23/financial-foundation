#!/usr/bin/env python3
"""Check the material inventory, original files, hashes and local links."""
import collections
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup

from acquire import ROOT, MANIFEST, original_file, sha, now


def main():
    data = json.loads(MANIFEST.read_text())
    records = []
    for record in data['resources']:
        records += [record] + record.get('parts', [])
    issues, checked, assets = [], set(), set()
    originals = collections.defaultdict(list)
    for r in records:
        original = original_file(r)
        if r['status'] in ['downloaded', 'reused_local'] and not original:
            issues.append([r['id'], '缺少原件'])
        if original:
            originals[original['sha256']].append(r['id'])
        entries = r.get('files', []) + r.get('cached_figures', [])
        for f in entries:
            path = ROOT / f['path']
            checked.add(str(path.resolve()))
            if not path.is_file():
                issues.append([r['id'], '文件缺失', f['path']])
            elif sha(path.read_bytes()) != f['sha256']:
                issues.append([r['id'], 'SHA256不一致', f['path']])
            if f in r.get('cached_figures', []):
                assets.add(f['path'])
            if f.get('role') == 'offline_view' and path.is_file():
                soup = BeautifulSoup(path.read_bytes(), 'lxml')
                for x in soup.select('img[src],a[href]'):
                    target = x.get('src') or x.get('href')
                    parsed = urlsplit(target)
                    if not parsed.scheme and not parsed.netloc and parsed.path:
                        target_path = path.parent / unquote(parsed.path)
                        if not target_path.exists():
                            issues.append([r['id'], '离线阅读链接失效', target])
        if r.get('parts') and r.get('parts_complete') and not all(original_file(x) for x in r['parts']):
            issues.append([r['id'], '分章完整状态不一致'])
    duplicate_originals = {k: v for k, v in originals.items() if len(v) > 1}
    for path in [ROOT/'README.md', ROOT/'LIST.md', ROOT/'CATALOG.md']:
        for target in re.findall(r'\]\(<?([^\n)>]+)>?\)', path.read_text()):
            parsed = urlsplit(target)
            if not parsed.scheme and not parsed.netloc and parsed.path and not (path.parent / unquote(parsed.path)).exists():
                issues.append([str(path.relative_to(ROOT)), 'Markdown链接失效', target])
    available = [r for r in data['resources'] if original_file(r)]
    report = dict(checked_at=now(), resources=len(data['resources']), available_originals=len(available), new_downloads=sum(r['status']=='downloaded' for r in data['resources']), reused_local=sum(r['status']=='reused_local' for r in data['resources']), unavailable=sum(r['status']=='unavailable' for r in data['resources']), report_sections=sum(len(r.get('parts',[])) for r in data['resources']), checked_files=len(checked), cached_image_files=len(assets), duplicate_originals=duplicate_originals, issue_count=len(issues), issues=issues)
    (ROOT/'validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(report, ensure_ascii=False))
    raise SystemExit(bool(issues or duplicate_originals))


if __name__ == '__main__':
    main()
