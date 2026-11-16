# 金融认知 Map v5

完整整合包，2026-10-24。包含本轮限定的目录调整，以及此前尚未一并交付的 Event／Source、课程图文和说明文件更新。

**163 个概念／对象、177 个关系／机制候选，四份完整样例；18 个既有观察 ID 归入 8 份事件正文，另含 1 份课程图文材料集。** 对象与关系正文各完成2份。关系目录其余旧候选保留待审；其中24项需要重新整理关联节点。

## 建议审阅顺序

1. [v5 调整记录](50_reviews/V5_CHANGES.md)：只采纳用户限定的回补、五项归属调整与三组拆分。
2. [正式对象目录](00_start/CONCEPT_IMPORT_LIST.md)、[关系候选目录](00_start/MECHANISM_IMPORT_LIST.md)；需要逐项核对时看[原349项去向](50_reviews/CONCEPT_SELECTION_349.md)。
3. [事件与分析入口](30_events/README.md)、[课程图文正文](30_events/course/MACRO_20250330.md)。
4. [Event／Source 组织指南](00_start/EVENT_SOURCE_GUIDE.md)、[制作标准](00_start/AUTHORING_STANDARD.md)与[对话记忆](00_start/CONVERSATION_MEMORY.md)。

## 四份完整样例

| 类型 | 文档 | 执笔与整合 | 历史资料截止 |
|---|---|---|---|
| 对象 | [实际利率](10_concepts/C-IR-REAL_real_interest_rate.md) | 原 subagent 重写，主 agent 审阅 | 2024-12-18 |
| 对象 | [期限溢价](10_concepts/C-IR-TERM_term_premium.md) | Astra medium 新稿，主 agent 精简与整合 | 2025-05-28 |
| 关系 | [黄金的机会成本机制](20_mechanisms/R-GOLD-REALRATES_real_rates_gold.md) | 主 agent | 2026-07-01 |
| 关系 | [国债供给的定价机制](20_mechanisms/R-FISCAL-LONGYIELD_fiscal_long_yields.md) | Astra medium 新稿，主 agent 整合 | 2025-04-30 |

《国债供给》继续完整采用新稿；《期限溢价》保持已整合版本。本轮只调整引用和节点角色，经济论证与数字保留。

## 内容与文件

- `00_start/`：正式目录、索引、制作标准、任务单、四种模板和项目记忆。正文术语登记仅供旧ID追溯，不是隐式对象目录。
- `10_concepts/`、`20_mechanisms/`：四份完整样例。
- `30_events/`：事件、分析和课程图文；原页可直接阅读。
- `40_sources/`：来源记录、原PDF、文本转录和[资料搜集方案](40_sources/ACQUISITION_SHORTLIST.md)。
- `assets/`：课程46张原页图及校验清单。
- `50_reviews/`：本轮调整、原349项完整去向、旧ID迁移和历史记录。

课程原件：[2025年3月30日宏观课程 PDF](40_sources/originals/macro_course_20250330.pdf)。P20–29 作为连续论述保留，P23–26、P27–28 在其内分节；P31 单列到伊核协议。无需联网即可查看随包原页。

## 制作与维护

按[批量任务单](00_start/BATCH_TASK.md)安排具体工作，并依[审阅清单](00_start/REVIEW_CHECKLIST.md)检查。只从本版正式对象目录选择节点；普通变量直接进入解释，未入选条目不因旧ID存在而自动恢复。

来源实际阅读范围、历史信息截止和具体缺口随正文保存。课程原文观点保留其归属，未宣称全部独立核验。结构与材料完整性校验见[VALIDATION.json](50_reviews/VALIDATION.json)。
