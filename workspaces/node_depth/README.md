# 节点纵深研究

2026-11-17；分支`research/node-depth-20261117`。CDS试点已制作、核读，等待用户审阅；其余19项仅准备任务。正式graph保持275节点。

- [审阅报告](报告.html)：研究增量、完整制作稿、后续20项名单。
- [CDS导读](cds_pilot/research.md)：更新CDS、证券化机制，新增危机事件材料集及Source笔记。
- [主agent核读](ROOT_REVIEW.md)：事实、组织与范围检查。
- [15概念＋5机制](selection/SELECTION.md)：CDS计入15个概念；每项链接独立任务。
- [Subagent制作说明](selection/GUIDE.md)：阅读、历史研究、共同事件与交付要求。
- [历史原件](../../materials/historical/node_depth/CDS/README.md)：本地资料及实际阅读登记入口。

`cds_pilot/drafts/`按拟接入graph的位置组织链接，报告已将四份制作稿相互连接；直接打开Markdown时，新事件与Source的未来路径尚未进入正式graph。`delivery.json`保存修改目标与制作稿校验值，`base.json`保留两份原节点基线。

重建报告：`python workspaces/node_depth/build_report.py`。检查结果见[validation.json](validation.json)、[正式graph检查](graph_check.json)与[浏览器检查](browser_check.json)。
