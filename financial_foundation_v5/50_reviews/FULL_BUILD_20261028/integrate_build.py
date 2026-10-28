"""Integrate the full reviewed map; refuses to run before all 222 new reviews exist.

Only metadata, navigation, catalog status, and release records are generated here.
Economic prose is authored and reviewed separately. Frozen first drafts are untouched.
"""
import argparse
import copy
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

import yaml

ap = argparse.ArgumentParser()
ap.add_argument('--apply', action='store_true', help='write the prepared integration')
args = ap.parse_args()
out = Path(__file__).resolve().parent
root = out.parent.parent
readj = lambda p: json.loads(p.read_text())
digest = lambda s: hashlib.sha256(s.encode()).hexdigest()
flat = lambda j, k: [i for g in j[k] for i in g['items']]
baseline = readj(out / 'BASELINE_INDEX.json')
index = copy.deepcopy(baseline)
paths = readj(out / 'PATHS.json')
review = readj(out / 'MAIN_REVIEW.json')
state = readj(out / 'RUN_STATE.json')
items = {i['id']: i for k in ('concepts', 'mechanisms') for i in flat(index, k)}
new_ids = {n for n, i in items.items() if i['status'] != 'complete'}
assert len(new_ids) == 222 and set(review['entries']) == new_ids, 'Complete every full-text review first.'
assert all(b['status'] == 'reviewed' for b in state['batches']), 'An assigned batch remains unreviewed.'
texts, meta = {}, {}
for n, rel in paths.items():
    texts[n] = (root / rel).read_text()
    meta[n] = yaml.safe_load(texts[n].split('---', 2)[1])
    assert meta[n]['status'] == 'reviewed_seed', n
    if n in new_ids:
        assert digest(texts[n]) == review['entries'][n]['sha256'], n + ': unreviewed edit'

changes = defaultdict(list)
for n in paths:
    items[n]['status'] = 'complete'
    items[n]['path'] = '../' + paths[n]
    if n.startswith('R-') and n in new_ids:
        y = meta[n]
        # References outside a logic group still belong in the page's related list.
        path_ids = {rel: node for node, rel in paths.items()}
        linked_paths = re.findall(r'\]\(\.\./(20_mechanisms/[^)#]+)(?:#[^)]*)?\)', texts[n].split('---', 2)[2])
        mentioned = [path_ids[p] for p in linked_paths if p in path_ids]
        group_related = [r for g in y['logic_groups'] for r in g.get('related_mechanism_ids', [])]
        related = list(dict.fromkeys(y.get('related_mechanism_ids', []) + group_related + [r for r in mentioned if r in items and r != n]))
        if related != y.get('related_mechanism_ids', []):
            y['related_mechanism_ids'] = related
            # Authors may use either inline or block YAML; replace the parsed field.
            body = texts[n].split('---', 2)[2]
            texts[n] = '---\n' + yaml.safe_dump(y, allow_unicode=True, sort_keys=False, width=10000) + '---' + body
            changes[n].append('page related_mechanism_ids reconciled with logic groups and explicit body links')
        for field in ('node_ids', 'related_mechanism_ids', 'logic_groups'):
            items[n][field] = copy.deepcopy(y[field])
        items[n]['node_mapping_stage'] = 'authored_logic_groups'


def direct_links(text):
    """Convert only live catalog node destinations, preserving labels and prose."""
    for n, rel in paths.items():
        filename = 'CONCEPT_IMPORT_LIST.md' if n.startswith('C-') else 'MECHANISM_IMPORT_LIST.md'
        for prefix in ('../00_start/', ''):
            text = text.replace(f'({prefix}{filename}#{n})', f'(../{rel})')
    return text


# Build exact concept -> authored mechanism logic anchors, with original headings.
backlinks = defaultdict(list)
for mechanism in flat(index, 'mechanisms'):
    rn = mechanism['id']
    body = texts[rn].split('---', 2)[2]
    for group in mechanism['logic_groups']:
        anchor = group['anchor']
        match = re.search(r'<a id="' + re.escape(anchor) + r'"></a>\s*\n(#{1,6})\s+([^\n]+)', body)
        assert match, rn + ': missing logic heading ' + anchor
        label = match.group(2).replace('|', '／')
        for cn in group['node_ids']:
            assert cn in items and cn.startswith('C-')
            backlinks[cn].append((rn, anchor, label))

