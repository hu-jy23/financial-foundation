---
id: R-TGA-RESERVES
type: mechanism
title: TGA收支对准备金的影响
status: reviewed_seed
draft_author: "/root/full_b054"
model: gpt-6-astra
reasoning_effort: medium
reviewed_by: /root
updated: 2026-10-28
evidence_as_of: 2026-03-26
source_ids: [S-R-TGA-RESERVES-01, S-R-TGA-RESERVES-02, S-R-TGA-RESERVES-03, S-R-TGA-RESERVES-04]
node_ids: [C-MONEY-13, C-MONEY-CBBS, C-MONEY-RESERVES, C-MONEY-14]
related_mechanism_ids: []
logic_groups:
  - anchor: logic-1
    node_ids: [C-MONEY-13, C-MONEY-CBBS, C-MONEY-RESERVES]
    related_mechanism_ids: []
  - anchor: logic-2
    node_ids: [C-MONEY-13, C-MONEY-14, C-MONEY-RESERVES, C-MONEY-CBBS]
    related_mechanism_ids: []
---

# TGA收支对准备金的影响

> 执笔：`/root/full_b054`，GPT-6-Astra，medium；制作日2026-10-28。资料截止2026-03-26；2026年4月税期结果未核验。

## 概念定义

财政部一般账户TGA的收付款，会改变美联储负债由谁持有。私人部门通过银行向TGA付款时，银行准备金通常转为财政部存款；财政部向私人部门付款时，方向相反。但准备金的最终净变化，还取决于付款资金是否先来自ON RRP到期，以及联储资产和其他负债是否同时变化。本机制把财政现金流、结算路径与央行全表联系起来，解释为什么“TGA增加”有时抽走准备金，有时主要替代另一项央行负债。

## 概念详解

