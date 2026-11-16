# 每个subagent的启动要求

先读取下列全部说明文件并查看当前repo，再开展任务；继承会话上下文不能代替读取当前文件。长文件分段读取，不将工具截断输出记为读完。可通过rg按标题定位，逐段完整读说明正文及涉及目录取舍的内容。目录与历史明细用于理解现有选择，遇到候选再对照相关成品正文。

本轮最高优先规则见[执行流程](PIPELINE_REVIEW.md)，候选每unit两份，先筛再写；两批均读Step0思想。无用或复审失败的直接弃掉，无阅读地图、缺口清单或弃稿归档。模型默认排除，例外须主agent拉三个完整上下文subagent讨论。不得自行拉起子agent。

本轮仅T1、T2；I/D/R暂不扩展。输出只写指定工作区路径，正式repo/source原件不改、不上传、不commit/push。所有引用准确区分PDF页序与印刷页，作者解释、教学设定与经验事实分别表述。复核关键图、公式时查看原页。无需为正文无须的模型安排推导或截图。

## 所有现行说明文件

- [README.md](../../README.md)
- [graph/README.md](../../graph/README.md)
- [graph/00_start/AUTHORING_STANDARD.md](../../graph/00_start/AUTHORING_STANDARD.md)
- [graph/00_start/BATCH_TASK.md](../../graph/00_start/BATCH_TASK.md)
- [graph/00_start/CONCEPT_CONTEXT_TERMS.md](../../graph/00_start/CONCEPT_CONTEXT_TERMS.md)
- [graph/00_start/CONCEPT_IMPORT_LIST.md](../../graph/00_start/CONCEPT_IMPORT_LIST.md)
- [graph/00_start/CONCEPT_SELECTION_HISTORY.md](../../graph/00_start/CONCEPT_SELECTION_HISTORY.md)
- [graph/00_start/CONVERSATION_MEMORY.md](../../graph/00_start/CONVERSATION_MEMORY.md)
- [graph/00_start/EVENT_SOURCE_GUIDE.md](../../graph/00_start/EVENT_SOURCE_GUIDE.md)
- [graph/00_start/FILE_NAMING.md](../../graph/00_start/FILE_NAMING.md)
- [graph/00_start/MECHANISM_ARCHIVE.md](../../graph/00_start/MECHANISM_ARCHIVE.md)
- [graph/00_start/MECHANISM_IMPORT_LIST.md](../../graph/00_start/MECHANISM_IMPORT_LIST.md)
- [graph/00_start/MECHANISM_SELECTION_HISTORY.md](../../graph/00_start/MECHANISM_SELECTION_HISTORY.md)
- [graph/00_start/NODE_SELECTION_GUIDE.md](../../graph/00_start/NODE_SELECTION_GUIDE.md)
- [graph/00_start/PROJECT_PLAN.md](../../graph/00_start/PROJECT_PLAN.md)
- [graph/00_start/README.md](../../graph/00_start/README.md)
- [graph/00_start/REVIEW_CHECKLIST.md](../../graph/00_start/REVIEW_CHECKLIST.md)
- [graph/00_start/templates/CONCEPT_TEMPLATE.md](../../graph/00_start/templates/CONCEPT_TEMPLATE.md)
- [graph/00_start/templates/EVENT_TEMPLATE.md](../../graph/00_start/templates/EVENT_TEMPLATE.md)
- [graph/00_start/templates/MECHANISM_TEMPLATE.md](../../graph/00_start/templates/MECHANISM_TEMPLATE.md)
- [graph/00_start/templates/SOURCE_NOTE_TEMPLATE.md](../../graph/00_start/templates/SOURCE_NOTE_TEMPLATE.md)
- [graph/30_events/README.md](../../graph/30_events/README.md)
- [graph/40_sources/README.md](../../graph/40_sources/README.md)
- [graph/40_sources/ACQUISITION_SHORTLIST.md](../../graph/40_sources/ACQUISITION_SHORTLIST.md)
- [graph/40_sources/新LIST.md](../../graph/40_sources/%E6%96%B0LIST.md)
- [materials/textbooks/README.md](../../materials/textbooks/README.md)

另读当前工作区README、PIPELINE_REVIEW、UNIT_PLAN（生成后）、前轮skill与references三份手册；前轮试点流程与最新用户要求冲突时按本轮规则。

## 启动后简报

用一两句消息确认已读哪些说明、看到的repo状态及实际型号/档位可否核验。若无法核验型号和thinking，如实写“完整fork继承父会话，实际配置未核验”；不要把用户请求冒记为实际设置。不要往另一个agent的目录写入，也不改主agent进度log。
