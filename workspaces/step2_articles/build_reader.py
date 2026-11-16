from pathlib import Path
import json,re,html,os
from collections import Counter
from urllib.parse import unquote,urlsplit
from markdown_it import MarkdownIt
import yaml

R=Path(__file__).resolve().parent;G=R/'graph'
CASES=[('ai','AI CDS'),('korea','韩国股市'),('basis','美债基差交易')]
D={k:json.loads((R/'deliveries'/f'{k}.json').read_text()) for k,_ in CASES}
files={f['path']:f for d in D.values() for f in d['files']}
anchors={p:'doc-'+str(i) for i,p in enumerate(files)}
KINDS={'concept':'概念','subconcept':'子概念','relation':'关系','subrelation':'子关系','event':'事件分析','source':'来源记录'}
META={p:yaml.safe_load((G/p).read_text().split('---',2)[1]) for p in files}
INDEX=json.loads((G/'00_start/catalog_index.json').read_text())
NODES={x['id']:x for kind in ['concepts','mechanisms'] for group in INDEX[kind] for x in group['items']}
for path,f in files.items():
 m=META[path];base={'concept':'concept','mechanism':'relation','analysis_note':'event','event':'event','event_collection':'event','source_note':'source'}[m['type']]
 parents=m.get('parent_ids',[])
 expected={'concept':'subconcept','relation':'subrelation'}.get(base,base) if parents else base
 if f.get('entry_kind')!=expected:raise ValueError(f"{path}: entry_kind与正文类型或父项不一致")
 if parents!=f.get('parent_ids',[]):raise ValueError(f"{path}: parent_ids与正文不一致")
 if any(i not in NODES for i in parents):raise ValueError(f"{path}: 父项未登记")
M=MarkdownIt('commonmark',{'html':True}).enable('table')
def E(x):return html.escape(str(x),quote=True)
def render(path):
 p=G/path;raw=p.read_text();parts=raw.split('---',2)
 meta=yaml.safe_load(parts[1]) if raw.startswith('---\n') else {}
 body=parts[2].strip() if raw.startswith('---\n') else raw
 tokens=M.parse(body)
 for t in tokens:
  for c in [t]+(t.children or []):
   attr='src' if c.type=='image' else 'href';u=c.attrGet(attr)
   if not u:continue
   v=urlsplit(u)
   if v.scheme or v.netloc:continue
   target=(p.parent/unquote(v.path)).resolve() if v.path else p
   rel=os.path.relpath(target,R)
   # Keep document fragment links in actual Markdown rather than guessing rendered IDs.
   target_key=os.path.relpath(target,G)
   if attr=='href' and target_key in anchors:
    c.attrSet(attr,'#'+anchors[target_key]+('--'+v.fragment if v.fragment else ''))
   else:c.attrSet(attr,rel+('#'+v.fragment if v.fragment else ''))
 body=M.renderer.render(tokens,M.options,{})
 body=re.sub(r'(<(?:a|span)\b[^>]*?\bid=["\'])([^"\']+)',lambda m:m[1]+anchors[path]+'--'+m[2],body)
 return body,meta
def parent_info(f, markdown=False):
 parents=f.get('parent_ids',[])
 if not parents:return '—' if markdown else ''
 links=[]
 for pid in parents:
  node=NODES[pid];target=os.path.relpath((G/'00_start'/node['path']).resolve(),G.resolve())
  url='graph/'+target if markdown else ('#'+anchors[target] if target in anchors else 'graph/'+target)
  links.append(f"[{node['name']}]({url})" if markdown else f'<a href="{E(url)}">{E(node["name"])}</a>')
 label='母概念' if f['entry_kind']=='subconcept' else '母关系'
 relation={'thematic_collection':'专题集合','instrument_specific_basis':'工具细分类'}.get(META[f['path']].get('parent_relation'), '')
 return label+'：'+'、'.join(links)+(' · '+relation if relation else '')
parts=[];summary=[];rows=[]
for k,title in CASES:
 d=D[k];items=d['files'];new=sum(f['operation']=='new' for f in items);updates=sum(f['operation']=='update' for f in items)
 summary.append(f'<a href="#{k}">{E(title)} · 新建{new} / 更新{updates}</a>')
 section=[f'<section id="{k}"><p class="eyebrow">{E(title)}</p><h2>{E(d.get("title",title))}</h2><div class="filelist">']
 for f in items:
  section.append(f'<a href="#{anchors[f["path"]]}">{E(f["title"])} <small>{"新建" if f["operation"]=="new" else "更新"} · {KINDS[f["entry_kind"]]}</small></a>')
 section.append('</div>')
 for f in items:
  body,meta=render(f['path']);a=anchors[f['path']];op='新建' if f['operation']=='new' else '更新';kind=KINDS[f['entry_kind']];parent=parent_info(f);parent_html=('<p class="parent">'+parent+'</p>') if parent else ''
  section.append(f'<details class="document" id="{a}" open><summary><span class="tag">{op} · {kind}</span><strong>{E(f["title"])}</strong><small>{E(f["id"])}</small></summary><div class="doc">{parent_html}<p class="placement">{E(f.get("why",""))}</p><p class="file"><a href="graph/{E(f["path"])}">打开Markdown原文件</a> · {E(meta.get("status",meta.get("editing_status","")))}</p>{body}</div></details>')
  rows.append(f'| {title} | {op} | {kind} | [{f["title"]}](graph/{f["path"]}) | {parent_info(f,True)} | {f.get("why","")} |')
 section.append('</section>');parts.append(''.join(section))
