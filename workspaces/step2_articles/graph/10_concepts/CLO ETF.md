---
id: C-WS-3763441-CLOETF
type: concept
title: CLO ETF
status: step2_draft
draft_author: /root/scale_21
model: inherited_unverified
reasoning_effort: inherited_unverified
workspace_reviewed_by: /root
workspace_reviewed_on: 2026-11-16
updated: '2026-11-16'
revision_author: /root/scale_21
revision_on: '2026-11-16'
evidence_as_of: '2026-11-16'
source_ids:
- S-WS-3763441
parent_ids:
- C-WS-3749421-BONDETF
parent_relation: instrument_subtype
historical_observation_as_of: '2026-01-16'
---

# CLO ETF

## 概念定义与继承

CLO ETF在本页指主要持有担保贷款凭证（Collateralized Loan Obligations，CLO）债务档证券的交易所交易基金。本页作为[债券ETF](债券ETF.md)的工具细类，继承债权组合估值、份额交易和一级申赎的解释；集中维护CLO分层、浮息及其进入基金后的风险。本文例子主要是美国AAA债务档产品，不把母页中国指数型产品的规则套为所有CLO ETF条款。

## 贷款池、分层债务与基金份额

企业借款形成贷款池，CLO发行载体把该池现金流按合同分成不同优先级的债务和权益。借款人支付本息，经费用、覆盖测试与现金分配规则，再支付各档持有人；较低档先吸收损失，可能为优先档提供保护。基础分层原理见[证券化与资产支持证券](证券化与资产支持证券.md)。

AAA通常描述特定债务档的信用评级，底层企业贷款可以低于投资级。评级对应受保护的支付顺序及分析假设，不能将贷款池、AAA债务档、其他债务档和权益档当成同一信用风险。ETF又持有一组相关证券，投资者买的是基金份额；其净值随持仓估值及费用变化，二级成交价还受份额供求影响。[发行人定义及产品样本](../40_sources/S-WS-3763441.md#clo)支持这几层区别。

## 浮息降低哪一种敏感度

常见CLO债务档以参考利率加合同利差付息，重置使基准利率变化较快进入票息，因而相对长期固定利率债，利率久期通常较低。降息也可能降低未来票息收入；信用利差扩大、底层损失或交易流动性变差，仍会使价格承压。利率久期低不等于信用利差敏感度、最终到期或全部风险为零。

当借款人偿债改善、优先保护充足且利差收入能够覆盖费用和价格波动时，这类基金可提供一种信用收益敞口。若避险推动长国债收益率大降，长债可能取得较大资本利得，CLO ETF也未必跑赢。比较须统一持有期、票息再投资、费用和币种。ETF交易便利本身不会保证底层每笔证券都能即时按净值变现；[申赎套利](../20_mechanisms/ETF申赎套利.md)还受篮子和执行成本约束。

<a id="outlook-202601"></a>
## 2026年1月：低违约与替代长债的判断

美银当时预期降息和经济韧性支持借款人偿付，认为AAA档CLO ETF可能优于长期美债。这一比较同时涉及信用改善、浮息收入下降和长债资本利得；结果须用同一持有期的产品总回报检验。[机构报价、贷款违约图与流量差异](../30_events/markets/十项反共识情景与旧预测复盘：美银2026年1月展望.md#credit)及[2026年检验安排](../30_events/markets/十项反共识情景与旧预测复盘：美银2026年1月展望.md#checks)在事件维护。

[来源及补核范围](../40_sources/S-WS-3763441.md#clo)记录2026-11-16后补的发行人定义与风险说明，用于本页基础解释。
