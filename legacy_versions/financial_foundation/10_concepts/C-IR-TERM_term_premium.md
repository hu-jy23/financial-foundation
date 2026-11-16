---
id: C-IR-TERM
type: concept
subtype: latent_asset_pricing_component
title: 期限溢价
aliases: [Term premium, Treasury term premium]
status: reviewed_seed
author_role: subagent_concept
created: 2026-10-20
knowledge_as_of: 2026-10-20
market_snapshot_as_of: null
source_ids: [S-AGENT-C-01, S-AGENT-C-02, S-AGENT-C-03, S-AGENT-C-04, S-AGENT-C-05, S-AGENT-C-06]
related_ids: [C-IR-NOMINAL, C-IR-REAL, R-FISCAL-LONGYIELD]
---

# 期限溢价 / Term premium

## 定义与范围

[定义] 期限溢价是长期债券收益率中，相对于未来短期利率预期路径的额外定价成分。其经济含义是承担期限相关风险所获得的补偿；在不同定价约定中，还可能包含凸性调整。

本页讨论美元名义国债。公司债还包含信用、违约及流动性等成分；不同国家国债也存在制度和信用差异。将它们的收益率减去某个短端预测，所得差额未必全是期限溢价。

期限溢价无法直接交易或直接观测。新闻里的“期限溢价上涨”应附模型名称、期限和数据版本。研究模型的输出不能自动代表所有交易者的共识。[S-AGENT-C-01、03]

## 概念详解：同一次长端上行，可以有不同来源

在连续复利、相同时间单位下，一种常见的定义为：

\[
TP^{path}_{t,n}=y^{(n)}_t-\frac{1}{n}\sum_{j=0}^{n-1}E_t^P[r_{t+j}].
\]

这里，\(y^{(n)}_t\) 是 n 期零息国债收益率，\(r\) 是每期短端利率，\(E^P\) 表示真实概率下的条件预期。实际使用时，要注明各输入的年化、复利和取样方式。若采用模型拟合收益率，观测收益率与拟合值之间还存在拟合误差。

**假设算例。** 十年收益率为 4.5%，模型给出的未来十年平均短端利率为 3.7%，则按上述约定，期限溢价为 0.8 个百分点，即 80 bp。随后十年收益率升至 4.8%：若预期路径升至 4.0%，溢价仍为 80 bp；若预期路径不变，溢价升至 110 bp。仅看长债报价无法分辨两种情况。

### 收益率溢价与持有期超额回报

上述 TP 是收益率的组成部分。持有一段时间后的超额回报，还取决于期间曲线怎样变化、债券剩余期限、票息、融资成本与滚动收益。TP 为正不保证下一月赚钱；TP 为负也不排除短期价格上涨。

[条件性理论] 当长债在投资者更需要财富的坏状态中表现较差时，投资者可能要求较高补偿；若长债具有危机对冲价值，持有人可能接受较低预期回报。久期供给、投资者负债匹配需求和风险承受能力也会影响定价。期限越长，并不意味着溢价必然更高或永远为正。[S-AGENT-C-01、05]

## 易混淆概念

| 对象 | 与期限溢价的区别 | 读新闻时应检查 |
|---|---|---|
| 十年减两年利差 | 同时含两段预期路径和溢价差 | 陡峭化来自哪个期限、哪类成分 |
| 加息概率或预期政策路径 | 描述未来短端利率的判断 | 风险调整、调查主体及期限 |
| 信用利差 | 包括违约风险和其他相对定价因素 | 主体信用、担保与流动性 |
| 实际期限溢价 | 针对实际利率风险 | 名义溢价还可能包含通胀风险 |
| 久期 | 债价对收益率变化的敏感度 | 风险暴露与风险补偿分别计量 |
| 利率波动率 | 描述不确定性幅度 | 风险价格和对冲属性也影响补偿 |
| 凸性调整 | 来自债价与收益率的非线性 | 模型是否将其包含在 TP 定义中 |

Fed 的 KW 说明页采用“收益率减平均预期短率”的定义，将凸性调整计入 TP；部分文献另报不含该项的纯期限溢价。跨模型比较数值前，先核对约定。[S-AGENT-C-03]

## 如何估计：模型提供什么

**ACM。** Adrian、Crump、Moench 用多步线性回归估计期限结构模型：从收益率因子动态与债券超额回报中估计风险暴露、风险价格，再生成模型收益率和分解。其五因子实现能产生日频结果；文献中的日频输出仍使用低频估计参数，输出频率与估计频率须区分。[S-AGENT-C-02]

**KW。** Kim–Wright 类模型结合收益率与短端利率调查，为远期预期路径增加外部约束。[S-AGENT-C-03]

**调查差额。** 将期限一致的调查预期路径与长债收益率配对，可得到一种替代估计；调查覆盖、反应速度和受访者代表性仍需判断。

[经验结果] Fed 2017 年比较发现，是否纳入调查信息可以显著改变估计；调查有助于约束长期均值，却也可能带入偏差。模型间某些共同趋势比绝对水平、符号和波动更稳健。[S-AGENT-C-04]

## 指标、单位与可得时间

| 指标/入口 | 使用口径 | 频率与可得性 | 主要风险 |
|---|---|---|---|
| NY Fed ACM 期限溢价 | 指定年限的模型收益率分解；百分比或 bp | 官方历史说明提供日频观测；实际下载时核对当前发布安排 | 更新版本可能重新估计历史；动态页面不等于完整 vintage 档案 |
| Fed KW 模型 | 同时保存预期路径、TP 和拟合收益率 | 官方说明通常按周发布此前日频估计 | 日频观测日期早于公开日期；参数与方法可更新 |
| 调查预期差额 | 同一币种、期限和时点的收益率减调查平均短率 | 由调查发布时间决定 | 十年终点预测不能替代十年平均路径 |
| 曲线斜率、MOVE 等 | 状态或辅助解释变量 | 各自数据发布规则 | 代理变量与 TP 没有固定换算关系 |

