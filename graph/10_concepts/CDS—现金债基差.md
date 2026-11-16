---
id: C-S2-CDS-CASH-BASIS
type: concept
title: CDS—现金债基差
status: step2_reviewed
workspace_reviewed_by: /root
workspace_reviewed_on: 2026-11-16
updated: '2026-11-16'
evidence_as_of: '2026-10-31'
draft_author: /root/produce_ai
model: inherited_unverified
reasoning_effort: inherited_unverified
source_ids:
- S-WS-3784900
parent_ids:
- C-DERIV-15
parent_relation: instrument_specific_basis
editor: /root/revise_ai
editing_status: step2_reviewed
revision_author: /root/revise_ai
revision_status: reviewed
editor_model: inherited_unverified
editor_reasoning_effort: inherited_unverified
formal_integrated_on: 2026-11-16
formal_integration_batch: wallstreetcn_30_20261116
---

# CDS—现金债基差

> 执笔：`/root/produce_ai`；2026-11-13制作，工作区待审稿。

## 概念定义

CDS—现金债基差比较同一信用参考对象在衍生品保护市场与现金债券市场的定价。本页采用CDS保护利差减匹配现金债信用利差的方向，单位为基点。正基差表示保护报价高于匹配现金债的信用利差，负基差表示相反状态。

本页是[基差](基差.md)的信用工具细分类，继承“相关价格比较须先明确方向、单位、期限及可比性”的原则；美债现券—期货的交割因子、净基差和到期安排不直接适用于这一比较。

## 如何形成可比读数

比较需要匹配实体、币种、债务顺位、期限和合同覆盖，并说明现金债使用哪种基准和利差指标。[信用利差](信用利差.md)介绍收益率差、Z-spread及OAS的区别；不能将不同口径下的两个数字视作完全对称的信用补偿。若CDS以upfront报价，还须先按合同输入转换成可比利差。

信用风险恶化可能让两种利差一起上升；只有两侧变化幅度不同，基差才随之改变。不同投资者群体、保护供给、债券流动性、融资和借券条件可以改变相对价格。因而正基差同时提供两个信息：两市场的报价存在差额，以及用理论复制关系消除差额可能需要成本和风险。其交易过程见[定价与交易机制](../20_mechanisms/CDS—现金债基差的定价与交易.md)。

## 本对象的历史

2026年10月报道显示AI组合基差由负转正，非AI组合仍负，同期名称之间又有差别。这使本对象承担一个具体观察任务：企业保护与现金债是否共同重估，还是保护相对变贵？[完整事件](../30_events/AI融资扩张中的CDS价格分化：2026年10月.md#basis)展开比较，[来源图3、7读数](../40_sources/S-WS-3784900.md#basis-readings)保留数据。匹配规则及组合权重尚未取得，不能由差额独立分配保护需求和基本面的贡献。

## 关系与来源

[CDS—现金债基差的定价与交易](../20_mechanisms/CDS—现金债基差的定价与交易.md)解释保护需求、价差交易两腿及融资约束；[AI相关企业CDS](AI相关企业CDS.md)维护本次标的群。

定义、正负基差两腿及中介约束另核读[纽约联储作者的2018年研究说明](../40_sources/S-WS-3784900.md#nyfed-basis)。本次AI观察来自[文章与图3、7](../40_sources/S-WS-3784900.md#article)，未取得同日底层匹配债券数据。
