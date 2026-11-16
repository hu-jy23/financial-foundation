#!/usr/bin/env python3
"""锁定输入核对、去标识盲评包、图谱引用核查及解盲汇总。"""
import argparse,hashlib,json,random,re
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
M=ROOT/'维护'
def load(p):return json.loads(p.read_text())
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def verify_inputs():
 f=load(M/'freeze.json')
 assert digest(M/'questions.json')==f['questions_sha256'],'题目已变化'
 assert digest(ROOT/'参考答案.json')==f['gold_sha256'],'参考答案已变化'
 for name,value in f['files'].items():assert digest(ROOT/'graph_snapshot'/name)==value,name
 return f

def answers(arm):
 d=load(ROOT/arm/'answers.json');a=d['answers'];assert [r['id'] for r in a]==[f'Q{i:02d}'for i in range(1,11)]
 assert not d['access_declaration']['internet_used']
 return d

def blind():
 verify_inputs();a0=answers('agent0');a1=answers('agent1');q=load(M/'questions.json');gold=load(ROOT/'参考答案.json');rng=random.Random(2026110401);packet=[];mapping={}
 for i,(question,g) in enumerate(zip(q,gold['cases'])):
  arms=['agent0','agent1'];rng.shuffle(arms);mapping[question['id']]={'A':arms[0],'B':arms[1]}
  candidates={label:({'agent0':a0,'agent1':a1}[arm]['answers'][i]['answer']) for label,arm in zip(['A','B'],arms)}
  # 仅传内容；引用、资料条件和缺口说明不进入盲评包。
  assert not any(re.search('graph|图谱|检索|查阅',s,re.I) for s in candidates.values()),'正文出现资料条件，需要检查盲评可行性'
  packet.append({'question':question,'reference':{k:g[k] for k in ['cause','reference_result','mechanism_points','valid_boundary_examples','overclaim_traps','reference_note']},'candidates':candidates})
 save(M/'blind_packet.json',{'rubric':gold['rubric'],'scoring_notes':gold['scoring_notes'],'cases':packet})
 save(M/'blind_mapping.json',mapping)
 save(M/'submissions.json',{arm:{'sha256':digest(ROOT/arm/'answers.json'),'characters':{a['id']:len(a['answer']) for a in d['answers']},'access_declaration':d['access_declaration']}for arm,d in [('agent0',a0),('agent1',a1)]})
 print('Blind packet ready: 10 paired cases; per-case randomized A/B')

def citation_audit():
 verify_inputs();a=answers('agent1');logs=[json.loads(l)for l in (ROOT/'agent1/graph_reads.jsonl').read_text().splitlines()];reads=[r for r in logs if r['operation']=='read'];out=[]
 for case in a['answers']:
  for e in case.get('evidence',[]):
   rel=e['path'];p=(ROOT/'graph_snapshot'/rel).resolve();assert p.is_relative_to((ROOT/'graph_snapshot').resolve())
   lines=p.read_text().splitlines();lo=e['line_start'];hi=e['line_end'];span='\n'.join(lines[lo-1:hi]);norm=lambda s:re.sub(r'\s+','',s)
   chunks=[norm(c)for c in re.split(r'[…]+|\.{3,}',e['quote']) if norm(c)]
   pos=0;match=True
   for chunk in chunks:
    found=norm(span).find(chunk,pos)
    if found<0:match=False;break
    pos=found+len(chunk)
   read=any(r['arguments']['path']==rel and r['arguments']['start']<=lo and r['arguments']['end']>=hi for r in reads)
   out.append({'question':case['id'],**e,'quote_found_in_range':match,'range_was_read':read,'passed':match and read})
 report={'citations':out,'citation_count':len(out),'passed':sum(x['passed']for x in out),'issues':[x for x in out if not x['passed']],'graph_tool_calls':len(logs),'graph_search_calls':sum(r['operation']=='search'for r in logs),'graph_read_calls':len(reads),'unique_read_files':len({r['arguments']['path']for r in reads}),'graph_tool_return_characters':sum(r['result_characters']for r in logs),'graph_gap_notes':{r['id']:r.get('graph_gap','')for r in a['answers']}}
 save(M/'citation_audit.json',report);print(json.dumps({k:v for k,v in report.items()if k not in ['citations','graph_gap_notes']},ensure_ascii=False,indent=2))

def unblind():
 verify_inputs();mapping=load(M/'blind_mapping.json');grade=load(M/'blind_scores.json');sub=load(M/'submissions.json')
 for arm in ['agent0','agent1']:assert digest(ROOT/arm/'answers.json')==sub[arm]['sha256'],'评分后答题发生变化'
 results=[]
 for case in grade['cases']:
  qid=case['id'];r={'id':qid}
  for label in ['A','B']:
   score=case['scores'][label]
   for dim,maximum in [('direction',2),('mechanism',4),('conditions',2),('discipline',2)]:assert 0<=score[dim]<=maximum
   assert len(score['mechanism_point_scores'])==4
   assert abs(sum(score['mechanism_point_scores'])-score['mechanism'])<1e-9
   score['total']=sum(score[k] for k in ['direction','mechanism','conditions','discipline']);r[mapping[qid][label]]=score
  r['delta']=r['agent1']['total']-r['agent0']['total'];results.append(r)
 assert {r['id']for r in results}=={f'Q{i:02d}'for i in range(1,11)}
 results.sort(key=lambda r:r['id'])
 totals={arm:sum(r[arm]['total']for r in results)for arm in ['agent0','agent1']};dimensions={arm:{d:sum(r[arm][d]for r in results)for d in ['direction','mechanism','conditions','discipline']}for arm in totals}
 report={'totals':totals,'delta':totals['agent1']-totals['agent0'],'dimensions':dimensions,'wins':sum(r['delta']>0 for r in results),'ties':sum(r['delta']==0 for r in results),'losses':sum(r['delta']<0 for r in results),'cases':results}
 save(M/'scores.json',report);print(json.dumps({k:v for k,v in report.items()if k!='cases'},ensure_ascii=False,indent=2))

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('command',choices=['blind','audit','unblind']);a=p.parse_args();{'blind':blind,'audit':citation_audit,'unblind':unblind}[a.command]()
