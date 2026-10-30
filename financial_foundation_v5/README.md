# 金融认知 Map v5

2026-10-29统一Concept／Mechanism标题文件名并接入已审正文；节点范围沿用2026-10-25定稿。Event／Source仅同步正文链接，课程PDF与图文材料保持原样。

**初步build map节点已确定：163个概念／对象、71个关系／机制，共234个节点。** 现有168份经审阅正文（117个Concepts、51个Mechanisms），其余66份尚未完成主审。18个既有观察ID归入8份事件正文，另含1份课程图文材料集。

## 入口

后续制作先读[00_start制作入口](00_start/README.md)，了解现行规范、索引字段和历史记录的区别。当前进度见[阶段提交记录](50_reviews/FULL_BUILD_20261028/REVIEWED_CHECKPOINT_20261028.md)，改名规则见[文件命名](00_start/FILE_NAMING.md)。此前试产见[国债供给批次审阅与分工](50_reviews/FISCAL_CONCEPT_PILOT_20261027/MAIN_REVIEW.md)，前批见[黄金批次记录](50_reviews/CONCEPT_PILOT_20261027/MAIN_REVIEW.md)；此前说明修订见[审阅记录](50_reviews/DOCUMENTATION_REVIEW_20261025.md)。

1. [正式对象目录](00_start/CONCEPT_IMPORT_LIST.md)、[正式关系目录](00_start/MECHANISM_IMPORT_LIST.md)：后续制作以这234个节点为范围。
2. [177项关系勾叉与最终名称](50_reviews/MECHANISM_SELECTION_177.md)、[349项对象去向](50_reviews/CONCEPT_SELECTION_349.md)：保留完整审阅轨迹。
3. [v5定稿记录](50_reviews/V5_CHANGES.md)、[制作标准](00_start/AUTHORING_STANDARD.md)、[批量任务单](00_start/BATCH_TASK.md)和[对话记忆](00_start/CONVERSATION_MEMORY.md)。
4. [事件与分析入口](30_events/README.md)、[课程图文正文](30_events/course/MACRO_20250330.md)、[Event／Source指南](00_start/EVENT_SOURCE_GUIDE.md)。

## 早期12份成品与作者记录

| 类型 | 文档 | 执笔与整合 | 历史资料截止 |
|---|---|---|---|
| 对象 | [实际利率](10_concepts/实际利率.md) | 原 subagent 重写，主 agent 审阅 | 2024-12-18 |
| 对象 | [期限溢价](10_concepts/期限溢价.md) | Astra medium 新稿，主 agent 精简与整合 | 2025-05-28 |
| 关系 | [黄金的机会成本机制](20_mechanisms/黄金的机会成本机制.md) | 主 agent | 2026-07-01 |
| 关系 | [国债供给的定价机制](20_mechanisms/国债供给的定价机制.md) | Astra medium 新稿，主 agent 整合 | 2025-04-30 |
| 对象 | [黄金](10_concepts/黄金.md) | 前批主 agent 执笔与自审 | 2026-07-30；制度说明另记核读日 |
| 对象 | [政策利率与目标区间](10_concepts/政策利率与目标区间.md) | 前批 GPT-6-Astra medium 独立首稿，主 agent 审阅 | 2024-12-18；中国对照为2024年7—8月 |

| 对象 | [财政赤字与初级赤字](10_concepts/财政赤字与初级赤字.md) | fiscal_tga_concepts：Astra medium，主 agent 审阅 | 2025-04-28 |
| 对象 | [财政部一般账户TGA](10_concepts/财政部一般账户TGA.md) | fiscal_tga_concepts：Astra medium，主 agent 审阅 | 2025-08-06 |
| 对象 | [融资流动性](10_concepts/融资流动性.md) | 本轮主 agent 唯一新写条目，自审 | 2025-05-09；动态定义另记核读日 |
| 对象 | [央行资产负债表](10_concepts/央行资产负债表.md) | cbbs_qe_qt_concepts：Astra medium，主 agent 审阅 | 2025年5月；余额至4月30日 |
| 对象 | [量化宽松QE](10_concepts/量化宽松QE.md) | cbbs_qe_qt_concepts：Astra medium，主 agent 审阅 | 2022-03-16 |
| 对象 | [量化紧缩QT](10_concepts/量化紧缩QT.md) | cbbs_qe_qt_concepts：Astra medium，主 agent 审阅 | 2025-04-28 |

《国债供给》继续完整采用新稿；《期限溢价》保持已整合版本。名称与引用已随节点定稿同步；本轮保留此前六篇的经济正文及资料覆盖，只将新完成对象的导航指向正文。黄金机制的三个、国债供给机制的八个关联对象现均有正文；各篇历史截止分别保留，不自动延长至制作日。

## 内容与文件

- `00_start/`：正式目录、索引、制作标准、任务单、四种模板和项目记忆。正文术语登记仅供旧ID追溯，不是隐式对象目录。
- `10_concepts/`、`20_mechanisms/`：正文使用定稿标题作为文件名；已审正文及进度从两份正式目录进入。
- `30_events/`：事件、分析和课程图文；原页可直接阅读。
- `40_sources/`：来源记录、原PDF、文本转录和[资料搜集方案](40_sources/ACQUISITION_SHORTLIST.md)。
- `assets/`：课程46张原页图及校验清单。
- `50_reviews/`：定稿记录、原349项对象与177项关系的完整审阅、旧ID迁移和历史记录。

课程原件：[2025年3月30日宏观课程 PDF](40_sources/originals/macro_course_20250330.pdf)。P20–29 作为连续论述保留，P23–26、P27–28 在其内分节；P31 单列到伊核协议。无需联网即可查看随包原页。

## 制作与维护

按[批量任务单](00_start/BATCH_TASK.md)安排具体工作，并依[审阅清单](00_start/REVIEW_CHECKLIST.md)检查。按本版163项对象和71项关系安排节点制作；普通变量直接进入解释，退出项留作追溯。索引中selection_status表示选取结果，pending／complete表示正文状态。

来源实际阅读范围、历史信息截止和具体缺口随正文保存。课程原文观点保留其归属，未宣称全部独立核验。本次改名校验见[迁移校验](50_reviews/FILENAME_MIGRATION_VALIDATION_20261029.json)；[历史材料校验](50_reviews/VALIDATION.json)保留当时结果。
