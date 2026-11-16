#!/usr/bin/env python3
"""公开文章图文采集；派生HTML、Markdown、SQLite；断点续传与完整性检查。"""
import argparse
import concurrent.futures as futures
import copy
import hashlib
import html
import io
import json
import mimetypes
import re
import sqlite3
import subprocess
import threading
import time
from collections import Counter
from functools import lru_cache
from datetime import datetime
from pathlib import Path
from urllib.parse import quote, unquote, urljoin, urlparse
from zoneinfo import ZoneInfo

import requests
from bs4 import BeautifulSoup, Comment
from PIL import Image
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
MAINTENANCE = ROOT / '维护'
CATALOG = MAINTENANCE / 'selection.json'
POSTS = ROOT / 'SourcePost'
LOCAL = threading.local()
CSS = '''
:root{color-scheme:light}*{box-sizing:border-box}body{margin:0;background:#f5f4f0;color:#202428;font:17px/1.85 system-ui,"Microsoft YaHei",sans-serif}main{max-width:1000px;margin:32px auto;padding:36px 46px;background:#fff;border:1px solid #e5e3de}h1{font-size:29px;line-height:1.5}h2{font-size:23px;margin-top:2em}h3{font-size:20px}a{color:#126090;overflow-wrap:anywhere}.meta,.notice,figcaption{font-size:14px;color:#555}.meta{border-bottom:1px solid #ddd;padding-bottom:18px}.summary{background:#f4f7f9;padding:12px 20px}p{margin:1em 0}blockquote{border-left:3px solid #a5b9c6;margin:1em 0;padding:1px 18px;background:#f7f8f9}article img{display:block;max-width:100%!important;width:auto!important;height:auto!important;margin:12px auto}article section,article div,article p,article span{max-width:100%!important}article table{border-collapse:collapse;display:block;overflow-x:auto;max-width:100%}td,th{border:1px solid #ccc;padding:8px}.local-copy{font-size:12px;margin-left:5px}.missing{color:#a22;border:1px solid #a22;padding:8px}pre{overflow:auto}.asset-nav{font-size:14px;padding:12px 0;border-top:1px solid #ddd}article [id]{scroll-margin-top:12px}@media(max-width:700px){main{margin:0;padding:22px 18px;border:0}h1{font-size:24px}}@media print{body{background:#fff}main{margin:0;padding:0;border:0}.asset-nav{display:none}}
'''


def now():
    return datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(timespec='seconds')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temp.replace(path)


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


@lru_cache(maxsize=1)
def selected():
    return load(CATALOG)['articles']



@lru_cache(maxsize=1)
def directory_names():
    # 目录供人浏览；ID仅用于来源追踪、重试和重名消歧。
    replacements = str.maketrans('\\/:*?"<>|', '＼／：＊？＂＜＞｜')
    names = {}
    for item in selected():
        name = re.sub(r'[\x00-\x1f]', '', item['title']).translate(replacements).strip(' .')
        if not name:
            raise ValueError('文章缺少标题')
        suffix = f'（{item["article_id"]}）'
        if len(name.encode('utf-8')) > 230:
            while len((name + suffix).encode('utf-8')) > 240:
                name = name[:-1]
            name += suffix
        names[str(item['article_id'])] = name
    counts = Counter(n.casefold() for n in names.values())
    return {aid: name + (f'（{aid}）' if counts[name.casefold()] > 1 else '') for aid, name in names.items()}


def post_folder(article_id):
    return POSTS / directory_names()[str(article_id)]


def url_path(path):
    return quote(str(path), safe='/')

def get(url):
    if not hasattr(LOCAL, 'session'):
        LOCAL.session = requests.Session()
    error = None
    for attempt in range(3):
        try:
            r = LOCAL.session.get(url, timeout=(10, 35), headers={'Referer': 'https://wallstreetcn.com/'})
            r.raise_for_status()
            return r
        except requests.RequestException as exc:
            error = exc
            if attempt < 2:
                time.sleep(0.8 * (attempt + 1))
    raise RuntimeError(str(error))


def article_body(data):
    """extract=0通常直接含img，也兼容占位符格式；不凭images封面字段补图。"""
    body = data.get('content') or ''
    for arg in data.get('content_args') or []:
        placeholder = arg.get('placeholder')
        if not placeholder or placeholder not in body:
            continue
        if arg.get('type') == 'image' and arg.get('src'):
            attrs = {'src': arg['src'], 'alt': arg.get('alt', '')}
            body = body.replace(placeholder, '<img ' + ' '.join(f'{k}="{html.escape(str(v), quote=True)}"' for k, v in attrs.items()) + '>')
    return body


