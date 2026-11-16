#!/usr/bin/env python3
"""Download selected public originals; refresh the Step2 inventory."""
import argparse
import concurrent.futures
import hashlib
import html as html_lib
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin
from zoneinfo import ZoneInfo

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'manifest.json'
TOPICS = {
    'US': '01_美国通胀与政策预期', 'EU': '02_欧洲通胀与政策预期',
    'CN': '03_中国需求地产与化债', 'FISCAL': '04_美国财政融资与流动性',
    'JPY': '05_日元套息与去杠杆', 'GOLD': '06_黄金需求与储备',
    'TRADE': '07_贸易冲突与增长预期',
}


def article_body(soup):
    selectors = ['.TRS_Editor', '.TRS_UEDITOR', '.Custom_UnionStyle', '.detail-news', '.detail-content', '.cms-html', '#article', '.article-content', 'article', 'main', '#content']
    return next((x for x in (soup.select_one(s) for s in selectors) if x and len(x.get_text(' ', strip=True)) > 1200), soup.body or soup)


def now():
    return datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(timespec='seconds')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def original_file(record):
    return next((x for x in record.get('files', []) if x.get('role') == 'original'), None)


def fetch(record):
    record = dict(record)
    if original_file(record):
        return record
    session = requests.Session()
    errors = []
    for url in [record['source_url']] + record.get('alternatives', []):
        try:
            api_data = None
            if 'cf40.org.cn/article/' in url:
                api_url = url.replace('/article/', '/api/web/data/')
                response = session.get(api_url, headers={'Content-Type': 'application/json;charset=utf-8'}, data='{"unusekey":false}', timeout=(12, 45))
                response.raise_for_status()
                payload = response.json()
                api_data = payload['data']
                html = '<html><head><meta charset="utf-8"><title>' + html_lib.escape(api_data['title']) + '</title></head><body><article><h1>' + html_lib.escape(api_data['title']) + '</h1><p>' + html_lib.escape(str(api_data.get('author', '')) + ' ' + str(api_data.get('send_time', ''))) + '</p>' + api_data['content'] + '</article></body></html>'
                record['published_at'] = str(api_data['send_time'])[:10]
                record['title'] = api_data['title']
                record['retrieval_method'] = '网站公开前端接口，沿用公开页面请求格式'
                record['source_updated_at'] = api_data.get('updated_at')
                record['time_note'] = '保存本次取得的网页版本；发布日期不保证正文此后未修改'
                data = html.encode('utf-8')
            else:
                response = session.get(url, timeout=(12, 45))
                data = response.content
            response.raise_for_status()
            pdf = data.startswith(b'%PDF-')
            if url.lower().split('?')[0].endswith('.pdf') and not pdf:
                raise ValueError('PDF链接返回介绍页，未取得PDF正文')
            if not pdf and not any(x in response.headers.get('Content-Type', '').lower() for x in ['html', 'text', 'json']):
                raise ValueError('返回内容不是PDF或网页正文')
            stem = record['id'] + '_' + re.sub(r'[<>:"/\\|?*]', '＿', record['title'])[:75]
            folder = ROOT / TOPICS[record['topic']]
            folder.mkdir(exist_ok=True)
            if pdf:
                path = folder / (stem + '.pdf')
                path.write_bytes(data)
                info = subprocess.run(['pdfinfo', str(path)], capture_output=True, text=True)
                if info.returncode:
                    path.unlink()
                    raise ValueError('PDF结构检查失败')
                pages = re.search(r'^Pages:\s+(\d+)', info.stdout, re.M)
                text = subprocess.check_output(['pdftotext', '-layout', str(path), '-'], text=True)
                page_title = None
                record['pages'] = int(pages.group(1)) if pages else None
            else:
                if response.encoding in [None, 'ISO-8859-1']:
                    response.encoding = response.apparent_encoding
                if api_data is None:
                    html = response.text
                soup = BeautifulSoup(html, 'lxml')
                page_title = soup.title.get_text(' ', strip=True) if soup.title else ''
                for node in soup(['script', 'style', 'noscript', 'nav', 'header', 'footer', 'svg']):
                    node.decompose()
                body = article_body(soup)
                text = body.get_text('\n', strip=True)
                if re.search(r'\{\{\s*(data\.|itemTitle|documentType)', text):
                    raise ValueError('返回动态网页模板，未取得正文')
                if len(text) < record.get('minimum_characters', 650) or re.search(r'access denied|request rejected|just a moment|enable javascript and cookies', page_title, re.I):
                    raise ValueError('未取得可阅读正文：' + page_title[:100])
                if record.get('language') == 'zh' and len(re.findall(r'[\u4e00-\u9fff]', text)) < 150:
                    raise ValueError('未取得中文正文')
                path = folder / (stem + '.html')
                path.write_bytes(data)
                record['page_title'] = page_title
                record['figure_links'] = list(dict.fromkeys(urljoin(response.url, x.get('src')) for x in body.select('img[src]') if not re.search(r'logo|icon|avatar|qr|wechat', x.get('src', ''), re.I)))
                record['figures_status'] = '保留原页；图像/交互数据尚未逐图核读'
            txt = folder / (stem + '.txt')
            txt.write_text(text, encoding='utf-8')
            record['files'] = [
                {'path': str(path.relative_to(ROOT)), 'role': 'original', 'bytes': len(data), 'sha256': sha(data)},
                {'path': str(txt.relative_to(ROOT)), 'role': 'search_text', 'bytes': txt.stat().st_size, 'sha256': sha(txt.read_bytes())},
            ]
            if api_data is not None:
                raw = folder / (stem + '_公开接口原文.json')
                raw.write_bytes(response.content)
                record['files'].append({'path': str(raw.relative_to(ROOT)), 'role': 'source_response', 'bytes': raw.stat().st_size, 'sha256': sha(raw.read_bytes())})
            record['status'] = 'downloaded'
            record['resolved_url'] = response.url
            record['retrieved_at'] = now()
            record['reading_status'] = '已取得并检查文件与正文；待精读'
            record['extracted_characters'] = len(text)
            record.pop('failure', None)
            if errors:
                record['retrieval_notes'] = errors
            return record
        except Exception as exc:
            errors.append({'url': url, 'error': str(exc)[:280]})
    record['status'] = 'unavailable'
    record['failure'] = errors
    record['checked_at'] = now()
    return record


