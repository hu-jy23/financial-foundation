from pathlib import Path
import argparse,hashlib,json,os,re,urllib.parse,yaml
P=argparse.ArgumentParser();P.add_argument('--apply',action='store_true');args=P.parse_args()
W=Path(__file__).resolve().parents[1];ROOT=W.parents[1];F=ROOT/'graph'
reg=json.loads((W/'accepted/registry.json').read_text());units=json.loads((W/'units.json').read_text());baseline=json.loads((W/'inputs/formal_baseline_hashes.json').read_text())
assert len(units['units'])==36 and all(u['status']=='screened' and u['candidates']==2 for u in units['units'])
decisions={}
for p in (W/'reviews').glob('selection_T*.md'):
 for line in p.read_text().splitlines():
  x=re.match(r'\|\s*(T[12]-U\d\d-[AB])\s*\|\s*([^|]+)\|',line)
  if x:
   if x[1] in decisions:raise SystemExit('Duplicate selection decision: '+x[1])
   decisions[x[1]]=x[2].strip()
assert len(decisions)==72
passed={cid for cid,d in decisions.items() if d.startswith('通过')}
adopted={cid for v in reg.values() for cid in v['candidate_ids']}
assert passed==adopted,(passed-adopted,adopted-passed)
assert len(reg)==23
index_path=F/'00_start/catalog_index.json';index=json.loads(index_path.read_text())
flat={x['id']:x for kind in ['concepts','mechanisms'] for g in index[kind] for x in g['items']}
config={
 'C-DERIV-CCP':('DERIV','交易对手替换、集中净额、担保与关键节点风险'),
 'C-LABOR-WAGE-POWER':('INFLATION','招聘替代与换岗约束下的雇主工资定价空间'),
 'R-GROWTH-HYSTERESIS':('GROWTH','长期失业、技能与劳动参与的持续损伤'),
 'R-CREDIT-RATIONING':('BANKING','信息不对称下的价格与授信数量门槛'),
 'R-FX-TRADE-ADJUSTMENT':('INTERNATIONAL','合同计价、价格传递与贸易数量调整时序'),
 'R-RESOURCE-FX-COMPETITION':('COMMODITY','资源收入预期经汇率影响非资源出口竞争力')}
outputs={};new_items={'concepts':[],'mechanisms':[]};metas={};dst_by_title={}
for title,v in reg.items():
 src=W/v['accepted_file'];raw=src.read_text();assert hashlib.sha256(src.read_bytes()).hexdigest()==v['accepted_sha256']
 m=yaml.safe_load(raw.split('---',2)[1]);metas[title]=m;section='10_concepts' if m['type']=='concept' else '20_mechanisms';dst_by_title[title]=F/section/(title+'.md')
link_re=re.compile(r'(!?\[[^\]]*\])\((?:<([^>]+)>|([^\s)]+))\)')
def rebase(raw,src,dst):
 def change(match):
  url=match[2] or match[3]
  if url.startswith(('http:','https:','mailto:','#','data:')):return match[0]
  path,sep,frag=url.partition('#');target=(src.parent/urllib.parse.unquote(path)).resolve()
  if target.suffix=='.md' and str(target).startswith(str(W)) and target.stem in dst_by_title:target=dst_by_title[target.stem]
  rel=os.path.relpath(target,dst.parent).replace(os.sep,'/')+(sep+frag if sep else '')
  enc='<'+rel+'>' if re.search(r'[\s()<>]',rel) else rel
  return match[1]+'('+enc+')'
 return link_re.sub(change,raw)
for title,v in reg.items():
 src=W/v['accepted_file'];dst=dst_by_title[title];m=metas[title];outputs[dst]=rebase(src.read_text(),src,dst)
 kind='concepts' if m['type']=='concept' else 'mechanisms';ident=m['id']
 if ident not in flat:
  group_code,scope=config[ident];group=next(g for g in index[kind] if g['code']==group_code)
  item={'id':ident,'name':title,'scope':scope,'priority':'P1','status':'complete','path':f'../{dst.parent.name}/{dst.name}','planned_path':f'../{dst.parent.name}/{dst.name}','catalog_anchor':ident,'catalog_ref':('CONCEPT_IMPORT_LIST.md' if kind=='concepts' else 'MECHANISM_IMPORT_LIST.md')+'#'+ident,'selection_status':'confirmed_step1','selection_basis':'T1_T2_source_review_20261103','selection_confirmed_on':'2026-11-03'}
  if kind=='concepts':item['role']='domain_objects'
  group['items'].append(item);flat[ident]=item;new_items[kind].append((group['title'],item))
 item=flat[ident];item['status']='complete';item['last_source_review_on']='2026-11-03';item['last_source_batch']='T1_T2_20261103'
 if kind=='mechanisms':
  item['node_ids']=m.get('node_ids',[]);item['related_mechanism_ids']=m.get('related_mechanism_ids',[]);item['logic_groups']=m.get('logic_groups',[])