def markdown_of(soup):
    """输出轻量GFM，保留正文结构与图位；移除展示属性和派生导航。"""
    s = copy.copy(soup)
    for t in s.select('.local-copy'):
        t.decompose()
    for t in s.find_all(['script', 'style', 'noscript']):
        t.decompose()
    for t in s.find_all('a'):
        if not t.get_text(strip=True) and not t.find('img'):
            t.decompose()
    # CommonMark要求标点相邻的中文强调有明确边界，空格避免星号被显示为正文。
    for t in list(s.find_all(['strong', 'em'])):
        for nodes in [list(t.descendants), list(t.descendants)[::-1]]:
            for node in nodes:
                if isinstance(node, str) and node.strip():
                    break
                if getattr(node, 'name', None) == 'br':
                    node.unwrap()
        strings = list(t.find_all(string=lambda n: not isinstance(n, Comment)))
        if strings:
            first = strings[0]
            first.replace_with(str(first).lstrip())
            last = list(t.find_all(string=lambda n: not isinstance(n, Comment)))[-1]
            last.replace_with(str(last).rstrip())
        if t.find_parent(t.name) or not t.get_text(strip=True):
            t.unwrap()
        else:
            t.insert_before(' ')
            t.insert_after(' ')
    for t in s.find_all():
        attrs = {k: v for k, v in t.attrs.items() if k in ['href', 'src', 'alt', 'colspan', 'rowspan']}
        if t.name == 'img':
            attrs['alt'] = f"图{int(t.get('data-local-order', 0)):03d}"
        t.attrs = attrs
    for a in list(s.find_all('a')):
        if a.find('img') and a.get('href') == a.img.get('src'):
            a.unwrap()
    result = subprocess.run(['pandoc', '--from=html', '--to=gfm-raw_html', '--wrap=none'], input=str(s), text=True, capture_output=True, check=True)
    # 正文图表独占一段，相邻图题及注释继续按原顺序保留。
    text = re.sub(r'(?m)^(!\[[^\]]*\]\(assets/[^)]+\))(?=\S)', r'\1\n\n', result.stdout.replace('\\\n', '  \n'))
    return re.sub(r'\n{3,}', '\n\n', text).strip()


def markdown_issues(markdown, original):
    """使用独立的CommonMark解析器核对可见文字、图片顺序与标题。"""
    rendered = BeautifulSoup(MarkdownIt('commonmark').render(markdown), 'html.parser')
    expected = copy.copy(original)
    for t in expected.select('.local-copy'):
        t.decompose()
    issues = []
    if normalized_text(expected) != normalized_text(rendered):
        issues.append('Markdown还原正文文字不一致')
    def sequence(s):
        s = copy.copy(s)
        for t in s.find_all('img'):
            t.replace_with(f'⟪IMAGE:{t.get("src")}⟫')
        return normalized_text(s)
    if sequence(expected) != sequence(rendered):
        issues.append('Markdown图文位置不一致')
    if [t.get('src') for t in expected.find_all('img')] != [t.get('src') for t in rendered.find_all('img')]:
        issues.append('Markdown图片顺序或路径不一致')
    def headings(s):
        return [(t.name, re.sub(r'\s+', '', t.get_text())) for t in s.find_all(re.compile(r'^h[1-6]$'))]
    if headings(expected) != headings(rendered):
        issues.append('Markdown标题层级或内容不一致')
    return issues


def write_markdown(folder, soup, meta):
    body = markdown_of(soup)
    issues = markdown_issues(body, soup)
    if issues:
        raise ValueError('；'.join(issues))
    e = lambda v: html.escape(str(v or ''), quote=True)
    header_html = f'<h1>{e(meta["title"])}</h1><ul><li>页面显示时间：{e(meta["page_display_time"])}</li><li>页面署名：{e(meta["page_byline"])}</li><li>标注来源：{e(meta["source_label"] or "未单列，见正文")}</li><li>原文：<a href="{e(meta["url"])}">华尔街见闻</a></li><li>取得时间：{e(meta["acquired_at"])}</li><li><a href="article.html">HTML阅读版</a> · <a href="metadata.json">来源记录</a></li></ul>'
    if meta.get('subtitle'):
        header_html += f'<h2>导语</h2><p>{e(meta["subtitle"])}</p>'
    header = markdown_of(BeautifulSoup(header_html, 'html.parser'))
    (folder / 'article.md').write_text(header + '\n\n---\n\n' + body + '\n', encoding='utf-8')


