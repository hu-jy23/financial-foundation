# 财政赤字／TGA：执笔与研究记录

- 实际作者：`/root/fiscal_tga_concepts`；用户指定模型GPT-6-Astra、reasoning effort medium；任务2篇，未另派agent。
- 日期：2026-10-27，按任务以Asia/Shanghai记日期。
- 输入：当前共享`financial_foundation_v5`；完整任务为本目录`FISCAL_TGA_TASK.md`。读取README、AUTHORING_STANDARD、BATCH_TASK、REVIEW_CHECKLIST、NODE_SELECTION_GUIDE、CONCEPT_TEMPLATE、实际利率／期限溢价／政策利率样例、国债供给机制、相关catalog_index节点及关系、ACQUISITION_SHORTLIST与SOURCES_FISCAL。长输出曾截断，后按范围补读；未改共享输入。
- 新写两篇，未复制旧成品正文，未建Event或Source文件，来源在各Concept页用独立前缀登记。跨页链接按OUTPUT_PATHS；待写机制与其他节点链接正式目录锚点。

## 输出

1. `10_concepts/财政赤字与初级赤字.md`
2. `10_concepts/财政部一般账户TGA.md`
3. 本笔记。
4. 本目录`C-FISCAL-DEFICIT_FIRST_DRAFT.md`、`C-MONEY-13_FIRST_DRAFT.md`为首次交审完整快照；此后退修不覆盖。

## 研究路径与已核内容

### 财政篇

优先搜财政部FY2024预算结果、CBO年度月报、IMF债务动态与GFSM原始资料。搜索引擎1对部分域名查询返回无关结果，改用引擎2定位官方原文，再逐页open。未据搜索摘要填重要数字。

- 财政部2024-10-18联合声明 `https://home.treasury.gov/news/press-releases/jy2657`：Summary及表1，实际4439/6135/1695与4919/6752/1833的十亿美元级量；FY2024两个OMB预测版本的baseline与policy差别。正文重点不采用政治因果评价。
- 通过FY2024财务报告中September MTS链接找到可访问的最终PDF `https://fiscal.treasury.gov/system/files/files/reports-statements/mts/mts0924.pdf`。初试Fiscal Data静态路径无法读取，未以失败路径登记为读过。
- MTS PDF第3页明确“modified cash basis”，公众发行债务利息按accrual确认；第5页表1/2：FY2023赤字1695240百万美元、FY2024赤字1832816；第38页表9：净利息659182及881651百万美元。计算的初级赤字1036058及951165百万美元。正文标明是本页算术，不是原表直接发布的初级行。
- MTS表2融资：1959809向公众借款，运营现金增加228836，其他融资101843，单位百万美元。复算1959809−228836+101843＝1832816。注意表2各列PDF文本可能换行错位，最终算式同时与合计对账；主审可重点看PDF第5页原表。
- GAO 2025-02-05 `https://www.gao.gov/products/gao-25-107714` Highlights直接给约9500亿初级赤字、8820亿净利息，交叉核对定义与数量级；未采用其未来200%债务率情景。
- CBO `https://www.cbo.gov/publication/60843/html` 开篇与表1、调整和预测比较：观察到9490亿“net outlays for interest on the public debt”，与MTS功能900净利息不是同一数。没有冒充已完成差额逐账户解释。FY2024实际低于2024年6月CBO基线820亿，收入＋290、支出−530，不能与OMB预测混用。学生贷款和支付日历调整分开。
- Fiscal Service FY2024财务报告MD&A，表1、Accounting Differences、Budget Deficit vs. Net Operating Cost及表2：2425.0净经营成本与1832.8预算赤字，单位十亿美元；只解释两种会计口径，不把差额解释成隐性新增市场借款。
- IMF Escolano 2010原PDF、eLibrary正文、GFSM2014第4章均403；另试HTTP下载仍403。只取得目录／搜索摘要，不作为已读理论来源。
- 改读ECB Cristina Checherita-Westphal 2019原始技术分析全文 `https://www.ecb.europa.eu/press/economic-bulletin/focus/2019/html/ecb.ebbox201902_06~0c96ee6f7c.en.html`，尤其脚注1精确分母1+g与Chart A有效利息定义。模型边界、SFA、i−g不固定由本页解释，未复算欧元区经验表，未替作者声称因果。
- 2025-04-28财政部sb0115脚注1核私人持有净市场借款、SOMA、回购范围；用于融资桥，不将MTS向公众借款与私人市场净借款合并。