TGA是财政部在联储的资产；准备金是商业银行等存款机构在联储的资产。两者均列在联储负债端，却不属于同一持有人。居民持有的银行存款又是商业银行负债，不能与准备金互换称呼。政府在银行体系之外持有现金，意味着财政现金管理能够改变银行可直接用于清算的资产数量。[S-R-TGA-RESERVES-01](#S-R-TGA-RESERVES-01)

应区分税收、支出、一级发行交割和二级市场交易。税款与新债认购款进入TGA，财政支付与偿还到期本金流出TGA；二级交易通常不向财政部提供新现金。财政赤字属于期间收支，TGA属于时点现金余额，发债可以先补现金、以后再支出。因此本页讨论结算与负债构成，并不把现金回补等同于财政紧缩，也不从准备金方向直接推导股票价格。

<a id="logic-1"></a>
## 核心逻辑1：财政收付款通过结算银行改变准备金

**关联节点／节点组**：[财政部一般账户TGA C-MONEY-13](../10_concepts/C-MONEY-13_treasury_general_account.md)、[央行资产负债表 C-MONEY-CBBS](../10_concepts/C-MONEY-CBBS_central_bank_balance_sheet.md)、[银行准备金 C-MONEY-RESERVES](../10_concepts/C-MONEY-RESERVES.md)。

**时间段**：适用于财政部通过联储账户办理收付的美国制度；历史观察重点为2024—2026年。

### 详细逻辑

以下均为假设的100美元交易，忽略利息、手续费、跨日差异及其他同步交易。居民用存款缴税，开户银行扣减其存款100，并在最终结算时减少准备金100；联储将负债由银行准备金转为TGA。银行资产和存款负债同时缩小。财政部向私人供应商付款，则联储扣减TGA100、增加收款银行准备金100，收款银行增加供应商存款100。它增加了银行结算资产，也让收款人拥有银行存款；不是财政部把某笔“闲置准备金”借给居民。[S-R-TGA-RESERVES-01](#S-R-TGA-RESERVES-01)

一级发行也有差别。银行用自身资金购买新债时，准备金减少、国债增加，客户存款未必变化；非银行用既有存款认购时，结算银行同时减少准备金和客户存款。两者都可抬高TGA，但对银行总资产和存款的影响不同。财政部随后花出募集款，准备金又可回到银行体系。因此，一次交割日的下降不是永久损失。

付款对象同样重要。若财政部偿还联储持有并不再续作的到期国债，TGA与联储证券资产同时下降，该步骤没有向商业银行支付，因而不会按上述支出算例增加准备金。不能对所有TGA下降使用同一个结论。

准备金数量减少是否推高资金利率，则取决于银行原有结算缓冲。若银行仍愿意按接近管理利率的价格出借资金，数量下降可不产生明显价格压力；若日内支付、内部缓冲和监管需求已使银行不愿继续降低余额，银行就会更积极借入或减少资金供给。同样的税款规模，在两种起点下会有不同利率结果。[S-R-TGA-RESERVES-02](#S-R-TGA-RESERVES-02)

### 该逻辑的时间线

**2024-09-25至2025-03-26：资产收缩期间准备金仍上升。** 2025年5月公布的联储报告表1显示，单位为十亿美元：总资产从7,080降至6,740，TGA从779降至316，准备金从3,142升至3,451。TGA减少463、准备金增加309并不相等，因为同期逆回购、纸币和其他项目也在变化。这是后来报告中的两个时点比较，不是把每笔财政支出识别出来的流量研究。[S-R-TGA-RESERVES-03](#S-R-TGA-RESERVES-03)

**2026-03-26：税期影响已经进入交易台操作考虑。** SOMA经理Roberto Perli称，交易台当时以每月400亿美元进行准备金管理购买，以提前平滑预计4月税款流入TGA造成的准备金下降。这显示财政现金流预测可以影响资产端安排；“TGA上升就必然出现同额准备金下降”在有对冲操作时不成立。此处保存当时安排与理由，没有把4月结果提前写成已实现事实。[S-R-TGA-RESERVES-04](#S-R-TGA-RESERVES-04)

### 该逻辑的预期

**专业判断，截至2026-03-26，期限为4月税期及其后。** Perli认为，若不提前行动，预计的税款流入很可能使准备金低于充裕区间；4月之后TGA随支付下降，其他条件不变将重新增加准备金，因此购买速度可能很快调整。他没有在所读讲话中给出4月准备金最低余额的确定预测。[S-R-TGA-RESERVES-04](#S-R-TGA-RESERVES-04)

**本库条件推演，2026-10-28按该历史信息集整理。** 未来数周的税款净流入若超过央行净购买与其他负债释放，准备金会下降；若资产端提前补充足够，税期可以表现为数量波动而不出现明显资金紧张。更新判断应同时核对实际入账、购买结算和利率，而不是仅以税收新闻判断。4月逐日DTS、H.4.1同口径数据和操作结算表尚未提取，故本页不判定上述预期最终准确程度。

<a id="logic-2"></a>
## 核心逻辑2：ON RRP与资产端调整决定TGA冲击由谁吸收

**关联节点／节点组**：[财政部一般账户TGA C-MONEY-13](../10_concepts/C-MONEY-13_treasury_general_account.md)、[隔夜逆回购ONRRP C-MONEY-14](../10_concepts/C-MONEY-14.md)、[银行准备金 C-MONEY-RESERVES](../10_concepts/C-MONEY-RESERVES.md)、[央行资产负债表 C-MONEY-CBBS](../10_concepts/C-MONEY-CBBS_central_bank_balance_sheet.md)。

**时间段**：适用于ON RRP可用、财政与联储账户并存的时期；本次覆盖2025年研究与2026年初回顾。

### 详细逻辑

货币基金若不续作100美元ON RRP，联储偿还时可先向其结算银行增加准备金，银行给基金记入存款。基金随后用这笔款认购新发国库券，准备金又转入TGA。两步合并，ON RRP负债减100、TGA增100，准备金净变化可为零。基金并不直接持有银行准备金；银行是结算中介，不能省略这一步后说基金“直接把准备金交给财政部”。这是按账户关系构造的假设算例。

缓冲能否出现，需要基金确实愿意转换资产。新发短券必须在可投资期限、收益和流动性上具有吸引力；余额存在不等于全部可即时动用，最终买方与资金提供者也未必相同。若基金继续保留ON RRP，而其他买家从银行存款出资，TGA增加仍会减少准备金。不能把全市场ON RRP下降全部归因于财政发行。

用同一时点和美元单位对账，令A为联储总资产、R为准备金、T为TGA、P为国内ON RRP、C为纸币、O为其他负债与资本净额，则：

\[
\Delta R=\Delta A-\Delta T-\Delta P-\Delta C-\Delta O.
\]

O必须包含外国官方逆回购及其他账户，不能将全部逆回购都记成ON RRP。假设T增加100、P减少60、A减少20，其余不变，则R减少60，而非100；如果央行另增加60资产，R又可不变。公式是会计约束，行为解释来自基金配置、财政现金安排和央行决策。[S-R-TGA-RESERVES-01](#S-R-TGA-RESERVES-01)、[S-R-TGA-RESERVES-02](#S-R-TGA-RESERVES-02)

### 该逻辑的时间线

**2025-08-06的研究视角。** Annette Vissing-Jorgensen将TGA波动的吸收方式分为准备金、ON RRP、证券和央行贷款调整。她认为，ON RRP缓冲趋小且准备金余裕减弱时，资产端应对的需要可能增加；其以短券资产配合TGA波动的方案属于研究者建议，不能写成已实施规则。[S-R-TGA-RESERVES-02](#S-R-TGA-RESERVES-02)

**较晚观察：2026-03-26回顾2025年。** Perli说明，2025年上半年TGA消耗提高了准备金与ON RRP之和，7月债务上限调整后现金重建使方向反转；ON RRP到10月已很小，私人回购缺少这部分易转移资金，利率需要更明显上升以吸引额外出借。这个回顾支持缓冲条件发生变化，不意味着TGA独自造成全年所有利率变化。[S-R-TGA-RESERVES-04](#S-R-TGA-RESERVES-04)

### 该逻辑的预期

**研究者判断，截至2025-08-06。** Vissing-Jorgensen预计，在ON RRP较小且准备金不再那么富余的条件下，联储更可能需要主动调整资产来应对TGA波动；没有给出下一次回补对准备金或回购利率的固定弹性。[S-R-TGA-RESERVES-02](#S-R-TGA-RESERVES-02)

**本库条件推演，以2026-03-26为信息边界，考察下一轮现金回补。** ON RRP已经较小时，不能继续照搬早期“现金回补主要由ON RRP吸收”的判断。应比较资产净增加、TGA净增加及其他负债变化，并观察银行支付和融资压力。若ON RRP重新累积，缓冲可恢复；若央行资产增长充分，准备金也可保持稳定。来源未提供每笔财政融资的最终资金来源，本页没有以总量余额估算某次发行的ON RRP出资比例。

## 来源与覆盖说明

<a id="S-R-TGA-RESERVES-01"></a>
**S-R-TGA-RESERVES-01**｜美联储，*Federal Reserve liabilities*，页面更新2021-11-15。[原文](https://www.federalreserve.gov/monetarypolicy/bst_frliabilities.htm)。实读存款机构账户、逆回购、财政部存款段落；未采用页面中的机构数量作最新统计。本文分录为注明假设的教学推导。

<a id="S-R-TGA-RESERVES-02"></a>
**S-R-TGA-RESERVES-02**｜Annette Vissing-Jorgensen，*Fluctuations in the Treasury General Account and their effect on the Fed’s balance sheet*，FEDS Notes，2025-08-06。[原文](https://www.federalreserve.gov/econres/notes/feds-notes/fluctuations-in-the-treasury-general-account-and-their-effect-on-the-feds-balance-sheet-20250806.html)。实读a—c节；使用四种调整及作者判断，未将提案当作政策，未复算图1。

<a id="S-R-TGA-RESERVES-03"></a>
**S-R-TGA-RESERVES-03**｜美联储，*Federal Reserve Balance Sheet Developments, May 2025*。[原文PDF](https://www.federalreserve.gov/publications/files/balance_sheet_developments_report_202505.pdf)。实读表1及总表变化段落；发布日期仅核到月份，表内单位为十亿美元，未重建逐日时序。

<a id="S-R-TGA-RESERVES-04"></a>
**S-R-TGA-RESERVES-04**｜Roberto Perli，*Reflections on the Early Days of Reserve Management Purchases and the Maintenance of Ample Reserves*，2026-03-26。[原文](https://www.newyorkfed.org/newsevents/speeches/2026/per260326)。实读Transition、Desk’s Approach及Outlook正文；演示图底层数据未下载。2025年回顾与2026年税期预期分开保存；截至制作日仍未补核4月结果。