def reformat():
    """仅重建Markdown与其引用，不请求网络，不改原件和图像。"""
    for item in selected():
        folder = post_folder(item['article_id'])
        meta = load(folder / 'metadata.json')
        doc_path = folder / 'article.html'
        doc_text = doc_path.read_text(encoding='utf-8')
        soup = BeautifulSoup(doc_text, 'html.parser').find('article')
        write_markdown(folder, soup, meta)
        doc_text = doc_text.replace('href="article.txt">检索文本</a>', 'href="article.md">Markdown正文</a>')
        doc_path.write_text(doc_text, encoding='utf-8')
        meta['files'].pop('article.txt', None)
        for name in ['article.html', 'article.md']:
            blob = (folder / name).read_bytes()
            meta['files'][name] = {'sha256': sha(blob), 'bytes': len(blob)}
        meta['markdown_updated_at'] = now()
        write_json(folder / 'metadata.json', meta)
        (folder / 'article.txt').unlink(missing_ok=True)
    build()


def normalized_text(soup):
    s = copy.copy(soup)
    for t in s.find_all(['script', 'style', 'noscript']):
        t.decompose()
    return re.sub(r'\s+', '', s.get_text())


def image_bytes(data, mime=''):
    if data.lstrip().startswith(b'<svg') or ('image/svg+xml' in mime and b'<svg' in data[:1000]):
        # 不允许SVG的脚本或外部依赖进入可用资源。
        if re.search(rb'<script|(?:href|src)\s*=\s*["\']https?://', data, re.I):
            raise ValueError('SVG含脚本或远程依赖')
        return 'svg', None, None
    with Image.open(io.BytesIO(data)) as im:
        fmt = im.format
        width, height = im.size
        im.verify()
    ext = {'JPEG': 'jpg', 'PNG': 'png', 'WEBP': 'webp', 'GIF': 'gif', 'TIFF': 'tiff', 'BMP': 'bmp', 'AVIF': 'avif'}.get(fmt)
    if not ext:
        raise ValueError(f'未知图片格式: {fmt}')
    return ext, width, height


