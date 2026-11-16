from pathlib import Path
import json,yaml
R=Path(__file__).resolve().parent;G=R.parent/'step2_articles/graph';S=G/'00_start';B=R.parents[1]/'graph/00_start'
d=json.loads((S/'catalog_index.json').read_text());formal=json.loads((B/'catalog_index.json').read_text())
run=json.loads((R/'run.json').read_text());changed={}
for a in run['articles']:
 if a['status']=='adopted':
  delivery=json.loads((R/'articles'/str(a['article_id'])/'delivery.json').read_text())
  for f in delivery['files']:
   if f['operation'] in ['new','update']:changed[f['id']]=f
for kind,folder,typ in [('concepts','10_concepts','concept'),('mechanisms','20_mechanisms','mechanism')]:
 old={x['id']:x for g in d[kind] for x in g['items']};extra=[]
 for p in (G/folder).glob('*.md'):
  m=yaml.safe_load(p.read_text().split('---',2)[1]);id=m['id'];f=changed.get(id,{})
  if id not in old:
   item={'id':id,'name':m['title'],'scope':f.get('why',m['title']),'priority':'P1','role':'domain_objects' if typ=='concept' else 'mechanisms','selection_status':'proposed_step2','selection_basis':'wallstreetcn_scaling_20261116'};extra.append(item)
  else:item=old[id]
  path='../'+str(p.relative_to(G));item.update(name=m['title'],path=path,planned_path=path,catalog_anchor=id,catalog_ref=('CONCEPT_IMPORT_LIST.md' if typ=='concept' else 'MECHANISM_IMPORT_LIST.md')+'#'+id)
  if id in changed or m.get('status')=='step2_draft' or m.get('editing_status')=='step2_draft':item.update(status='pending',editing_status='step2_draft')
  for key in ['parent_ids','parent_relation','node_ids','related_mechanism_ids','logic_groups']:
   if key in m:item[key]=m[key]
 if extra:
  group=next((g for g in d[kind] if g['code']=='WALLSTREET_SCALING'),None)
  if group is None:group={'code':'WALLSTREET_SCALING','title':'Wallstreet Scaling待整合条目','items':[]};d[kind].append(group)
  group['items'].extend(extra)
 allitems=[x for g in d[kind] for x in g['items']];d['counts'][kind]={'groups':len(d[kind]),'items':len(allitems),'p0':sum(x.get('priority')=='P0' for x in allitems),'complete':sum(x.get('status')=='complete' for x in allitems),'pending':sum(x.get('status')=='pending' for x in allitems)}
 formal_ids={x['id'] for g in formal[kind] for x in g['items']};new=[x for x in allitems if x['id'] not in formal_ids]
 file='CONCEPT_IMPORT_LIST.md' if typ=='concept' else 'MECHANISM_IMPORT_LIST.md'
 text='> **待整合工作图**：本目录包含三篇基准及Wallstreet Scaling采用稿，正式graph未接入。\n\n'+(B/file).read_text()+'\n\n## Step2待整合新增条目\n\n'
 for x in new:text+=f'<a id="{x["id"]}"></a>\n### [{x["name"]}]({x["path"]})\n\n`{x["id"]}` · 待整合 · {x["scope"]}\n\n'
 (S/file).write_text(text)
d['updated']='2026-11-16';d['workspace_only']=True;d['integration_status']='not_merged';(S/'catalog_index.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(d['counts'],ensure_ascii=False))