nav_start = '<!-- FULL_BUILD_MECHANISM_BACKLINKS_START -->'
nav_end = '<!-- FULL_BUILD_MECHANISM_BACKLINKS_END -->'
for n in paths:
    before = texts[n]
    texts[n] = direct_links(texts[n])
    if texts[n] != before:
        changes[n].append('catalog-node links changed to completed document paths')
    if n.startswith('C-') and backlinks[n]:
        rows = [nav_start, '### 机制正文中的关联位置', '', '下表定位到机制正文中明确使用本对象的逻辑组。', '', '| 机制 | 逻辑组 |', '|---|---|']
        grouped = defaultdict(list)
        for rn, anchor, label in backlinks[n]:
            grouped[rn].append(f'[{label}](../{paths[rn]}#{anchor})')
        for rn, links in grouped.items():
            rows.append(f'| [{items[rn]["name"]}](../{paths[rn]}) | ' + '；'.join(links) + ' |')
        block = '\n'.join(rows + [nav_end]) + '\n\n'
        text = re.sub(re.escape(nav_start) + r'.*?' + re.escape(nav_end) + r'\n*', '', texts[n], flags=re.S)
        source_heading = re.search(r'^## 来源[^\n]*', text, re.M)
        if source_heading:
            text = text[:source_heading.start()] + block + text[source_heading.start():]
        else:
            text = text.rstrip() + '\n\n' + block
        texts[n] = text
        changes[n].append('concept navigation to every indexed mechanism logic group')

for kind in ('concepts', 'mechanisms'):
    index['counts'][kind]['complete'] = len(flat(index, kind))
    index['counts'][kind]['pending'] = 0
index['updated'] = index['packaged_at'] = '2026-10-28'
index['maintenance_revision'] = 'full_build_20261028'
index['build_progress'] = {'as_of': '2026-10-28', 'authored_nodes': 234, 'pending_nodes': 0,
                           'complete_concepts': 163, 'complete_mechanisms': 71,
                           'review': '../50_reviews/FULL_BUILD_20261028/MAIN_REVIEW.md'}
index['notes'] = [note.replace('目录确认不代表222份待制作正文已完成。', '本轮234份正文均已有经审阅版本，资料截止并不统一。') for note in index['notes']]
index['notes'] = [note.replace('未完成关系的node_ids是初始关联入口；具体逻辑组与适用情境在后续精读、制作时细化。成品逻辑组与正文一致。', '关系的node_ids、logic_groups及related_mechanism_ids依据已完成正文同步；Concept提供指向具体逻辑组的反向导航。') for note in index['notes']]
index['notes'].append('2026-10-28全量制作新增222篇：main各写1篇Concept和Mechanism；74名GPT-6-Astra medium作者各最多3篇，main逐篇通读并记录复核，保留首稿及分工；既有12篇仅更新导航。')

outputs = {root / paths[n]: text for n, text in texts.items()}


def concept_link(n):
    return f'[{items[n]["name"]} {n}](../{paths[n]})'