def catalog(data):
    rows = data['resources']
    available = [r for r in rows if original_file(r)]
    acquired = [r for r in rows if r['status'] == 'downloaded']
    reused = [r for r in rows if r['status'] == 'reused_local']
    data['counts'] = {'selected': len(rows), 'available_originals': len(available), 'new_downloads': len(acquired), 'reused_local': len(reused), 'unavailable': sum(r['status'] == 'unavailable' for r in rows), 'planned': sum(r['status'] == 'planned' for r in rows)}
    lines = ['# Step2实际材料目录', '', f"更新：{now()[:10]}。已取得/复用{len(available)}份材料原文；新增下载{len(acquired)}份，复用已有{len(reused)}份。HTML与检索文本计为同一份材料。", '', '每项日期采用所列发布版本；日期未知保留未核。材料已按用途初筛，待精读。共同使用的旧原件通过链接复用。报告网页、摘要与全文附件的范围分别见下表及manifest。', '']
    for code, folder in TOPICS.items():
        selected = [r for r in rows if r['topic'] == code]
        lines += ['## ' + folder[3:], '', '| ID | 日期 | 材料／作者或机构 | 用途 | 取得状态 |', '| --- | --- | --- | --- | --- |']
        for r in selected:
            file = original_file(r)
            name = r['title'].replace('|', '／')
            reading = next((x for x in r.get('files', []) if x['role'] == 'offline_view'), file)
            title = f"[{name}](<{reading['path']}>)" if reading else f"[{name}]({r['source_url']})"
            status = {'downloaded': '已下载', 'reused_local': '已有原件', 'unavailable': '未取得正文', 'planned': '待取得'}[r['status']]
            if r.get('scope_note'):
                status += '；' + r['scope_note']
            lines.append(f"| {r['id']} | {r.get('published_at') or '未核'} | {title}／{r['publisher']} | {r['purpose']} | {status} |")
        lines.append('')
    lines += ['## 已有整理内容', '']
    for r in data.get('existing_map_materials', []):
        lines.append(f"- [{r['title']}](<{r['path']}>)：{r['scope']}")
    (ROOT / 'CATALOG.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    data['updated_at'] = now()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--download', action='store_true')
    parser.add_argument('--ids', nargs='*')
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    if args.download:
        wanted = [r for r in data['resources'] if not original_file(r) and (not args.ids or r['id'] in args.ids)]
        positions = {r['id']: i for i, r in enumerate(data['resources'])}
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
            futures = {pool.submit(fetch, r): r['id'] for r in wanted}
            for future in concurrent.futures.as_completed(futures):
                record = future.result()
                data['resources'][positions[record['id']]] = record
                MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
                print(record['id'], record['status'], record.get('extracted_characters', ''), flush=True)
    catalog(data)
    MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(data['counts'], ensure_ascii=False))


if __name__ == '__main__':
    main()
