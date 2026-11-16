# Subagent 概念文档：来源登记

作者角色：subagent_concept。检索与阅读日期：2026-10-20。六项核心来源均已打开并读取相关内容；未声称阅读全文所有附录，未下载并回测数据。

| ID | 材料 | 作者/机构与日期 | 已读位置；支持的命题 | 局限与使用位置 |
|---|---|---|---|---|
| S-AGENT-C-01 | [Treasury Term Premia: 1961–Present](https://libertystreeteconomics.newyorkfed.org/2014/05/treasury-term-premia-1961-present/) | Adrian、Crump、Mills、Moench；NY Fed；2014-05-12 | 正文定义、历史估计与数据说明；含负溢价观察 | 历史数据发布说明，不保证当前日程；用于概念与指标入口 |
| S-AGENT-C-02 | [Pricing the Term Structure with Linear Regressions](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr340.pdf) | Adrian、Crump、Moench；Staff Report 340，2008-08，2013-04 修订 | 摘要、引言、§2.4 风险调整、§4.4 日频实现 | 阅读部分原文；没有复现或独立验证论文结果；用于 ACM 方法 |
| S-AGENT-C-03 | [Three-Factor Nominal Term Structure Model](https://www.federalreserve.gov/data/three-factor-nominal-term-structure-model.htm) | Fed；页面标注更新 2019-11-05 | Q&A：定义、凸性、模型修订与发布 | 模型输出与发布安排可变化；用于测量边界及时间戳设计 |
| S-AGENT-C-04 | [Robustness of Long-Maturity Term Premium Estimates](https://www.federalreserve.gov/econres/notes/feds-notes/robustness-of-long-maturity-term-premium-estimates-20170403.html) | Canlin Li、Andrew Meldrum、Marius Rodriguez；2017-04-03 | 引言与模型差异；调查约束、样本与不确定性 | 调查本身可能偏；用于多模型比较 |
| S-AGENT-C-05 | [Yield-Oriented Investors and the Monetary Transmission Mechanism](https://www.federalreserve.gov/newsevents/speech/stein20130926a.htm) | Jeremy C. Stein；2013-09-26 | 春夏债市回顾、需求渠道和脚注 6 | 政策官员的研究解释，非统一 FOMC 结论；用于 O-20130926-STEIN |
| S-AGENT-C-06 | [The Treasury Tantrum of 2023](https://www.federalreserve.gov/econres/notes/feds-notes/the-treasury-tantrum-of-2023-20240903.html) | Anthony M. Diercks、Dev Asnani；2024-09-03 | 摘要、模型比较、表 2 与预期讨论 | 事后研究估计；用于 O-20240903-2023TERM |

另打开 [NY Fed 当前 Treasury Term Premia 页面](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs)，只读到静态入口，动态数据未加载，故没有据此填写最新数值或发布频率。本文有关历史日频数据说明来自 S-AGENT-C-01/02。

## 来源使用规则

来源正文的事实、来源作者的解释和本库推断分别标注。引用历史政策演讲中的估计时，同时保存演讲发布日期和被描述的市场日期；不把二者合并。后续添加实时数据需保留下载版本和模型估计样本截止，避免覆盖本次来源状态。
