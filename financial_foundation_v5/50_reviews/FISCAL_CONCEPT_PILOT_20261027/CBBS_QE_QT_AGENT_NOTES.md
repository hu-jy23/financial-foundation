# CBBS／QE／QT执笔与核读记录

执笔：`/root/cbbs_qe_qt_concepts`；用户指定并由主agent分派的GPT-6-Astra、medium；工作日2026-10-27（任务使用Asia/Shanghai）。本agent只写三个指定Concept及本目录的研究笔记、首次提交稿；未改共享索引、规范、旧正文、Event或Source，未上传，也未另派agent。

## 交付与覆盖

三篇均为新写的完整独立Concept，status=draft，reviewed_by=null，等待主agent逐篇审阅；不能把完成首稿当成审阅通过。

| 文件 | 资料边界 | 首次提交稿 |
|---|---|---|
| `10_concepts/C-MONEY-CBBS_central_bank_balance_sheet.md` | 历史余额到2025-04-30；使用2025年5月官方回顾报告，出版只核到月份，故evidence_as_of为字符串2025-05 | `C-MONEY-CBBS_FIRST_DRAFT.md` |
| `10_concepts/C-POL-QE_quantitative_easing.md` | 2022-03-16，净购买退出与全额再投资阶段 | `C-POL-QE_FIRST_DRAFT.md` |
| `10_concepts/C-POL-QT_quantitative_tightening.md` | 2025-04-28；2025年3月会议观点由4月9日纪要回顾 | `C-POL-QT_FIRST_DRAFT.md` |

三个首稿为本次提交时正文的逐字副本；主agent若要求修改，应保留首稿。

## 研究问题、实际阅读与选择

起点是任务书的三组问题：央行表怎样配平；资产购买为何可能影响风险补偿且不等于贷款乘数；到期缩表怎样穿过TGA、ONRRP与准备金，为什么上限／实际／融资口径必须分开。

已完整读指定规范与三篇旧concept、国债机制；较长工具输出曾截断，之后分块补读，不把一次被截断输出当成全部已读。catalog_index按相关对象和机制items核对，未将检索得到的普通变量新增为节点。已读ACQUISITION_SHORTLIST与SOURCES_FISCAL，采用前者BoE货币创造论文线索、后者FOMC和财政部入口，但全部用于本稿的关键原文另行亲自打开。

主动web检索包括Fed balance sheet/H.4.1/deferred asset、2017/2019正常化上限、Gagnon LSAP原研究，再直接打开美联储、纽约联储、英格兰银行、财政部原站。没有用新闻摘要的事实代替原文。搜索结果曾混入2025年末、2026年最新政策新闻，全部未采用。纽约联储sr441.pdf实际封面为2010年3月，故没有把它标成常见的2011年期刊版本。

- 理论与账户：BoE McLeay/Radia/Thomas 2014刊载页14—16、24—25及图3、APF脚注；Gagnon等2010 §1、§2（印刷页1—6）、§4.2事件研究假设（页14—17）、§4末／§5（页28—29）。没有借教材目录充作理论正文；没有通读整本教材或运行计量。
- 报表：H.4.1 2025-05-01表1、5、6相关行及脚注；美联储负债说明2021-11-15各节；2024年度审计报表印刷页3—4、附注3会计口径及汇缴、附注5到期／MBS／公允价值、附注12递延资产与分配。余下养老金、全设施附注未通读。
- 历史政策：2009-03-18、2010-11-03、2012-09-13、2014-10-29、2017-06-14和09-20、2019-03-20／07-31／10-11、2020-03-15／03-23、2022-01-26／03-16实施／05-04缩表计划、2024-05-01、2025-03-19声明与实施说明。声明采用实际政策条款，不把计划写成逐笔验证的实现。
- 近期解释：2025年3月会议纪要的交易台市场操作报告；2025年5月资产负债表回顾报告的表1及资产／负债正文；2025-04-28财政部借款估计全部关键段落、脚注1／3和Sources and Uses一页表的2025Q1/Q2行。

每项作者／机构、日期、正式链接、实际范围和未读部分均已分别落入三篇文末独立S-CBBS-PILOT、S-QE-PILOT、S-QT-PILOT前缀。访问均成功通过web原页或PDF；一次尝试本地requests下载审计PDF因环境没有requests模块失败，没有文件进入证据链，随后直接通过web读取原PDF。没有其他付费访问障碍，也没有保存原始市场行情数据。

## 需要主agent特别复核的实质问题

