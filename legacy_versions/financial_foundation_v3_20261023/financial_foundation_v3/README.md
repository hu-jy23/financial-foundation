# 金融认知 Map 基础包 v3

完整版本：2026-10-23。已整合此前全部修订，解压后从本页开始使用。

包含 **349个概念／对象候选、175个关系／机制候选、四份完整样例、18份事件／观察记录**，以及制作标准、任务单、四种模板、来源登记和25组资料搜集候选。概念已完成2份、待制作347份；关系已完成2份、待制作173份。

## 从这里开始

1. 阅读[批量制作标准](00_start/AUTHORING_STANDARD.md)。
2. 查看下表四份样例，按[概念清单](00_start/CONCEPT_IMPORT_LIST.md)与[关系清单](00_start/MECHANISM_IMPORT_LIST.md)选择制作对象。
3. 用[批量任务单](00_start/BATCH_TASK.md)分派工作；结合[资料搜集与阅读方案](40_sources/ACQUISITION_SHORTLIST.md)搜集、精读资料。

## 四份完整样例

| 类型 | 文档 | 正文执笔归属 | 审阅／修订 | 已覆盖历史资料截止 |
|---|---|---|---|---|
| 概念 | [实际利率](10_concepts/C-IR-REAL_real_interest_rate.md) | subagent `/root/concepts_v2` 重写 | 主agent | 2024-12-18 |
| 概念 | [期限溢价](10_concepts/C-IR-TERM_term_premium.md) | subagent `/root/concepts_v2` | 主agent | 2025-05-28 |
| 关系 | [黄金的机会成本机制](20_mechanisms/R-GOLD-REALRATES_real_rates_gold.md) | 主agent `/root` | 主agent，已纳入10月23日修订 | 2026-07-01 |
| 关系 | [国债供给的定价机制](20_mechanisms/R-FISCAL-LONGYIELD_fiscal_long_yields.md) | subagent `/root/fiscal_edge_v2` | 主agent | 2025-04-30 |

署名保留实际执笔历史，v3整合由主agent完成。关系页以每组节点的一条完整逻辑为单位，连续保存逻辑、历史和预期；时间线可用连贯段落充分解释具体情况。重要数字依据对象或逻辑本身选择，保留含义、口径和来源；缺失说明已查范围与原因。定性条件推演保留并标明归属。

## 包内目录

- `00_start/`：两份候选清单、制作标准、任务单、四种模板和[catalog_index.json](00_start/catalog_index.json)。
- `10_concepts/`：实际利率、期限溢价。
- `20_mechanisms/`：黄金的机会成本机制、国债供给的定价机制。
- `30_events/`：18份独立事件／观察，按概念、黄金、国债供给分组。
- `40_sources/`：来源登记、阅读工作区说明及资料搜集方案。
- `50_reviews/`：[审阅记录](50_reviews/COMPARISON.md)与[本版校验结果](50_reviews/VALIDATION.json)。

## 后续维护

候选清单中的ID保持稳定；制作完成后更新状态、路径与关系入口。尚未制作的节点链接到候选清单锚点。JSON中的`logic_groups`记录两份关系样例的节点与锚点，完整含义由正文论证表达。`schema_version`保留数据结构版本，`package_version`标记本次完整包版本。

文件采用相对Markdown链接，可作为笔记目录继续编辑。模板中的占位内容供制作时替换。

## 材料覆盖

老师的宏观PPT仍待接入；教材、研究与深度文章由研究agent主动搜集。候选资料中的未读部分已有标注。各篇`evidence_as_of`表示实际覆盖的历史信息范围，完整包日期不代表市场信息已更新至该日。

黄金样例已补充原报告中的重要数字和央行储备预期调查。图内数据、原始调查截面等仍未取得的项目，在对应记录中说明原因。外部观点、模型结果和本库条件推演保留各自归属。
