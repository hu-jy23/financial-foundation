#!/usr/bin/env python3
"""Cache article figures once and create local reading views."""
import concurrent.futures
import html
import io
import json
import os
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from PIL import Image

from acquire import ROOT, MANIFEST, TOPICS, article_body, original_file, sha


def get_image(url):
    try:
        request_url = 'https://' + url[7:] if url.startswith('http://') else url
        try:
            r = requests.get(request_url, timeout=(10, 25))
        except requests.ConnectionError:
            r = requests.get(request_url, timeout=(10, 25))
        r.raise_for_status()
        if b'<svg' in r.content[:1000]:
            ext = 'svg'
        else:
            im = Image.open(io.BytesIO(r.content))
            im.verify()
            ext = Image.open(io.BytesIO(r.content)).format.lower()
        ext = 'jpg' if ext == 'jpeg' else ext
        path = ROOT / 'assets' / (sha(r.content) + '.' + ext)
        path.parent.mkdir(exist_ok=True)
        if not path.exists():
            path.write_bytes(r.content)
        return url, dict(path=str(path.relative_to(ROOT)), source_url=url, resolved_url=r.url, bytes=len(r.content), sha256=sha(r.content))
    except Exception as exc:
        return url, dict(source_url=url, error=str(exc)[:180])


def main():
    data = json.loads(MANIFEST.read_text())
    all_records = []
    for r in data['resources']:
        all_records += [r] + r.get('parts', [])
    records = [r for r in all_records if r['status'] in ['downloaded', 'reused_local'] and original_file(r) and original_file(r)['path'].endswith('.html')]
    def view_path(r):
        if r['status'] == 'reused_local':
            folder = ROOT / TOPICS[r['topic']]
            folder.mkdir(exist_ok=True)
            return folder / (r['id'] + '_阅读.html')
        path = ROOT / original_file(r)['path']
        return path.with_name(path.stem + '_阅读.html')
    local_views = {}
    for r in records:
        local_views[r.get('resolved_url', r['source_url']).rstrip('/')] = view_path(r)
    bodies, urls = {}, set()
    for r in records:
        file = original_file(r)
        soup = BeautifulSoup((ROOT / file['path']).read_bytes(), 'lxml')
        for x in soup(['script', 'style', 'noscript', 'nav', 'header', 'footer']):
            x.decompose()
        body = article_body(soup)
        bodies[r['id']] = body
        for x in body.select('img[src]'):
            u = urljoin(r.get('resolved_url', r['source_url']), x['src'])
            urls.add(u)
    images = {}
    for r in records:
        for im in r.get('cached_figures', []):
            if (ROOT / im['path']).is_file():
                images[im['source_url']] = im
        old_manifest = r.get('legacy_manifest')
        if not old_manifest or not (ROOT / old_manifest).is_file():
            continue
        old = ROOT / old_manifest
        legacy = json.loads(old.read_text())
        for f in legacy.get('files', []):
            for im in f.get('images', []):
                existing = old.parent / im['file']
                if existing.is_file():
                    images[im['source_url']] = dict(path=os.path.relpath(existing, ROOT), source_url=im['source_url'], bytes=existing.stat().st_size, sha256=sha(existing.read_bytes()))
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        for url, result in pool.map(get_image, sorted(urls - images.keys())):
            images[url] = result
    count = 0
    for r in records:
        file = original_file(r)
        body = bodies[r['id']]
        txt = next((f for f in r['files'] if f['role'] == 'search_text'), None)
        if txt:
            if r['status'] == 'reused_local':
                path = view_path(r).with_suffix('.txt')
                r['files'] = [f for f in r['files'] if f['role'] != 'search_text']
                txt = {'path': str(path.relative_to(ROOT)), 'role': 'search_text'}
                r['files'].append(txt)
            else:
                path = ROOT / txt['path']
            path.write_text(body.get_text('\n', strip=True), encoding='utf-8')
            txt.update(bytes=path.stat().st_size, sha256=sha(path.read_bytes()))
            r['extracted_characters'] = len(path.read_text())
        used, failures = [], []
        for x in body.select('img[src]'):
            url = urljoin(r.get('resolved_url', r['source_url']), x['src'])
            item = images[url]
            if 'path' in item:
                x['src'] = '../' + item['path']
                x.attrs.pop('srcset', None)
                if item not in used:
                    used.append(item)
            else:
                x['src'] = url
                failures.append(item)
        for x in body.select('[href]'):
            resolved = urljoin(r.get('resolved_url', r['source_url']), x['href'])
            local = local_views.get(resolved.rstrip('/'))
            x['href'] = os.path.relpath(local, view_path(r).parent) if local else resolved
        view = view_path(r)
        toc = ''
        if r.get('parts'):
            toc = '<ul>' + ''.join('<li><a href="' + html.escape(os.path.relpath(view_path(p), view.parent), quote=True) + '">' + html.escape(p['title']) + '</a></li>' for p in r['parts']) + '</ul>'
        document = '<!doctype html><html lang="' + r['language'] + '"><meta charset="utf-8"><title>' + html.escape(r['title']) + '</title><style>body{max-width:1000px;margin:32px auto;padding:0 20px;line-height:1.8;font-family:system-ui}img{max-width:100%;height:auto}table{border-collapse:collapse;display:block;overflow:auto}td,th{border:1px solid #bbb;padding:5px}a{overflow-wrap:anywhere}</style><h1>' + html.escape(r['title']) + '</h1><p>' + html.escape(r['publisher'] + '｜' + str(r.get('published_at') or '日期待核')) + '｜<a href="' + html.escape(r['source_url'], quote=True) + '">原始入口</a></p>' + toc + str(body) + '</html>'
        view.write_text(document, encoding='utf-8')
        r['files'] = [x for x in r['files'] if x['role'] != 'offline_view'] + [dict(path=str(view.relative_to(ROOT)), role='offline_view', bytes=view.stat().st_size, sha256=sha(view.read_bytes()))]
        r['cached_figures'] = used
        r['figure_failures'] = failures
        r['figures_status'] = f'缓存{len(used)}张静态图片；{len(failures)}张未取得；交互图及引用数据待核读'
        count += len(used)
    MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'html_reading_views': len(records), 'figure_references': count, 'unique_images': sum('path' in x for x in images.values()), 'image_failures': sum('error' in x for x in images.values())}, ensure_ascii=False))


if __name__ == '__main__':
    main()
