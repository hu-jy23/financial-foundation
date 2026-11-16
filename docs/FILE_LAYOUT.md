# 文件管理约定

更新：2026-11-16。

## 唯一维护位置

`financial-foundation/`是唯一Git仓库和工作目录。外层只保留入口说明及运行环境隐藏目录。材料、进度和成品不再放到仓库外，也不保留一套手动同步的workspace备份。

- `graph/`维护现行图谱；思想、制作标准、目录和模板在`graph/00_start/`。
- `materials/`维护来源原文、图表、获取记录与检索库。
- `workspaces/`维护待整合成品及有明确用途的制作试验。
- `tests/`维护评测数据与固定快照；`reports/`维护报告。
- `docs/STEP1_LOG.md`与`docs/STEP2_LOG.md`记录阶段进度。

正式图、待整合工作图和评测快照分别承担维护、审阅、复现实验的职责。新材料优先链接已有原件；完整项目版本由Git保存。

## 分支与目录

默认在同一目录切换分支，不复制项目。切换前提交当前进度。需要同时开发或对照两个分支时，用`git worktree`建立独立检出目录。

本次整理只提交到scaling分支，未向原分支合并三篇成品。旧分支保留其旧目录布局，切换后以该分支README为入口。

## 旧文件如何回溯

旧`bin/`中的502个文件已保存到提交`de699d21c711f6e97c4c645311a6d7b775873046`的`legacy_versions/`，并已推送；工作目录不再保留旧版本文件夹。整理前完整工作进度另见提交`5a4744460ac44afdbce9e9d871af769c81a2e6f7`。

外层Source、临时工作区、测试和报告均与Git备份逐文件核对后清理。目录调整不改变节点ID、原文语言、证据时点或三篇成品的采用状态。

## 校验与历史记录

原件按SHA-256核对，22份重复PDF改为指向唯一原件。历史试验输入校验值及copied_from保留当时记录，原始文件可回溯整理前提交；当前三篇成品的工作图基线按新路径重新登记。

## 旧位置到新位置

| 旧位置 | 新位置 |
| --- | --- |
| `financial_foundation_v5_20261027/financial_foundation_v5/` | `graph/` |
| `source_2/` | `materials/textbooks/` |
| `sources/` | `materials/reference/` |
| `source_step2/` | `materials/institutional/` |
| 外层`Source/华尔街见闻/` | `materials/wallstreetcn/` |
| `tmp_Workspace/step2_delivery_20261113/` | `workspaces/step2_articles/` |
| 其余`tmp_Workspace/` | `workspaces/step1_books/` |
| `tmp_step1_material_pilot_20261103/` | `workspaces/step1_pilot/` |
| `graph_test_20261104/` | `tests/graph/` |
| `中期报告/` | `reports/中期报告/` |
| `STEP1_LOG.md`、`STEP2_LOG.md` | `docs/` |