for kind, filename in [('concepts', 'CONCEPT_IMPORT_LIST.md'), ('mechanisms', 'MECHANISM_IMPORT_LIST.md')]:
    text = (root / '00_start' / filename).read_text()
    count = len(flat(index, kind))
    text = re.sub(r'正文 \*\*\d+ 份已完成、\d+ 份待制作\*\*(?:（进度更新：[^）]+）)?', f'正文 **{count} 份已完成、0 份待制作**（进度更新：2026-10-28）', text, count=1)
    for g in index[kind]:
        size, p0 = len(g['items']), sum(i['priority'] == 'P0' for i in g['items'])
        text = re.sub(r'^\| ' + re.escape(g['title']) + r' \| \d+ \| \d+ \| \d+ \| \d+ \|$', f'| {g["title"]} | {size} | {p0} | {size} | 0 |', text, flags=re.M)
    lines = []
    for line in text.splitlines():
        match = re.search(r'<a id="([CR]-[^"]+)"></a>', line)
        if match and match.group(1) in items:
            n = match.group(1)
            cells = line.split(' | ')
            cells[-1] = f'complete／[正文](../{paths[n]}) |'
            if kind == 'mechanisms':
                cells[2] = '；'.join(concept_link(c) for c in items[n]['node_ids']) or '—'
                context = ['[' + t['name'] + '（正文术语）](CONCEPT_CONTEXT_TERMS.md#' + t['legacy_id'] + ')' for t in items[n].get('context_terms', [])]
                related = items[n].get('related_mechanism_ids', [])
                if related:
                    context.append('相关关系：' + '；'.join(concept_link(r) for r in related))
                cells[3] = '；'.join(context) or '—'
            line = ' | '.join(cells)
        lines.append(line)
    text = direct_links('\n'.join(lines) + '\n')
    outputs[root / '00_start' / filename] = text

manifest = []
for n in paths:
    y = meta[n]
    manifest.append({'id': n, 'title': items[n]['name'], 'path': paths[n], 'author': y.get('draft_author', 'legacy'),
                     'evidence_as_of': str(y.get('evidence_as_of', 'see page')), 'new_in_this_build': n in new_ids,
                     'sha256': digest(texts[n]), 'integration_changes': changes[n]})
    if n in new_ids:
        review['entries'][n].setdefault('reviewed_content_sha256', review['entries'][n]['sha256'])
        review['entries'][n]['sha256'] = digest(texts[n])
        review['entries'][n]['integration_changes'] = changes[n]
state['status'] = 'integrated_pending_final_validation'
state['reviewed_new_count'] = len(new_ids)
json_text = lambda x: json.dumps(x, ensure_ascii=False, indent=2) + '\n'
outputs[root / '00_start/catalog_index.json'] = json_text(index)
outputs[out / 'MAIN_REVIEW.json'] = json_text(review)
outputs[out / 'RUN_STATE.json'] = json_text(state)
outputs[out / 'BUILD_MANIFEST.json'] = json_text({'date': '2026-10-28', 'nodes': manifest})
outputs[out / 'INTEGRATION_CHANGES.json'] = json_text(dict(changes))
report = ['# 全量制作审阅记录：2026-10-28', '',
          '当前确认目录的163个Concept与71个Mechanism均有经审阅正文。本轮新增222篇，保留既有12篇的经济解释，仅更新导航。', '',
          'Main只执笔C-EXPECT-05和R-DERIV-CARRY；其余220篇由74名GPT-6-Astra、medium作者制作，每名最多3篇。批次目录保存原任务、研究笔记、交付清单与逐字首稿。', '',
          '每篇新稿由main全文通读，核对关键来源、公式、时期、样本和预测归属；发现的问题直接审改并记录。[逐篇复核记录](MAIN_REVIEW.json)保留文字证据和审阅哈希。目录整合随后只调整元数据和导航，[整合变动](INTEGRATION_CHANGES.json)单列。', '',
          '“完整”指目录内全部条目形成可独立阅读的正文；证据截止和未取得材料逐篇披露，并不表示所有数据已更新到制作日。结构校验见[VALIDATION.json](VALIDATION.json)，它不代替内容主审。', '',
          '## 全部条目与责任记录', '', '| ID | 条目 | 执笔 | 证据截止 | 本轮 |', '|---|---|---|---|---|']
for row in manifest:
    report.append(f'| {row["id"]} | [{row["title"]}](../../{row["path"]}) | `{row["author"]}` | {row["evidence_as_of"]} | ' + ('新增并主审' if row['new_in_this_build'] else '既有成品') + ' |')
outputs[out / 'MAIN_REVIEW.md'] = '\n'.join(report) + '\n'

