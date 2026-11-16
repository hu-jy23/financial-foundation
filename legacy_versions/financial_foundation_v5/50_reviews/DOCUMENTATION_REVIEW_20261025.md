# v5说明文件审阅与修订记录

日期：2026-10-25。执行：主agent；本次未分派subagent。范围：00_start全部现行说明和模板、根目录README、Event／Source入口与维护说明、资料搜集方案、审阅和历史任务记录。

## 审阅结论

上次v5已同步163个对象、71个关系及最终名称，当前数字没有过时。本次主要修正仍遗留的材料状态、内容归属和执行口径，并把对话中已确定的取舍转成可直接使用的规范。

| 发现 | 修订 |
|---|---|
| 资料搜集方案仍写“老师PPT待接入”，财政来源仍写课件尚未取得。 | 改为已接入46页课程材料及原件，链接实际内容与阅读范围；其他书籍和博客继续按各自记录说明访问状态。 |
| 搜集方案仍要求Event留简短来源入口、完整论证留材料工作区。 | 按已确认分工修正：Event／对象／关系承载完整入库内容；Source保存出处、阅读笔记和延伸探索。 |
| 平凡性判断和归属取舍主要留在项目记忆，缺少现行制作入口。 | 新增00_start/README及节点选取指南，将解释职责、选取资格、归属、拆分和命名分别讲清。 |
| 任务单把concepts和mechanisms合写为关联节点来源。 | node_ids只选对象；相关关系另用related_mechanism_ids；普通变量保留在解释中。 |
| “无需第二份参与名单”与索引已有逻辑组容易冲突。 | 正文形成具体逻辑组后同步索引，不另凭初始名单推定机制。 |
| 模板状态和元数据不一致，来源笔记缺少独立文件的元数据示例。 | 四模板明确复制后填写状态；补Source最小元数据；解释目录状态、正文状态与证据日期的区别。 |
| 部分任务示例默认必须另建独立事件。 | 根据完整内容单元选择附入现有文件或独立维护；保留清楚原页，按需解释。 |
| 旧Astra任务未在文件开头醒目标为历史，v4记录还指向当前校验。 | 补历史说明与审阅导航；保留原任务文本和实际核读记录；v4校验改连对应快照。 |

## 本次触及文件

- `00_start/AUTHORING_STANDARD.md`
- `00_start/BATCH_TASK.md`
- `00_start/CONVERSATION_MEMORY.md`
- `00_start/EVENT_SOURCE_GUIDE.md`
- `00_start/NODE_SELECTION_GUIDE.md`
- `00_start/README.md`
- `00_start/REVIEW_CHECKLIST.md`
- `00_start/templates/CONCEPT_TEMPLATE.md`
- `00_start/templates/EVENT_TEMPLATE.md`
- `00_start/templates/MECHANISM_TEMPLATE.md`
- `00_start/templates/SOURCE_NOTE_TEMPLATE.md`
- `30_events/README.md`
- `40_sources/ACQUISITION_SHORTLIST.md`
- `40_sources/README.md`
- `40_sources/SOURCES_FISCAL.md`
- `50_reviews/ASTRA_RUN_NOTES.md`
- `50_reviews/ASTRA_RUN_TASK.md`
- `50_reviews/COMPARISON.md`
- `50_reviews/EVENT_SOURCE_WORKING_REVIEW.md`
- `50_reviews/README.md`
- `50_reviews/V5_CHANGES.md`
- `50_reviews/history/VALIDATION_V4_20261023.json`
- `README.md`

## 检查后保留

- 两份正式目录、两份勾叉清单、旧ID登记、目录索引及命名决定：数量、ID、名称、顺序、勾叉和归属保持原结果。
- 四份样例与Event正文、课程PDF及页图：内容未改。本次维护不代表重写正文或刷新资料覆盖。
- 概念与黄金的来源登记、课程来源页：现有日期、原件状态及组织说明符合当前决定，保留；财政来源只修正维护段落中的材料状态。
- 历史运行记录、已读范围和具体资料缺口保留原日期；付费章节、数据快照及外部事实未因本次编辑而变成已取得或已验证。

## 结果范围

版本仍为v5，初步建图节点保持234个；当前4份样例、230份待制作。完成本次说明维护后，后续工作可按现行入口开始制作；目录扩充或改名另作明确变更。

校验结果见[说明修订校验](DOCUMENTATION_VALIDATION_20261025.json)和[当前结构校验](VALIDATION.json)。本次未开展新一轮外部事实研究。