1. CBBS：H.4.1对递延资产采用负的“Earnings remittances due to Treasury”，年度审计表则列资产。本文恒等式允许带符号的其他负债，同时明确禁止混用。2024利息收入158,756、支出226,766、净利息支出68,010、年末递延资产215,955，单位均百万美元；递延资产年增82,637不是净利息损失。来源为审计表印刷页3—4、附注12。
2. CBBS：2024-09-25至2025-03-26总资产−340、证券−240、贷款−86、准备金+309、TGA−463、全部逆回购−204（其中ONRRP−175），单位十亿美元；用于说明资产缩小与准备金上升可以共存。数据来自2025年5月报告表1，不假称3月已知分析。
3. QE：30—100bp是Gagnon等2010综合估计的十年期限溢价效应区间，针对首轮LSAP组合，非置信区间、非仅3000亿美元国债计划、非当前通用系数。作者事件研究承认公告包含经济信息和其他政策，本文保留识别限制。
4. QE：2012年声明的每月长期持仓增加约850亿美元含期限延长计划，不能写成净扩表850亿。2014结束购买而维持本金再投资；2022年3月亦保留全额再投资，均不等同QT立即启动。
5. QT：2024/2025机构超额本金转投国债，因此350亿美元上限约束该组本金对总证券持仓的净减少贡献，不保证机构持仓本身最多减少350亿。min(M,C)公式专门交代同类再投资假设及跨类例外。
6. QT：财政部私人持有净市场借款已经含SOMA赎回所需融资。2025Q2预测由123变514，SOMA赎回75变15，现金起点850变406，单位十亿美元；不能给514再加15。原表SOMA括号负数在本文转成正的赎回额，已说明。
7. 2019计划原拟9月底结束，7月决定提前至8月；本文不把9月市场压力写成当时才结束QT，也不把10月技术性购票自动称QE。

## 尚未补齐的具体证据

没有完整公告前调查、逐券DV01、逐月实际赎回与MBS交割，也没有2019逐银行准备金分布；不能做公告意外、稀缺阈值或固定基点贡献的量化。2025年3月调查仅读纪要汇总，未取问卷原表。2025Q2最终财政融资结果及其后QT决策在选定历史截止之外。跨国主动售券实践、中国／欧元区合并及盈亏分担未专题研究。概念解释已完成，以上缺口影响更深入实证或扩展国别，而非用空标签替代当前正文。

## 自查

已检查三篇定义互相一致、美元单位和年月上限、正文来源锚点、YAML要求、已选机制ID、跨页文件路径及目录锚点。31个本地来源锚点均可解析；所有正文相对文件／目录锚点可解析（本批TGA／融资流动性按OUTPUT_PATHS使用正式路径）。机械检查不代替逐篇内容审阅。未修改catalog状态。

## 输入文件版本记录

以下为提交时读取到的SHA-256；共享文件按只读使用，若主agent同时修改其版本，需以本任务运行时间及内容审阅为准。

| 输入路径 | SHA-256 |
|---|---|
| `00_start/README.md` | `c4410609a7c1267585cbdc1752e08d50e410ea4565e10a387efe5492140a083b` |
| `00_start/AUTHORING_STANDARD.md` | `fd1a6e552e59c08044b4b545340c248397d81c2125790f08412e46c1a472e1c8` |
| `00_start/BATCH_TASK.md` | `64cda196d0872fab2c61c8610cc96fea2f5d4211fc2994539b298cd07f61953c` |
| `00_start/REVIEW_CHECKLIST.md` | `7d24a21e1ddecd3c58726544283e072268e388a71c1955da1211c3fe9e5422ee` |
| `00_start/NODE_SELECTION_GUIDE.md` | `f143df64bccddf5ad35124707125d39431d41c9cd0c65cdfb05029a43f50a0fa` |
| `00_start/templates/CONCEPT_TEMPLATE.md` | `90b2bf37e8525eb8946f4feb1643ea889b8b7732817db69e6cf2a62f0364ac5a` |
| `00_start/catalog_index.json` | `2e3507d689f8fac421a9bf94110c6d2bc55ac937c75554b277b53d5f3f258915` |
| `10_concepts/C-IR-REAL_real_interest_rate.md` | `b6067a0e4cbba0e425bedb0ef04a77a8d98baa4f38e8a860620329a497ced7ad` |
| `10_concepts/C-IR-TERM_term_premium.md` | `54163ad222e8212e3a40339e87fdb58a3d58252522ebc8719225ab61c7d4f842` |
| `10_concepts/C-IR-POLICY_policy_rate_target_range.md` | `169f200583909fb3e5f32ed07bf64e6200f0b1b784d75c9cf1b08506e28944cd` |
| `20_mechanisms/R-FISCAL-LONGYIELD_fiscal_long_yields.md` | `653d2aed2ef2184ceaa05e64be00f609d057e3763d9b7bbabb6f75fc12b490bd` |
| `40_sources/ACQUISITION_SHORTLIST.md` | `c0c4964479be518eee09d08116b90416e66fd8d60d49004ad54c8c94a7effa9b` |
| `40_sources/SOURCES_FISCAL.md` | `05158ece98178b262aee624ea3b67bf069de53cff0eb466639bafacc9f0b60be` |
| `50_reviews/FISCAL_CONCEPT_PILOT_20261027/CBBS_QE_QT_TASK.md` | `e6dc3788f910fa26b828c2d8c659a2336e1558622fa159a7483c5de2024accc8` |
| `50_reviews/FISCAL_CONCEPT_PILOT_20261027/OUTPUT_PATHS.json` | `3f2a2b694f9fb581795216feebaabe901442eb6d4b6460725caea3d59fcc4a9a` |
