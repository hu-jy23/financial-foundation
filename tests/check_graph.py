#!/usr/bin/env python3
"""Validate the current graph; optionally verify an adopted batch's preservation record."""
from pathlib import Path
from collections import Counter
from urllib.parse import urlsplit, unquote
from functools import lru_cache
import argparse, hashlib, json, os, re
import yaml
from markdown_it import MarkdownIt

ROOT=Path(__file__).resolve().parents[1]
G=ROOT/'graph'
parser=argparse.ArgumentParser()
parser.add_argument('--integration',type=Path)
parser.add_argument('--output',type=Path,default=ROOT/'docs/GRAPH_CHECK.json')
args=parser.parse_args()
issues=[]
def digest(s):return hashlib.sha256(s.encode()).hexdigest()
@lru_cache(None)
def content(p):return p.read_text()
def meta(p):return yaml.safe_load(content(p).split('---',2)[1]) or {}
def metadata_hash(m):
 m={k:v for k,v in m.items() if k not in ['status','editing_status','formal_integrated_on','formal_integration_batch']}
 return digest(json.dumps(m,ensure_ascii=False,sort_keys=True,default=str))
idx=json.loads((G/'00_start/catalog_index.json').read_text())
nodes={};bykind={}
for kind in ['concepts','mechanisms']:
 items=[x for group in idx[kind] for x in group['items']];bykind[kind]={x['id']:x for x in items}
 if len(items)!=len(bykind[kind]):issues.append({'duplicate_index_id':kind})
 counts=idx['counts'][kind]
 actual={'items':len(items),'groups':len(idx[kind]),'p0':sum(x.get('priority')=='P0' for x in items),'complete':sum(x.get('status')=='complete' for x in items),'pending':sum(x.get('status')=='pending' for x in items)}
 if any(counts.get(k)!=v for k,v in actual.items()):issues.append({'counts_mismatch':kind,'actual':actual})
 nodes.update(bykind[kind])
all_md=list(G.rglob('*.md'));ids={};node_meta={}
for p in all_md:
 s=content(p)
 if not s.startswith('---\n'):continue
 m=meta(p)
 if not m.get('id'):continue
 if m['id'] in ids:issues.append({'duplicate_document_id':m['id']})
 ids[m['id']]=p
 if m.get('type') in ['concept','mechanism'] and p.parent.name in ['10_concepts','20_mechanisms']:node_meta[m['id']]=m
for ident,x in nodes.items():
 p=Path(os.path.abspath(G/'00_start'/x['path']))
 if not p.exists():issues.append({'missing_node':ident});continue
 m=meta(p)
 if m.get('id')!=ident or m.get('title')!=x['name']:issues.append({'node_identity':ident})
 if m.get('status')=='step2_draft' or m.get('editing_status')=='step2_draft':issues.append({'unpromoted_draft':ident})
 expected='concept' if ident in bykind['concepts'] else 'mechanism'
 if m.get('type')!=expected:issues.append({'wrong_type':ident})
 for key in ['node_ids','related_mechanism_ids','logic_groups','parent_ids','parent_relation']:
  if key in m and x.get(key)!=m[key]:issues.append({'index_metadata':ident,'field':key})
 for key,allowed in [('node_ids',bykind['concepts']),('related_mechanism_ids',bykind['mechanisms']),('parent_ids',bykind['concepts'] if expected=='concept' else bykind['mechanisms'])]:
  for ref in m.get(key,[]):
   if ref not in allowed:issues.append({'unknown_reference':ref,'node':ident,'field':key})
 for lg in m.get('logic_groups',[]):
  if f'id="{lg["anchor"]}"' not in content(p):issues.append({'missing_logic_anchor':ident,'anchor':lg['anchor']})
  for ref in lg.get('node_ids',[]):
   if ref not in bykind['concepts']:issues.append({'unknown_logic_object':ref,'node':ident})
 if content(G/'00_start'/('CONCEPT_IMPORT_LIST.md' if expected=='concept' else 'MECHANISM_IMPORT_LIST.md')).count(f'id="{ident}"')!=1:issues.append({'directory_anchor':ident})
