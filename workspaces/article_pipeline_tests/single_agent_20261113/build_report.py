import ast,html,json,os,re
from pathlib import Path
from urllib.parse import quote
from markdown_it import MarkdownIt
R=Path(__file__).resolve().parent;W=R.parent.parent.parent;M=MarkdownIt('commonmark',{'html':False})
E=lambda x:html.escape(x if isinstance(x,str)else json.dumps(x,ensure_ascii=False),quote=True)
def rich(x):
 if not x:return ''
 if isinstance(x,str) and re.fullmatch(r'https?://[^\s]+',x):return '<p><a href="'+E(x)+'">'+E(x)+'</a></p>'
 if isinstance(x,list):return '<ul>'+''.join('<li>'+rich(v)+'</li>'for v in x)+'</ul>'
 if isinstance(x,dict):return '<dl>'+''.join('<dt>'+E(k)+'</dt><dd>'+rich(v)+'</dd>'for k,v in x.items())+'</dl>'
 return M.render(str(x))
def plain(x):
 if isinstance(x,str):return x
 if isinstance(x,list):return '\n'.join('- '+plain(v)for v in x)
 if isinstance(x,dict):return '\n'.join(str(k)+'：'+plain(v)for k,v in x.items())
 return str(x)
def link(t,p):return '<a href="'+E(quote(os.path.relpath(p,R),safe='/'))+'">'+E(t)+'</a>'
old=ast.parse((R.parent/'multi_agent_20261113/build_report.py').read_text());CSS=next(ast.literal_eval(n.value)for n in old.body if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='CSS'for t in n.targets))
meta=json.loads((R/'run_manifest.json').read_text());review=json.loads((R/'review.json').read_text())if(R/'review.json').exists()else{}
results=[json.loads(p.read_text())for p in sorted((R/'成果').glob('*.json'))]
sections=[];toc=[];total_c=total_r=0
for d in results:
 key=d['run_id']
 draft=['# '+d['title']+'：知识与分析草稿','', '本轮试作导出稿；内容维护建议尚未接入正式graph。','', '## 文章问题','',plain(d.get('problem',''))]
 for group,label in [('concepts','重要概念与对象'),('relations','重要关系')]:
  draft+=['','## '+label]
  for v in d.get(group,[]):
   draft+=['','### '+v['name'],'',plain(v.get('core_text','')),'','处理：'+plain(v.get('action','')),'现有覆盖：'+plain(v.get('existing_match','')),'','来源：'+plain(v.get('sources',[]))]
 draft+=['','## 进一步分析','',plain(d.get('analysis','')),'','## 维护安排','',plain(d.get('organization','')),'','## 资料边界','',plain(d.get('limitations',''))]
 (R/'成果'/f'{key}.md').write_text('\n'.join(draft)+'\n')
 toc.append('<a href="#'+key+'">'+E(d['title'])+'</a>');parts=[]
 for group,label in [('concepts','重要概念与对象'),('relations','重要关系')]:
  entries=d.get(group,[]);total_c+=len(entries)if group=='concepts'else 0;total_r+=len(entries)if group=='relations'else 0
  rows=[];cards=[]
  for i,v in enumerate(entries):
   anchor=f'{key}-{group}-{i}';rows.append('<tr><td><a href="#'+anchor+'">'+E(v.get('name',''))+'</a></td><td>'+E(v.get('action',''))+'</td><td>'+rich(v.get('existing_match',''))+'</td></tr>')
   info=rich(v.get('role',v.get('participants','')));source=rich(v.get('sources',[]))
   cards.append(f'<details class="agent" id="{anchor}"><summary><span class="run">{E(v.get("action",""))}</span><span>{E(v.get("name",""))}</span><span class="expand">展开</span></summary><div class="inside">{info}<div class="sample">{rich(v.get("core_text",""))}</div><h4>对照现有graph</h4>{rich(v.get("existing_match",""))}<h4>来源</h4>{source}</div></details>')
  parts.append('<h3>'+label+'</h3><div class="table-wrap"><table><thead><tr><th>内容</th><th>处理</th><th>现有覆盖</th></tr></thead><tbody>'+''.join(rows)+'</tbody></table></div>'+''.join(cards))
 case=meta['cases'][key];p=W/case['markdown']
 sections.append('<section id="'+key+'"><p class="eyebrow">'+str(d['article_id'])+' · 单篇单agent</p><h2>'+E(d['title'])+'</h2><p>'+link('本地原文',p)+' · '+link('HTML原文',p.with_suffix('.html'))+' · '+link('知识与分析草稿MD',R/'成果'/f'{key}.md')+' · '+link('完整结果JSON',R/'成果'/f'{key}.json')+'</p><div class="boundary">'+rich(review.get('cases',{}).get(key,''))+'</div><h3>文章问题</h3>'+rich(d.get('problem',''))+''.join(parts)+'<h3>进一步分析</h3>'+rich(d.get('analysis',''))+'<h3>维护与结构安排</h3>'+rich(d.get('organization',''))+'<details><summary>限制、实际阅读与外部来源</summary>'+rich(d.get('limitations',''))+rich(d.get('external_sources',[]))+rich(d.get('reading',{}))+'</details><h3>对本轮说明的反馈</h3>'+rich(d.get('guidance_feedback',''))+'</section>')
