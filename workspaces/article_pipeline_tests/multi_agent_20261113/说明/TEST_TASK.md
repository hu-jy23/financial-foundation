# 独立试作任务

按主agent分配的run_id与article_id工作。只写`成果/<run_id>.json`，不改其他文件，不再派生agent。不读取其他试作结果。

先按README读取纲领、四份测试版说明、其余现行说明及相关graph正文，独立通读文章并核看关键图表。交付实际的材料分析、组织判断与内容样稿，不能只提交流程或模板。篇幅以解释清楚为准，全文建议约1500—2500汉字，不为凑字段堆叠。

唯一JSON文件使用以下键：

- run_id、article_id、title。
- problem：你认为文章真正要解释的变化／矛盾；简短完整段落。
- passages：3—5个关键论述，每项含location、quote、analysis、method。分析方法由文章决定，说明具体怎样使用，不只给方法名称。
- structures：实际建议维护的少量内容，每项含name、kind（existing_update/new_concept/child_concept/new_mechanism/child_mechanism/event/section）、parent（现有ID／页名或父项调整建议，无则为空）、inherits、difference、why_register、inline_alternative、decision。子项需明确其继承或归属关系，不是组合词就注册；无需提出子项时给出理由。这里的建议不等于正式注册。
- sample_title、sample：选最值得保留的一处，写约300—600字可读样稿，体现你的解释与组织；可更多以讲清为准。样稿可作为对象段落、关系解释或事件分析，不要求全文成品。
- limitations：具体尚不能成立／还需核实的判断。
- guidance_feedback：这套纲领和测试版说明帮助了什么、哪里仍会诱发模板化或错误注册。
- reading：含documents、graph_pages、figures三个列表，列实际读取的文件路径；未看部分不声称已读。
- summary：一句主要发现与结构选择，供报告导航。

引用原文不代表确认其事实；数值、预测和作者推断保持归属，自己的推理应能辨认。本轮不联网抓取，不编造新史实，使用现有材料完成所能支持的试作。不得声称通过本次测试验证了全部市场事实。模型与档位只能写继承且不可核验，不推断具体配置。

最终向主agent只回复：文件路径、主要结构选择、实际看了哪些图及关键限制。