### TGA篇

- NY Fed Cipriani等，2022-04-11，亲读四部门简化表、Treasury偿付Fed、银行买债、MMF动用存款／ON RRP及结论。税款／政府付款100元例子由本页按相同账户逻辑展开，发债与其后政府花钱分别解释。
- Annette Vissing-Jorgensen 2025-08-06 FEDS Notes，a—c节全文，四种配平及短券配套提案；采用资料使TGA篇evidence_as_of扩展至该日，但主要现金历史仍为2025年4月以前。没有将提案写成现行规则，也没有核读其脚注工作论文。
- Treasury Brian Smith 2021-04-08演讲现金段落，2015规则为回顾：一周流出、1500亿最低缓冲；2021二月假设三月末8000亿、六月末5000亿，三月末约1.1万亿结果。当时判断与结果分开。
- 2024-03-01 MPR Part2：2023年6月以来TGA＋6540亿、ON RRP−1.5万亿、准备金＋2170亿。它是至2024年2月的较长窗口，不是2023Q3单季，也不是全部TGA流量来自ON RRP的归因。
- sb0115，2025-04-28全文及脚注：一季度3690亿借款、4060亿现金；二季度预测1230→5140亿，起点8500→4060亿，季末假设8500亿，依赖债务上限解决；现金贡献4440亿，SOMA下降抵消600亿。5140是预测，非结果。
- Sources_and_Uses_Table_April_2025.pdf一页：2023Q2/Q3实际与2025预测行；Q3现金变动254与端点差255十亿美元存在分项四舍五入，正文保留原数而不改表；SOMA原表括号负值，正文对照表按正偿还额，明确是改符号。
- H.4.1 2025-04-24表1：周均606632与周三576159百万美元；差30473，展示同报表不同时间聚合。未提取后续序列。
- Treasury Receipts & Outlays说明页实读DTS可得时点和MTS描述。DTS数据集与2025-03-31单日报表访问403，未从搜索摘要取每日余额；改用已核季度现金表。

## 自查与需主审的实质点

两篇均从对象本身解释，财政篇不只作为发行附注，TGA篇不把“流动性”一词替代账户过程。所有假设算例显式标识；所有官方预测均注明主体、版本、期间和条件。没有2026最新政策断言，没有写会前市场概率。

建议主审重点复核：

1. MTS表2的现金与其他融资三项对账；表9净利息用于初级赤字是否一致。CBO949与MTS881.651的差额逐账户解释仍明确留缺口。
2. 债务方程的有效利息与债务存量范围；本页将净利息／毛债务混配风险写在公式附近，未给“当前美国”债务率预测。
3. TGA发行三种资金来源以及财政部直接偿还Fed的例外；税收／支出说明均设其他交易固定，第三行ON RRP反映完整链条净结果。
4. TGA 2023/2024窗口、2025Q2预测与8月研究提案的时间分隔；2015现金规则只作为2021演讲回顾。
5. 待写的跨页C-LIQ-FUND和C-MONEY-CBBS路径按OUTPUT_PATHS预留，由主agent合并时核实文件存在。

未解决事项均保留在文末；这些不妨碍当前定义、基本账户与已核历史成立，但不足以进行每日资金归因、逐账户利息差额归因或当前财政预测。未上传。
