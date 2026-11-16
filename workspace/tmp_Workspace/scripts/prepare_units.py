from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
WORK=ROOT/'tmp_Workspace'
SOURCES=ROOT/'financial_foundation_v5_20261027/source_2'
t1=[
('导言与需求侧',[0,1],1,62),('供给侧',[2],63,114),('三方程与预期',[3,4],115,202),
('货币、银行与宏观',[5],203,258),('货币政策',[6],259,306),('财政政策',[7],307,364),
('金融不稳定及危机应用',[8,9],365,459),('金融稳定政策',[10],460,484),
('开放经济基础',[11,12],485,591),('油价、失衡与国际相互依赖',[13],592,642),
('固定汇率与欧元区',[14],643,698),('供给侧制度',[15],699,747),
('增长与创新',[16],748,810),('ICT、生产率与不均衡增长',[17],811,856),
('异质主体宏观',[18],857,924)]
starts=[1,22,44,73,101,129,158,184,211,238,266,294,326,357,393,421,448,479,521,553,577,615,647,673]
names=['金融系统概览','货币与支付','工具、市场与机构','现值、终值与利率','风险','债券与利率决定','利率风险与期限结构','股票与市场效率','期货、期权与互换','外汇','金融中介经济学','银行与银行管理','金融业结构','金融监管','中央银行目标','美联储与ECB结构','央行资产负债表及货币供给','国内货币政策操作','汇率政策','货币增长与需求','产出、通胀与政策','经济波动','现代货币政策挑战']
t2=[('金融系统、货币支付与工具',[1,2,3],1,72)]+[(names[i-1],[i],starts[i-1],starts[i]-1) for i in range(4,24)]
manifest={'sources':{},'units':[]}
for book,specs,offset,version in [('T1',t1,36,'Carlin & Soskice, 2024; PDF有2023校样页眉'),('T2',t2,35,'Cecchetti & Schoenholtz, 6e ISE, ©2021, ISBN9781260571363')]:
 folder=next(SOURCES.glob(book+' *')); src=max(folder.glob('*.pdf'),key=lambda p:p.stat().st_size)
 pages=(WORK/'inputs'/f'{book}_full.txt').read_text().split('\f')
 if not pages[-1].strip(): pages.pop()
 manifest['sources'][book]={'path':str(src.relative_to(ROOT)),'version':version,'pages':len(pages),'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'printed_page_offset':offset}
 out=WORK/'inputs'/book;out.mkdir(exist_ok=True)
 for n,(title,chapters,a,b) in enumerate(specs,1):
  ident=f'{book}-U{n:02d}';lo=a+offset;hi=b+offset
  assert 1<=lo<=hi<=len(pages)
  text=''.join(f'\n\n===== PDF {i} | 印刷页 {i-offset} =====\n\n'+pages[i-1] for i in range(lo,hi+1))
  dest=out/f'{ident}.txt';dest.write_text(text)
  manifest['units'].append({'id':ident,'book':book,'title':title,'chapters':chapters,'printed_pages':[a,b],'pdf_pages':[lo,hi],'text':str(dest.relative_to(WORK)),'status':'assigned','candidates':0,'passed':0})
(WORK/'units.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
s='''# T1、T2阅读单元与派工

保留原书章节顺序；仅合并连续、共享前提与论证的章节，避免打散知识依赖。T1合并第3–4章、第8–9章、第11–12章；导言随第1章，分部页随相邻正文。T2第1–3章作为系统导入，其余按章。共36个unit，每unit先交2份最优候选，共72份首轮候选；通过数量不设配额。两份全通过才追加检查；全弃则结束。

这是一份派工清单，不是阅读地图。分unit文本是抽取结果，不代表已读或知识已吸收。原PDF中的目录、版权页与重要图表仍须核对；书后参考文献、索引不另设生产unit。所有章节正文和章末附录／练习均包含在指定范围内。

## 实际版本

'''
for book,v in manifest['sources'].items():
 s+=f'- {book}：{v["version"]}，{v["pages"]} PDF页。源路径与SHA-256见units.json。\n'
s+='\nT2使用用户刚提供的第6版，不冒称2024 Release。只依据实际版本写作，不把旧参数、制度截面写成当前状态。\n\n## unit列表\n\n| unit | 主题 | 章 | 印刷页 | PDF页 | 抽取文本 |\n|---|---|---|---|---|---|\n'
for u in manifest['units']:
 s+=f'| {u["id"]} | {u["title"]} | '+','.join(map(str,u['chapters']))+f' | {u["printed_pages"][0]}–{u["printed_pages"][1]} | {u["pdf_pages"][0]}–{u["pdf_pages"][1]} | [文本]({u["text"]}) |\n'
s+='''
## 候选接口

每unit写一个 `candidates/T1/T1-U01.md` 形式的文件，两份候选ID为 `T1-U01-A`、`T1-U01-B`。每份保留标题／类型、核心解释段落、现有图对照与实质增量、源PDF与印刷页定位、拟归属。先读取指定完整unit，再选择两份；不要把泛泛常识包装为模型新节点。第一批3个unit完成即通知主agent并继续。

筛选结论由另一批agent写reviews目录的短表；只给通过项写作范围与必要改进，不为弃用项建详细档案。主agent管理状态及跨书去重。全文接入正式图之前仍需逐篇读完。
'''
(WORK/'UNIT_PLAN.md').write_text(s)
print('Prepared',len(manifest['units']),'units; PDF pages',[(k,v['pages']) for k,v in manifest['sources'].items()])
for book in ['T1','T2']:
 first=next(u for u in manifest['units'] if u['book']==book)
 print(book,first)