# Entry pages are updated only after all authors finish reading the frozen inputs.
p = root / '00_start/README.md'
text = p.read_text()
text = text.replace('更新：2026-10-27，国债供给关联Concepts试产。初步建图范围已定稿：163个对象、71个关系／机制，共234个节点。当前已有12份经审阅正文，222份待制作；本批分工和验收见[试产记录](../50_reviews/FISCAL_CONCEPT_PILOT_20261027/MAIN_REVIEW.md)。', '更新：2026-10-28，完成正式目录全部163个Concept与71个Mechanism，共234篇经审阅正文。全量分工、逐篇审阅及校验见[本批记录](../50_reviews/FULL_BUILD_20261028/MAIN_REVIEW.md)；各篇资料截止单独保存。')
outputs[p] = text
p = root / 'README.md'
text = p.read_text()
text = text.replace('初步建图节点确认版；2026-10-27完成黄金及国债供给关联Concepts试产，节点范围沿用2026-10-25定稿。完整保留已有样例、Event／Source、课程PDF与图文材料。', '2026-10-28完成Concept与Mechanism全量制作，节点范围沿用2026-10-25定稿。已有样例、Event／Source、课程PDF与图文材料保留。')
text = text.replace('现有12份经审阅正文（10个Concepts、2个Mechanisms），其余222份正文待制作。', '234份正文均已完成并审阅，本轮新增153个Concept和69个Mechanism。')
text = text.replace('本次试产见[国债供给批次审阅与分工]', '本轮见[全量制作审阅与分工](50_reviews/FULL_BUILD_20261028/MAIN_REVIEW.md)，此前试产见[国债供给批次审阅与分工]')
text = text.replace('：后续制作以这234个节点为范围。', '：全部234篇正文的阅读入口。')
text = text.replace('## 已有正文', '## 早期成品与作者记录')
text = text.replace('本轮主 agent 唯一新写条目，自审', '国债供给试产时主 agent 唯一新写条目，自审')
text = text.replace('2024年7—8月 |\n\n| 对象', '2024年7—8月 |\n| 对象')
old = '《国债供给》继续完整采用新稿；《期限溢价》保持已整合版本。名称与引用已随节点定稿同步；本轮保留此前六篇的经济正文及资料覆盖，只将新完成对象的导航指向正文。黄金机制的三个、国债供给机制的八个关联对象现均有正文；各篇历史截止分别保留，不自动延长至制作日。'
text = text.replace(old, '上表保留早期12篇成品的作者与资料截止。本轮保留其经济解释，更新正文链接和机制逻辑组回链。全部234篇的作者、资料截止与路径见[完整清单](50_reviews/FULL_BUILD_20261028/BUILD_MANIFEST.json)。')
text = text.replace('十份对象正文、两份机制正文。', '163份对象正文、71份机制正文。')
text = text.replace('按本版163项对象和71项关系安排节点制作；普通变量直接进入解释，退出项留作追溯。', '本版163项对象和71项关系已有正文，后续按实际材料补证据和修订解释；普通变量直接进入解释，退出项留作追溯。')
text = text.replace('结构与材料完整性校验见[VALIDATION.json](50_reviews/VALIDATION.json)。', '本轮结构、分工、链接与保留范围校验见[VALIDATION.json](50_reviews/FULL_BUILD_20261028/VALIDATION.json)；此前材料完整性记录仍保留。')
outputs[p] = text
p = root / '50_reviews/README.md'
text = p.read_text().replace('更新：2026-10-27。', '更新：2026-10-28。')
text = text.replace('|---|---|', '|---|---|\n| [全量Concept与Mechanism制作](FULL_BUILD_20261028/MAIN_REVIEW.md) | 234篇正文；main各写一篇，74名Astra medium作者各最多三篇；逐篇主审、冻结首稿与[全量校验](FULL_BUILD_20261028/VALIDATION.json)。 |', 1)
text = text.replace('[当前校验](VALIDATION.json)', '[此前建图校验](VALIDATION.json)').replace('当前包的结构、范围与文件完整性检查', '此前包的结构、范围与文件完整性检查')
outputs[p] = text
print(json.dumps({'prepared_files': len(outputs), 'new_reviewed': len(new_ids), 'all_complete': len(paths), 'apply': args.apply}, ensure_ascii=False))
if args.apply:
    for path, content in outputs.items():
        path.write_text(content)
