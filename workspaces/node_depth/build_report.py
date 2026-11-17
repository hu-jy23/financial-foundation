"""Build the local node-depth pilot reader from reviewed Markdown drafts."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
import os,re,html,json,yaml
from markdown_it import MarkdownIt
R=Path(__file__).resolve().parent;ROOT=R.parents[1];P=R/'cds_pilot';G=ROOT/'graph'
M=MarkdownIt('commonmark',{'html':True}).enable('table')
def E(s):return html.escape(str(s),quote=True)
paths=sorted((P/'drafts').rglob('*.md'))
anchor={str(p.relative_to(P/'drafts')):'draft-'+str(i) for i,p in enumerate(paths)}
def render(path,origin=None,namespace='',body_override=None):
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
   if attr=='href' and key in anchor:link='#'+anchor[key]+('--'+u.fragment if u.fragment else '')
   elif not u.path and namespace:link='#'+namespace+'--'+u.fragment
   else:link=os.path.relpath(dest,R)+('#'+u.fragment if u.fragment else '')
   c.attrSet(attr,link)
 out=M.renderer.render(tokens,M.options,{})
 if namespace:out=re.sub(r'(<(?:a|span)\b[^>]*?\bid=["\'])([^"\']+)',lambda m:m[1]+namespace+'--'+m[2],out)
 return out
cards=[]
for p in paths:
 rel=str(p.relative_to(P/'drafts'));raw=p.read_text();meta=yaml.safe_load(raw.split('---',2)[1]) if raw.startswith('---\n') else {};typ=meta.get('type','note');kind={'concept':'概念修订','mechanism':'机制修订','event_collection':'历史材料集','analysis_note':'事件分析','event':'历史事件','source_note':'来源核读'}.get(typ,'研究笔记')
 opened=' open' if typ in ['concept','event_collection','event','analysis_note'] else ''
 cards.append(({'concept':0,'event_collection':1,'event':1,'analysis_note':1,'mechanism':2,'source_note':3}.get(typ,4),f'<details class="document" id="{anchor[rel]}"{opened}><summary><span class="tag">{kind}</span><strong>{E(meta.get("title",p.stem))}</strong></summary><div class="doc"><p class="file"><a href="{E(os.path.relpath(p,R))}">独立制作稿</a> · 拟归属 graph/{E(rel)}</p>{render(p,G/rel,anchor[rel])}</div></details>'))
research=render(P/'research.md',namespace='research')
selection=render(R/'selection/SELECTION.md',namespace='selection')
css='''*{box-sizing:border-box}body{margin:0;background:#f4f1e9;color:#20352f;font-family:system-ui,"Noto Sans CJK SC",sans-serif;line-height:1.9}main{max-width:1140px;margin:auto;padding:56px 28px}h1{font-size:42px;line-height:1.4}h2{font-size:27px;margin-top:40px}h3{font-size:22px}.lead{font-size:18px;color:#53665d}.eyebrow{font-size:12px;letter-spacing:2px;color:#28715c}.stats{display:flex;gap:34px;margin:26px 0}.stats b{display:block;font:34px serif}.stats small,.file{font-size:13px;color:#64796e}nav{display:flex;gap:20px;flex-wrap:wrap;border-block:1px solid #d3d9d0;padding:16px 0}a{color:#246c58;overflow-wrap:anywhere;text-underline-offset:4px}section{margin:42px 0}.document{background:#fffcf6;border:1px solid #d8ded4;margin:20px 0}.document>summary{cursor:pointer;display:flex;gap:14px;flex-wrap:wrap;padding:18px 22px}.doc{padding:0 24px 24px;overflow-wrap:anywhere}.doc h1{font-size:29px}.doc h2{font-size:23px}.tag{font-size:12px;color:#39735e;border:1px solid #b7c9b9;padding:0 7px}.track{display:grid;grid-template-columns:150px 1fr;gap:16px;background:#eef0e8;padding:15px;margin:10px 0}.track strong{color:#315f51}table{border-collapse:collapse;display:block;overflow-x:auto;max-width:100%;font-size:14px}th,td{border:1px solid #d6ddd2;padding:8px 11px;text-align:left}img,svg{max-width:100%;height:auto}blockquote{border-left:3px solid #c5d2c1;margin-left:0;padding-left:18px;color:#586a5a}pre{overflow-x:auto;background:#eef0e8;padding:15px}code{font-family:monospace;font-size:.9em}@media(max-width:600px){main{padding:26px 16px}h1{font-size:31px}.stats{gap:25px}.track{grid-template-columns:1fr;gap:4px}.doc{padding:0 15px 18px}table{font-size:12px}}'''
script='''function reveal(){const id=decodeURIComponent(location.hash.slice(1));const el=document.getElementById(id);if(!el)return;for(let p=el;p;p=p.parentElement){if(p.tagName==='DETAILS')p.open=true;}requestAnimationFrame(()=>el.scrollIntoView({block:'start'}));}addEventListener('hashchange',reveal);addEventListener('DOMContentLoaded',reveal);'''
page=f'''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>节点纵深研究 · CDS试点</title><style>{css}</style><main><p class="eyebrow">FINANCIAL FOUNDATION / NODE DEPTH / 2026.11.17</p><h1>沿CDS回到危机，再理解今天的类比。</h1><p class="lead">本报告展示实际研究、拟接入的完整制作稿及下一批任务准备。当前正式graph保持275节点；制作稿供审阅，尚未接入。</p><div class="stats"><div><b>1</b><small>完成研究的试点</small></div><div><b>15</b><small>概念选题，含CDS</small></div><div><b>5</b><small>机制选题</small></div></div><nav><a href="#findings">研究与认识</a><a href="#drafts">实际制作稿</a><a href="#selection">15概念＋5机制</a><a href="selection/GUIDE.md">Subagent制作说明</a></nav><section id="findings">{research}</section><section><h2>三种身份，分别追踪</h2><p>本库示意；具体合同、时间与证据见下方历史材料。箭头表示本试点追踪的联系。</p><div class="track"><strong>AIG：保护卖方</strong><span>结构化信用敞口 → 合同估值／评级条件 → 追加抵押与现金需求 → 融资约束</span></div><div class="track"><strong>雷曼：参考实体</strong><span>参考实体违约 → 信用事件处理与拍卖 → 抵销后的合约现金结算</span></div><div class="track"><strong>雷曼：交易对手</strong><span>交易对手破产 → 合同终止与净额安排 → 头寸替换、抵押及对手方损失</span></div></section><section id="drafts"><h2>实际制作稿</h2><details class="document"><summary>对照：现行CDS的历史段落</summary><div class="doc">{render(G/'10_concepts/信用违约互换CDS.md',namespace='before',body_override=(G/'10_concepts/信用违约互换CDS.md').read_text().split('## 历史与关系入口',1)[1].split('## 来源',1)[0])}</div></details>{''.join(card for _,card in sorted(cards,key=lambda x:x[0]))}</section><section id="selection"><h2>后续任务准备</h2>{selection}</section><footer><a href="README.md">工作区说明</a> · <a href="ROOT_REVIEW.md">主agent核读</a> · <a href="cds_pilot/review_notes.md">试点核读与审阅记录</a> · <a href="cds_pilot/sources.json">来源清单</a></footer></main><script>{script}</script></html>'''
(R/'报告.html').write_text(page)
print(json.dumps({'draft_documents':len(paths),'html':str(R/'报告.html')},ensure_ascii=False))
