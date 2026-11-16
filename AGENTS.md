# 工作约定

- 本目录是唯一工作仓库；项目版本由Git管理，不复制整份目录创建新版本。
- 修改知识内容前读`graph/00_start/README.md`和`PROJECT_PLAN.md`；新闻制作另读`materials/wallstreetcn/维护/ARTICLE_AUTHORING_CHARTER.md`。
- 来源原文在`materials/`维护，制作稿在`workspaces/`；按用户任务决定何时接入`graph/`。
- 评测快照与正式图谱分别维护。材料移动后更新链接及登记，不改变原始出处和证据日期。
- 修改图谱或目录后运行`python tests/check_graph.py`，文件迁移后另运行`python tests/check_layout.py`；详细目录职责见`docs/FILE_LAYOUT.md`。
