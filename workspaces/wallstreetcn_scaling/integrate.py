"""Integrate main-agent-reviewed deliveries using a saved wave base."""
from pathlib import Path
import json,subprocess,tempfile,yaml,hashlib,re
R=Path(__file__).resolve().parent; G=R.parent/'step2_articles/graph'
def meta(p):
 s=p.read_text();return yaml.safe_load(s.split('---',2)[1]) if s.startswith('---\n') else {}
def integrate(article_id,base_path):
 A=R/'articles'/str(article_id);d=json.loads((A/'delivery.json').read_text());base=json.loads(Path(base_path).read_text());prepared=[]
 ids={meta(p).get('id'):str(p.relative_to(G)) for p in G.rglob('*.md') if meta(p).get('id')}
 for f in d['files']:
  if f['operation'] not in ['new','update']:continue
  p=G/f['path'];q=A/f['draft_path'];text=q.read_text();m=meta(q)
  for key in ['id','type','title']:
   if m.get(key)!=f[key]:raise ValueError(f"{article_id}: {key} mismatch {f['path']}")
  if m['id'] in ids and ids[m['id']]!=f['path']:raise ValueError(f"ID collision {m['id']}")
  if f['operation']=='new' and p.exists():raise ValueError(f"new path exists: {p}")
  if f['operation']=='update':
   if not p.exists() or meta(p)['id']!=f['id']:raise ValueError(f"update target mismatch {p}")
   original=base.get(f['path'])
   if original is None:raise ValueError(f"No wave base {p}")
   if p.read_text()!=original:
    with tempfile.TemporaryDirectory(prefix='ff-merge-') as td:
     ts=[Path(td)/n for n in ['ours','base','theirs']]
     for t,s in zip(ts,[p.read_text(),original,text]):t.write_text(s)
     result=subprocess.run(['git','merge-file','-p',*[str(x) for x in ts]],text=True,capture_output=True)
     if result.returncode:raise ValueError(f"Merge conflict {p}: {result.stdout[:1200]}")
     text=result.stdout
  if 'workspace_reviewed_on:' in text:text=re.sub(r'^workspace_reviewed_on:.*$','workspace_reviewed_on: 2026-11-16',text,flags=re.M)
  else:text=text.replace('\nupdated:', '\nworkspace_reviewed_by: /root\nworkspace_reviewed_on: 2026-11-16\nupdated:',1)
  prepared.append((p,text))
 for p,text in prepared:p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
 d['review_status']='adopted';d['reviewed_by']='/root';d['integrated_files']=[str(p.relative_to(G)) for p,_ in prepared]
 (A/'delivery.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 run=json.loads((R/'run.json').read_text())
 for x in run['articles']:
  if x['article_id']==int(article_id):x.update(status='adopted',files=len(prepared))
 (R/'run.json').write_text(json.dumps(run,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'article_id':article_id,'integrated_files':len(prepared)},ensure_ascii=False))
if __name__=='__main__':
 import sys
 integrate(int(sys.argv[1]),sys.argv[2])
