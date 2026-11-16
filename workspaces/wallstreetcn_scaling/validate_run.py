from pathlib import Path
from urllib.parse import urlsplit,unquote
from collections import Counter
import json,re,yaml
from functools import lru_cache
from markdown_it import MarkdownIt
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parent;G=R.parents[1]/'graph' if (R/'formal_integration.json').exists() else R.parent/'step2_articles/graph';run=json.loads((R/'run.json').read_text());idx=json.loads((G/'00_start/catalog_index.json').read_text());parser=MarkdownIt('commonmark',{'html':True});cache={};issues=[];checks=0

@lru_cache(None)
def canonical(p):return p.resolve()
@lru_cache(None)
def exists(p):return p.exists()

def content(p):
 p=canonical(p)
 if p not in cache:cache[p]=p.read_text()
 return cache[p]
def meta(p):
 s=content(p);return yaml.safe_load(s.split('---',2)[1]) if s.startswith('---\n') else {}
concepts={x['id']:x for g in idx['concepts'] for x in g['items']};relations={x['id']:x for g in idx['mechanisms'] for x in g['items']};nodes={**concepts,**relations};targets=set()
deliveries=[json.loads((R.parent/'step2_articles/deliveries'/f'{name}.json').read_text()) for name in ['ai','korea','basis']]
for a in run['articles']:
 if a['status']=='adopted':deliveries.append(json.loads((R/'articles'/str(a['article_id'])/'delivery.json').read_text()))
for d in deliveries:
 for f in d['files']:
  if f['operation'] in ['new','update']:
   p=G/f['path'];targets.add(p);m=meta(p)
   if any(m.get(k)!=f[k] for k in ['id','title','type']):issues.append({'metadata_mismatch':f['path']})
   expected={'concept':'subconcept' if m.get('parent_ids') else 'concept','mechanism':'subrelation' if m.get('parent_ids') else 'relation','analysis_note':'event','event':'event','event_collection':'event','source_note':'source'}.get(m.get('type'))
   if f.get('entry_kind')!=expected:issues.append({'entry_kind_mismatch':f['path'],'expected':expected})
for id,x in nodes.items():
 p=canonical(G/'00_start'/x['path']);m=meta(p)
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
 m=meta(p)
 for nid in m.get('node_ids',[]):
  if nid not in concepts:issues.append({'unknown_event_node':nid,'file':str(p.relative_to(G))})
 for rid in m.get('related_mechanism_ids',[]):
  if rid not in relations:issues.append({'unknown_event_relation':rid,'file':str(p.relative_to(G))})
 for t in parser.parse(content(p)):
  for c in [t]+(t.children or []):
   url=c.attrGet('href') or c.attrGet('src')
   if not url:continue
   u=urlsplit(url)
   if u.scheme or u.netloc:continue
   checks+=1;target=canonical(p.parent/unquote(u.path)) if u.path else canonical(p)
   if not exists(target):issues.append({'file':str(p.relative_to(G)),'missing':url});continue
   if u.fragment and target.suffix=='.md':
    s=content(target);frag=unquote(u.fragment);heads=re.findall(r'^#{1,6}\s+(.+?)\s*#*$',s,re.M);slugs={re.sub(r'[^\w\-\s\u3400-\u9fff]','',h.lower()).replace(' ','-') for h in heads}
    if not re.search(r'(?:id|name)=["\']'+re.escape(frag)+r'["\']',s) and frag not in slugs:issues.append({'file':str(p.relative_to(G)),'anchor':url})
coverage_checks=0
coverage_items=sum(len(d.get('coverage',[])) for d in deliveries)
for d in deliveries:
 for item in d.get('coverage',[]):
  references=item.get('paths', [item['path']] if item.get('path') else [])
  for reference in references:
   coverage_checks+=1;u=urlsplit(reference);target=canonical(G/unquote(u.path))
   if not exists(target):issues.append({'coverage_missing':reference,'article_id':d['article_id']});continue
   if u.fragment:
    fragment=unquote(u.fragment)
    if not re.search(r'(?:id|name)=["\']'+re.escape(fragment)+r'["\']',content(target)):
     issues.append({'coverage_anchor':reference,'article_id':d['article_id']})
for p in targets | {G/'00_start/CONCEPT_IMPORT_LIST.md',G/'00_start/MECHANISM_IMPORT_LIST.md',R/'增量清单.md'}:
 if not p.exists():continue
 for raw in re.findall(r'!?\[[^\]\n]*\]\(([^<\n][^\n]*?)\)',content(p)):
  if ' ' in raw and not urlsplit(raw).scheme and (p.parent/unquote(raw)).exists():issues.append({'unparsed_link_with_space':str(p),'target':raw})
p=R/'报告.html'
if p.exists():
 soup=BeautifulSoup(p.read_text(),'html.parser');ids=[e['id'] for e in soup.select('[id]')]
 if len(ids)!=len(set(ids)):issues.append('duplicate HTML anchors')
 for e in soup.select('[href],[src]'):
  u=urlsplit(e.get('href',e.get('src','')))
  if u.scheme or u.netloc:continue
  if u.path and not exists(R/unquote(u.path)):issues.append({'report_missing':u.path})
  if not u.path and u.fragment and unquote(u.fragment) not in ids:issues.append({'report_anchor':u.fragment})
result={'accepted':sum(a['status']=='adopted' for a in run['articles']),'total_articles_checked':len(deliveries),'working_nodes':len(nodes),'changed_documents_checked':len(targets),'links_checked':checks,'coverage_items_checked':coverage_items,'coverage_references_checked':coverage_checks,'issues':issues,'passed':not issues};(R/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(0 if not issues else 1)