def acquire_one(item):
    aid = str(item['article_id'])
    folder = post_folder(aid)
    folder.mkdir(parents=True, exist_ok=True)
    meta_path = folder / 'metadata.json'
    previous = load(meta_path) if meta_path.exists() else {}
    api_url = f'https://api-one.wallstcn.com/apiv1/content/articles/{aid}?extract=0'
    meta = {'article_id': int(aid), 'selection': item, 'url': item['url'], 'api_url': api_url, 'status': 'error', 'errors': [], 'acquired_at': previous.get('acquired_at') or now(), 'assets': [], 'scope': 'current public article body and inline figures; excludes platform TTS, cover, avatars, comments, and external linked works'}
    try:
        raw_path = folder / 'raw.json'
        if raw_path.exists():
            raw = raw_path.read_bytes()
        else:
            response = get(api_url)
            raw = response.content
            obj = json.loads(raw)
            if obj.get('code') != 20000 or not isinstance(obj.get('data'), dict):
                raise ValueError(f"接口未成功: {obj.get('code')} {obj.get('message', '')}")
            data = obj['data']
            if data.get('is_need_pay') or data.get('is_priced') or data.get('is_trial'):
                raise ValueError('当前访问标记为付费或试读，未保存正文')
            if len(BeautifulSoup(data.get('content', ''), 'html.parser').get_text(strip=True)) < 600:
                raise ValueError('正文过短，可能仅返回摘要')
            raw_path.write_bytes(raw)
        obj = json.loads(raw)
        data = obj['data']
        if obj.get('code') != 20000 or str(data.get('id')) != aid:
            raise ValueError('响应文章ID或状态不匹配')
        if data.get('is_need_pay') or data.get('is_priced') or data.get('is_trial'):
            raise ValueError('付费或试读正文不纳入完整采集')
        soup = BeautifulSoup(article_body(data), 'html.parser')
        body_chars = len(soup.get_text('', strip=True))
        meta.update({'title': data.get('title'), 'page_display_time': datetime.fromtimestamp(data['display_time'], ZoneInfo('Asia/Shanghai')).isoformat(), 'page_byline': (data.get('author') or {}).get('display_name'), 'source_label': data.get('source_name'), 'source_url': data.get('source_uri'), 'subtitle': data.get('content_short'), 'access_flags': {k: data.get(k) for k in ['is_need_pay', 'is_priced', 'is_trial', 'is_video']}, 'body_characters': body_chars, 'body_sha256': sha(data['content'].encode()), 'raw_sha256': sha(raw), 'raw_bytes': len(raw), 'platform_tts_url_not_downloaded': data.get('audio_uri'), 'image_occurrences': len(soup.find_all('img')), 'html_table_count': len(soup.find_all('table')), 'catalog_image_count': item.get('page_image_count'), 'catalog_text_characters': item.get('public_text_characters'), 'notes': []})
        if body_chars < item.get('public_text_characters', 0) * 0.85:
            meta['errors'].append('正文长度低于旧目录的85%，需要人工检查')
        if meta['image_occurrences'] != item.get('page_image_count'):
            meta['errors'].append(f"正文图片数与目录不一致: {meta['image_occurrences']}/{item.get('page_image_count')}")
        unresolved = re.findall(r'<!--(?:image|video|audio)[^>]*-->', str(soup))
        if unresolved:
            meta['errors'].append(f'未恢复资源占位符: {unresolved}')
        media = [str(t) for t in soup.find_all(['video', 'audio', 'iframe', 'embed', 'object', 'canvas'])]
        meta['embedded_media'] = media
        if media:
            meta['errors'].append(f'正文有{len(media)}个待处理的非静态组件')
        for t in soup.find_all(['script', 'style', 'noscript']):
            t.decompose()
        # 保存正文可见内容，去掉事件、外部样式及可触发远程请求的展示属性。
        for t in soup.find_all():
            for attr in list(t.attrs):
                if attr.lower().startswith('on') or attr.lower() in ['srcset', 'sizes', 'loading', 'data-src', 'data-original', 'data-srcset']:
                    del t[attr]
            style = t.get('style', '')
            if 'url(' in style.lower():
                meta['errors'].append(f'正文含CSS资源，需要检查: {style}')
                del t['style']
        old_assets = {a['source_url']: a for a in previous.get('assets', []) if a.get('status') == 'complete'}
        asset_by_url = {}
        for order, t in enumerate(soup.find_all('img'), 1):
            url = urljoin(item['url'], t.get('src') or '')
            record = {'order': order, 'source_url': url, 'status': 'error', 'alt': t.get('alt', ''), 'context_before': t.find_previous('p').get_text(' ', strip=True)[-400:] if t.find_previous('p') else '', 'context_after': t.find_next('p').get_text(' ', strip=True)[:400] if t.find_next('p') else ''}
            try:
                if not url.startswith(('https://', 'http://')):
                    raise ValueError(f'不支持的图像地址: {url[:100]}')
                old = old_assets.get(url)
                if old and (folder / old.get('path', '')).is_file() and sha((folder / old['path']).read_bytes()) == old['sha256']:
                    blob = (folder / old['path']).read_bytes()
                    mime = old.get('content_type', '')
                    final_url = old.get('final_url', url)
                elif url in asset_by_url:
                    a = asset_by_url[url]
                    blob = (folder / a['path']).read_bytes()
                    mime = a['content_type']
                    final_url = a['final_url']
                else:
                    r = get(url)
                    blob, mime, final_url = r.content, r.headers.get('Content-Type', ''), r.url
                ext, width, height = image_bytes(blob, mime)
                rel = asset_by_url[url]['path'] if url in asset_by_url else f'assets/figure_{order:03d}.{ext}'
                (folder / rel).parent.mkdir(parents=True, exist_ok=True)
                if not (folder / rel).exists() or sha((folder / rel).read_bytes()) != sha(blob):
                    (folder / rel).write_bytes(blob)
                record.update({'status': 'complete', 'path': rel, 'sha256': sha(blob), 'bytes': len(blob), 'width': width, 'height': height, 'content_type': mime or mimetypes.guess_type(rel)[0], 'final_url': final_url})
                asset_by_url[url] = record
                t['src'] = rel
                t['data-source-url'] = url
                t['data-local-order'] = str(order)
                t['id'] = f'figure-{order:03d}'
                for k in ['width', 'height']:
                    t.attrs.pop(k, None)
                # 单击原图查看，已有链接不改其正文含义。
                if not t.find_parent('a'):
                    a = soup.new_tag('a', href=rel)
                    a['title'] = f'查看图{order:03d}完整尺寸'
                    t.wrap(a)
            except Exception as exc:
                record['error'] = str(exc)
                meta['errors'].append(f'图{order:03d}: {exc}')
                t['alt'] = f"[未取得图{order:03d}] {t.get('alt', '')}"
            meta['assets'].append(record)
        # 移除可加载的未知媒体；原始代码和URL完整记录在metadata及raw中。
        for t in soup.find_all(['video', 'audio', 'iframe', 'embed', 'object', 'canvas']):
            marker = soup.new_tag('p', attrs={'class': 'missing'})
            marker.string = '正文媒体未取得，原始嵌入信息见metadata.json。'
            t.replace_with(marker)
        for order, t in enumerate(soup.find_all(['p', 'h2', 'h3', 'h4', 'li', 'table']), 1):
            if not t.get('id'):
                t['id'] = f'block-{order:04d}'
        known = {str(a['article_id']) for a in selected()}
        links = []
        for a in list(soup.find_all('a', href=True)):
            href = a['href']
            if href.startswith(('assets/', '#')):
                continue
            absolute = urljoin(item['url'], href)
            if not absolute.startswith(('https://', 'http://', 'mailto:')):
                a.attrs.pop('href', None)
                continue
            a['href'] = absolute
            links.append({'text': a.get_text(' ', strip=True), 'url': absolute})
            match = re.fullmatch(r'https?://(?:www\.)?wallstreetcn.com/articles/(\d+)(?:[?#].*)?', absolute)
            if match and match[1] in known:
                local = soup.new_tag('a', href=url_path(f'../{directory_names()[match[1]]}/article.html'), attrs={'class': 'local-copy'})
                local.string = '[本地]'
                a.insert_after(local)
        meta['external_links'] = links
        # 链接补充文字不属于原文正文比较范围。
        comp = copy.copy(soup)
        for a in comp.select('.local-copy'):
            a.decompose()
        original = BeautifulSoup(article_body(data), 'html.parser')
        if not media and normalized_text(original) != normalized_text(comp):
            meta['errors'].append('离线版可见正文与原始正文不一致')
        meta['status'] = 'complete' if not meta['errors'] else 'partial'
        meta['processed_at'] = now()
        title = html.escape(data.get('title', item['title']))
        e = lambda v: html.escape(str(v or ''), quote=True)
        status_note = '图文资源完整' if meta['status'] == 'complete' else '有待处理项目：' + '；'.join(meta['errors'])
        figures = ' · '.join(f'<a href="#figure-{a["order"]:03d}">图{a["order"]:03d}</a>' for a in meta['assets'])
        header = f'<header><p><a href="../../index.html">材料库</a> · <a href="{e(item["url"])}">原文</a> · <a href="article.md">Markdown正文</a> · <a href="metadata.json">来源记录</a></p><h1>{title}</h1><p class="meta">页面显示：{e(meta["page_display_time"])}<br>页面署名：{e(meta["page_byline"])}　标注来源：{e(meta["source_label"] or "未单列；保留正文归属")}<br>取得：{e(meta["acquired_at"])}　主题：{e(item["category"])}</p><p class="notice">当前取得版本；{e(status_note)}。正文图片可单击查看完整尺寸。</p></header>'
        summary = f'<aside class="summary">{e(data.get("content_short", ""))}</aside>' if data.get('content_short') else ''
        doc = f'<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="default-src \'none\'; img-src \'self\' data:; style-src \'unsafe-inline\'"><title>{title}</title><style>{CSS}</style></head><body><main>{header}{summary}<nav class="asset-nav">{figures}</nav><article>{soup}</article></main></body></html>'
        (folder / 'article.html').write_text(doc, encoding='utf-8')
        write_markdown(folder, soup, meta)
        (folder / 'article.txt').unlink(missing_ok=True)
        meta['files'] = {name: {'sha256': sha((folder / name).read_bytes()), 'bytes': (folder / name).stat().st_size} for name in ['raw.json', 'article.html', 'article.md']}
    except Exception as exc:
        meta['errors'].append(str(exc))
    write_json(meta_path, meta)
    return meta


