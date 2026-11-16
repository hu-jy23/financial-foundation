from pathlib import Path
from urllib.parse import urlsplit,unquote
from collections import Counter
import json,html,os,re,ast,yaml
from markdown_it import MarkdownIt
R=Path(__file__).resolve().parent;W=R.parent/'step2_articles';G=W/'graph';ROOT=R.parents[1]
run=json.loads((R/'run.json').read_text());M=MarkdownIt('commonmark',{'html':True}).enable('table')
PARENT_LABELS={'concrete_subject':'具体主体','thematic_collection':'专题集合','instrument_specific_basis':'特定工具的基差','instrument_subtype':'工具细类','company_product':'公司产品线','policy_subtype':'政策工具细类'}
K={'concept':'概念','subconcept':'子概念','relation':'关系','subrelation':'子关系','event':'事件分析','source':'来源记录'}
css=next(ast.literal_eval(t.value) for t in ast.parse((W/'build_reader.py').read_text()).body if isinstance(t,ast.Assign) and any(isinstance(a,ast.Name) and a.id=='css' for a in t.targets))
def E(s):return html.escape(str(s),quote=True)
def meta(path):return yaml.safe_load((G/path).read_text().split('---',2)[1])
cases=[]
for name in ['ai','korea','basis']:
 d=json.loads((W/'deliveries'/f'{name}.json').read_text());cases.append({'id':d['article_id'],'title':d.get('title',{'ai':'AI CDS','korea':'韩国股市','basis':'美债基差交易'}[name]),'files':d['files'],'baseline':True,'summary':'三篇基准，已含2026-11-16规则复审。'})
for a in run['articles']:
 if a['status']=='adopted':
  d=json.loads((R/'articles'/str(a['article_id'])/'delivery.json').read_text());cases.append({'id':a['article_id'],'title':a['title'],'files':[f for f in d['files'] if f['operation'] in ['new','update']],'baseline':False,'summary':d.get('summary','')})
files={f['path']:f for c in cases for f in c['files']};anchors={path:'doc-'+str(i) for i,path in enumerate(files)}
index=json.loads((G/'00_start/catalog_index.json').read_text());nodes={x['id']:x for k in ['concepts','mechanisms'] for g in index[k] for x in g['items']}
def kind(f):
 m=meta(f['path']);b={'concept':'concept','mechanism':'relation','analysis_note':'event','event_collection':'event','event':'event','source_note':'source'}[m['type']]
 return {'concept':'subconcept','relation':'subrelation'}.get(b,b) if m.get('parent_ids') else b
def rich(value):
 if isinstance(value,list):value='\n'.join('- '+str(x) for x in value)
 elif not isinstance(value,str):value=json.dumps(value,ensure_ascii=False,indent=2)
 return M.render(value)
def render(path):
 p=G/path;raw=p.read_text();body=raw.split('---',2)[2];tokens=M.parse(body)
 for t in tokens:
  for c in [t]+(t.children or []):
   attr='src' if c.type=='image' else 'href';url=c.attrGet(attr)
   if not url:continue
   if c.type=='image':c.attrSet('loading','lazy')
   u=urlsplit(url)
   if u.scheme or u.netloc:continue
   target=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve();key=os.path.relpath(target,G)
   dest=('#'+anchors[key]+('--'+u.fragment if u.fragment else '')) if attr=='href' and key in anchors else os.path.relpath(target,R)+('#'+u.fragment if u.fragment else '')
   c.attrSet(attr,dest)
 out=M.renderer.render(tokens,M.options,{})
 return re.sub(r'(<(?:a|span)\b[^>]*?\bid=["\'])([^"\']+)',lambda m:m[1]+anchors[path]+'--'+m[2],out)
rows=[];details=[];changes=[]
for c in cases:
 cid='article-'+str(c['id']);flag='基准' if c['baseline'] else '本轮新增材料'
 rows.append(f'<tr><td>{flag}</td><td><a href="#{cid}">{E(c["title"])}</a></td><td>{len(c["files"])}</td></tr>')
 cards=[]
 for f in c['files']:
  op='新增' if f['operation']=='new' else '修改';label=K[kind(f)];why=f.get('why','')
  cards.append(f'<li><span class="tag">{op} · {label}</span> <a href="#{anchors[f["path"]]}">{E(f["title"])}</a>：{E(why)}</li>')
  if not c['baseline']:changes.append(f'- {op}{label}《{f["title"]}》：{why}')
 details.append(f'<section id="{cid}"><p class="eyebrow">{flag} · {c["id"]}</p><h2>{E(c["title"])}</h2>{rich(c["summary"])}<ul>{"".join(cards)}</ul></section>')
