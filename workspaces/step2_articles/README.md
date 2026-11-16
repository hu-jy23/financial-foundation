# Step2待整合工作图

`graph/`由原三篇与Scaling新增27篇共用。当前全量成品及审阅返修见[30篇报告](../wallstreetcn_scaling/报告.html)，目录及节点数以工作图索引为准。

以下统计和检查记录描述原三篇的制作基准。

报告以“操作 · 类型”标注每份成品；子项显示父项链接。本轮新增5个概念、3个子概念、4个关系、0个子关系、3篇事件分析和3份来源记录。CoreWeave按具体主体子概念归于云服务。

[阅读报告](阅读报告.html)直接展示25份成品正文；[制作说明](制作说明.md)列明每份文件的归属和改动。[主审意见](review.md)记录内容判断与具体缺件。

| 材料 | 新对象 | 新关系 | 新事件／来源 | 更新旧页 |
| --- | ---: | ---: | ---: | ---: |
| AI CDS | 5 | 2 | 1／1 | 4 |
| 韩国股市 | 3 | 2 | 1／1 | 2 |
| 美债基差交易 | 0 | 0 | 1／1 | 1 |
| 合计 | 8 | 4 | 3／3 | 7 |

每篇由一个继承完整上下文的subagent制作，主agent逐篇审阅。原试作55项知识均有去向，映射在[AI](deliveries/ai.json)、[韩国](deliveries/korea.json)、[基差](deliveries/basis.json)的coverage中。

`graph/`是现有工作图的独立副本，正文、目录与JSON索引已在副本中同步。新增节点为proposed_step2，新增正文及旧页编辑保持step2_draft，尚未整合main。正式图的知识范围保持240个节点；本次仅调整目录与引用路径，工作图基线已按新布局更新。

- [工作图入口](graph/00_start/README.md) · [对象目录](graph/00_start/CONCEPT_IMPORT_LIST.md) · [关系目录](graph/00_start/MECHANISM_IMPORT_LIST.md)
- [文件与链接检查](validation.json)：目录迁移后重新检查本地链接及正式图基线。
- [知识覆盖与引用检查](content_checks.json)：55项覆盖完整，节点引用及报告链接通过。
- [浏览器检查](browser_check.json)：原三篇成品的图像、展开收起及手机布局检查。

来源正文和图片统一引用仓库内materials材料库。旧兼容符号链接已移除，路径按当前目录结构维护。

新制作任务读取仓库[现行节点原则](../../graph/00_start/NODE_SELECTION_GUIDE.md)及[制作标准](../../graph/00_start/AUTHORING_STANDARD.md)；工作图内的说明副本保留试作时版本。

2026-11-16新规则复审：新增节点0，更新9份正文，采用内容见[增量汇总](rule_review_20261116/汇总.md)。
