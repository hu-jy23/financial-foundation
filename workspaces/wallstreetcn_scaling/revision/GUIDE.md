# 本轮逐篇审阅与原作者返修

范围：原3篇及scaling新增27篇，共30篇。每篇一名独立审阅agent，完整继承主agent上下文；原写作agent负责返修。共用正文由主agent合并，正式graph不修改。

3749421原作者三次无法恢复，原三个试点作者会话已不存在。四篇均经用户明确授权，由完整继承上下文的新agent接手；原署名保留，返修者另记。

## 阅读

先读仓库AGENTS.md、README.md；graph/00_start中的思想、标准、节点选择、历史选择记录、Event/Source指南、审阅清单和模板；materials/wallstreetcn/维护/ARTICLE_AUTHORING_CHARTER.md。再读本篇原文、metadata、所有分析图、delivery.json列出的现行成品及关联正文。不要把旧排除表当永久禁令，也不机械推翻明确的用户取舍。

## 判断标准

- 原文要解释什么变化？成品是否形成清楚、具体、有解释力的认识？检查参与者、付款、合同、资源与风险承担、推断条件。
- 图表转录、单位、分母、日期、汇总与明细是否一致？必须亲自看图片；疑点保留差异，不为闭合数字改写原图。CoreWeave已确认两处相互抵消的转录错误：Edged应114MW被写144MW，ELNFOR/APLD后续债应150MW被写120MW；正确七笔合计仍是1512MW。主agent此前只修第一处而判断1482与1512冲突是误判。审阅以原图为准，并核对所有采用位置。
- 基础知识有没有遗漏？通用概念/关系是否被不合适地埋进事件？PMI旧排除安排可重新讨论；不强设新增配额。
- 概念、关系、事件、来源职责是否清楚？同一事实和分析是否重复展开？一个主要维护位置，其他页用必要的短解释及定位引用，不能把有用知识删成空壳。
- 正文是否被逐图校勘、重复限定语、执行过程说明淹没？保留影响核心结论的条件；技术核读细节放来源或图注，解释顺序服务学习者。无需所有图都重复嵌入事件，保留支持理解的图并能定位其余原图。
- 子项父项是合理继承还是勉强挂靠？公司观察用途有实际经营/金融链条吗？亲缘关系不清不能靠大量限定语维持。需要新增父项/迁移/合并的跨篇结构问题先交主agent协调。
- 预期是否落到具体主体、信息日、期限与能区分解释的新观察？避免泛泛“资金不足就承压”。不要把作者模型变成通用规律；保留有价值的分析和竞争解释。
- 用可定位的原句/图/段说明问题，区分确定错误、组织问题和可讨论建议。无需为每个标准凑问题，好的内容明确保留。勿把审阅写成冗长说明书。

## 审阅交付

只写revision/<article_id>/audit.md与audit.json，不改共享工作图。audit.json字段article_id、verdict、issues（id,severity,error/structure/clarity/coverage/attribution,location,evidence,requested_change）、retain、cross_article_requests。audit.md简写保留点及必须返修点。完成后通知主agent。不得自行派生agent。

## 原作者返修

读取本轮audit及现行正文，不用旧草稿覆盖后续内容。主agent先协调跨篇结构。只写revision/<article_id>/drafts/<目标工作图相对路径>与revision_delivery.json；不直接修改共享工作图、登记或原始材料。revision_delivery字段article_id、files（path,draft_path,operation,id,type,entry_kind,title,why及与YAML一致的父项/关系信息）、responses（对应issue及具体修改），另写简短revision.md。未改文件不必重交。保留原作者/原来源/其他篇贡献及已有较晚证据，编辑标注真实。本篇事件、来源与归属条目一起维护，消除失效锚点和重复。若确实不采纳某意见要给具体理由。

返修前保存本篇所读工作图MD基线至revision/<id>/base.json（相对路径→文本）；主agent三方合并并复核。完成采用后删除drafts与base等临时正文副本，保留审阅、修改响应和交付记录。报告最后统一重建。
