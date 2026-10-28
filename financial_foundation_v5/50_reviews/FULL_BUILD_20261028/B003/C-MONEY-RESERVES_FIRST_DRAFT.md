---
id: C-MONEY-RESERVES
type: concept
title: 银行准备金
status: draft
draft_author: "/root/full_b003"
model: gpt-6-astra
reasoning_effort: medium
reviewed_by: null
updated: 2026-10-28
evidence_as_of: 2026-03-31
source_ids: [S-C-MONEY-RESERVES-01, S-C-MONEY-RESERVES-02, S-C-MONEY-RESERVES-03, S-C-MONEY-RESERVES-04, S-C-MONEY-RESERVES-05, S-C-MONEY-RESERVES-06, S-C-MONEY-RESERVES-07, S-C-MONEY-RESERVES-08, S-C-MONEY-RESERVES-09]
---

# 银行准备金

> 执笔：`/root/full_b003`，GPT-6-Astra，medium。历史和专业判断资料截至2026-03-31；制作与原文核读日为2026-10-28。本文以美国准备金余额为主要制度例子，英国材料用于解释账户关系，不将一国参数移用于其他国家。

## 概念定义

银行准备金在本页主要指银行等合资格存款类机构持有的央行账户余额：它是银行的资产，同时是央行的负债，用于银行间最终支付结算、满足适用的准备金要求及维持流动性缓冲。它与公众在商业银行持有的存款属于不同层级的货币。某些统计和历史制度把库存现金也计入准备金，因此“准备金余额”和包含库存现金的广义准备金必须分清；美国旧制度允许以库存现金及央行账户余额满足法定要求。[S-C-MONEY-RESERVES-01](#S-C-MONEY-RESERVES-01)、[S-C-MONEY-RESERVES-02](#S-C-MONEY-RESERVES-02)

最重要的三个问题分别是：体系一共有多少准备金，准备金在哪些银行账户中，以及这些银行在某个付款时点愿意和能够动用多少。总量充足并不自动回答后两个问题。

## 概念详解

### 付款会转移准备金，贷款创造的首先是存款

设客户甲在A银行付款100给B银行客户乙，忽略手续费，且采用央行账户结算。A减少甲的存款负债100并支付准备金100；B增加准备金资产100，并增加乙的存款负债100。央行只是将账户余额从A转记B，银行体系准备金总额没有因此变化。

若A先发放一笔贷款100，通常是同时增加贷款资产100和客户存款负债100。客户随后跨行使用这笔存款时，A才面临上述准备金支付。A需要吸收存款、借入同业资金、变现资产或通过合资格央行工具取得结算资金，并承担相应成本。贷款的盈利、资本、信用风险和借款需求约束都仍然存在。“贷款先创造存款”不等于银行可以不管理付款资源。英国央行2014年文章以贷款、跨行付款和银行再融资说明这一过程；其账户逻辑有一般意义，具体操作框架须按国家核对。[S-C-MONEY-RESERVES-01](#S-C-MONEY-RESERVES-01)

公众通常不持有银行准备金账户，银行不能把准备金余额直接交给家庭当作其普通存款。银行可以借出资金给另一银行，这会转移已有准备金；对非银行贷款则改变存款及贷款资产，随后支付再改变准备金分布。因此，准备金总量增长不能按固定乘数机械推出新增贷款；准备金下降也不意味着每一美元银行贷款必须同时减少。

### 谁能改变体系总量

将央行资产负债表简化为资产\(A\)、准备金\(R\)、流通现金\(C\)、财政账户\(G\)、逆回购负债\(Q\)、其他净负债与资本\(O\)，同币种金额满足：

\[
R=A-C-G-Q-O,\qquad
\Delta R=\Delta A-\Delta C-\Delta G-\Delta Q-\Delta O.
\]

这是记账恒等式，不是每一项变化的因果识别。它说明准备金既受央行资产操作影响，也受负债构成影响。Vissing-Jorgensen的2025年分析分别讨论以准备金、ON RRP、证券或贷款吸收TGA波动；本式为加入其他项后对该框架的归纳。[S-C-MONEY-RESERVES-03](#S-C-MONEY-RESERVES-03)

**假设算例：** 央行资产缩减100，其他项不变，准备金减少100；若同期ON RRP下降80，则准备金只减少20。若财政账户又增加50，准备金合计减少70。三个流量使用同一期间、同一金额单位，计算为\(-100-50-(-80)=-70\)。不能仅看到资产缩减100就断言银行准备金恰好缩减100。

央行从非银行购买证券时，卖方银行通常获得准备金、卖方获得银行存款；从银行自营持仓买入时，则可表现为该银行证券资产换成准备金。财政向私人部门付款通常将财政账户负债转换为银行准备金，收税反向转换。私人部门购买国债的最终准备金影响还与资金是否来自ON RRP等渠道有关。相应完整传导分别见[TGA收支对准备金的影响](../20_mechanisms/R-TGA-RESERVES.md)及[QT与准备金、ONRRP及资金市场](../20_mechanisms/R-QT-LIQ.md)。

### 法定要求、主动缓冲与“充裕”是三种不同概念

法定准备金要求由适用负债基数、比率和考核办法决定；超过法定要求的部分可被称为超额准备金，但“超额”不等于没有用途。银行仍需要应付日内付款、存款流出和压力情景，可能愿意持有远高于法定最低值的央行余额。

美国自2020-03-26将相关准备金要求比率降至零，消除了存款类机构的法定准备金要求。这没有取消准备金账户，也没有消除银行的结算需求、流动性管理和其他审慎约束。把全部余额称为“超额”，容易让读者误以为所有余额都可无成本借出。[S-C-MONEY-RESERVES-02](#S-C-MONEY-RESERVES-02)

“充裕准备金”（ample reserves）则是货币政策操作状态：主要依靠管理利率维持短端利率控制，准备金供给的小幅变动不应引发很大的市场利率反应。纽约联储2026年解释把更宽松的abundant、ample及scarce区分开；ample是一个范围，不是永久固定的美元阈值。随着银行资产、支付规模、内部缓冲和制度改变，相同总额可以对应不同紧张程度。[S-C-MONEY-RESERVES-08](#S-C-MONEY-RESERVES-08)

### 余额存在，为什么还可能不够用

一家银行在央行的余额，是其自身清算资产；其他银行拥有余额不等于它可以无条件使用。取得别家资金需要对方愿意出借、信用或抵押安排成立，并能在付款截止前结算。持有国债也不等同于已经拥有准备金，卖出或回购融资需要经过市场和操作流程。

银行还会比较外借收益与放弃缓冲的代价。[准备金利率](../10_concepts/C-MONEY-07.md)给持有余额提供收益基准；外借利率即使略高，若新增交易占用资产负债表、提高日内支付风险或使内部压力缓冲不足，银行仍可能不借。央行设施改善取得准备金的后备能力，但准入、抵押品和时间安排决定它对哪家机构有效。Perli在2025-05-22特别指出，当时SRF下午操作结算与回购市场早间活动之间存在时间摩擦，并讨论净额处理和分配不确定性。这是当时工具安排的具体限制，不是2026年现行时刻表。[S-C-MONEY-RESERVES-06](#S-C-MONEY-RESERVES-06)

2019年的事后研究还发现，在利率大幅上升时，银行和非银行出借人都没有迅速扩张资金供给；研究者提出现金流不确定性、交易关系和监管／内部风控等可能解释。因此不能把所有“不愿出借”都归因于一条监管比率，更不能用总准备金余额证明市场中介必定无摩擦。[S-C-MONEY-RESERVES-04](#S-C-MONEY-RESERVES-04)

## 观测与相近概念

| 观察项目 | 用途与口径 |
|---|---|
| 央行准备金余额 | 美国H.4.1等央行资产负债表统计提供总量；周平均、星期三截面、月平均与年末时点需分别保存 |
| 其他央行负债和资产 | 同看财政账户、ON RRP、现金、证券与贷款，解释总量变化来自哪里 |
| 利率相对管理利率的位置 | EFFR及回购利率相对IORB等的变化，有助于观察稀缺程度；绝对利率上升也可能只是政策加息 |
| 交易分布与支付时间 | 高利率成交占比、银行借入结构、日内支付延后及设施使用，补足平均价格和总量的盲点 |
| 银行自身需求 | 流动性压力测试、内部最低余额及调查回答；调查反映受访机构需求，不能直接当成系统确定阈值 |

准备金不同于[银行资本](../10_concepts/C-CREDIT-02.md)：前者解决结算与流动性，后者吸收损失。准备金也不同于[财政部一般账户](../10_concepts/C-MONEY-13_treasury_general_account.md)及[ON RRP](../10_concepts/C-MONEY-14.md)，后两者是另外的央行负债。对非银行而言的现金可包括银行存款；对银行而言最直接的央行结算资源才是本页讨论的余额。跨币种余额、海外实体与本地法人之间也不能在付款分析中自动合并。

## 本对象的历史、判断与结果

### 2007—2020：从稀缺余额转向大量余额，需求却没有归零

美联储研究者2020年的回顾记录，准备金从2007年末不足100亿美元升至2014年10月约2.8万亿美元；资产购买改变了央行负债的量级。后来即使资产未继续缩减，流通现金和其他负债增长仍可减少准备金。[S-C-MONEY-RESERVES-04](#S-C-MONEY-RESERVES-04)

2019年9月的企业缴税及国债结算集中发生，准备金在两个营业日减少约1200亿美元，并在月中低于1.4万亿美元。9月17日EFFR达到2.30%，超过当时目标区间上限；事后研究认为，低准备金基数与融资需求和交易摩擦共同放大波动。文章说市场预料到一些季节性压力，却未预料到实际幅度；本文没有取得当时完整调查，因此不为“意外”补造数值。2020年法定要求归零是另一项制度变化，不能倒过来用于解释2019年的最低要求。[S-C-MONEY-RESERVES-04](#S-C-MONEY-RESERVES-04)、[S-C-MONEY-RESERVES-02](#S-C-MONEY-RESERVES-02)

### 2024：年末低点与月平均不是同一状态

纽约联储《2024年公开市场操作》报告记载，2024年12月准备金平均约3.2万亿美元，年末时点为2.89万亿美元，较2023年末减少2424亿美元。报告认为准备金仍处于abundant状态；证券缩减和BTFP余额下降的影响，部分由ON RRP下降抵消。这里只保留报告所用口径，不拿2.89万亿与其他月份平均数直接比较紧张程度。[S-C-MONEY-RESERVES-05](#S-C-MONEY-RESERVES-05)

### 2025年5月的判断与年末的制度变化

**当时判断，2025-05-22。** Perli称准备金约3.2万亿美元且指标仍显示abundant，认为ample所需数量低于当时水平，但明显高于2019年的水平。他预计资产负债表最终停止收缩，并在满足日益增长的央行负债需求时重新增长。这是操作框架的方向判断，没有给出精确停止月份或统一门槛。[S-C-MONEY-RESERVES-06](#S-C-MONEY-RESERVES-06)

**后来结果。** 2026-03-26讲话回顾，FOMC于2025年10月决定从12月1日起结束证券持有总量缩减，12月判断准备金已降至ample范围，并要求启动准备金管理购买（RMP）。2025-12-10纽约联储操作公告安排首期约400亿美元国库券购买，自12月12日开始。购买用于满足央行负债趋势增长及季节性波动；不能只因资产重新增长就直接称其为旨在降低长期收益率的QE。[S-C-MONEY-RESERVES-07](#S-C-MONEY-RESERVES-07)、[S-C-MONEY-RESERVES-09](#S-C-MONEY-RESERVES-09)

### 截至2026-03-31：为季节性需求提前保留缓冲

Perli、LeSueur与Molloy记录，自2025年12月中旬以来RMP月度速度为400亿美元。作者解释，高速度主要为2026年4月缴税流入财政账户、预期抽走准备金提前安排，并非2025年末必须立即投入同样规模才能控制利率。其历史观察是近几年4月税期TGA曾累计增加约1750亿至4000亿美元；这是过去变化范围，不是2026年精确预测。[S-C-MONEY-RESERVES-08](#S-C-MONEY-RESERVES-08)

**该时点的专业预期：** 作者预计从4月中旬至5月中旬购买期开始，RMP速度很可能显著降低，可能逐步实施；以后速度依赖央行负债需求和资金市场反馈。本文资料在3月31日截止，没有把后来实际购买规模或4月税收结果填入这项预期。它展示的是准备金管理如何面向未来付款高峰，而不是仅追着上周余额操作。

**本库条件推演，2026-10-28整理：** 若非准备金负债增加、其他资产负债不变，准备金将下降；若下降时市场利率对供给变动更敏感、银行支付延后且后备融资使用增加，紧张程度的证据会更强。若央行购买或贷款及时抵消，余额或资金价格未必出现同幅压力。此推演以账户和需求状态为条件，不设跨年份固定“危险余额”。

## 涉及的关系

- [QT与准备金、ONRRP及资金市场 R-QT-LIQ](../20_mechanisms/R-QT-LIQ.md)：准备金是负债替代后需要解释的余额及资金市场状态变量。
- [利率走廊 R-MONETARY-07](../20_mechanisms/R-MONETARY-07.md)：准备金供需状态与管理利率、常备工具共同决定隔夜利率控制方式。
- [TGA收支对准备金的影响 R-TGA-RESERVES](../20_mechanisms/R-TGA-RESERVES.md)：财政现金流可在央行负债之间转移余额，影响须看其他吸收项。
- [降准的资金与信贷传导 R-CHINA-01](../20_mechanisms/R-CHINA-01.md)：在有法定要求的制度中，降准改变银行所需保留及可调动的余额；不机械等于贷款创造。
- [资本流出、储备干预与本币流动性 R-INTERNATIONAL-09](../20_mechanisms/R-INTERNATIONAL-09.md)及[港元联系汇率与HIBOR传导 R-INTERNATIONAL-14](../20_mechanisms/R-INTERNATIONAL-14.md)：准备金是本币结算侧的变量，外汇交易是否被冲销及具体货币制度决定传导；不套用美国余额阈值。

## 来源与具体缺口

| 来源ID | 原始材料及实际阅读范围 |
|---|---|
| <a id="S-C-MONEY-RESERVES-01"></a>S-C-MONEY-RESERVES-01 | Michael McLeay、Amar Radia、Ryland Thomas／英国央行，[Money Creation in the Modern Economy](https://www.bankofengland.co.uk/-/media/boe/files/quarterly-bulletin/2014/money-creation-in-the-modern-economy.pdf)，2014-03-14；核读贷款创造、约束、图2跨行结算、图3与QE的两项误解（印刷页15—21、24—25相关段落）；未读取全部数据附件，英国2014框架不当作现行美国规则。 |
| <a id="S-C-MONEY-RESERVES-02"></a>S-C-MONEY-RESERVES-02 | 美联储，[Reserve Requirements](https://www.federalreserve.gov/monetarypolicy/reservereq.htm)，动态页，2026-10-28核读；2020归零说明、要求表及库存现金／账户余额脚注；未逐项核读1982年以来历史豁免表。 |
| <a id="S-C-MONEY-RESERVES-03"></a>S-C-MONEY-RESERVES-03 | Annette Vissing-Jorgensen，[Fluctuations in the Treasury General Account and their Effect on the Fed’s Balance Sheet](https://www.federalreserve.gov/econres/notes/feds-notes/fluctuations-in-the-treasury-general-account-and-their-effect-on-the-feds-balance-sheet-20250806.html)，2025-08-06；核读简化资产负债表及§a四种调整、§b/c提案。仅用会计与状态分析，未将作者TGA隔离提案写成实施政策。 |
| <a id="S-C-MONEY-RESERVES-04"></a>S-C-MONEY-RESERVES-04 | Sriya Anbil、Alyssa Anderson、Zeynep Senyuz，[What Happened in Money Markets in September 2019?](https://www.federalreserve.gov/econres/notes/feds-notes/what-Happened-in-Money-Markets-in-September-2019-20200227.htm)，2020-02-27；核读利率事实、Why did this happen、Broad Market Trends及Structure of the Repo Market；未重估微观交易资料。 |
| <a id="S-C-MONEY-RESERVES-05"></a>S-C-MONEY-RESERVES-05 | 纽约联储，[Open Market Operations during 2024](https://www.newyorkfed.org/medialibrary/media/markets/omo/omo2024-pdf.pdf)，2025年发布，精确发布日未核；核读报告页28—29 Reserve Balances及图18口径说明；未重建日频余额。 |
| <a id="S-C-MONEY-RESERVES-06"></a>S-C-MONEY-RESERVES-06 | Roberto Perli，[The Evolution of the Federal Reserve’s Monetary Policy Implementation Framework](https://www.newyorkfed.org/newsevents/speeches/2025/per250522)，2025-05-22；核读准备金需求、3.2万亿判断、Implementation Tools及跨国框架比较；讲话者观点，未提取原SFOS回答。 |
| <a id="S-C-MONEY-RESERVES-07"></a>S-C-MONEY-RESERVES-07 | 纽约联储，[Statement Regarding Reserve Management Purchases Operations](https://www.newyorkfed.org/markets/opolicy/operating_policy_251210a)，2025-12-10；核读操作公告全文，首期规模、开始日及未来调整条件；未提取逐次成交。 |
| <a id="S-C-MONEY-RESERVES-08"></a>S-C-MONEY-RESERVES-08 | Roberto Perli、Eric LeSueur、Linsey Molloy，[The Implementation of Reserve Management Purchases to Maintain Ample Reserves](https://tellerwindow.newyorkfed.org/2026/03/31/the-implementation-of-reserve-management-purchases-to-maintain-ample-reserves/)，2026-03-31；核读Abundant to Ample、Amounts to Date、Outlook及Operations正文，图表未复算；未来节奏保留当时预期。 |
| <a id="S-C-MONEY-RESERVES-09"></a>S-C-MONEY-RESERVES-09 | Roberto Perli，[Reflections on the Early Days of Reserve Management Purchases and the Maintenance of Ample Reserves](https://www.newyorkfed.org/newsevents/speeches/2026/per260326)，2026-03-26；核读引言中2025政策日期、状态指标与RMP安排及Outlook；未提取附件全部面板。 |

具体缺口：未取得银行逐家、逐时支付及内部最低余额，不能由公开总量计算谁缺资金；2024数据为官方事后年报口径，2019的意外幅度缺当时原始调查。2026-03-31以后的购买执行、税期余额和工具参数未核，因此不说明2026年10月的实际准备金状态。中国及港元节点在此仅给概念入口，其制度参数和历史不在本页已核范围。
