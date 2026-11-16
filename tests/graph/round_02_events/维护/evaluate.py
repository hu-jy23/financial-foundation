#!/usr/bin/env python3
"""第二轮：匿名评审包、客观题计分、引用及冻结核查、双评审解盲。"""
import argparse,hashlib,json,random,re
from collections import Counter
from pathlib import Path
W=Path(__file__).resolve().parents[1];M=W/'维护';GRAPH=(W.parent/'graph_snapshot').resolve()
def load(p):return json.loads(p.read_text())
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def locked():
 f=load(M/'freeze.json');assert sha(M/'input.json')==f['input_sha256'];assert sha(W/'参考答案.json')==f['gold_sha256'];return f

def prepare():
 locked();q=load(M/'input.json')['questions'];g=load(W/'参考答案.json')['cases'];sub={};all_answers={}
 for arm in ['agent0','agent1']:
  p=W/arm/'answers.json';a=load(p);assert not a['access_declaration']['internet_used'];rows=a['answers'];assert [x['id']for x in rows]==[x['id']for x in q]
  for x,t in zip(rows,q):
   assert len(x.get('evidence',[]))<=2
   if t['type']=='mcq':assert x['choice'] in ['A','B','C','D']
   else:assert x.get('choice')is None
   if t['type']=='forward':assert 1<=len(x['predictions'])<=2
  sub[arm]={'sha256':sha(p),'access_declaration':a['access_declaration'],'answer_characters':{r['id']:len(r['answer'])for r in rows}};all_answers[arm]=rows
 save(M/'submissions.json',sub)
 for judge in [1,2]:
  rng=random.Random(2026110402+judge);cases=[];mapping={}
  for i,(question,ref)in enumerate(zip(q,g)):
   arms=['agent0','agent1'];rng.shuffle(arms);mapping[question['id']]=dict(zip(['A','B'],arms));candidates={}
   for label,arm in zip(['A','B'],arms):
    a=all_answers[arm][i];assert not re.search(r'图谱|graph|检索工具',a['answer'],re.I)
    candidates[label]={k:a.get(k)for k in ['choice','answer','predictions']}
   cases.append({'question':question,'reference':{k:ref[k]for k in ['reference','points','correct_choice']},'candidates':candidates})
  save(M/f'blind_packet_{judge}.json',{'grading':load(W/'参考答案.json')['rules'],'cases':cases});save(M/f'blind_mapping_{judge}.json',mapping)
 print('Prepared two separately randomized blind packets; 20 submissions locked')

def audit():
 f=locked();parent=load(W.parent/'维护/freeze.json');freeze_issues=[]
 for rel,digest in parent['files'].items():
  if sha(GRAPH/rel)!=digest:freeze_issues.append(rel)
 assert not freeze_issues,freeze_issues
 logs=[json.loads(l)for l in (W/'agent1/graph_reads.jsonl').read_text().splitlines()];read=[l for l in logs if l['operation']=='read'];citations=[]
 for a in load(W/'agent1/answers.json')['answers']:
  for e in a.get('evidence',[]):
   rel=e['path'];path=(GRAPH/rel).resolve();assert path.is_relative_to(GRAPH);lo=e['line_start'];hi=e['line_end'];span='\n'.join(path.read_text().splitlines()[lo-1:hi]);norm=lambda s:re.sub(r'\s+','',s)
   pieces=[norm(s)for s in re.split(r'[…]+|\.{3,}',e['quote'])if norm(s)];pos=0;quoted=True
   for piece in pieces:
    i=norm(span).find(piece,pos)
    if i<0:quoted=False;break
    pos=i+len(piece)
   seen=any(r['arguments']['path']==rel and r['actual_range'][0]<=lo<=hi<=r['actual_range'][1]for r in read)
   citations.append({'id':a['id'],**e,'quote_found':quoted,'read_record':seen,'passed':quoted and seen})
 report={'freeze_unchanged':True,'input_and_gold_unchanged':True,'citations':citations,'citation_count':len(citations),'passed_citations':sum(c['passed']for c in citations),'issues':[c for c in citations if not c['passed']],'graph_operations':dict(Counter(r['operation']for r in logs)),'unique_read_files':len({r['arguments']['path']for r in read}),'returned_characters':sum(r['result_characters']for r in logs)}
 save(M/'audit.json',report);print(json.dumps({k:v for k,v in report.items()if k!='citations'},ensure_ascii=False,indent=2))

def unblind():
 if (M/'submission_revision.json').exists():
  assert all((M/f'regrade_scores_{j}.json').exists()for j in [1,2]),'等待最终版E01的两份补评'
 locked();subs=load(M/'submissions.json');g=load(W/'参考答案.json')['cases'];ans={arm:load(W/arm/'answers.json')['answers']for arm in ['agent0','agent1']}
 for arm in subs:assert sha(W/arm/'answers.json')==subs[arm]['sha256']
 grades={j:load(M/f'blind_scores_{j}.json')for j in [1,2]};maps={j:load(M/f'blind_mapping_{j}.json')for j in [1,2]};out=[]
 for i,ref in enumerate(g):
  qid=ref['id'];row={'id':qid,'type':ref['type'],'correct_choice':ref['correct_choice']}
  for arm in ['agent0','agent1']:
   a=ans[arm][i];objective=6*int(a['choice']==ref['correct_choice'])if ref['type']=='mcq'else 0;js=[];details=[]
   for j in [1,2]:
    if qid=='E01' and (M/f'regrade_scores_{j}.json').exists():
     case=load(M/f'regrade_scores_{j}.json')['cases'][0];mapping=load(M/f'regrade_mapping_{j}.json')
    else:
     case=next(c for c in grades[j]['cases']if c['id']==qid);mapping=maps[j]
    label=next(k for k,v in mapping[qid].items()if v==arm);s=case['scores'][label];p=s['point_scores'];expected=3 if ref['type']=='mcq'else 10;assert len(p)==expected
    maxes=[2,1,1]if ref['type']=='mcq'else [1]*10
    assert all(0<=v<=mx for v,mx in zip(p,maxes));assert abs(sum(p)-s['content_score'])<1e-9
    js.append(objective+sum(p));details.append({'judge':j,**s})
   row[arm]={'choice':a.get('choice'),'objective':objective,'judge_totals':js,'mean':sum(js)/2,'grading':details}
  row['delta']=row['agent1']['mean']-row['agent0']['mean'];out.append(row)
 report={'case_count':len(out),'totals':{arm:sum(r[arm]['mean']for r in out)for arm in ['agent0','agent1']},'judge_totals':{str(j):{arm:sum(r[arm]['judge_totals'][j-1]for r in out)for arm in ['agent0','agent1']}for j in [1,2]},'choice_correct':{arm:sum(r['type']=='mcq' and r[arm]['choice']==r['correct_choice']for r in out)for arm in ['agent0','agent1']},'by_type':{t:{arm:sum(r[arm]['mean']for r in out if r['type']==t)for arm in ['agent0','agent1']}for t in ['forward','inverse','mcq']},'wins':sum(r['delta']>0 for r in out),'ties':sum(r['delta']==0 for r in out),'losses':sum(r['delta']<0 for r in out),'future_hit_rate':None,'cases':out}
 report['delta']=report['totals']['agent1']-report['totals']['agent0'];save(M/'scores.json',report);print(json.dumps({k:v for k,v in report.items()if k!='cases'},ensure_ascii=False,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('command',choices=['prepare','audit','unblind']);a=p.parse_args();{'prepare':prepare,'audit':audit,'unblind':unblind}[a.command]()
