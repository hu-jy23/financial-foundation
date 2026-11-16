# Step1执行流程

依据[用户提案](../../记录prompt.md)及后续确认。本文件是本轮工作区的流程入口；前轮试点的强制阅读地图、缺口清单和最小交付要求不适用于本轮。本轮T1、T2生产、审阅与正式接入已结束；结果见RESULTS.md。

## 分工与必读

制作与筛选审阅由主agent分别拉起两批subagent负责，均继承当前上下文、可读取全仓库；同一稿件由不同agent执笔和审阅。

两批都须读Step0思想文件：

- [整体规划](../financial_foundation_v5_20261027/financial_foundation_v5/00_start/PROJECT_PLAN.md)：项目用途、alignment及原型暂定性。
- [节点选取原则](../financial_foundation_v5_20261027/financial_foundation_v5/00_start/NODE_SELECTION_GUIDE.md)：独立知识价值、平凡性和关系职责。
- [对象选择过程](../financial_foundation_v5_20261027/financial_foundation_v5/00_start/CONCEPT_SELECTION_HISTORY.md)、[机制选择过程](../financial_foundation_v5_20261027/financial_foundation_v5/00_start/MECHANISM_SELECTION_HISTORY.md)：实际取舍及判断思想。
- [制作标准](../financial_foundation_v5_20261027/financial_foundation_v5/00_start/AUTHORING_STANDARD.md)、[审阅标准](../financial_foundation_v5_20261027/financial_foundation_v5/00_start/REVIEW_CHECKLIST.md)：成品应达到的解释程度与质量。

最新用户指示优先。Step0的234节点范围可以改写；前轮[试点skill](../tmp_step1_material_pilot_20261103/skills/step1-source-to-map/SKILL.md)中的阅读、核验和写作指导可参考，流程与交付数量以本文为准。

## 制作、筛选、返修

1. 按实际教材章节或连续论证界定unit，制作agent阅读后提出两份最优候选。每份包含核心解释段落、实质增量、来源定位及拟新增／更新的归属，先不写全文。不要求另交阅读地图或全章内容去向表。
2. 筛选agent按项目思想、现实联系、核心程度、分析用途和制作要求筛选；与正式图及其他候选去重。有重要新增性质／逻辑才合并更新；无用、低价值或仅有小差异的直接弃掉，不另设“不能独立成页但仍需保留”的分类。
3. 入选候选交制作agent完成中文全文或融入现有页的更新，避免整块追加造成冗长。支持核心判断的来源与必要条件随稿保留。
4. 审阅全文。低价值的直接弃掉；很值得保留且有问题的，带具体意见返修一次，然后复审。复审仍不合格则直接弃掉，不另建知识缺口、待补证队列或替代材料保留清单。
5. 一个unit两份均弃即结束，不追加阅读地图或漏项复查。两份均入选则标记，交制作agent再看是否还有值得制作的内容。两份中有弃用的unit按现有结果收尾。

弃用内容不另行归档或转存附录；工作状态只需在派工记录中简记unit是否完成、通过数量及成品路径，避免重复派工。

## 模型与材料范围

教材／作者特有的教学toy model默认排除。具有超出单本教材的解释、应用价值，或首次建模意义的具体例外候选，启动三个继承上下文的subagent讨论是否保留；不因材料清单安排阅读模型而自动纳入Map。

本轮按[新LIST](../financial_foundation_v5_20261027/financial_foundation_v5/40_sources/新LIST.md)推进T部分主教材，I、D、R后续开展。新LIST中“每章形成阅读记录”的旧要求以本轮用户确认的简化流程为准。现有A—E阅读路线及连续章节分组尚需按实际文件定位成派工unit。

本轮接入核验补充：新增段落要核对相邻指代、旧来源ID与锚点是否保留，并对齐教材简化口径与现有页的核算口径；不用全局替换旧source ID完成新增引用。