concept_ids={x['id'] for g in index['concepts'] for x in g['items']};mechanism_ids={x['id'] for g in index['mechanisms'] for x in g['items']}
for title,m in metas.items():
 assert set(m.get('node_ids',[]))<=concept_ids,(title,'unknown concept')
 assert set(m.get('related_mechanism_ids',[]))<=mechanism_ids,(title,'unknown mechanism')
for kind in ['concepts','mechanisms']:
 items=[x for g in index[kind] for x in g['items']]
 index['counts'][kind].update(groups=len(index[kind]),items=len(items),p0=sum(x.get('priority')=='P0' for x in items),complete=sum(x['status']=='complete' for x in items),pending=sum(x['status']!='complete' for x in items))
index['updated']='2026-11-03';outputs[index_path]=json.dumps(index,ensure_ascii=False,indent=2)+'\n'
C=len(concept_ids);M=len(mechanism_ids);assert (C,M)==(165,75)
for kind,filename in [('concepts','CONCEPT_IMPORT_LIST.md'),('mechanisms','MECHANISM_IMPORT_LIST.md')]:
 dest=F/'00_start'/filename;text=dest.read_text()
 if kind=='concepts':text=re.sub(r'共\d+个对象，\d+个主题组；正文已全部完成。与\[机制目录\]\(MECHANISM_IMPORT_LIST.md\)共同构成\d+个节点。',f'共{C}个对象，{len(index[kind])}个主题组；正文已全部完成。与[机制目录](MECHANISM_IMPORT_LIST.md)共同构成{C+M}个节点。',text,count=1)
 else:text=re.sub(r'共\d+个机制，\d+个主题组；正文已全部完成。',f'共{M}个机制，{len(index[kind])}个主题组；正文已全部完成。',text,count=1)
 for group in index[kind]:
  count=len(group['items']);p0=sum(x.get('priority')=='P0' for x in group['items'])
  text=re.sub(r'^\| '+re.escape(group['title'])+r' \| \d+ \| \d+ \|$',f'| {group["title"]} | {count} | {p0} |',text,flags=re.M)
 for group_title,item in new_items[kind]:
  if f'<a id="{item["id"]}"></a>' in text:continue
  if kind=='concepts':row=f'| <a id="{item["id"]}"></a>{item["id"]} | {item["name"]} | {item["scope"]} | P1 | complete／[正文]({item["path"]}) |'
  else:
   nodes='；'.join(f'[{flat[i]["name"]} {i}]({flat[i]["path"]})' for i in item['node_ids']) or '—'
   rels='；'.join(f'[{flat[i]["name"]} {i}]({flat[i]["path"]})' for i in item['related_mechanism_ids']) or '—'
   row=f'| <a id="{item["id"]}"></a>{item["id"]} | {item["name"]} | {nodes} | {rels} | {item["scope"]} | P1 | complete／[正文]({item["path"]}) |'
  start=text.index('## '+group_title+'\n');end=text.find('\n## ',start+1);end=len(text) if end<0 else end
  text=text[:end].rstrip()+'\n'+row+'\n\n'+text[end:].lstrip('\n')
 outputs[dest]=text
# Preflight every body and index/catalog against the launch snapshot before writing anything.
for dest,text in outputs.items():
 rel=str(dest.relative_to(F));current=dest.read_bytes() if dest.exists() else None
 if current is not None and current!=text.encode():
  expected=baseline.get(rel)
  if expected is None or hashlib.sha256(current).hexdigest()!=expected:raise SystemExit('Concurrent change requires manual merge: '+rel)
 for hit in link_re.finditer(text):
  url=hit[2] or hit[3]
  if url.startswith(('http:','https:','mailto:','#','data:')):continue
  target=(dest.parent/urllib.parse.unquote(url.split('#',1)[0])).resolve()
  if not target.exists() and target not in outputs:raise SystemExit(f'Unresolved planned link: {dest}: {url}')
report={'date':'2026-11-03','mode':'applied' if args.apply else 'dry_run','units':36,'candidates':72,'retained_candidates':len(passed),'discarded_candidates':72-len(passed),'accepted_targets':len(reg),'new_concepts':len(new_items['concepts']),'new_mechanisms':len(new_items['mechanisms']),'current_counts':{'concepts':C,'mechanisms':M,'total':C+M},'written_files':[str(p.relative_to(F)) for p in outputs]}
if args.apply:
 for dest,text in outputs.items():dest.write_text(text)
 for title,v in reg.items():
  v['formal_merged']=True;v['formal_path']=str(dst_by_title[title].relative_to(F));v['formal_sha256']=hashlib.sha256(dst_by_title[title].read_bytes()).hexdigest()
 (W/'accepted/registry.json').write_text(json.dumps(reg,ensure_ascii=False,indent=2))
(W/'integration_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False))
