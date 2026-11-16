# Scaling执行约定

工作目录为financial-foundation。先读仓库AGENTS、README；读graph/00_start全部现行说明、思想及形成记录和模板，再读materials/wallstreetcn/维护/ARTICLE_AUTHORING_CHARTER.md、workspaces/step2_articles/rule_review_20261116/汇总.md及相关样例。现行有效标准优先于工作图内保留的旧说明副本。

基础工作图为workspaces/step2_articles/graph，正式graph只读。本篇先通读指定文章、元数据和全部图片，再对照工作图及相关正文。先提交proposal.json并通知主agent，包含重要知识清单、现有匹配及拟修改位置、新节点的范围和父项、具体主体的观察用途；不要为每个术语注册，不设产量配额。等待主agent归属协调后，由同一agent继续制作全文。不再派生agent。

文件只写articles/<文章ID>/内，禁止直接覆盖共享工作图或索引。采用归属后交drafts/<目标相对路径>完整正文，delivery.json列文件操作new/update/reuse/inline、entry_kind、稳定ID、标题、目标path、draft_path、实际增量和来源。new/update的基础type与既有目录一致，子项必须有parent_ids及parent_relation；related关系和知识依赖不自动构成父项。已有对象优先复用同一ID，重叠旧页由主agent统一合并。

草稿按最终工作图目标位置计算链接；主agent整合后检查。通用知识、对象特性、机制过程与完整事件按职责安排，保留有用原图及关键数字。观点、事实、条件推演和后续结果分别注明主体与时点，evidence_as_of不随录入日期自动延长。不引入仅作者专用的toy model。真正有泛用意义而需讨论的模型交主agent处理。

新增页status为step2_draft，署名实际agent；旧页保留原作者及来源，新增editor、editing_status。模型与档位仅按可核验运行记录填写。新建候选ID先用C-WS-<文章ID>-<短名>或R-WS-<文章ID>-<短名>，由主agent去重协调；事件E-WS-<文章ID>、来源S-WS-<文章ID>。

交付必须有可读正文，不能仅列建议。结尾review.md简写新建哪些条目、修改哪些条目及内容、实际已读材料和具体限制。无实质内容可仅复用或弃稿，不生成待补知识池。原文和图片链接materials，不再复制。最终向主agent返回交付路径及关键判断。

## 统一交付接口

`delivery.json`须为对象，含article_id、title、files、coverage、summary。files每项必须有path（目标工作图相对路径）、draft_path（相对本篇目录）、operation（new/update）、id、type（concept/mechanism/analysis_note/source_note）、entry_kind（concept/subconcept/relation/subrelation/event/source）、title、why（具体增量）。已有页完整稿也标update，来源与事件文件作为new列入。关系的node_ids、related_mechanism_ids、logic_groups须与最终YAML正文相符；子项parent_ids、parent_relation须相符。可直接从YAML提取，不能填写空泛占位内容。

coverage列本篇重要知识最终去向，未形成文件的复用/内文项给path或锚点。summary直接写本篇新增哪些条目、修改哪些条目及修改内容。主agent仅将采用稿整合到唯一工作图，交付阶段草稿按最终工作图位置计算链接，不为临时目录另复制素材。

更新旧页时保留已有较晚证据及资料截止；本篇较早材料按历史窗口补录，不将整页evidence_as_of倒退。摘要summary优先写简明中文操作句，避免原始技术JSON作为报告正文。

本轮离线报告不加载LaTeX引擎；新补公式使用可直接阅读的Unicode或行内代码，保留符号定义及单位。
