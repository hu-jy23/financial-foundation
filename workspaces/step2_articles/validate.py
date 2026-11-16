from pathlib import Path
from hashlib import sha256
import json, re
from urllib.parse import unquote, urlsplit
import yaml
from markdown_it import MarkdownIt

R=Path(__file__).resolve().parent
if (R.parent/'wallstreetcn_scaling/formal_integration.json').exists():
 import os,sys
 os.execv(sys.executable,[sys.executable,str(R.parents[1]/'tests/check_graph.py'),'--integration',str(R.parent/'wallstreetcn_scaling/formal_integration.json'),'--output',str(R/'validation.json')])
G=R/'graph'
baseline=json.loads((R/'baseline.json').read_text())
formal=R.parents[1]/baseline['source']
def digest(p): return sha256(p.read_bytes()).hexdigest()
def fm(p):
 s=p.read_text()
 if s.startswith('---\n'):
  return yaml.safe_load(s.split('---',2)[1]) or {}
 return {}
formal_now={str(p.relative_to(formal)):digest(p) for p in formal.rglob('*') if p.is_file()}
formal_changes=[s for s in set(formal_now)|set(baseline['files']) if formal_now.get(s)!=baseline['files'].get(s)]
allowed=baseline.get('authorized_instruction_updates',{})
authorized_changes=[s for s in formal_changes if formal_now.get(s)==allowed.get(s,{}).get('sha256')]
unexpected_changes=[s for s in formal_changes if s not in authorized_changes]
changed=[]
for p in G.rglob('*'):
 if p.is_file() and digest(p)!=baseline['files'].get(str(p.relative_to(G))):changed.append(p)
md=MarkdownIt('commonmark',{'html':True})
issues=[]; ids={}
for p in G.rglob('*.md'):
 d=fm(p)
 if d.get('id'):
  if d['id'] in ids: issues.append({'file':str(p.relative_to(G)),'duplicate_id':d['id']})
  ids[d['id']]=str(p.relative_to(G))
checked=0
for p in changed:
 if p.suffix!='.md':continue
 for t in md.parse(p.read_text()):
  for c in [t]+(t.children or []):
   url=c.attrGet('href') or c.attrGet('src')
   if not url:continue
   u=urlsplit(url)
   if u.scheme or u.netloc:continue
   checked+=1; target=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve()
   if not target.exists():issues.append({'file':str(p.relative_to(G)),'broken_link':url});continue
   if u.fragment and target.suffix=='.md':
    content=target.read_text();frag=unquote(u.fragment)
    # Explicit anchors and heading anchors, including Markdown-rendered Chinese text.
    heads=re.findall(r'^#{1,6}\s+(.+?)\s*#*$',content,re.M)
    slugs={re.sub(r'[^\w\-\s\u3400-\u9fff]','',h.lower()).replace(' ','-') for h in heads}
    if not re.search(r'(?:id|name)=["\']'+re.escape(frag)+r'["\']',content) and frag not in slugs:
     issues.append({'file':str(p.relative_to(G)),'missing_anchor':url})
cat=json.loads((G/'00_start/catalog_index.json').read_text())
known={x['id'] for kind in ['concepts','mechanisms'] for group in cat[kind] for x in group['items']}
for kind in ['concepts','mechanisms']:
 for group in cat[kind]:
  for x in group['items']:
   for nid in x.get('node_ids',[]):
    if nid not in known:issues.append({'catalog_item':x['id'],'unknown_node_id':nid})
   p=(G/'00_start'/x['path']).resolve() if x.get('path') else None
   if p and (not p.exists() or fm(p).get('id')!=x['id']):issues.append({'catalog_item':x['id'],'path_id_mismatch':x.get('path')})
result={'formal_graph_unchanged':not formal_changes,'formal_changes':formal_changes,'authorized_instruction_changes':authorized_changes,'unexpected_formal_changes':unexpected_changes,'formal_knowledge_unchanged':not unexpected_changes,'changed_workspace_files':len(changed),'local_links_checked':checked,'issues':issues,'passed':not issues and not unexpected_changes}
(R/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps(result,ensure_ascii=False,indent=2))
