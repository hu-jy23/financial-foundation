# 金融认知 Map

本目录是唯一工作仓库。所有开发、资料维护和Git操作都在这里进行。

| 目录 | 职责 | 入口 |
| --- | --- | --- |
| `graph/` | 现行正式图谱，275个节点 | [制作入口](graph/00_start/README.md) |
| `materials/` | 教材、机构材料及华尔街见闻本地库 | [材料目录](materials/README.md) |
| `workspaces/` | 独立制作与流程试验，尚未接入的成品 | [工作区目录](workspaces/README.md) |
| `tests/` | 评测题目、答案、评分和固定图谱快照 | [评测入口](tests/README.md) |
| `reports/` | 对外报告及编译源文件 | [报告入口](reports/README.md) |
| `docs/` | 文件管理约定及阶段进度 | [目录约定](docs/FILE_LAYOUT.md) |

Step2首批30篇已接入正式`graph/`：194个对象、81个机制。新增35节点，更新45个原有节点，接入30篇事件与30份来源记录。[采用范围](graph/40_sources/STEP2_WALLSTREET_30.md)。

使用Git保存版本，不再复制整份项目生成v6、v7等工作目录。需要同时打开不同分支时使用`git worktree`。

[Wallstreet Scaling执行报告](workspaces/wallstreetcn_scaling/报告.html)展示从三篇扩至30篇的正式采用结果及逐篇增量。
