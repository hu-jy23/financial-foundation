#!/usr/bin/env python3
"""检查项目自编页面的本地链接；原始下载HTML的站点导航保留原样。"""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json, os, re
from markdown_it import MarkdownIt

ROOT=Path(__file__).resolve().parents[1]
MD=MarkdownIt('commonmark',{'html':True}).enable('table')
def main():
 files=[];known={str(ROOT)}
 for parent,dirs,names in os.walk(ROOT,followlinks=False):
  dirs[:]=[x for x in dirs if x not in {'.git','__pycache__'}]
  known.add(parent);known.update(str(Path(parent)/x) for x in names)
  files.extend(Path(parent)/x for x in names)
 issues=[];checked=0;external_cache={}
 for p in files:
  if p.suffix.lower() not in {'.md','.html','.htm'}:continue
  rel=p.relative_to(ROOT)
  if p.suffix!='.md' and rel.parts[0]=='materials' and rel.parts[1]!='wallstreetcn':continue
  try:s=p.read_text()
  except UnicodeDecodeError:continue
  urls=set()
  if p.suffix=='.md':
   s=re.sub(r'\\+\[.*?\\+\]','',s,flags=re.S)
   for token in MD.parse(s):
    for child in [token]+(token.children or []):
     url=child.attrGet('href') or child.attrGet('src')
     if url:urls.add(url)
  urls.update(m[2] for m in re.finditer(r'\b(?:href|src|poster)\s*=\s*(["\'])(.*?)\1',s,re.S|re.I))
  for url in urls:
   try:u=urlsplit(url)
   except ValueError:continue
   if u.scheme or u.netloc or not u.path:continue
   checked+=1;target=os.path.abspath(p.parent/unquote(u.path))
   if target in known:continue
   if target not in external_cache:
    try:external_cache[target]=Path(target).exists()
    except OSError:external_cache[target]=False
   if not external_cache[target]:issues.append({'file':str(rel),'url':url})
 result={'local_links_checked':checked,'broken_links':issues,'passed':not issues,'scope':'Markdown and authored HTML; original downloaded HTML navigation excluded'}
 out=ROOT/'docs/LAYOUT_CHECK.json';out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'local_links_checked':checked,'broken_count':len(issues),'first':issues[:30]},ensure_ascii=False,indent=2))
 return 0 if not issues else 1
if __name__=='__main__':raise SystemExit(main())
