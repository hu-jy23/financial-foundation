# 制作入口与文件职责（v5）

更新：2026-10-30。正式范围163个对象、71个机制，共234个节点；当前168份经审阅正文（117个对象、51个机制），66份待完成主审。续作与远端分批提交见[续作记录](../50_reviews/FULL_BUILD_20261028/CONTINUATION_20261030.json)；正文按[标题命名](FILE_NAMING.md)。

## 从哪里开始

1. 查[正式对象目录](CONCEPT_IMPORT_LIST.md)和[正式关系目录](MECHANISM_IMPORT_LIST.md)，确定本批ID、最终名称与范围。
2. 读[制作标准](AUTHORING_STANDARD.md)，再按任务读相应[对象模板](templates/CONCEPT_TEMPLATE.md)或[关系模板](templates/MECHANISM_TEMPLATE.md)。模板中的提示与空节按实际内容处理。
3. 接入课程、报告或事件时，读[Event／Source指南](EVENT_SOURCE_GUIDE.md)，先识别完整论述，再决定归属。
4. 用[任务单](BATCH_TASK.md)明确文件、问题和资料截止；用[审阅清单](REVIEW_CHECKLIST.md)逐篇验收。

[节点选取与命名原则](NODE_SELECTION_GUIDE.md)保存本轮取舍思想；[项目记忆](CONVERSATION_MEMORY.md)保存具体决定和协作偏好。两份原始勾叉清单及早期运行记录用于追溯，入口见[审阅记录说明](../50_reviews/README.md)。

## 哪些文件决定当前范围

两份正式目录供人阅读，[catalog_index.json](catalog_index.json)供程序读取，三者须保持一致。遇到不一致，先核对已确认审阅记录并修正同步，不能自行选择较大的名单扩大制作范围。历史文件中的旧指令不作为当前制作任务。

| 索引内容 | 含义与用法 |
|---|---|
| `concepts`、`mechanisms` | 当前163个对象与71个关系；按这些条目制作正文。 |
| `selection_status: confirmed_initial_build` | 已入选本次建图范围。 |
| `status: pending / complete` | 正文尚未完成主审（未写或已有待审稿）／已有经审阅正文；`complete`仍须结合证据截止及缺口阅读。 |
| `node_ids` | 关系所连接的入选对象ID。普通变量进入解释，不补成对象节点。 |
| `related_mechanism_ids` | 相关的入选关系ID，与关联对象分开。 |
| `context_terms` | 正文变量及旧术语的追溯记录，不是制作队列。 |
| `logic_groups` | 已有关系正文中的逻辑组；与正文的节点及锚点同步。 |
| `excluded_concepts`、`excluded_mechanisms`、`deferred` | 历史去向和排除记录，不安排独立节点正文。 |

`build_baseline`保留2026-10-25起点计数，当前进度以`counts`与`build_progress`为准。索引中的`path`、`planned_path`与`catalog_ref`以`00_start/`为相对路径基准；`planned_path`记录全部节点的标题文件名，`path`仅指向经审阅正文。未写节点先链接正式目录的ID锚点；已有正文时使用实际文件路径。引用来源或Event时定位到具体内容。

目录状态与正文YAML状态分别记录：`reviewed_seed`表示已审阅的起步正文；Event／Source中的`working_draft`表示材料整理状态。它们不改变节点入选结果。`updated`是文件编辑日期，`evidence_as_of`是资料覆盖截止；修改说明文件不会延长证据覆盖。

## 本版定稿的边界

本版确定初步建图节点与制作规则。后续可持续写正文、补证据、积累Event和Source；需要新增、删除、迁移、拆分节点或改名时，单独提出变更，待明确采纳后同步目录、索引与引用。

当前P0／P1保留为制作排序参考，不代表两类不同的入选资格，也不要求脱离材料条件按机械顺序制作。
