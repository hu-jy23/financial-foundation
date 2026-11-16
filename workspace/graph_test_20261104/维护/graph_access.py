#!/usr/bin/env python3
"""答题期间只读冻结graph；每次访问写入agent1日志。无网络功能。"""
import argparse,hashlib,json,re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
ROOT=Path(__file__).resolve().parents[1]
GRAPH=(ROOT/'graph_snapshot').resolve()
LOG=ROOT/'agent1/graph_reads.jsonl'

def paths():
 return sorted(p for p in GRAPH.rglob('*') if p.is_file() and p.suffix in {'.md','.json'})

def emit(args,data):
 result=json.dumps(data,ensure_ascii=False,indent=2)
 record={'time':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(timespec='seconds'),'question':args.question,'operation':args.operation,'arguments':{k:v for k,v in vars(args).items() if k not in ['question','operation']},'result_sha256':hashlib.sha256(result.encode()).hexdigest(),'result_characters':len(result)}
 with LOG.open('a',encoding='utf-8') as f:f.write(json.dumps(record,ensure_ascii=False)+'\n')
 print(result)

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--question',default='setup');s=p.add_subparsers(dest='operation',required=True)
 a=s.add_parser('list');a.add_argument('--contains',default='')
 a=s.add_parser('search');a.add_argument('pattern',help='Python正则，支持用|分隔多个关键词');a.add_argument('--limit',type=int,default=18)
 a=s.add_parser('read');a.add_argument('path');a.add_argument('--start',type=int,default=1);a.add_argument('--end',type=int,default=180)
 args=p.parse_args()
 if args.operation=='list':
  emit(args,[str(x.relative_to(GRAPH)) for x in paths() if args.contains.casefold() in str(x.relative_to(GRAPH)).casefold()]);return
 if args.operation=='read':
  f=(GRAPH/args.path).resolve()
  if not f.is_relative_to(GRAPH) or not f.is_file() or f.suffix not in {'.md','.json'}:p.error('只可读取冻结graph中的Markdown或JSON')
  lines=f.read_text().splitlines();lo=max(1,args.start);hi=min(len(lines),args.end,lo+399)
  emit(args,{'path':str(f.relative_to(GRAPH)),'total_lines':len(lines),'lines':[{'line':i,'text':lines[i-1]} for i in range(lo,hi+1)]});return
 pattern=re.compile(args.pattern,re.I);hits=[]
 for f in paths():
  rel=str(f.relative_to(GRAPH));lines=f.read_text().splitlines();matches=[{'line':i,'text':line[:900]} for i,line in enumerate(lines,1) if pattern.search(line)]
  if matches:hits.append({'path':rel,'match_count':len(matches),'matches':matches[:5],'rank':len(matches)+(15 if pattern.search(f.stem) else 0)})
 hits.sort(key=lambda x:(-x['rank'],x['path']))
 emit(args,{'total_files':len(hits),'hits':hits[:min(40,max(1,args.limit))]})

if __name__=='__main__':main()
