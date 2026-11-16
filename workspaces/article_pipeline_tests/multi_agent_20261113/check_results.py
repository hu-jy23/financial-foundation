import json,hashlib,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
WORK=ROOT.parent.parent.parent
m=json.loads((ROOT/'run_manifest.json').read_text())
expected={f'{case}_{i:02d}'for case in ['ai','korea']for i in range(1,7)}
issues=[];rows=[]
required=['run_id','article_id','title','problem','passages','structures','sample_title','sample','limitations','guidance_feedback','reading','summary']
for p in sorted((ROOT/'成果').glob('*.json')):
 try:d=json.loads(p.read_text())
 except Exception as exc:issues.append(f'{p.name}: {exc}');continue
 rid=p.stem
 if d.get('run_id')!=rid:issues.append(f'{rid}: run_id不一致')
 for k in required:
  if k not in d:issues.append(f'{rid}: missing {k}')
 case='ai' if rid.startswith('ai_') else 'korea'
 if d.get('article_id')!=m['cases'][case]['article_id']:issues.append(f'{rid}: article_id不一致')
 for s in d.get('structures',[]):
  for k in ['name','kind','parent','inherits','difference','why_register','inline_alternative','decision']:
   if k not in s:issues.append(f'{rid}: structure missing {k}')
 reading=d.get('reading',{});missing=[]
 for k in ['documents','graph_pages','figures']:
  for raw in reading.get(k,[]):
   if isinstance(raw,str):
    q=raw.split('#')[0]
    if not (WORK/q).exists():missing.append(raw)
 rows.append({'run_id':rid,'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'passages':len(d.get('passages',[])),'structures':len(d.get('structures',[])),'reported_figures':len(reading.get('figures',[])),'reading_path_notes':missing})
changed=[]
for p,h in m['input_hashes'].items():
 f=WORK/p
 if not f.exists() or hashlib.sha256(f.read_bytes()).hexdigest()!=h:changed.append(p)
missing=sorted(expected-{r['run_id']for r in rows})
report={'expected_runs':12,'completed':len(rows),'missing':missing,'schema_issues':issues,'changed_inputs':changed,'results':rows,'complete':not missing and not issues and not changed}
(ROOT/'result_check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items()if k!='results'},ensure_ascii=False,indent=2))
