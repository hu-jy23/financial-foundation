# 制作入口与文件职责（v5）

Step0原型为163个对象、71个机制。T1、T2本轮接入后，现行目录为165个对象、75个机制，共240个节点；[来源与采用范围](../40_sources/STEP1_T1_T2.md)记录本轮边界。后续材料可以继续改写内容与结构。正文按[标题命名](FILE_NAMING.md)。

## 从哪里开始

先读[整体规划与研究思想](PROJECT_PLAN.md)，理解原型的暂定性、alignment目的及各阶段职责。

1. 查[正式对象目录](CONCEPT_IMPORT_LIST.md)和[正式关系目录](MECHANISM_IMPORT_LIST.md)，确定本批ID、最终名称与范围。
2. 读[制作标准](AUTHORING_STANDARD.md)，再按任务读相应[对象模板](templates/CONCEPT_TEMPLATE.md)或[关系模板](templates/MECHANISM_TEMPLATE.md)。模板中的提示与空节按实际内容处理。
3. 接入课程、报告或事件时，读[Event／Source指南](EVENT_SOURCE_GUIDE.md)，先识别完整论述，再决定归属。
4. 用[任务单](BATCH_TASK.md)明确文件、问题和资料截止；用[审阅清单](REVIEW_CHECKLIST.md)逐篇验收。

[节点选取与命名原则](NODE_SELECTION_GUIDE.md)解释节点取舍原则；[项目约定](CONVERSATION_MEMORY.md)保存具体决定和协作偏好。目录形成过程与逐项结果见[对象形成记录](CONCEPT_SELECTION_HISTORY.md)、[机制形成记录](MECHANISM_SELECTION_HISTORY.md)。

## 哪些文件决定当前范围

两份正式目录供人阅读，[catalog_index.json](catalog_index.json)供程序读取，三者须保持一致。遇到不一致，核对正式范围与正文并同步修正，材料阅读可提出范围与结构修改，按[整体规划](PROJECT_PLAN.md)明确依据并同步实施。

| 索引内容 | 含义与用法 |
|---|---|
| `concepts`、`mechanisms` | 现行对象与机制；具体数量及条目以索引为准。 |
| `selection_status: confirmed_initial_build / confirmed_step1` | 已入选本次建图范围。 |
| `status: pending / complete` | 正文尚未完成主审（未写或已有待审稿）／已有经审阅正文；`complete`仍须结合证据截止及缺口阅读。 |
| `node_ids` | 关系所连接的入选对象ID。普通变量进入解释，不补成对象节点。 |
| `related_mechanism_ids` | 相关的入选关系ID，与关联对象分开。 |
| `context_terms` | 正文变量及旧术语的追溯记录，不是制作队列。 |
| `logic_groups` | 已有关系正文中的逻辑组；与正文的节点及锚点同步。 |
| `excluded_concepts`、`excluded_mechanisms`、`deferred` | 历史去向和排除记录，不安排独立节点正文。 |

索引中的`counts`记录当前条目数量。索引中的`path`、`planned_path`与`catalog_ref`以`00_start/`为相对路径基准；`planned_path`记录全部节点的标题文件名，`path`仅指向经审阅正文。未写节点先链接正式目录的ID锚点；已有正文时使用实际文件路径。引用来源或Event时定位到具体内容。

目录状态与正文YAML状态分别记录：`reviewed_seed`表示已审阅的起步正文；`step1_reviewed`表示Step1本轮新增与接入已审，保留旧稿的来源复核范围另见正文。Event／Source中的`working_draft`表示材料整理状态。它们不改变节点入选结果。`updated`是文件编辑日期，`evidence_as_of`是资料覆盖截止；修改说明文件不会延长证据覆盖。

## 原型目录与后续修改

本版记录Step0原型的节点选择与制作规则。教材阅读可以改变其内容与结构。后续可持续写正文、补证据、积累Event和Source；需要新增、删除、迁移、拆分节点或改名时，单独提出变更，待明确采纳后同步目录、索引与引用。

当前P0／P1保留为制作排序参考，不代表两类不同的入选资格，也不要求脱离材料条件按机械顺序制作。