数据入口：[NY Fed Treasury Term Premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs)、[Fed KW 数据与方法](https://www.federalreserve.gov/data/three-factor-nominal-term-structure-model.htm)。本批已读方法说明，未下载全历史数据，未核实当日最新值。

Agent 应同时保存 `observation_date`、`published_at`、`retrieved_at`、`model_version`、`estimation_sample_end` 和单位。用今天重估的历史 TP 回测过去决策，会引入未来信息；必须使用当时版本，或仅使用截至当时的数据重新估计。若只能拿到后验序列，应将实验明确标为事后解释。[本库实施规范]

## 涉及关系与角色

| 机制 | 期限溢价的角色 | 需要的额外背景 |
|---|---|---|
| [财政扩张与长期收益率](../20_mechanisms/R-FISCAL-LONGYIELD_fiscal_long_yields.md) | 久期供给和风险补偿渠道 | 发行期限、央行持仓、需求与增长预期 |
| QE/QT 与久期供给 | 政策传导的可能中介 | 购买预期、净供给、投资者约束 |
| 股债对冲属性变化 | 风险补偿变化的结果 | 通胀/增长冲击、风险偏好 |
| 长端融资条件与实体经济 | 影响长期融资成本 | 信用利差、银行信贷、利率锁定期限 |
| [实际利率](C-IR-REAL_real_interest_rate.md)的分解 | 实际长期收益率的一个组成 | 通胀风险与 TIPS 流动性 |

## 历史观察与时间线

### 2013：负期限溢价及其逆转讨论

> 截至时间：2013-09-26 演讲发布｜当时状态：回顾当年春夏长债重定价｜谁对什么、哪个期限有何预期：事前市场分布未核实｜新增证据：Stein 引述 5 月 2 日十年收益率 1.63%，KW 溢价估计 −0.78%｜判断变化：负溢价是可能的模型结果，政策和持仓渠道需共同分析｜后续结果：原演讲已观察到春夏收益率上升；本批未新增价格检验｜来源：S-AGENT-C-05；[完整观察](../30_events/agent_concept/O-20130926-STEIN.md)。

### 2023：相同价格变化对应不同分解

> 截至时间：2024-09-03 研究发布｜当时状态：回顾 2023 年 7–10 月十年收益率上行｜谁对什么、哪个期限有何预期：研究比较模型与调查，但本批未取得当时调查原始版本｜新增证据：该文对同一窗口的 ACM 和 KW 溢价增幅估计分别为 116 bp 与 69 bp｜判断变化：对解释保留模型分歧；区分事件当时可得判断与后来估计｜后续结果：文献讨论随后收益率回落，不能据此将前期上行全部判为可套利偏离｜来源：S-AGENT-C-06；[完整观察](../30_events/agent_concept/O-20240903-2023TERM.md)。

### Latest

截至 2026-10-20：概念、方法和两个历史观察已建立。当前 TP 水平、市场预期与可交易信号尚未填写。当前文档状态属于知识整理。

## Agent 输出与候选信号

看到“长债收益率因财政担忧上涨”，先生成一个归因假说，再检查发行变化、预期短率、不同 TP 模型和相同窗口内的其他消息。模型残差不应直接被赋予“财政信用崩塌”等具体含义。

[待检验假说] 可以先输出三类信号：同一模型 TP 的变化、跨模型方向一致性、预期路径与 TP 对收益率变化的贡献。分解后再预测债券回报或融资条件；贡献率在收益率变化接近零时不稳定，宜保留 bp 绝对变化。

验证时固定期限和生成时刻，将普通曲线变量作为基准，检验 TP 的增量预测信息。跨模型分歧可作为测量不确定性指标，不能直接称为市场分歧。任何策略映射还需处理久期、交易成本与实时数据版本。

## 待补资料

- 可获得的实时 vintage、模型下载版本和发布时间。
- 匹配期限的调查原表，以及受访主体和调查形成日期。
- 中国国债的模型与制度适配，不能直接复用美国参数。
- 用户宏观 PPT 中关于期限结构、资产负债表和风险偏好的原始论证。

## 来源

阅读范围、日期和局限见 [subagent 概念来源表](../40_sources/SOURCES_AGENT_CONCEPT.md)。

- [S-AGENT-C-01 NY Fed：Treasury Term Premia: 1961–Present，2014-05-12](https://libertystreeteconomics.newyorkfed.org/2014/05/treasury-term-premia-1961-present/)
- [S-AGENT-C-02 ACM 原论文工作稿，2013-04 修订](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr340.pdf)
- [S-AGENT-C-03 Fed：Three-Factor Nominal Term Structure Model](https://www.federalreserve.gov/data/three-factor-nominal-term-structure-model.htm)
- [S-AGENT-C-04 Fed：Robustness of Long-Maturity Term Premium Estimates，2017-04-03](https://www.federalreserve.gov/econres/notes/feds-notes/robustness-of-long-maturity-term-premium-estimates-20170403.html)
- [S-AGENT-C-05 Stein：Yield-Oriented Investors and the Monetary Transmission Mechanism，2013-09-26](https://www.federalreserve.gov/newsevents/speech/stein20130926a.htm)
- [S-AGENT-C-06 Fed：The Treasury Tantrum of 2023，2024-09-03](https://www.federalreserve.gov/econres/notes/feds-notes/the-treasury-tantrum-of-2023-20240903.html)
