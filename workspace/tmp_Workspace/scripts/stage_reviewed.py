import argparse,hashlib,json,re
from pathlib import Path
p=argparse.ArgumentParser(description='Stage a draft explicitly read by the root and independently approved; does not judge content.')
p.add_argument('draft');p.add_argument('--candidate',action='append',required=True);p.add_argument('--supersedes-reviewed-source',action='store_true');a=p.parse_args()
w=Path(__file__).resolve().parents[1];src=(w/a.draft).resolve();raw=src.read_text();sha=hashlib.sha256(src.read_bytes()).hexdigest();review=(w/'reviews/content_review.md').read_text()
if sha not in review:raise SystemExit('Current draft hash is not in independent review.')
approved_ids=set()
for line in review.splitlines():
 cells=[c.strip() for c in line.strip().strip('|').split('|')]
 if len(cells)<4:continue
 label,state=cells[0],cells[2]
 if not state.startswith(('通过','一次返修后通过','复审通过')):continue
 hit=re.fullmatch(r'(T[12]-U\d\d)-([AB])(?:/([AB]))?',label)
 if hit:
  approved_ids.add(hit[1]+'-'+hit[2])
  if hit[3]:approved_ids.add(hit[1]+'-'+hit[3])
 else:approved_ids.add(label)
for cid in a.candidate:
 if cid not in approved_ids:raise SystemExit(f'No approval row for {cid}.')
def field(key):
 m=re.search('^'+key+r':\s*(.+)$',raw,re.M)
 if not m:raise SystemExit(f'Missing {key}.')
 return m[1].strip().strip('\"\'')
title=field('title');kind=field('type');section={'concept':'10_concepts','mechanism':'20_mechanisms'}.get(kind)
if section is None:raise SystemExit('Full concept/mechanism required.')
regpath=w/'accepted/registry.json';reg=json.loads(regpath.read_text()) if regpath.exists() else {};old=reg.get(title)
if old and old['source_draft']!=str(src.relative_to(w)) and not a.supersedes_reviewed_source:raise SystemExit('Cross-source target collision: root must merge and review explicitly.')
out=w/'accepted'/section/(title+'.md');out.parent.mkdir(exist_ok=True)
text=raw.replace('status: step1_draft','status: step1_reviewed',1)
text=re.sub(r'^reviewed_by:.*$','reviewed_by: [/root/step1_selector_reviewer, /root]',text,count=1,flags=re.M)
text=text.replace('本次更新待审','本次增量已审').replace('本次编辑待复审','本次增量已审').replace('，待复审。','，本次增量已审。').replace('待复审。','本轮新增内容已审。')
out.write_text(text)
prior=old.get('candidate_ids',[]) if old else []
reg[title]={'candidate_ids':list(dict.fromkeys(prior+a.candidate)),'source_draft':str(src.relative_to(w)),'reviewed_draft_sha256':sha,'accepted_file':str(out.relative_to(w)),'accepted_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'target_type':'existing_update' if (w.parent/'financial_foundation_v5_20261027/financial_foundation_v5'/section/(title+'.md')).exists() else 'new_node','review_scope':'本轮教材增量及接入；保留的旧稿外部来源未重新核验','reviewers':['/root/step1_selector_reviewer','/root'],'formal_merged':False}
regpath.write_text(json.dumps(reg,ensure_ascii=False,indent=2));print('Staged:',title,sha)
