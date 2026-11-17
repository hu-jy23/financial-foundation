"""Build the local node-depth pilot reader from reviewed Markdown drafts."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
import os,re,html,json,yaml,subprocess
from difflib import SequenceMatcher
from bs4 import BeautifulSoup, Tag, NavigableString
from markdown_it import MarkdownIt
R=Path(__file__).resolve().parent;ROOT=R.parents[1];P=R/'cds_pilot';G=ROOT/'graph'
M=MarkdownIt('commonmark',{'html':True}).enable('table')
def E(s):return html.escape(str(s),quote=True)
paths=sorted((P/'drafts').rglob('*.md'))
legacy=['10_concepts/信用违约互换CDS.md','20_mechanisms/证券化中的风险转移与激励.md','30_events/次贷与金融危机中的CDS：风险集中、现金压力与违约结算.md','40_sources/S-HIST-CDS-CRISIS.md']
ordered=legacy+[str(p.relative_to(P/'drafts')) for p in paths if str(p.relative_to(P/'drafts')) not in legacy]
anchor={rel:'draft-'+str(i) for i,rel in enumerate(ordered)}
BASE=json.loads((P/'base.json').read_text())['graph_files']
DELIVERY=json.loads((P/'delivery.json').read_text());OPERATIONS={x['path']:x['operation'] for x in DELIVERY['files']}
REV_COMMIT=DELIVERY['revision']['base_commit'];REV_BASE={}
subprocess.run(['git','cat-file','-e',REV_COMMIT+'^{commit}'],cwd=ROOT,check=True,capture_output=True)
for rel in anchor:
 old=subprocess.run(['git','show',REV_COMMIT+':'+str((P/'drafts'/rel).relative_to(ROOT))],cwd=ROOT,capture_output=True,text=True)
 if old.returncode==0:REV_BASE[rel]=old.stdout
 elif rel in BASE:REV_BASE[rel]=BASE[rel]['text']
MOVED={('30_events/次贷与金融危机中的CDS：风险集中、现金压力与违约结算.md','ai-comparison'):('30_events/AI融资扩张中的CDS价格分化：2026年10月.md','ai-comparison')}
def render(path,origin=None,namespace='',body_override=None,link_prefix=''):
 raw=path.read_text();body=raw.split('---',2)[2] if raw.startswith('---\n') else raw
 if body_override is not None:body=body_override
 origin=origin or path;tokens=M.parse(body)
 for t in tokens:
  for c in [t]+(t.children or []):
   attr='src' if c.type=='image' else 'href';raw=c.attrGet(attr)
   if not raw:continue
   u=urlsplit(raw)
   if u.scheme or u.netloc:continue
   dest=Path(os.path.abspath(origin.parent/unquote(u.path))) if u.path else origin
   key=str(dest.relative_to(G)) if dest.is_relative_to(G) else str(dest.relative_to(P/'drafts')) if dest.is_relative_to(P/'drafts') else None
   fragment=u.fragment
   if (key,fragment) in MOVED:
    key,fragment=MOVED[(key,fragment)];c.attrSet('data-original-href',raw)
   if attr=='href' and key in anchor:link='#'+link_prefix+anchor[key]+('--'+fragment if fragment else '')
   elif not u.path and namespace:link='#'+namespace+'--'+u.fragment
   else:link=os.path.relpath(dest,R)+('#'+u.fragment if u.fragment else '')
   c.attrSet(attr,link)
 out=M.renderer.render(tokens,M.options,{})
 if namespace:out=re.sub(r'(<(?:a|span)\b[^>]*?\bid=["\'])([^"\']+)',lambda m:m[1]+namespace+'--'+m[2],out)
 return out
def body(text):return text.split('---',2)[2] if text.startswith('---\n') else text
def highlight_rewrite(soup,old,new):
 """Mark changed visible characters while preserving the new Markdown's HTML."""
 old_text=old.get_text();new_text=new.get_text()
 spans=[(j1,j2) for op,i1,i2,j1,j2 in SequenceMatcher(None,old_text,new_text,autojunk=False).get_opcodes() if op!='equal' and j1<j2]
 if not spans:
  new['class']=new.get('class',[])+['diff-mod'];return
 offset=0
 for node in list(new.find_all(string=True)):
  text=str(node);start=offset;offset+=len(text);cuts=[(max(a,start)-start,min(b,offset)-start) for a,b in spans if a<offset and b>start]
  if not cuts:continue
  pos=0
  for a,b in cuts:
   if pos<a:node.insert_before(NavigableString(text[pos:a]))
   marked=soup.new_tag('span',attrs={'class':'diff-mod','title':'本轮改写'});marked.string=text[a:b];node.insert_before(marked);pos=b
  if pos<len(text):node.insert_before(NavigableString(text[pos:]))
  node.extract()