checks=review.get('coverage',[]);findings=review.get('findings',[])
body=f'''<header><p class="eyebrow">FINANCIAL FOUNDATION / 2026.11.13</p><h1>先补齐重要知识，<br>再展开文章分析。</h1><p class="lead">三篇文章，各一个继承完整上下文的subagent。概念与关系覆盖在前，深入解释和结构安排在后。</p><div class="stats"><div><strong>{len(results)}</strong><span>篇文章／试作</span></div><div><strong>{total_c}</strong><span>项概念清单条目</span></div><div><strong>{total_r}</strong><span>项关系清单条目</span></div></div><p class="muted">清单包含引用与更新，以上数量不等于新增节点数；正式graph尚未接入本轮提案。</p></header><nav><a href="#overview">修改与顺序</a><a href="#coverage">覆盖检查</a><a href="#results">三篇成果</a><a href="#docs">说明文件</a></nav><main><section id="overview"><h2>本轮如何调整</h2><p>通读与看图 → 重要概念／关系清单 → 对照现有graph → 基础解释制作 → 进一步分析 → 内容维护安排 → 主agent审阅。</p><ul class="findings">{''.join('<li>'+rich(x)+'</li>'for x in findings)}</ul></section><section id="coverage"><h2>重点内容是否真正写出</h2>{rich(checks)}</section><section id="results"><h2>三篇文章的基础与分析</h2><p>{' · '.join(toc)}</p><p><button id="open">展开全部知识条目</button> <button id="close">收起知识条目</button></p></section>{''.join(sections)}<section id="docs"><h2>修改了哪些说明</h2>{rich(review.get('document_changes',[]))}<p>{link('制作纲领',R.parent/'维护/ARTICLE_AUTHORING_CHARTER.md')} · {link('本轮流程',R/'说明/README.md')} · {link('交付任务',R/'说明/TEST_TASK.md')} · {link('子层级讨论',R/'说明/SUBSTRUCTURE_DISCUSSION.md')}</p><p>{' · '.join(link(n,R/'说明'/n)for n in ['AUTHORING_STANDARD.md','NODE_SELECTION_GUIDE.md','EVENT_SOURCE_GUIDE.md','REVIEW_CHECKLIST.md'])}</p><div class="boundary"><p>每篇只分派一个agent；主agent统一审阅，没有为同文生成多个并行版本。运行继承完整上下文，具体模型与档位未独立核验。原新闻与补查资料的读取范围在各篇结果中说明，转引数字不自动视为已核实事实。</p></div><p>{link('运行记录',R/'run_manifest.json')} · {link('审阅记录',R/'review.json')} · {link('检查记录',R/'checks.json')}</p></section></main><footer>本地报告 · 重要知识覆盖与正式注册分别判断</footer>'''
js="document.getElementById('open').onclick=()=>document.querySelectorAll('details.agent').forEach(x=>x.open=true);document.getElementById('close').onclick=()=>document.querySelectorAll('details.agent').forEach(x=>x.open=false);document.querySelectorAll('a[href^=\"#\"]').forEach(a=>a.onclick=()=>{const x=document.querySelector(a.getAttribute('href'));if(x?.tagName==='DETAILS')x.open=true});"
(R/'报告.html').write_text('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>三篇文章：基础知识与进一步分析</title><style>'+CSS+' main section{scroll-margin-top:16px}.stats{flex-wrap:wrap}dl{overflow-wrap:anywhere}.sample{overflow-wrap:anywhere}</style></head><body>'+body+'<script>'+js+'</script></body></html>')
print('built',len(results),total_c,total_r)
