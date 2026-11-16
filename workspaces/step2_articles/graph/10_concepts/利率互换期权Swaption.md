---
id: C-WS-3783332-SWAPTION
type: concept
title: 利率互换期权Swaption
status: step2_draft
draft_author: /root/scale_11
model: inherited_unverified
reasoning_effort: inherited_unverified
workspace_reviewed_by: /root
workspace_reviewed_on: 2026-11-16
updated: '2026-11-16'
source_ids:
- S-WS-3783332
evidence_as_of: '2026-11-16'
---

# 利率互换期权Swaption

## 概念定义

利率互换期权（swaption）让买方支付权利金，取得在约定日期或日期范围、按既定条件进入利率互换或获得相应现金结算的权利。底层互换交换固定与浮动利息；期权额外给予买方选择是否执行的权利。固定利率、浮动基准、名义本金、行权方式、期权到期日、互换起止与结算规则共同决定合同。[ICE定义](https://idd.ice.com/IRHelp/Content/FM/Swaption.htm)。

## 两种权利与两个期限

Payer买方有权支付约定固定利率、收取浮动利率；到期可交易的同规格互换固定利率高于执行利率时，锁定较低的付息条件具有价值。Receiver买方有权收固定、付浮动，方向相反。行权后须履行互换的后续支付义务；现金结算按合约计算价值，名义本金不等于买方当初支付的权利金。[TW SEF合约规则901(d)](https://www.cftc.gov/filings/orgrules/rules0705243158.pdf)给出一种具体交易场所的约定。

市场简写“1y×1y”通常依次指一年期期权和行权后一年期互换；“20y×20y”对应二十年期权与二十年互换。期权到期前，它的市值已经随远期互换利率、利率隐含波动及时间变化。两段期限都长的头寸，不是只对下一次央行会议敏感的工具。浮动基准为隔夜复利时，可接[隔夜指数掉期OIS](隔夜指数掉期OIS.md)的利息结构；OIS与其上的期权仍是不同合同。

<a id="volatility-position"></a>
## 方向判断与波动头寸

同期限、同本金、同执行利率同时买入payer和receiver，是跨式组合straddle。它为两个方向的较大变动提供选择权，成本是两份权利金；宽跨式strangle使用不同执行利率，触发区间和成本相应改变。[ICE跨式说明](https://idd.ice.com/IRHelp/Content/FM/Swaption_Straddle_Strate.htm)。到期若互换利率没有充分偏离执行利率，赔付可能不足覆盖权利金。

在到期前，Delta描述对利率方向的局部敏感度，Gamma描述该敏感度怎样变化，Vega描述价格对所用隐含波动报价的敏感度，Theta描述时间经过的影响。持有多头Vega可以从隐波上升取得估值收益，仍同时面对时间损耗、利率曲线和对冲变化。利率市场可用正态基点波动报价，与价格期权的对数正态百分比波动有不同单位；跨来源比较Vega须先对齐报价尺度。[CME的利率波动报价说明](https://www.cmegroup.com/articles/2026/introduction-to-eris-options-for-swaptions-users.html)。

<a id="history-202610"></a>
## 2026年10月：用长利率波动对冲柴油与政策路径不确定性

野村Charlie McElligott的10月分析提出持有美元/欧元利率Vega：柴油短缺若使通胀与终端利率路径难以判断，长波动可以提供另一种风险暴露。报道图14使用美元20y×20y **straddle** 的恒定Vega滚动回测，而正文称“宽跨式”。回测显示2003—2026年美国CPI同比最高五分组的平均月度超额收益超过1%，Vega贡献最大。

图注没有交代百分比收益所用资金分母、完整滚动和对冲算法、交易成本，本轮没有独立复现。该数不能解释为投入权利金的固定月回报；它也没有验证原文所称的宽跨式。对冲股票损失还需要利率隐波在股票受损情景中上升，且收益足以抵销成本及基差；股市下跌本身不触发swaption赔付。[事件策略与图14](../30_events/markets/美股集中、波动供给与柴油风险：野村2026年10月跨资产分析.md#scenarios)保存当时三个分支。

## 来源与范围

[S-WS-3783332](../40_sources/S-WS-3783332.md#swaption)登记ICE工具说明、TW SEF 2024规则与CME报价说明的实读范围。定义于2026-11-16补核，具体行情与观点仅覆盖2026-10-10转载；没有该策略成交确认书、完整研究回测或后续对冲结果。