new=sum(f['operation']=='new' for f in files.values());updates=sum(f['operation']=='update' for f in files.values())
counts=Counter(f['entry_kind'] for f in files.values() if f['operation']=='new')
type_summary=' · '.join(f'{label} {counts[k]}' for k,label in KINDS.items())
css='''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f4f1e9;color:#20352f;font-family:system-ui,"Noto Sans CJK SC",sans-serif;line-height:1.85}main{max-width:1160px;margin:auto;padding:64px 32px}h1{font-family:serif;font-size:clamp(34px,5vw,60px);line-height:1.35;margin:20px 0}h2{font-size:29px}h3{font-size:23px}h4{font-size:19px}.eyebrow{font-size:12px;letter-spacing:2px;color:#28715c;font-weight:bold}.lead{font-size:18px;color:#58685f;max-width:880px}.stats{display:flex;gap:40px;margin:32px 0}.stats b{display:block;font:36px serif}.stats small{color:#68796f}nav{display:flex;gap:22px;flex-wrap:wrap;border-block:1px solid #d3d9d0;padding:16px 0}a{color:#246c58;text-underline-offset:4px;overflow-wrap:anywhere}section{margin-top:60px}.filelist{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px 20px;margin-bottom:28px}.filelist small{color:#748279}.document{background:#fffcf6;border:1px solid #d8ded4;margin:18px 0;scroll-margin-top:12px}.document>summary{cursor:pointer;display:flex;gap:14px;align-items:baseline;flex-wrap:wrap;padding:18px 24px}.document>summary strong{font-size:21px}.document>summary small{font-size:11px;color:#77867c}.tag{font-size:12px;border:1px solid #b7c9b9;padding:0 8px;color:#39735e}.doc{padding:0 28px 28px;overflow-wrap:anywhere}.doc h1{font-family:inherit;font-size:30px}.doc h2{font-size:24px;margin-top:34px}.parent{font-size:14px;color:#395e78}.type-summary{font-size:14px;color:#476451}.placement{border-left:3px solid #6b9b7d;padding-left:15px;color:#55705f}.file{font-size:12px;color:#6d7c70}table{border-collapse:collapse;display:block;overflow-x:auto;max-width:100%;font-size:14px}th,td{border:1px solid #d6ddd2;padding:8px 12px;text-align:left}img{max-width:100%;height:auto;background:white}pre{overflow-x:auto;background:#eef0e8;padding:16px}code{font-family:monospace;font-size:.9em}blockquote{border-left:3px solid #c5d2c1;margin-left:0;padding-left:18px;color:#586a5a}footer{margin-top:44px;font-size:13px;color:#687b6c}@media(max-width:600px){main{padding:28px 16px}.stats{gap:24px}.filelist{grid-template-columns:1fr}.doc{padding:0 16px 20px}.document>summary{padding:14px 16px}table{font-size:12px}}'''
page=f'''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Step2三篇正式制作 · 工作区</title><style>{css}</style><main><header><p class="eyebrow">FINANCIAL FOUNDATION / 2026.11.13</p><h1>三篇文章，制作成可维护的知识。</h1><p class="lead">本页直接展示成品条目正文。一般定义放在对象页，作用过程放在关系页，具体状态、机构判断与图表保存在事件中。工作图副本独立保存，尚未整合main。</p><div class="stats"><div><b>3</b><small>篇材料</small></div><div><b>{new}</b><small>份新文件</small></div><div><b>{updates}</b><small>份更新文件</small></div></div><p class="type-summary">新增分类：{type_summary}</p><p class="file">操作与类型分别标注；子概念、子关系同时显示父项。类型依据正文元数据，知识依赖与普通关联不计为继承。</p></header><nav>{''.join(summary)}<a href="制作说明.md">归属与改动</a><a href="review.md">主审意见</a></nav>{''.join(parts)}<footer><a href="README.md">工作区入口</a> · <a href="validation.json">结构与链接检查</a> · 新建数量包含对象、关系、事件与来源文件。</footer></main></html>'''
(R/'阅读报告.html').write_text(page)
text='''# 三篇制作的归属与改动

正式graph及main未改动；本目录graph是当前工作图的独立副本。本轮新页为step2_draft，旧页新编辑另有editing_status，尚未正式接入。

| 材料 | 操作 | 类型 | 成品 | 父项 | 维护职责／改动 |
| --- | --- | --- | --- | --- | --- |
'''+ '\n'.join(rows)+'\n\n原试作每项知识的最终去向见[AI CDS](deliveries/ai.json)、[韩国股市](deliveries/korea.json)、[美债基差](deliveries/basis.json)中的coverage。\n'
(R/'制作说明.md').write_text(text)
print(json.dumps({'new_files':new,'updated_files':updates,'report':str(R/'阅读报告.html')},ensure_ascii=False))
