---
id: C-COMMOD-03
type: concept
title: 原油与Brent/WTI
status: reviewed_seed
draft_author: "/root/full_b021"
model: gpt-6-astra
reasoning_effort: medium
reviewed_by: /root
updated: 2026-10-28
evidence_as_of: 2026-10-06
source_ids: [S-C-COMMOD-03-01, S-C-COMMOD-03-02, S-C-COMMOD-03-03, S-C-COMMOD-03-04, S-C-COMMOD-03-05, S-C-COMMOD-03-06, S-C-COMMOD-03-07, S-C-COMMOD-03-08]
---

# 原油与Brent/WTI

> 执笔：`/root/full_b021`；制作日2026-10-28。市场资料截止2026-10-06，EIA该期预测输入截止10月1日；交易所制度页于制作日核读，不表示取得当日行情。

## 概念定义

原油是经过地面分离后仍以液态存在的天然烃类混合物，是炼制汽油、柴油、航空燃料及石化原料的投入品。不同油田、品质、交货地点和交付时间的原油不是完全可互换的商品。“油价”通常指某一基准，实际货物则以基准加减升贴水交易。Brent与WTI是最常用的两组基准名称，分别连接海运原油与美国原油的现货、远期和期货市场，但二者都具有全球市场联系。[S-C-COMMOD-03-01](#S-C-COMMOD-03-01)、[S-C-COMMOD-03-02](#S-C-COMMOD-03-02)

Brent已不是单指一个北海油田；WTI也不能不加区分地指代库欣交割原油、Midland产区油或美国湾岸出口货物。读价格之前，应先明确具体评估或合约。

## 概念详解

### 品质决定炼厂能生产什么，地点决定油能否运到

原油品质常从密度和硫含量认识。API度越高一般越轻；轻油含有较多较轻烃组分，简单蒸馏更容易产出汽柴油等产品。重油通常需要额外加工装置，含硫量较高还增加脱硫及产品质量处理要求。品质影响加工成本和产品收率，却不是价格唯一来源：装有复杂炼化设备的炼厂可能利用重质高硫油折价获得收益，具体价值取决于产品价格与装置能力。[S-C-COMMOD-03-01](#S-C-COMMOD-03-01)

运输使同品质油也会有不同价格。内陆原油需要管道运到消费地或出口港；海运货物需支付运费、保险和港口成本。若管道满负荷，内陆供应无法立即向高价地区流动，产地折价可以扩大；若海运保险上涨，跨区套利所需价差又会上升。品质、地点和时间共同决定一个升贴水，不能把Brent高于WTI全部归因于“Brent品质更好”。

一个**假设**净回值算例：欧洲同等品质到岸买价82美元／桶，美国湾岸装船与运费合计5美元／桶，内陆至湾岸管输2美元／桶，则忽略融资、损耗和容量约束的内陆最高采购价约为75美元／桶。若管输能力不足，账面有利可图也不能立刻完成套利。这是物流条件下的算例，不是实时Brent—WTI价差估计。

### Brent和WTI各包含哪些对象

| 对象 | 实际含义及结算联系 |
|---|---|
| Dated Brent | 对规定装运／交付窗口实货的价格评估；2023年加入WTI Midland，形成包含北海五种油和Midland的篮子 |
| Brent远期／cash市场 | 按交付月份交易的实货远期体系；这里的cash并不意味着立即交货 |
| ICE Brent期货 | 每手1,000桶；交易所定义为基于期转现EFP交割、可选择按ICE Brent Index现金结算的合约 |
| NYMEX WTI期货（CL） | 每手1,000桶，最终实物交割连接俄克拉何马州库欣的指定管道／储存设施 |
| WTI Midland | 具有自身来源、质量规范和定价地点的油流；进入Brent篮子的是按规定运到欧洲、经过调整的货物，不能直接拿库欣期货价替代 |

表中制度依据：[S-C-COMMOD-03-02](#S-C-COMMOD-03-02)、[S-C-COMMOD-03-03](#S-C-COMMOD-03-03)、[S-C-COMMOD-03-04](#S-C-COMMOD-03-04)、[S-C-COMMOD-03-05](#S-C-COMMOD-03-05)。

ICE Brent Index是期货最终现金结算的依据，不等同于Dated Brent评估。现金结算仍通过指数与实货市场相连，不能理解成脱离原油供需的纯金融价格。EFP是交换期货与实货头寸的安排，也不意味着每个普通期货持有人必须自己安排船运。

期限同样重要。现行ICE Brent在合约月份之前第二个月的最后营业日结束交易，例如3月合约通常在1月底到期；WTI在交割前一月的25日之前第三个营业日到期，遇非营业日按规则前移。两个屏幕上的“近月”因此未必覆盖相同日历月份和剩余期限。比较价差时，要对齐月份、时间戳及结算方式。[S-C-COMMOD-03-02](#S-C-COMMOD-03-02)、[S-C-COMMOD-03-03](#S-C-COMMOD-03-03)

### 基准价差与期货曲线回答不同问题

Brent减WTI比较两组原油基准的相对价格，受品质、区域供需和运输条件影响；同一基准近月减远月比较不同时间的交付价值，受库存、储存成本、融资及即时用油价值影响。两种价差可能同时变化，但不可互换。

当近月高于远月，通常称backwardation，说明近端交付相对昂贵；远月高于近月则称contango。持有原油库存可以保证炼厂不停工，这种即时可用性具有价值；库存稀缺时价值可能较高。库存充裕却缺乏空余储罐时，接收新增油又会带来很高边际成本。总库存“高”与下一桶油“容易储存”并非同一问题。

期货投资回报也不是现货价格变化的复制。长期保持敞口需要换到后续月份，投资者会受到所持合约沿曲线变化、展期时间、抵押现金收益和费用的共同影响。某天近月负价不代表所有未来月份都负价，更不意味着全球所有油生产商都按该价格出售。

## 观测与数据口径

一条可解释的油价应记录：基准全名、现货或具体期货月份、美元／桶、日期和时区、收盘或结算价。原油桶是体积单位，每桶42美制加仑；吨是质量单位，吨桶换算依赖密度。供需中的“百万桶／日”是流量，“百万桶库存”是存量，二者只有指定天数后才能转换。

EIA的“petroleum and other liquids”比原油更宽，通常包含天然气液体、生物燃料等；不能拿广义液体消费与狭义原油产量相减并称为原油缺口。库存也要区分库欣、全美商业库存和战略储备；库欣当地储存压力无法只看全美总量判断。

交易所库存和库容通常仍不提供“某投资者当天能租到多少空间”。已租但尚未装满的储罐，在物理统计上有空位，却未必向其他人开放。合约到期前的价格同时反映接货能力和退出头寸的成交条件。[S-C-COMMOD-03-06](#S-C-COMMOD-03-06)

## 本对象的历史与预期

### 2020年负WTI：特定合约与交割约束

2020-04-20，次日到期的5月WTI期货首次出现负价。EIA于4月27日回顾，约美东14:30盘中一度低至**−40.32美元／桶**；这是盘中价，不是最终结算价。截至4月17日，库欣库存约**6,000万桶**，其中约200万桶在途，罐区约5,800万桶，相对约7,600万桶工作库容为**76%**。未装满不等于剩余空间全部可租，很多空间已经承诺给他人。没有储存安排的多头为了避免接货，可能支付代价退出。[S-C-COMMOD-03-06](#S-C-COMMOD-03-06)

同一EIA文章记录，4月21日6月Brent合约仍收于**19.33美元／桶**，较远期WTI及其他多种原油也仍为正价。该例说明需求骤降是共同背景，而到期时间、市场流动性和当地接货条件决定了极端价格表现。EIA当时还预期未来数周库欣储存约束可能继续造成6月WTI及其他美国油价波动；本页未用后来结果将这段风险提示改写为精确价格预测。

### 2023—2024年：美国原油进入Brent的定价基础

Platts从**2023-05-02**开始在Dated Brent评估中纳入6月运抵鹿特丹的合格WTI Midland货物，经运费净回值调整后与北海离岸口径比较；6月货物的篮子标准船货规模由60万桶增至**70万桶**。这扩充了北海产量下降背景下的可用实货基础，也使美国出口物流与Brent评估联系更紧密。[S-C-COMMOD-03-04](#S-C-COMMOD-03-04)

ICE研究负责人Mike Wittner在**2024年10月**的回顾称，2023年5月至2024年7月，Midland约在**50%—60%**的时间成为Dated Brent定价中最有竞争力的油种。这是交易所作者的历史统计与判断，不是所有全球原油交易有50%—60%改用WTI期货。Brent是海运篮子、WTI库欣是特定交割地合约的差别仍然存在。[S-C-COMMOD-03-02](#S-C-COMMOD-03-02)

### 2025年与2026年：先保存各自信息集

EIA **2026-01-05**回顾2025年时，将价格下降联系到供应超过需求：Brent月均价由2025年1月约**79美元／桶**降至12月约**63美元／桶**，全年约**69美元／桶**。该文引用2025年12月展望估计，下半年广义液体隐含库存增量超过**250万桶／日**。这些是当时对2025年的回顾及模型估计，不是精确清点全球每个储罐所得。[S-C-COMMOD-03-07](#S-C-COMMOD-03-07)

较晚的**2026-10-06 STEO**采用截至10月1日的信息，描述中东运输受限及绕行、运输保险成本上升的状态。EIA预计2026年第四季度Brent现货均价约**105美元／桶**，较上月预测提高14美元；条件是当季中东原油流动仍受限、停产平均约450万桶／日。它又预计替代出口路线和产量恢复逐步缓解紧张，2027年Brent全年均价约**84美元／桶**。这些是机构条件预测，不是10月28日实时价格，也不是期货市场隐含概率。[S-C-COMMOD-03-08](#S-C-COMMOD-03-08)

这两个材料分别保存供给过剩与运输约束状态下的判断。不能把较晚发生的运输中断放入2025年当时的信息集，也不能仅因预测均价较高，就认定未来每个交易日都会维持该水平。

**本库条件推演，2026-10-28整理。** 若全球供给恢复但出口瓶颈仍在，油价总水平和Brent—WTI价差可能走出不同路径：可出口地区增产会压低其本地价格，而受阻地区到岸成本仍高。若运输、保险和储存条件同时恢复，跨地区套利会更有效地约束价差。检验时应联合观察对应月份价格、管道与港口吞吐、运费和可用库存，而不是用一个“地缘溢价”解释所有变化。

## 涉及的关系

- [原油供给冲击的宏观传导 R-OIL-SHOCK](../20_mechanisms/原油供给冲击的宏观传导.md)：原油的可达供应、库存缓冲及炼厂加工连接生产中断与成品油、通胀和需求调整；冲击不能只用名义产能衡量。
- [库存与便利收益、期货曲线 R-COMMODITY-03](../20_mechanisms/库存与便利收益、期货曲线.md)：本对象提供可储存、地点受限且存在交割期限的具体商品，库存可用性使现货和跨期价差具有经济联系。

## 来源与待补问题

<a id="S-C-COMMOD-03-01"></a>**S-C-COMMOD-03-01** — EIA，*Refining crude oil—inputs and outputs*，页面更新2024-06-20。[原文](https://www.eia.gov/energyexplained/oil-and-petroleum-products/refining-crude-oil-inputs-and-outputs.php)。实际读Not all crude oil is the same及Refineries use more than just crude oil，核轻重、硫及加工边界；未分析全部产品收率表。

<a id="S-C-COMMOD-03-02"></a>**S-C-COMMOD-03-02** — Mike Wittner／ICE，*What are the differences between ICE Brent and NYMEX WTI Futures?*，2024年10月。[原文](https://www.ice.com/insights/energy/what-are-the-differences-between-ice-brent-and-nymex-wti-futures)。实际读Brent、EFP、Midland加入、Cushing及到期交割段；未复算波动率和展期收益图。交易所比较有产品立场，本页不沿用其“Brent无区域约束”的绝对化表述，也不采用文内库容单位笔误。

<a id="S-C-COMMOD-03-03"></a>**S-C-COMMOD-03-03** — ICE，*Brent Crude Futures*产品219，动态制度页，2026-10-28核读。[原文](https://www.ice.com/products/219/Brent-Crude-Futures)。读规模、到期、Delivery/Settlement Terms；未逐项核所有清算细则和历史规则版本。

<a id="S-C-COMMOD-03-04"></a>**S-C-COMMOD-03-04** — Platts／S&P Global，*Platts reflects WTI Midland cargoes in Dated Brent from May 2*，2023-05-02 09:21 UTC。[原文](https://www.spglobal.com/energy/en/pricing-benchmarks/our-methodology/subscriber-notes/050223-platts-reflects-wti-midland-cargoes-in-dated-brent-from-may-2)。读生效时间、鹿特丹净回值及船货规模；未重建每笔MOC评估或全部质量调整公式。

<a id="S-C-COMMOD-03-05"></a>**S-C-COMMOD-03-05** — CME Group，*WTI Crude Oil Futures*，动态产品页，2026-10-28核读。[原文](https://www.cmegroup.com/markets/energy/wti-crude-oil-futures.html)。读CL与微型／迷你合约规模及What is WTI；未使用页面示例保证金作为固定要求。库欣交割另由EIA及ICE正文交叉支持。

<a id="S-C-COMMOD-03-06"></a>**S-C-COMMOD-03-06** — Jesse Barnett、Jeff Barron／EIA，*Low liquidity and limited available storage pushed WTI crude oil futures prices below zero*，2020-04-27。[原文](https://www.eia.gov/todayinenergy/detail.php?id=43495)。实际读全文分析，核盘中价格、库存／库容、已承诺空间和当时预期；未下载盘中逐笔数据或核最终结算。

<a id="S-C-COMMOD-03-07"></a>**S-C-COMMOD-03-07** — Alex de Keyserling、Jimmy Troderman／EIA，*Crude oil prices fell in 2025 amid oversupply*，2026-01-05。[原文](https://www.eia.gov/TodayinEnergy/detail.php?id=66944)。读正文全年价格、供需与库存段，未复算图表底层数据；引用的是当时回顾版本。

<a id="S-C-COMMOD-03-08"></a>**S-C-COMMOD-03-08** — EIA，*Short-Term Energy Outlook, October 2026*，2026-10-06发布。[原始PDF](https://www.eia.gov/outlooks/steo/archives/Oct26.pdf)。实际读印刷页2—6的Overview、Forecast timeline及Global Oil Markets；核输入截止10月1日、第四季度和2027年预测，未通读后部天然气／电力章节或复现模型。

具体缺口：未取得制作日逐合约行情、完整库欣可出租库容及运输合同，不能计算当日无套利价差。EIA动态年度数据页跳转后正文表格未显示，本页未用搜索摘要数字拼接年均序列；2025采用1月5日回顾，2026采用明确版本预测。2020最终结算与逐笔交易未核，因此只报告已核的盘中最低观察。
