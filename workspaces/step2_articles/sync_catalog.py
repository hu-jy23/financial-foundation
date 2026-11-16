from pathlib import Path
if (Path(__file__).resolve().parents[1]/'wallstreetcn_scaling/formal_integration.json').exists():
 raise SystemExit('本批已接入正式graph；旧工作图写入脚本停用。请从graph/00_start/README.md开始新任务。')
from pathlib import Path
import json,yaml
R=Path(__file__).resolve().parent;G=R/'graph';S=G/'00_start'
base=R.parents[1]/'graph/00_start'
d=json.loads((base/'catalog_index.json').read_text())
files=[f for k in ['ai','korea','basis'] for f in json.loads((R/'deliveries'/f'{k}.json').read_text())['files']]
for kind,typ in [('concepts','concept'),('mechanisms','mechanism')]:
 new=[];old={x['id']:x for g in d[kind] for x in g['items']}
 for f in files:
  if f['type']!=typ:continue
  p=G/f['path'];m=yaml.safe_load(p.read_text().split('---',2)[1]);id=m['id'];path='../'+f['path']
  item=old.get(id,{'id':id,'name':m['title'],'scope':f['why'],'priority':'P1','role':'domain_objects' if typ=='concept' else 'mechanisms','selection_status':'proposed_step2','selection_basis':'three_article_working_copy_20261113'})
  item.update(name=m['title'],status='pending',path=path,planned_path=path,catalog_anchor=id,catalog_ref=('CONCEPT_IMPORT_LIST.md' if typ=='concept' else 'MECHANISM_IMPORT_LIST.md')+'#'+id,editing_status='step2_draft')
  for key in ['parent_ids','parent_relation','node_ids','related_mechanism_ids','logic_groups']:
   if key in m or key in f:item[key]=m.get(key,f.get(key))
  if id not in old:new.append(item)
 if new:d[kind].append({'code':'STEP2_DRAFT','title':'Step2工作副本拟新增条目','items':new,'role':'domain_objects' if typ=='concept' else 'mechanisms'})
 allitems=[x for g in d[kind] for x in g['items']]
 d['counts'][kind]={'groups':len(d[kind]),'items':len(allitems),'p0':sum(x.get('priority')=='P0' for x in allitems),'complete':sum(x['status']=='complete' for x in allitems),'pending':sum(x['status']=='pending' for x in allitems)}
 name='CONCEPT_IMPORT_LIST.md' if typ=='concept' else 'MECHANISM_IMPORT_LIST.md'
 text=(base/name).read_text();text='> **工作副本**：本目录含本轮拟新增条目；正式仓库未变。新增与更新正文供审阅，未整合main。\n\n'+text
 if new:
  text+='\n\n## Step2工作副本拟新增\n\n'
  for x in new:text+=f'<a id="{x["id"]}"></a>\n### [{x["name"]}]({x["path"]})\n\n`{x["id"]}` · 待整合 · {x["scope"]}\n\n'
 (S/name).write_text(text)
d['updated']='2026-11-13';d['workspace_only']=True;d['integration_status']='not_merged';d['notes'].append('本索引仅用于独立工作副本；proposed_step2条目和pending编辑未整合正式main。')
(S/'catalog_index.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=S/'README.md';s=(base/'README.md').read_text();p.write_text('> **独立工作副本**：原始范围为165对象、75关系；本轮拟新增范围和旧页编辑见[制作说明](../../制作说明.md)。索引已同步本副本，正文保持step2_draft等待整合。下方保留原制作说明。\n\n'+s)
print(json.dumps(d['counts'],ensure_ascii=False))