def build():
    items = selected()
    rows = []
    for item in items:
        p = post_folder(item['article_id']) / 'metadata.json'
        if p.exists():
            m = load(p)
        else:
            m = {'article_id': item['article_id'], 'status': 'pending', 'assets': [], 'errors': []}
        rows.append({'article_id': item['article_id'], 'title': m.get('title') or item['title'], 'category': item['category'], 'reading_priority': item['reading_priority'], 'page_display_time': m.get('page_display_time') or item['page_display_time'], 'byline': m.get('page_byline') or item['page_byline'], 'source_label': m.get('source_label') or item.get('page_source_label'), 'status': m['status'], 'path': f'SourcePost/{directory_names()[str(item["article_id"])]}/article.html' if (post_folder(item['article_id']) / 'article.html').exists() else None, 'markdown_path': f'SourcePost/{directory_names()[str(item["article_id"])]}/article.md' if (post_folder(item['article_id']) / 'article.md').exists() else None, 'metadata': f'SourcePost/{directory_names()[str(item["article_id"])]}/metadata.json' if p.exists() else None, 'images': len(m.get('assets', [])), 'images_downloaded': sum(a['status'] == 'complete' for a in m.get('assets', [])), 'html_tables': m.get('html_table_count', 0), 'errors': m.get('errors', []), 'reading_value': item['reading_value']})
    counts = dict(Counter(r['status'] for r in rows))
    manifest = {'generated_at': now(), 'selection_file': str(CATALOG.relative_to(ROOT)), 'scope': 'public article body and inline figures of the acquired version', 'selected': len(items), 'counts': counts, 'image_occurrences': sum(r['images'] for r in rows), 'downloaded_image_occurrences': sum(r['images_downloaded'] for r in rows), 'html_tables': sum(r['html_tables'] for r in rows), 'articles': rows}
    write_json(MAINTENANCE / 'manifest.json', manifest)
    cats = list(dict.fromkeys(a['category'] for a in items))
    out = ['# 华尔街见闻本地材料目录', '', f'206篇入选；状态：{counts}。正文图片{manifest["downloaded_image_occurrences"]}/{manifest["image_occurrences"]}。', '', '[浏览器入口](index.html) · [使用说明](README.md)', '']
    for cat in cats:
        out += [f'## {cat}', '', '| 日期 | 文章 | 署名／标注来源 | 图 | 状态 |', '| --- | --- | --- | ---: | --- |']
        for r in rows:
            if r['category'] != cat:
                continue
            title = r['title'].replace('|', '／')
            label = f'[{title}]({url_path(r["path"])})' if r['path'] else title
            if r['markdown_path']:
                label += f' · [MD]({url_path(r["markdown_path"])})'
            byline = (r['byline'] or '') + ('／' + r['source_label'] if r['source_label'] else '')
            out.append(f'| {r["page_display_time"][:10]} | {label} | {byline.replace("|", "／")} | {r["images_downloaded"]}/{r["images"]} | {r["status"]} |')
        out.append('')
    (ROOT / 'CATALOG.md').write_text('\n'.join(out), encoding='utf-8')
    e = lambda v: html.escape(str(v or ''), quote=True)
    cards = []
    for r in rows:
        href = e(url_path(r['path']) if r['path'] else f'https://wallstreetcn.com/articles/{r["article_id"]}')
        cards.append(f'<li data-search="{e(" ".join(str(r[k] or "") for k in ["title","category","byline","source_label","reading_value"]))}"><h3><a href="{href}">{e(r["title"])}</a></h3><p class="meta">{e(r["page_display_time"][:10])} · {e(r["category"])} · {e(r["byline"])} · {e(r["source_label"])} · {r["images_downloaded"]}图 · {e(r["status"])}</p><p>{e(r["reading_value"])}</p></li>')
    index = f'<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>华尔街见闻本地材料库</title><style>{CSS}input{{width:100%;padding:12px;font:inherit}}ul{{padding:0;list-style:none}}li{{padding:12px 0;border-bottom:1px solid #ddd}}.meta{{border:0;padding:0}}</style></head><body><main><h1>华尔街见闻本地材料库</h1><p>206篇 · 正文插图{manifest["downloaded_image_occurrences"]}张 · {e(counts)}</p><p><a href="README.md">使用说明</a> · <a href="CATALOG.md">文字目录</a></p><label for="q">筛选标题、作者、主题及选文理由</label><input id="q" type="search" placeholder="例如：AI CDS、基差、中金、稳定币"><p id="n">206篇</p><ul>{"".join(cards)}</ul></main><script>const input=document.getElementById("q");input.addEventListener("input",()=>{{let n=0;const terms=input.value.toLowerCase().trim().split(/\\s+/);document.querySelectorAll("li[data-search]").forEach(x=>{{x.hidden=!terms.every(t=>x.dataset.search.toLowerCase().includes(t));if(!x.hidden)n++}});document.getElementById("n").textContent=n+"篇"}});</script></body></html>'
    (ROOT / 'index.html').write_text(index, encoding='utf-8')
    # SQLite可随时删除重建，原始内容与图像不依赖数据库。
    db_path = MAINTENANCE / 'library.sqlite'
    temp = MAINTENANCE / 'library.sqlite.tmp'
    if temp.exists():
        temp.unlink()
    db = sqlite3.connect(temp)
    db.execute('CREATE TABLE articles(id INTEGER PRIMARY KEY,title TEXT,category TEXT,byline TEXT,source_label TEXT,page_display_time TEXT,status TEXT,path TEXT,markdown_path TEXT,body TEXT)')
    db.execute('CREATE TABLE assets(article_id INTEGER, image_order INTEGER,path TEXT,source_url TEXT,sha256 TEXT,width INTEGER,height INTEGER,status TEXT,PRIMARY KEY(article_id,image_order))')
    db.execute("CREATE VIRTUAL TABLE search USING fts5(title,body,tokenize='trigram')")
    for r in rows:
        p = post_folder(r['article_id'])
        body = (p / 'article.md').read_text(encoding='utf-8') if (p / 'article.md').exists() else ''
        db.execute('INSERT INTO articles VALUES (?,?,?,?,?,?,?,?,?,?)', (r['article_id'], r['title'], r['category'], r['byline'], r['source_label'], r['page_display_time'], r['status'], r['path'], r['markdown_path'], body))
        db.execute('INSERT INTO search(rowid,title,body) VALUES (?,?,?)', (r['article_id'],r['title'],body))
        if (p / 'metadata.json').exists():
            for a in load(p / 'metadata.json').get('assets', []):
                db.execute('INSERT INTO assets VALUES (?,?,?,?,?,?,?,?)', (r['article_id'],a['order'],f'SourcePost/{directory_names()[str(r["article_id"])]}/{a["path"]}' if a.get('path') else None,a['source_url'],a.get('sha256'),a.get('width'),a.get('height'),a['status']))
    db.commit()
    db.close()
    temp.replace(db_path)
    print(json.dumps({k:v for k,v in manifest.items() if k!='articles'}, ensure_ascii=False), flush=True)


