#!/usr/bin/env python3
"""仅检索冻结graph，输出带行号文本并记录访问；没有网络功能。"""
import argparse,hashlib,json,re
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
ROOT=Path(__file__).resolve().parents[1];GRAPH=(ROOT.parent/'graph_snapshot').resolve();LOG=ROOT/'agent1/graph_reads.jsonl'
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--question',default='setup');sub=p.add_subparsers(dest='operation',required=True)
 a=sub.add_parser('read');a.add_argument('path');a.add_argument('--start',type=int,default=1);a.add_argument('--end',type=int,default=140)
 a=sub.add_parser('search');a.add_argument('pattern');a.add_argument('--limit',type=int,default=8)
 a=sub.add_parser('list');a.add_argument('--contains',default='')
 args=p.parse_args();record={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(timespec='seconds'),'question':args.question,'operation':args.operation,'arguments':vars(args)}
 files=sorted(p for p in GRAPH.rglob('*')if p.is_file()and p.suffix in ['.md','.json'])
 if args.operation=='read':
  f=(GRAPH/args.path).resolve()
  if not f.is_relative_to(GRAPH)or not f.is_file()or f.suffix not in ['.md','.json']:p.error('仅可读取冻结graph中的MD或JSON')
  lines=f.read_text().splitlines();lo=max(1,args.start);hi=min(len(lines),args.end,lo+249);record['actual_range']=[lo,hi]
  out=f'{f.relative_to(GRAPH)} — {len(lines)} lines\n'+'\n'.join(f'{i}: {lines[i-1]}'for i in range(lo,hi+1))
 elif args.operation=='list':out='\n'.join(str(f.relative_to(GRAPH))for f in files if args.contains.casefold()in str(f.relative_to(GRAPH)).casefold())
 else:
  pattern=re.compile(args.pattern,re.I);hits=[]
  for f in files:
   rel=str(f.relative_to(GRAPH))
   if not rel.startswith(('10_concepts/','20_mechanisms/','30_events/')):continue
   matches=[(i,t)for i,t in enumerate(f.read_text().splitlines(),1)if pattern.search(t)]
   if matches:hits.append((len(matches)+(15 if pattern.search(f.stem)else 0),rel,matches))
  hits.sort(key=lambda r:(-r[0],r[1]));out=f'Matched {len(hits)} files\n'+'\n\n'.join(rel+'\n'+'\n'.join(f'{i}: {t[:350]}'for i,t in matches[:3])for _,rel,matches in hits[:min(25,max(1,args.limit))])
 record.update(result_characters=len(out),result_sha256=hashlib.sha256(out.encode()).hexdigest())
 with LOG.open('a')as f:f.write(json.dumps(record,ensure_ascii=False)+'\n')
 print(out)
if __name__=='__main__':main()
