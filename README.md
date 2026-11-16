# 金融认知 Map

本目录是唯一工作仓库。所有开发、资料维护和Git操作都在这里进行。

| 目录 | 职责 | 入口 |
| --- | --- | --- |
| `graph/` | 现行正式图谱，240个节点 | [制作入口](graph/00_start/README.md) |
| `materials/` | 教材、机构材料及华尔街见闻本地库 | [材料目录](materials/README.md) |
| `workspaces/` | 独立制作与流程试验，尚未接入的成品 | [工作区目录](workspaces/README.md) |
| `tests/` | 评测题目、答案、评分和固定图谱快照 | [评测入口](tests/README.md) |
| `reports/` | 对外报告及编译源文件 | [报告入口](reports/README.md) |
| `docs/` | 文件管理约定及阶段进度 | [目录约定](docs/FILE_LAYOUT.md) |

本轮整理与scaling测试使用分支`step2/wallstreetcn-scaling-20261116`。[三篇成品报告](workspaces/step2_articles/阅读报告.html)包含8个新对象、4个新关系及旧页更新，仍在独立工作区，未接入`graph/`。

使用Git保存版本，不再复制整份项目生成v6、v7等工作目录。需要同时打开不同分支时使用`git worktree`。