def render_changes(path,rel,view,prefix):
 new_html=render(path,G/rel,prefix+anchor[rel],link_prefix=prefix)
 old=REV_BASE.get(rel) if view=='revision' else BASE.get(rel,{}).get('text')
 if old is None:
  return '<p class="change-label added-label">新增整篇</p><div class="draft-body diff-add new-entry">'+new_html+'</div>'
 # The comparison uses the saved pre-edit text, even after the formal graph changes.
 old_html=render(path,G/rel,prefix+anchor[rel],body_override=body(old),link_prefix=prefix)
 old_soup=BeautifulSoup(old_html,'html.parser');new_soup=BeautifulSoup(new_html,'html.parser')
 old_blocks=[x for x in old_soup.contents if isinstance(x,Tag)];new_blocks=[x for x in new_soup.contents if isinstance(x,Tag)];removed=[]
 for op,i1,i2,j1,j2 in SequenceMatcher(None,[str(x) for x in old_blocks],[str(x) for x in new_blocks],autojunk=False).get_opcodes():
  if op=='equal':continue
  before=old_blocks[i1:i2];after=new_blocks[j1:j2]
  if op in ['delete','replace']:
   for x in before:
    for el in [x]+list(x.find_all(True)):el.attrs.pop('id',None)
    removed.append(str(x))
  paired=min(len(before),len(after)) if op=='replace' else 0
  for n,x in enumerate(after):
   if n<paired and x.name==before[n].name:highlight_rewrite(new_soup,before[n],x)
   else:x['class']=x.get('class',[])+['diff-add']
 retired='<details class="diff-removals"><summary>删除／替换前内容（'+str(len(removed))+'段）</summary><div class="diff-remove">'+''.join(removed)+'</div></details>' if removed else ''
 return '<div class="draft-body">'+str(new_soup)+'</div>'+retired
views=[]
card_order=['C-S2-CDS','E-HIST-FINANCIAL-CRISIS-2007-2009','E-HIST-CDS-2007-2009','C-S2-AI-CDS','E-WS-3784900','R-BANKING-09','S-HIST-CDS-CRISIS-20261117']
for view,prefix in [('revision',''),('full','full-')]:
 cards=[]
 for p in paths:
  rel=str(p.relative_to(P/'drafts'));meta=yaml.safe_load(p.read_text().split('---',2)[1]);typ=meta['type'];kind={'concept':'概念修订','mechanism':'机制修订','event_collection':'危机共同事件','analysis_note':'事件分析','source_note':'来源核读'}.get(typ,'研究笔记')
  if meta['id']=='E-HIST-CDS-2007-2009':kind='CDS历史专题'
  opened=' open' if typ in ['concept','event_collection','analysis_note'] else ''
  operation='modify' if rel in (REV_BASE if view=='revision' else BASE) else 'create'
  cards.append((card_order.index(meta['id']),f'<details class="document" id="{prefix+anchor[rel]}" data-diff-kind="{operation}" data-path="{E(rel)}"{opened}><summary><span class="tag">{kind}</span><strong>{E(meta["title"])}</strong></summary><div class="doc"><p class="file"><a href="{E(os.path.relpath(p,R))}">独立制作稿</a> · 拟归属 graph/{E(rel)}</p>{render_changes(p,rel,view,prefix)}</div></details>'))
 note=f'本次返修对照上次审阅稿（Git {REV_COMMIT[:7]}）；新纳入修改的AI两页对照该时点正式原稿。' if view=='revision' else '全部制作增量对照正式graph原稿（cds_pilot/base.json；输入提交3a3f44e）。'
 hidden='' if view=='revision' else ' hidden'
 views.append(f'<div class="comparison-view" data-view="{view}"{hidden}><p class="diff-note">{note} 删除及替换前内容在各稿末尾折叠展示。</p>'+''.join(c for _,c in sorted(cards))+'</div>')
