---
id: SOURCES-CONCEPTS-V2
type: source_register
title: 两份概念样例的来源登记
status: reviewed_seed
updated: 2026-10-21
---

# 两份概念样例的来源登记

本目录自包含地支持[实际利率](../10_concepts/实际利率.md)、[期限溢价](../10_concepts/期限溢价.md)及 `30_events/concepts/` 下的对应历史记录。以下 URL 均于 **2026-10-21** 实际打开，并读取所列相关位置；没有完整复现论文或下载模型全历史数据。网页动态显示的最新行情没有写入样例。

对象历史的材料覆盖分别截至 2024-12-18、2025-05-28。方法和制度入口的核实日期不构成新的市场状态记录。下列“材料日期”是材料公开或修订日期；若精确时刻未核实，保持缺项。通用写作规范见[批量制作标准](../00_start/AUTHORING_STANDARD.md)。

## 实际利率：制度、测量与历史

<a id="S-CV2-01"></a>
### S-CV2-01 · TIPS 制度说明

- **来源**：[Treasury Inflation-Protected Securities (TIPS)](https://www.treasurydirect.gov/marketable-securities/tips/)，美国财政部 TreasuryDirect。
- **材料日期**：持续维护的制度页面，正文未提供本次所读内容的单独发布日期；读取日 2026-10-21。
- **已读位置／支持范围**：开头说明、“TIPS at a Glance”“How TIPS protects you against inflation”；本金指数化、调整后本金计息、到期原始本金下限、允许负实际收益率报价。
- **边界／使用位置**：不提供历史某日可交易价格；实际利率概念的 TIPS 边界。买入价与本金下限之区别是依据条款所作的本库解释。

<a id="S-CV2-02"></a>
### S-CV2-02 · TIPS 与实际收益率的模型分解

- **来源**：[Tips from TIPS: Update and Discussions](https://www.federalreserve.gov/econres/notes/feds-notes/tips-from-tips-update-and-discussions-20190521.html)，Don Kim、Cait Walsh、Min Wei，FEDS Notes。
- **材料日期**：2019-05-21；日内公开时刻未取得。
- **已读位置／支持范围**：§1–2，公式 (1)–(4)；实际短率预期、实际期限溢价、通胀风险补偿及 TIPS 流动性成分的区分。
- **边界／使用位置**：模型及作者解释，不是每个成分可直接观测的恒等测量；用于两份概念的名义／实际／流动性边界。

<a id="S-CV2-03"></a>
### S-CV2-03 · DFII10 数据口径

- **来源**：[DFII10](https://fred.stlouisfed.org/series/DFII10)，FRED；原始来源为美联储 H.15。
- **材料日期**：持续更新的数据入口；读取日 2026-10-21。
- **已读位置／支持范围**：序列标题、Units、Frequency、Source/Release；十年恒定期限通胀挂钩国债收益率，百分比、日频。
- **边界／使用位置**：仅核实指标定义，未提取动态页面的 2026 数值或完整历史；用于实际利率观测表。

<a id="S-CV2-04"></a>
### S-CV2-04 · T10YIE 数据口径

- **来源**：[10-Year Breakeven Inflation Rate](https://fred.stlouisfed.org/series/T10YIE)，FRED／圣路易斯联储。
- **材料日期**：持续更新的数据入口；读取日 2026-10-21。
- **已读位置／支持范围**：序列说明、单位与频率；DGS10 与 DFII10 的期限匹配差额。
- **边界／使用位置**：数据页的简化通胀预期描述须与 S-CV2-02 的风险和流动性辨析配合；未提取最新行情。

<a id="S-CV2-05"></a>
### S-CV2-05 · 自然利率测量入口

- **来源**：[Measuring the Natural Rate of Interest](https://www.newyorkfed.org/research/policy/rstar)，纽约联储。
- **材料日期**：持续维护的方法／数据页；读取日 2026-10-21。
- **已读位置／支持范围**：r-star 定义、LW/HLW 方法简介、real-time/current estimates 区分。
- **边界／使用位置**：只用于概念与版本边界，没有读取或采用最新估计；LW/HLW 输出不等于 FOMC 官方预测。

<a id="S-CV2-06"></a>
### S-CV2-06 · 2020-03-15 FOMC 声明

- **来源**：[Federal Reserve issues FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20200315a.htm)，FOMC。
- **材料日期**：2020-03-15 17:00 EDT。
- **已读位置／支持范围**：政策区间、条件性维持指引，以及市场通胀补偿与调查长期预期的分歧。
- **边界／使用位置**：政策制定者指引，不是市场逐期限预测；用于 [E-C-20200315-FOMC](../30_events/concepts/E-C-20200315-FOMC.md)。


已整理内容：[2020年3月15日紧急降息与通胀预期观察](../30_events/concepts/E-C-20200315-FOMC.md)。

<a id="S-CV2-07"></a>
### S-CV2-07 · 2022-09-21 FOMC 声明

- **来源**：[Federal Reserve issues FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20220921a.htm)，FOMC。
- **材料日期**：2022-09-21 14:00 EDT。
- **已读位置／支持范围**：3–3.25% 目标区间、继续加息的预期、缩表安排。
- **边界／使用位置**：没有完整事前市场共识，也未提供实际利率计算所需全部输入；用于 [E-C-20220921-FOMC](../30_events/concepts/E-C-20220921-FOMC.md)。


已整理内容：[2022年9月21日加息及继续收紧的政策指引](../30_events/concepts/E-C-20220921-FOMC.md)。

<a id="S-CV2-08"></a>
### S-CV2-08 · 2024 年 9 月 SEP

- **来源**：[September 18, 2024: FOMC Projections materials](https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20240918.htm)，FOMC 会议参与者。
- **材料日期**：2024-09-18 14:00 EDT。
- **已读位置／支持范围**：开头预测条件说明、表 1 和表下注释；2024／2025 年末政策率中位数 4.4%／3.4%，PCE 通胀中位数 2.3%／2.1%，政策率与通胀的时间口径。
- **边界／使用位置**：参与者各自假设下的预测汇总；不同列中位数不可视为某位参与者的联合预测；用于 [O-C-20240918-REAL-INPUTS](../30_events/concepts/O-C-20240918-REAL-INPUTS.md)。


已整理内容：[2024年9月降息、官员预测及年底对照](../30_events/concepts/O-C-20240918-REAL-INPUTS.md)。

<a id="S-CV2-09"></a>
### S-CV2-09 · 2024 年 9 月 Powell 发布会

- **来源**：[Transcript of Chair Powell’s Press Conference](https://www.federalreserve.gov/mediacenter/files/fomcpresconf20240918.pdf)，Jerome Powell／美联储。
- **材料日期**：发布会发生于 2024-09-18；最终文字稿标注同日，首次上线精确时刻未取得。
- **已读位置／支持范围**：正文第 3–4 页的政策调整与预测条件，第 12 页关于政策仍具限制性的回答。
- **边界／使用位置**：主席对政策与经济的说明；未提供单个实际利率数值。用于 2024-09-18 记录，不用于高频盘中判断。


已整理内容：[2024年9月降息、官员预测及年底对照](../30_events/concepts/O-C-20240918-REAL-INPUTS.md)。

<a id="S-CV2-10"></a>
### S-CV2-10 · 2024 年 12 月后续政策端点

- **来源**：[Federal Reserve issues FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20241218a.htm)，FOMC。
- **材料日期**：2024-12-18 14:00 EST。
- **已读位置／支持范围**：目标区间下调至 4.25–4.50%。
- **边界／使用位置**：只用于 9 月记录的后来政策端点对照；没有把 12 月信息回填到 9 月，也不证明实际利率预测实现。

## 期限溢价：方法与历史


已整理内容：[2024年9月降息、官员预测及年底对照](../30_events/concepts/O-C-20240918-REAL-INPUTS.md)。

<a id="S-CV2-11"></a>
### S-CV2-11 · ACM 历史与数据发布说明

- **来源**：[Treasury Term Premia: 1961–Present](https://libertystreeteconomics.newyorkfed.org/2014/05/treasury-term-premia-1961-present/)，Tobias Adrian、Richard Crump、Benjamin Mills、Emanuel Moench，纽约联储 Liberty Street Economics。
- **材料日期**：2014-05-12。
- **已读位置／支持范围**：五因子模型说明、与调查/KW 比较、历史负溢价、1–10 年日频数据介绍。
- **边界／使用位置**：文章反映当时的方法和发布安排，不能保证当前发布日程；用于期限溢价定义和观测入口。

<a id="S-CV2-12"></a>
### S-CV2-12 · ACM 原论文

- **来源**：[Pricing the Term Structure with Linear Regressions](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr340.pdf)，Tobias Adrian、Richard K. Crump、Emanuel Moench，NY Fed Staff Report 340。
- **材料日期**：2008-08 初稿，2013-04 修订版。
- **已读位置／支持范围**：摘要、收益率与超额回报分解的相关说明、§4.4（PDF 第 40–41 页；正文第 38–39 页）；线性回归估计与月频参数／日频因子的结合。
- **边界／使用位置**：仅阅读相关部分，未复现模型；用于 ACM 方法和收益率溢价／持有期回报边界。

<a id="S-CV2-13"></a>
### S-CV2-13 · KW 方法说明

- **来源**：[Three-Factor Nominal Term Structure Model](https://www.federalreserve.gov/data/three-factor-nominal-term-structure-model.htm)，美联储。
- **材料日期**：持续维护的说明页；本次以 2026-10-21 读取版本记录，未采用最新模型数值。
- **已读位置／支持范围**：模型简介及 Q&A 1–7；凸性、调查信息、参数重新估计、日频估计与通常周更、研究产品属性。
- **边界／使用位置**：模型输出不是直接观测或正式统计发布；数值可被修订。用于期限溢价定义、凸性和观测版本边界。

<a id="S-CV2-14"></a>
### S-CV2-14 · 模型估计稳健性

- **来源**：[Robustness of long-maturity term premium estimates](https://www.federalreserve.gov/econres/notes/feds-notes/robustness-of-long-maturity-term-premium-estimates-20170403.html)，Canlin Li、Andrew Meldrum、Marius Rodriguez，FEDS Notes。
- **材料日期**：2017-04-03。
- **已读位置／支持范围**：引言、调查约束和样本选择讨论；调查可提高识别精度，也可能引入偏差；水平、符号和波动的模型依赖。
- **边界／使用位置**：该文讨论的模型与样本有限，不构成对所有 TP 模型的统一排名；用于期限溢价估计方法。

<a id="S-CV2-15"></a>
### S-CV2-15 · Stein 回顾 2013 年债市

- **来源**：[Yield-Oriented Investors and the Monetary Transmission Mechanism](https://www.federalreserve.gov/newsevents/speech/stein20130926a.htm)，Jeremy C. Stein，美联储理事演讲。
- **材料日期**：2013-09-26；日内公开时刻未取得。
- **已读位置／支持范围**：春夏市场回顾及脚注 6；2013-05-02 十年收益率 1.63%、KW 溢价 −0.78%，6 月 25 日十年名义收益率 2.61%。
- **边界／使用位置**：9 月演讲中的事后历史估计，不是已验证的 5 月实时数据；用于 [O-C-20130926-STEIN](../30_events/concepts/TERM_PREMIUM_HISTORY.md#O-C-20130926-STEIN)。


已整理内容：[期限溢价：历史观察与模型解读](../30_events/concepts/TERM_PREMIUM_HISTORY.md)。

<a id="S-CV2-16"></a>
### S-CV2-16 · 2023 年长债波动的事后分解

- **来源**：[The Treasury Tantrum of 2023](https://www.federalreserve.gov/econres/notes/feds-notes/the-treasury-tantrum-of-2023-20240903.html)，Anthony M. Diercks、Dev Asnani，FEDS Notes。
- **材料日期**：2024-09-03；日内公开时刻未取得。
- **已读位置／支持范围**：引言、模型与调查比较、表 1–2；同一 2023 年窗口的 ACM/KW 分解差异；文中回顾后续回落。
- **边界／使用位置**：作者的事后研究分解，未取得原调查实时版本；本概念仅采用测量比较，不把其归因升级为确定因果。用于 [O-C-20240903-2023TERM](../30_events/concepts/TERM_PREMIUM_HISTORY.md#O-C-20240903-2023TERM)。


已整理内容：[期限溢价：历史观察与模型解读](../30_events/concepts/TERM_PREMIUM_HISTORY.md)。

<a id="S-CV2-17"></a>
### S-CV2-17 · 2025 年 5 月会议纪要

- **来源**：[Minutes of the Federal Open Market Committee, May 6–7, 2025](https://www.federalreserve.gov/monetarypolicy/fomcminutes20250507.htm)，FOMC 纪要中的公开市场操作台与工作人员报告。
- **材料日期**：会议 2025-05-06/07，公开 2025-05-28 14:00 EDT（由 S-CV2-18 核实）。
- **已读位置／支持范围**：“Developments in Financial Markets and Open Market Operations”“Staff Review of the Financial Situation”；政策路径预期、短中期与长期收益率变化、工作人员对 TP 上升的定性判断。
- **边界／使用位置**：未披露 TP 模型与数值，原调查形成／公开时刻未取得；用于 [O-C-20250528-TERM-MINUTES](../30_events/concepts/TERM_PREMIUM_HISTORY.md#O-C-20250528-TERM-MINUTES)。


已整理内容：[期限溢价：历史观察与模型解读](../30_events/concepts/TERM_PREMIUM_HISTORY.md)。

<a id="S-CV2-18"></a>
### S-CV2-18 · 2025 年 5 月纪要公开时刻

- **来源**：[Minutes of the Federal Open Market Committee, May 6–7, 2025 — release](https://www.federalreserve.gov/newsevents/pressreleases/monetary20250528a.htm)，美联储新闻稿。
- **材料日期**：2025-05-28 14:00 EDT。
- **已读位置／支持范围**：发布时间和正文；纪要描述的是会议时可得信息。
- **边界／使用位置**：仅核实公开时间及信息集边界；用于 2025 纪要记录，不提供 TP 数据。


已整理内容：[期限溢价：历史观察与模型解读](../30_events/concepts/TERM_PREMIUM_HISTORY.md)。

<a id="S-CV2-19"></a>
### S-CV2-19 · 当前 ACM 数据入口

- **来源**：[Treasury Term Premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs)，纽约联储。
- **材料日期**：持续维护的数据入口；读取日 2026-10-21。
- **已读位置／支持范围**：静态页面标题与数据入口已打开。
- **边界／使用位置**：动态数据未加载，不支持任何当日数值、当前更新安排或完整 vintage 档案的断言。日频历史方法说明取自 S-CV2-11/12。

## 2026-10-23 核读补记

v4 沿用本表来源 ID，并纳入 Astra 对照重写时对原文的再次核读。逐来源阅读位置、用途和未取得资料见[核读记录](../50_reviews/ASTRA_RUN_NOTES.md)。本次扩大了正文对既有资料的使用范围；不代表下载了完整模型序列或补齐了所有原始调查。

## 工作稿维护记录

2026-10-23 重组了 Event 与 Source 的入口及组织。上方记载的原始阅读日期和范围保持不变，本次没有重新访问全部外部来源。课程资料已另行登记，原页与已核读公开资料分别保留。