if set(node_meta)!=set(nodes):issues.append({'unregistered_nodes':sorted(set(node_meta)-set(nodes)),'missing_node_pages':sorted(set(nodes)-set(node_meta))})
visiting=set();done=set()
def visit(ident):
 if ident in visiting:issues.append({'parent_cycle':ident});return
 if ident in done:return
 visiting.add(ident)
 for p in node_meta[ident].get('parent_ids',[]):
  if p in node_meta:visit(p)
 visiting.remove(ident);done.add(ident)
for i in node_meta:visit(i)
for key in ['excluded_concepts','excluded_mechanisms','deferred']:
 if idx['counts'][key]['items']!=len(idx[key]):issues.append({'exclusion_count':key})
 if set(x['id'] for x in idx[key])&set(nodes):issues.append({'active_node_still_excluded':key})
if idx.get('workspace_only'):issues.append('Formal index marked workspace_only')
# Check graph links and fragments, including table and raw HTML links.
known=set()
for parent,dirs,names in os.walk(ROOT):
 dirs[:]=[d for d in dirs if d not in ['.git','__pycache__']]
 known.add(parent);known.update(str(Path(parent)/n) for n in names)
md=MarkdownIt('commonmark',{'html':True}).enable('table');links=0
@lru_cache(None)
def anchors(p):
 s=content(p);explicit=set(re.findall(r'(?:id|name)=["\']([^"\']+)',s))
 headings=re.findall(r'^#{1,6}\s+(.+?)\s*#*$',s,re.M)
 return explicit|{re.sub(r'[^\w\-\s\u3400-\u9fff]','',h.lower()).replace(' ','-') for h in headings}
for p in all_md:
 s=content(p)
 s=re.sub(r'\\\[.*?\\\]','',s,flags=re.S)
 s=re.sub(r'\\\(.*?\\\)','',s,flags=re.S)
 urls=set(re.findall(r'\b(?:href|src)\s*=\s*["\']([^"\']+)',s))
 for t in md.parse(s):
  for child in [t]+(t.children or []):
   u=child.attrGet('href') or child.attrGet('src')
   if u:urls.add(u)
 for raw in urls:
  u=urlsplit(raw)
  if u.scheme or u.netloc:continue
  target=Path(os.path.abspath(p.parent/unquote(u.path))) if u.path else p;links+=1
  if str(target) not in known:issues.append({'broken_link':raw,'file':str(p.relative_to(G))});continue
  if u.fragment and target.suffix=='.md' and unquote(u.fragment) not in anchors(target):issues.append({'missing_fragment':raw,'file':str(p.relative_to(G))})
preservation=None
if args.integration:
 batch=json.loads(args.integration.read_text());checked=0
 for row in batch['files']:
  p=G/row['path'];s=content(p)
  if digest(s)!=row['formal_sha256'] or digest(s.split('---',2)[2])!=row['body_sha256']:issues.append({'promoted_content_changed':row['path']})
  if metadata_hash(meta(p))!=row['preserved_metadata_sha256']:issues.append({'promoted_metadata_changed':row['path']})
  checked+=1
 for rel,sha in batch['protected_instruction_sha256'].items():
  if hashlib.sha256((G/rel).read_bytes()).hexdigest()!=sha:issues.append({'instruction_overwritten':rel})
 preservation={'adopted_files_checked':checked,'original_authors_sources_and_evidence_dates_retained':not any('promoted_metadata_changed' in i for i in issues if isinstance(i,dict))}
result={'concepts':len(bykind['concepts']),'mechanisms':len(bykind['mechanisms']),'nodes':len(nodes),'subconcepts':sum(bool(x.get('parent_ids')) for x in bykind['concepts'].values()),'documents':len(all_md),'local_links_checked':links,'preservation':preservation,'issues':issues,'passed':not issues}
args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(0 if not issues else 1)