comparison_views=''.join(views)
research=render(P/'research.md',namespace='research')
selection=render(R/'selection/SELECTION.md',namespace='selection')
css='''*{box-sizing:border-box}body{margin:0;background:#f4f1e9;color:#20352f;font-family:system-ui,"Noto Sans CJK SC",sans-serif;line-height:1.9}main{max-width:1140px;margin:auto;padding:56px 28px}h1{font-size:42px;line-height:1.4}h2{font-size:27px;margin-top:40px}h3{font-size:22px}.lead{font-size:18px;color:#53665d}.eyebrow{font-size:12px;letter-spacing:2px;color:#28715c}.stats{display:flex;gap:34px;margin:26px 0}.stats b{display:block;font:34px serif}.stats small,.file{font-size:13px;color:#64796e}nav{display:flex;gap:20px;flex-wrap:wrap;border-block:1px solid #d3d9d0;padding:16px 0}a{color:#246c58;overflow-wrap:anywhere;text-underline-offset:4px}section{margin:42px 0}.document{background:#fffcf6;border:1px solid #d8ded4;margin:20px 0}.document>summary{cursor:pointer;display:flex;gap:14px;flex-wrap:wrap;padding:18px 22px}.doc{padding:0 24px 24px;overflow-wrap:anywhere}.doc h1{font-size:29px}.doc h2{font-size:23px}.tag{font-size:12px;color:#39735e;border:1px solid #b7c9b9;padding:0 7px}.track{display:grid;grid-template-columns:150px 1fr;gap:16px;background:#eef0e8;padding:15px;margin:10px 0}.track strong{color:#315f51}table{border-collapse:collapse;display:block;overflow-x:auto;max-width:100%;font-size:14px}th,td{border:1px solid #d6ddd2;padding:8px 11px;text-align:left}img,svg{max-width:100%;height:auto}blockquote{border-left:3px solid #c5d2c1;margin-left:0;padding-left:18px;color:#586a5a}pre{overflow-x:auto;background:#eef0e8;padding:15px}code{font-family:monospace;font-size:.9em}@media(max-width:600px){main{padding:26px 16px}h1{font-size:31px}.stats{gap:25px}.track{grid-template-columns:1fr;gap:4px}.doc{padding:0 15px 18px}table{font-size:12px}}'''
css+='''[hidden]{display:none!important}.view-switch{display:flex;flex-wrap:wrap;gap:10px;margin:20px 0}.view-switch button{font:inherit;padding:8px 14px;background:#fffaf2;border:1px solid #b7c9b9;color:#315f51;cursor:pointer}.view-switch button[aria-pressed="true"]{background:#315f51;color:white}.diff-add{color:#17603d;background:#eaf5ec}.draft-body>.diff-add{border-left:3px solid #398552;padding:8px 12px}.diff-mod{color:#8b4200;background:#ffedcf;border-bottom:1px dotted #ad6b22}.diff-remove{color:#9d303b;background:#fdeef0;padding:10px 16px;text-decoration:line-through}.diff-remove a{color:inherit}.diff-removals{margin:24px 0;border:1px solid #e5b8bd;padding:10px 14px}.diff-removals>summary{cursor:pointer;color:#9d303b}.new-entry{border-left:3px solid #398552;padding:8px 16px}.new-entry a{color:inherit}.change-label{font-size:13px;font-weight:600}.added-label{color:#17603d}.diff-legend{display:flex;gap:12px;flex-wrap:wrap;margin:18px 0 26px}.diff-legend span{padding:4px 10px;border-radius:3px;font-size:13px}.diff-legend .unchanged{border:1px solid #d8ded4}.diff-note{font-size:13px;color:#64796e}'''
script='''function selectView(mode){document.querySelectorAll('.comparison-view').forEach(x=>x.hidden=x.dataset.view!==mode);document.querySelectorAll('[data-select-view]').forEach(x=>x.setAttribute('aria-pressed',String(x.dataset.selectView===mode)));}function reveal(){const id=decodeURIComponent(location.hash.slice(1));const el=document.getElementById(id);if(!el)return;const pane=el.closest('.comparison-view');if(pane)selectView(pane.dataset.view);for(let p=el;p;p=p.parentElement){if(p.tagName==='DETAILS')p.open=true;}requestAnimationFrame(()=>el.scrollIntoView({block:'start'}));}addEventListener('hashchange',reveal);addEventListener('DOMContentLoaded',()=>{document.querySelectorAll('[data-select-view]').forEach(x=>x.addEventListener('click',()=>selectView(x.dataset.selectView)));selectView('revision');reveal();});'''
page=f'''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>节点纵深研究 · CDS试点</title><style>{css}</style><main><p class="eyebrow">FINANCIAL FOUNDATION / NODE DEPTH / 2026.11.17</p><h1>沿CDS回到危机，再理解今天的类比。</h1><p class="lead">本报告展示实际研究、拟接入的完整制作稿及下一批任务准备。当前正式graph保持275节点；制作稿供审阅，尚未接入。</p><div class="stats"><div><b>1</b><small>完成研究的试点</small></div><div><b>15</b><small>概念选题，含CDS</small></div><div><b>5</b><small>机制选题</small></div></div><nav><a href="#findings">研究与认识</a><a href="#drafts">实际制作稿</a><a href="#selection">15概念＋5机制</a><a href="selection/GUIDE.md">Subagent制作说明</a></nav><section id="findings">{research}</section><section><h2>三种身份，分别追踪</h2><p>本库示意；具体合同、时间与证据见下方历史材料。箭头表示本试点追踪的联系。</p><div class="track"><strong>AIG：保护卖方</strong><span>结构化信用敞口 → 合同估值／评级条件 → 追加抵押与现金需求 → 融资约束</span></div><div class="track"><strong>雷曼：参考实体</strong><span>参考实体违约 → 信用事件处理与拍卖 → 抵销后的合约现金结算</span></div><div class="track"><strong>雷曼：交易对手</strong><span>交易对手破产 → 合同终止与净额安排 → 头寸替换、抵押及对手方损失</span></div></section><section id="drafts"><h2>实际制作稿</h2><div class="diff-legend" aria-label="增量颜色图例"><span class="diff-add">绿色 · 新增</span><span class="diff-mod">橙色 · 改写</span><span class="diff-remove">红色 · 删除／替换前原文</span><span class="unchanged">原色 · 未改</span></div><div class="view-switch" role="group" aria-label="选择增量比对基线"><button type="button" data-select-view="revision" aria-pressed="true">本次返修 · 对照上次报告</button><button type="button" data-select-view="full" aria-pressed="false">全部增量 · 对照正式graph</button></div><details class="document"><summary>对照：正式graph原有的CDS历史段落</summary><div class="doc">{render(G/'10_concepts/信用违约互换CDS.md',namespace='before',body_override=BASE['10_concepts/信用违约互换CDS.md']['text'].split('## 历史与关系入口',1)[1].split('## 来源',1)[0])}</div></details>{comparison_views}</section><section id="selection"><h2>后续任务准备</h2>{selection}</section><footer><a href="README.md">工作区说明</a> · <a href="ROOT_REVIEW.md">主agent核读</a> · <a href="cds_pilot/review_notes.md">试点核读与审阅记录</a> · <a href="cds_pilot/sources.json">来源清单</a></footer></main><script>{script}</script></html>'''
(R/'报告.html').write_text(page)
print(json.dumps({'draft_documents':len(paths),'html':str(R/'报告.html')},ensure_ascii=False))
