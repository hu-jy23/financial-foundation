from pathlib import Path
from urllib.parse import urlsplit,unquote
from collections import Counter
import json,re,yaml
from markdown_it import MarkdownIt
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parent;G=R.parent/'step2_articles/graph';run=json.loads((R/'run.json').read_text());idx=json.loads((G/'00_start/catalog_index.json').read_text());parser=MarkdownIt('commonmark',{'html':True});cache={};issues=[];checks=0

def content(p):
 p=p.resolve()
 if p not in cache:cache[p]=p.read_text()
 return cache[p]
def meta(p):
 s=content(p);return yaml.safe_load(s.split('---',2)[1]) if s.startswith('---\n') else {}
concepts={x['id']:x for g in idx['concepts'] for x in g['items']};relations={x['id']:x for g in idx['mechanisms'] for x in g['items']};nodes={**concepts,**relations};targets=set()
for a in run['articles']:
 if a['status']!='adopted':continue
 d=json.loads((R/'articles'/str(a['article_id'])/'delivery.json').read_text())
 for f in d['files']:
  if f['operation'] in ['new','update']:
   p=G/f['path'];targets.add(p);m=meta(p)
   if any(m.get(k)!=f[k] for k in ['id','title','type']):issues.append({'metadata_mismatch':f['path']})
for id,x in nodes.items():
 p=(G/'00_start'/x['path']).resolve();m=meta(p)
 if m.get('id')!=id:issues.append({'index_id_mismatch':id})
 for parent in m.get('parent_ids',[]):
  if parent not in (concepts if m['type']=='concept' else relations):issues.append({'unknown_parent':parent,'id':id})
 for nid in m.get('node_ids',[]):
  if nid not in concepts:issues.append({'unknown_node':nid,'id':id})
 for rid in m.get('related_mechanism_ids',[]):
  if rid not in relations:issues.append({'unknown_relation':rid,'id':id})
 if m['type']=='mechanism':
  for lg in m.get('logic_groups',[]):
   if f'id="{lg["anchor"]}"' not in content(p):issues.append({'missing_logic_anchor':id,'anchor':lg['anchor']})
for p in targets:
 for t in parser.parse(content(p)):
  for c in [t]+(t.children or []):
   url=c.attrGet('href') or c.attrGet('src')
   if not url:continue
   u=urlsplit(url)
   if u.scheme or u.netloc:continue
   checks+=1;target=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve()
   if not target.exists():issues.append({'file':str(p.relative_to(G)),'missing':url});continue
   if u.fragment and target.suffix=='.md':
    s=content(target);frag=unquote(u.fragment);heads=re.findall(r'^#{1,6}\s+(.+?)\s*#*$',s,re.M);slugs={re.sub(r'[^\w\-\s\u3400-\u9fff]','',h.lower()).replace(' ','-') for h in heads}
    if not re.search(r'(?:id|name)=["\']'+re.escape(frag)+r'["\']',s) and frag not in slugs:issues.append({'file':str(p.relative_to(G)),'anchor':url})
p=R/'报告.html'
if p.exists():
 soup=BeautifulSoup(p.read_text(),'html.parser');ids=[e['id'] for e in soup.select('[id]')]
 if len(ids)!=len(set(ids)):issues.append('duplicate HTML anchors')
 for e in soup.select('[href],[src]'):
  u=urlsplit(e.get('href',e.get('src','')))
  if u.scheme or u.netloc:continue
  if u.path and not (R/unquote(u.path)).exists():issues.append({'report_missing':u.path})
  if not u.path and u.fragment and unquote(u.fragment) not in ids:issues.append({'report_anchor':u.fragment})
result={'accepted':sum(a['status']=='adopted' for a in run['articles']),'working_nodes':len(nodes),'changed_documents_checked':len(targets),'links_checked':checks,'issues':issues,'passed':not issues};(R/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(0 if not issues else 1)