# One current document per path; repeated articles link to the same maintained content.
new_ids=set(nodes)-set(run['baseline_node_ids']);counts=Counter()
for id in new_ids:
 path=os.path.relpath((G/'00_start'/nodes[id]['path']).resolve(),G);f=files.get(path)
 if f:counts[K[kind(f)]]+=1
updates={f['id']:f for c in cases if not c['baseline'] for f in c['files'] if f['operation']=='update' and f['id'] in set(run['baseline_node_ids'])}
update_counts=Counter(K[kind(f)] for f in updates.values())
support_counts=Counter(K[kind(f)] for c in cases if not c['baseline'] for f in c['files'] if f['operation']=='new' and f['id'] not in nodes)
bodies=[]
for path,f in files.items():
 m=meta(path);label=K[kind(f)];parents=[]
 for pid in m.get('parent_ids',[]):
  x=nodes[pid];target=os.path.relpath((G/'00_start'/x['path']).resolve(),G);url='#'+anchors[target] if target in anchors else os.path.relpath(G/target,R)
  parents.append(f'<a href="{E(url)}">{E(x["name"])}</a>')
 parent='<p class="parent">父项：'+'、'.join(parents)+' · '+E(PARENT_LABELS.get(m.get('parent_relation',''),m.get('parent_relation','')))+'</p>' if parents else ''
 bodies.append(f'<details class="document" id="{anchors[path]}"><summary><span class="tag">{label}</span><strong>{E(f["title"])}</strong><small>{E(m["id"])}</small></summary><div class="doc">{parent}<p class="file"><a href="{E(os.path.relpath(G/path,R))}">Markdown原文</a></p>{render(path)}</div></details>')
complete=sum(x['status']=='adopted' for x in run['articles']);pending=27-complete
page=f'''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Wallstreet Scaling · 30篇</title><style>{css}</style><main><p class="eyebrow">FINANCIAL FOUNDATION / WALLSTREET SCALING</p><h1>从三篇到三十篇。</h1><p class="lead">保留三篇基准，新增27篇材料。每篇由一个继承完整上下文的agent制作，主agent审阅、去重后接入同一待整合工作图。</p><div class="stats"><div><b>{complete}</b><small>新增材料已采用</small></div><div><b>{pending}</b><small>待完成</small></div><div><b>{len(new_ids)}</b><small>本轮新增节点</small></div></div><p>本轮节点分类：{E('、'.join(k+str(v)+'个' for k,v in counts.items()) or '暂无')}。修改基准节点{len(updates)}个；新增事件{support_counts["事件分析"]}份、来源记录{support_counts["来源记录"]}份。工作图共{len(nodes)}节点，正式graph保持240节点。</p><nav><a href="SELECTION.md">选文</a><a href="PLAN.md">计划</a><a href="增量清单.md">本轮增量</a><a href="#documents">成品正文</a></nav><table><thead><tr><th>范围</th><th>材料</th><th>关联成品文件</th></tr></thead><tbody>{''.join(rows)}</tbody></table>{''.join(details)}<section id="documents"><h2>可持续维护的成品</h2><p>每份正文展示一次；不同文章引用同一对象时共用维护位置。展开查看正文。</p>{''.join(bodies)}</section></main></html>'''
(R/'报告.html').write_text(page)
text='# Wallstreet Scaling增量\n\n统计新增27篇相对三篇基准的采用内容。正式graph尚未接入。\n\n'
for c in cases:
 if c['baseline']:continue
 text+='## '+c['title']+'\n\n'
 for f in c['files']:
  op='新增' if f['operation']=='new' else '修改';text+=f'- {op}{K[kind(f)]}《{f["title"]}》：{f.get("why","")} [正文](<{os.path.relpath(G/f["path"],R)}>)\n'
 text+='\n'
(R/'增量清单.md').write_text(text)
(R/'report_counts.json').write_text(json.dumps({'accepted_additions':complete,'pending':pending,'new_nodes':len(new_ids),'node_types':dict(counts),'working_nodes':len(nodes),'unique_documents':len(files),'updated_nodes':len(updates),'updated_node_types':dict(update_counts),'new_support_documents':dict(support_counts)},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'accepted':complete,'pending':pending,'new_nodes':len(new_ids),'documents':len(files)},ensure_ascii=False))
