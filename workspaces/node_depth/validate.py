"""Check this pilot's draft links, evidence records and unmodified formal inputs."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
from html.parser import HTMLParser
from collections import Counter
import hashlib, json, os, re, subprocess
import yaml
from markdown_it import MarkdownIt
from bs4 import BeautifulSoup

R=Path(__file__).resolve().parent;ROOT=R.parents[1];G=ROOT/'graph';P=R/'cds_pilot'
md=MarkdownIt('commonmark',{'html':True}).enable('table');issues=[];links=0
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def meta(p):return yaml.safe_load(p.read_text().split('---',2)[1])
def check(ok,detail):
 if not ok:issues.append(detail)
def git(*args):return subprocess.check_output(['git','-c','core.quotepath=false',*args],cwd=ROOT,text=True)
def anchors(p):
 s=p.read_text();ids=set(re.findall(r'(?:id|name)=["\']([^"\']+)',s))
 return ids|{re.sub(r'[^\w\-\s\u3400-\u9fff]','',h.lower()).replace(' ','-') for h in re.findall(r'^#{1,6}\s+(.+?)\s*#*$',s,re.M)}
drafts={G/p.relative_to(P/'drafts'):p for p in (P/'drafts').rglob('*.md')}
class HTML(HTMLParser):
 def __init__(self):super().__init__();self.urls=[];self.ids=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  self.urls.extend(a[k] for k in ['href','src','poster'] if k in a)
def scan(p,origin=None):
 global links
 s=p.read_text();origin=origin or p;urls=set()
 if p.suffix=='.md':
  s=re.sub(r'\\\[.*?\\\]','',s,flags=re.S);s=re.sub(r'\\\(.*?\\\)','',s,flags=re.S)
  for t in md.parse(s):
   for c in [t]+(t.children or []):
    u=c.attrGet('href') or c.attrGet('src')
    if u:urls.add(u)
 parser=HTML();parser.feed(s);urls.update(parser.urls)
 if p.suffix=='.html':check(len(parser.ids)==len(set(parser.ids)),{'duplicate_html_ids':str(p.relative_to(ROOT))})
 for raw in urls:
  u=urlsplit(raw)
  if u.scheme or u.netloc:continue
  links+=1;target=Path(os.path.abspath(origin.parent/unquote(u.path))) if u.path else origin;target=drafts.get(target,target)
  check(target.exists(),{'missing_local_target':raw,'from':str(p.relative_to(ROOT))})
  if target.exists() and u.fragment:
   fragment=unquote(u.fragment)
   if target.suffix=='.md':check(fragment in anchors(target),{'missing_md_anchor':raw,'from':str(p.relative_to(ROOT))})
   elif target==p and p.suffix=='.html':check(fragment in parser.ids,{'missing_html_anchor':raw})
selection=json.loads((R/'selection/selection.json').read_text());items=selection['items']
check(Counter(x['type'] for x in items)=={'concept':15,'mechanism':5},'selection_count')
check(len({x['id'] for x in items})==20,'selection_duplicates')
check(Counter(x['status'] for x in items)=={'completed_pending_review':1,'awaiting_pilot_review':19},'task_statuses')
for x in items:
 p=ROOT/x['formal_path'];m=meta(p)
 check(m['id']==x['id'] and m['type']==x['type'] and sha(p)==x['input_sha256'],{'changed_selected_input':x['id']})
 check((R/'selection'/x['task_file']).exists(),{'missing_task':x['id']})
check(len(list((R/'selection/tasks').glob('*.md')))==20,'task_file_count')
delivery=json.loads((P/'delivery.json').read_text());base=json.loads((P/'base.json').read_text())
formal_ids={meta(p)['id'] for p in G.rglob('*.md') if p.read_text().startswith('---\n') and meta(p).get('id')}
check(len(delivery['files'])==7,'pilot_draft_count')
for x in delivery['files']:
 p=ROOT/x['draft_path'];m=meta(p);q=ROOT/x['target_path']
 check(sha(p)==x['draft_sha256'] and m['id']==x['id'] and m['type']==x['type'] and m['status']=='draft',{'draft_identity_or_hash':x['path']})
 if q.exists():
  old=meta(q);b=base['graph_files'][str(q.relative_to(G))]
  check(sha(q)==b['sha256'] and q.read_text()==b['text'],{'changed_baseline':x['path']})
  check(m.get('draft_author')==old.get('draft_author') and set(old.get('source_ids',[]))<=set(m.get('source_ids',[])) and m.get('evidence_as_of')==old.get('evidence_as_of'),{'lost_authorship_source_date':x['path']})
  explicit=set(re.findall(r'(?:id|name)=["\']([^"\']+)',q.read_text()))
  check(explicit<=anchors(p),{'lost_old_anchor':x['path']})
 else:check(m['id'] not in formal_ids,{'new_id_collision':m['id']})
catalog=json.loads((P/'sources.json').read_text());sources=catalog['sources'];adopted=[x for x in sources if x['adopted']]
check(len(adopted)==14,'adopted_source_count')
for x in sources:
 p=ROOT/x['local_path'];check(p.exists() and sha(p)==x['sha256'],{'source_hash':x['id']})
 if p.suffix=='.pdf':check(p.read_bytes().startswith(b'%PDF-'),{'not_pdf':x['id']})
 if x.get('text_path'):check((ROOT/x['text_path']).exists() and (ROOT/x['text_path']).stat().st_size>100,{'missing_or_empty_source_text':x['id']})
claims=json.loads((P/'claims.json').read_text())['claims'];source_ids={x['id'] for x in adopted}|{x['id'] for x in catalog['reused_graph_evidence']}
check(len({x['id'] for x in claims})==37,'claim_count_or_duplicates')
for x in claims:
 for evidence in x.get('evidence',[]):check(evidence['source_id'] in source_ids,{'unknown_claim_source':x['id']})
 for used in x.get('used_in',[]):
  u=urlsplit(used);target=drafts.get(G/u.path,G/u.path)
  check(target.exists() and (not u.fragment or u.fragment in anchors(target)),{'missing_claim_destination':x['id'],'target':used})
for p in R.rglob('*.md'):
 scan(p,G/p.relative_to(P/'drafts') if p.is_relative_to(P/'drafts') else None)
scan(R/'报告.html');scan(ROOT/'materials/historical/node_depth/CDS/README.md')
report=BeautifulSoup((R/'报告.html').read_text(),'html.parser')
for pane in report.select('.comparison-view'):
 for x in delivery['files']:
  card=next(c for c in pane.select('[data-diff-kind]') if c.select_one('p.file a')['href']==os.path.relpath(ROOT/x['draft_path'],R))
  raw=(ROOT/x['draft_path']).read_text().split('---',2)[2]
  check(card.select_one('.draft-body').get_text()==BeautifulSoup(md.render(raw),'html.parser').get_text(),{'diff_altered_draft_text':x['path'],'view':pane['data-view']})
check(not report.select_one('#draft-0 .draft-body h1').get('class'),'unchanged_CDS_title_marked')
check(len(report.select('[data-view="revision"] .new-entry.diff-add'))==1 and len(report.select('[data-view="full"] .new-entry.diff-add'))==3,'new_entries_not_marked')
check(bool(report.select('#draft-0 .diff-mod')) and bool(report.select('#full-draft-1 .draft-body .diff-add')),'modified_or_added_content_not_marked')
check(report.select_one('[data-view="full"]').has_attr('hidden') and not report.select_one('[data-view="revision"]').has_attr('hidden'),'wrong_default_comparison')
check(not report.select_one('#draft-2--ai-comparison') and bool(report.select('#draft-5--ai-comparison')),'AI_comparison_not_moved')
check(all(not x.has_attr('open') for x in report.select('.diff-removals')),'retired_content_not_folded')
changed=git('diff','--name-only',selection['input_graph_commit'],'--','graph').splitlines()
tracked=set(git('ls-tree','-r','--name-only',selection['input_graph_commit'],'--','graph').splitlines())
actual={str(p.relative_to(ROOT)) for p in G.rglob('*') if p.is_file()}
check(not changed and actual==tracked,{'formal_graph_changed':changed,'added_or_removed':sorted(actual^tracked)})
result={'passed':not issues,'pilot_drafts':len(delivery['files']),'adopted_sources':len(adopted),'key_claims':len(claims),'concept_tasks':15,'mechanism_tasks':5,'pending_user_review':1,'unstarted_tasks':19,'local_links_checked':links,'diff_body_text_preserved':not any(isinstance(x,dict) and 'diff_altered_draft_text' in x for x in issues),'formal_graph_files_unchanged':len(tracked),'issues':issues}
(R/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(bool(issues))
