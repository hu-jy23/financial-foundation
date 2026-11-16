from pathlib import Path
import json,re
from datetime import datetime
from zoneinfo import ZoneInfo
W=Path(__file__).resolve().parents[1]
R=W.parent
m=json.loads((W/'units.json').read_text())
decisions={}
for p in (W/'reviews').glob('selection_T*.md'):
 for line in p.read_text().splitlines():
  match=re.match(r'\|\s*(T[12]-U\d\d-[AB])\s*\|\s*([^|]+)\|',line)
  if match: decisions[match[1]]=match[2].strip()
for u in m['units']:
 if (W/'candidates'/u['book']/(u['id']+'.md')).exists():
  u['candidates']=2
  u['status']='candidate_ready'
 ds=[decisions.get(u['id']+'-'+x) for x in ['A','B']]
 if all(ds):
  u['status']='screened'
  u['passed']=sum('通过' in x for x in ds)
(W/'units.json').write_text(json.dumps(m,ensure_ascii=False,indent=2))
state={'run_status':m.get('run_status','running'),'units_total':len(m['units']),'units_submitted':sum(u['candidates']==2 for u in m['units']),'candidates_submitted':sum(u['candidates'] for u in m['units']),'candidates_screened':len(decisions),'candidates_passed_for_writing':sum('通过' in d for d in decisions.values()),'draft_files':len(list((W/'drafts').rglob('*.md'))),'accepted_files':len(list((W/'accepted').rglob('*.md')))}
p=W/'progress.json'
old=json.loads(p.read_text()) if p.exists() else {}
if old!=state:
 now=datetime.now(ZoneInfo('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M %Z')
 with (R/'STEP1_LOG.md').open('a') as f:
  f.write(f'### {now}｜流水线进度\n\n已交候选单元 {state["units_submitted"]}/{state["units_total"]}；候选 {state["candidates_submitted"]}份，已筛 {state["candidates_screened"]}份、准予全文 {state["candidates_passed_for_writing"]}份；全文文件 {state["draft_files"]}份，通过稿 {state["accepted_files"]}份。全文文件数不等于通过数；同一目标可合并多个候选。\n\n')
 p.write_text(json.dumps(state,ensure_ascii=False,indent=2))
regpath=W/'accepted/registry.json'
if regpath.exists():
 reg=json.loads(regpath.read_text())
 new=sum(v['target_type']=='new_node' for v in reg.values())
 lines=['# 本轮通过稿','',f'已通过 {len(reg)} 个目标页：{new} 个新节点、{len(reg)-new} 个既有页更新。本轮已完成，全部通过稿已写回正式图。','', '通过指本轮新增内容与接入已由独立审阅及主agent核读；保留旧稿的外部来源未全部重新核验。正式写回状态逐项记录，不能由通过稿数推断已合并。','', '| 条目 | 类型 | 候选 | 正式写回 |','|---|---|---|---|']
 for title,v in reg.items():
  kind='新增' if v['target_type']=='new_node' else '更新'
  link='../../graph/'+v['formal_path'] if v.get('formal_merged') else v['accepted_file']
  lines.append(f'| [{title}]({link}) | {kind} | '+', '.join(v['candidate_ids'])+' | '+('已写回' if v['formal_merged'] else '未写回')+' |')
 (W/'RESULTS.md').write_text('\n'.join(lines)+'\n')
print(json.dumps(state,ensure_ascii=False))