def validate():
    issues, observations = [], []
    image_hashes, article_hashes = Counter(), {}
    checked = 0
    for item in selected():
        folder = post_folder(item['article_id'])
        prefix = str(item['article_id'])
        if not (folder / 'metadata.json').exists():
            issues.append(f'{prefix}: 未处理')
            continue
        meta = load(folder / 'metadata.json')
        if meta['status'] != 'complete':
            issues.append(f'{prefix}: {meta["status"]}: {meta["errors"]}')
        for name, record in meta.get('files', {}).items():
            p = folder / name
            checked += 1
            if not p.exists() or sha(p.read_bytes()) != record['sha256']:
                issues.append(f'{prefix}/{name}: 文件缺失或校验失败')
        if not (folder / 'raw.json').exists() or not (folder / 'article.html').exists():
            continue
        raw = load(folder / 'raw.json')['data']
        original = BeautifulSoup(article_body(raw), 'html.parser')
        doc = BeautifulSoup((folder / 'article.html').read_text(encoding='utf-8'), 'html.parser')
        body = doc.find('article')
        if body is None:
            issues.append(f'{prefix}: 没有article正文')
            continue
        compare = copy.copy(body)
        for t in compare.select('.local-copy'):
            t.decompose()
        if normalized_text(original) != normalized_text(compare):
            issues.append(f'{prefix}: 正文文字不一致')
        origin_images = [urljoin(item['url'], t.get('src') or '') for t in original.find_all('img')]
        local_images = [t.get('data-source-url') for t in body.find_all('img')]
        if origin_images != local_images:
            issues.append(f'{prefix}: 图片来源或出现顺序不一致')
        if len(original.find_all('table')) != len(body.find_all('table')):
            issues.append(f'{prefix}: HTML表格数量不一致')
        if re.search(r'<!--(?:image|video|audio)[^>]*-->', str(body)):
            issues.append(f'{prefix}: 存在未恢复占位符')
        for t in doc.find_all():
            for attr in ['src', 'srcset', 'poster', 'data']:
                value = t.get(attr, '')
                if value.startswith(('https://', 'http://', '//')):
                    issues.append(f'{prefix}: 远程加载依赖: {attr}={value}')
                elif value and attr == 'src':
                    checked += 1
                    if not (folder / unquote(urlparse(value).path)).is_file():
                        issues.append(f'{prefix}: 资源不存在: {value}')
        md_path = folder / 'article.md'
        if not md_path.exists():
            issues.append(f'{prefix}: Markdown文件不存在')
        else:
            md_text = md_path.read_text(encoding='utf-8')
            if '\n---\n' not in md_text:
                issues.append(f'{prefix}: Markdown正文分隔缺失')
            else:
                md_body = md_text.split('\n---\n', 1)[1]
                issues.extend(f'{prefix}: {message}' for message in markdown_issues(md_body, body))
            md_doc = BeautifulSoup(MarkdownIt('commonmark').render(md_text), 'html.parser')
            for tag, attr in [('img', 'src'), ('a', 'href')]:
                for t in md_doc.find_all(tag):
                    value = t.get(attr, '')
                    u = urlparse(value)
                    if not u.scheme and not value.startswith('#'):
                        checked += 1
                        if not (folder / unquote(u.path)).resolve().is_file():
                            issues.append(f'{prefix}: Markdown本地链接不存在: {value}')
        if (folder / 'article.txt').exists():
            issues.append(f'{prefix}: 旧TXT尚未删除')
        for a in meta.get('assets', []):
            if a['status'] != 'complete':
                continue
            p = folder / a['path']
            checked += 1
            if not p.exists() or sha(p.read_bytes()) != a['sha256']:
                issues.append(f'{prefix}/{a["path"]}: 图片校验失败')
                continue
            try:
                image_bytes(p.read_bytes(), a.get('content_type') or '')
            except Exception as exc:
                issues.append(f'{prefix}/{a["path"]}: {exc}')
            image_hashes[a['sha256']] += 1
        for a in doc.find_all('a', href=True):
            u = urlparse(a['href'])
            if u.scheme or a['href'].startswith('#'):
                continue
            checked += 1
            if not (folder / unquote(u.path)).resolve().exists():
                issues.append(f'{prefix}: 本地链接不存在: {a["href"]}')
        if item['page_image_count'] != len(origin_images):
            observations.append(f'{prefix}: 目录图片数{item["page_image_count"]}，现正文{len(origin_images)}')
        digest = sha(normalized_text(original).encode())
        if digest in article_hashes:
            issues.append(f'{prefix}: 正文与{article_hashes[digest]}完全相同')
        article_hashes[digest] = prefix
    db = sqlite3.connect(MAINTENANCE / 'library.sqlite')
    db_integrity = db.execute('PRAGMA integrity_check').fetchone()[0]
    indexed = db.execute('SELECT COUNT(*) FROM articles').fetchone()[0]
    db.close()
    if db_integrity != 'ok' or indexed != len(selected()):
        issues.append(f'SQLite: {db_integrity}, articles={indexed}')
    report = {'validated_at': now(), 'article_count': len(selected()), 'checked_files_and_links': checked, 'unique_image_hashes': len(image_hashes), 'image_occurrences': sum(image_hashes.values()), 'duplicate_image_occurrences': sum(n-1 for n in image_hashes.values()), 'database_integrity': db_integrity, 'observations': observations, 'issues': issues, 'issue_count': len(issues), 'scope': 'HTML and Markdown text/headings/image order, static image files, hashes, local links, dependencies; does not verify chart meaning or external claims'}
    previous = load(MAINTENANCE / 'validation.json') if (MAINTENANCE / 'validation.json').exists() else {}
    if previous.get('browser'):
        report['browser'] = previous['browser']
    write_json(MAINTENANCE / 'validation.json', report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return not issues


def search(query, limit):
    db = sqlite3.connect(MAINTENANCE / 'library.sqlite')
    if len(query) >= 3:
        term = '"' + query.replace('"', '""') + '"'
        rows = db.execute('SELECT a.id,a.title,a.markdown_path,snippet(search,1,\'[\',\']\',\'…\',22) FROM search JOIN articles a ON a.id=search.rowid WHERE search MATCH ? ORDER BY rank LIMIT ?', (term, limit)).fetchall()
    else:
        rows = db.execute('SELECT id,title,markdown_path,substr(body,max(instr(body,?)-50,1),160) FROM articles WHERE instr(title,?)>0 OR instr(body,?)>0 LIMIT ?', (query,query,query,limit)).fetchall()
    for row in rows:
        print(json.dumps(dict(zip(['id','title','path','excerpt'],row)), ensure_ascii=False))
    db.close()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    a = sub.add_parser('acquire')
    a.add_argument('--ids', nargs='+', type=int)
    a.add_argument('--workers', type=int, default=4)
    sub.add_parser('reformat', help='从现有HTML重建Markdown，无网络请求')
    sub.add_parser('build')
    sub.add_parser('validate')
    s = sub.add_parser('search')
    s.add_argument('query')
    s.add_argument('--limit', type=int, default=10)
    args = p.parse_args()
    if args.command == 'acquire':
        items = selected()
        if args.ids:
            wanted = set(args.ids)
            items = [a for a in items if a['article_id'] in wanted]
            if wanted - {a['article_id'] for a in items}:
                p.error('部分ID不在清单内')
        with futures.ThreadPoolExecutor(max_workers=max(1,min(args.workers,4))) as pool:
            jobs = {pool.submit(acquire_one,item): item for item in items}
            for n, job in enumerate(futures.as_completed(jobs),1):
                m = job.result()
                print(json.dumps({'n':n,'of':len(items),'id':m['article_id'],'status':m['status'],'images':len(m['assets']),'errors':m['errors']},ensure_ascii=False),flush=True)
        build()
    elif args.command == 'reformat':
        reformat()
    elif args.command == 'build':
        build()
    elif args.command == 'validate':
        raise SystemExit(0 if validate() else 1)
    else:
        search(args.query, args.limit)


if __name__ == '__main__':
    main()
