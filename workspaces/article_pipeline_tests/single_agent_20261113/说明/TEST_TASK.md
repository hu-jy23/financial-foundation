# 本轮交付

每篇一个JSON：成果/<run_id>.json。它是报告的数据接口，不规定正文模板。

- run_id、article_id、title、problem、summary。
- concepts：重要概念／对象列表，每项name、aliases、role（为何重要）、existing_match（实际旧页及范围）、action（引用/更新/新建候选/正文解释）、core_text（实际解释，按难点展开）、sources（实际核读来源）。已有充分解释可简述并链接旧页，不需重复全文；缺失的重要对象必须给出可读解释。
- relations：重要关系列表，每项name、participants、existing_match、action、core_text、sources。关系可以是特定时点的具体联系，不以能否立为通用机制决定是否讲清。
- analysis：按文章自身问题写出的进一步分析，包含关键论述、比较或过程、观察与推断的联系、历史与具体预期。自由组织，不套AI案例章节。
- organization：有必要时说明独立维护、子项、旧页或Event的安排及实际理由；只为真正需要讨论结构的项目写，不强制每个概念填写父项。
- limitations、external_sources（URL及实际阅读范围，无则为空）、reading（documents、graph_pages、figures）、guidance_feedback。

无统一数量配额。不要只交清单或一个精彩样稿；应让读者能读懂每个重要对象和关系，并看见进一步分析。缺定义可定向核对一手资料；无法核对的部分标明边界，不伪造制度细节或历史数字。

韩国文必须覆盖SOX、KOSPI、杠杆ETF与持仓状态，并展开主要买盘联系；不要把SOX仅留在“收敛无依据”的批评中。美债文需比较现有基差、基差交易及相关融资机制的实际覆盖，重复者引用，重要增量实际写出。AI文同样先覆盖重要基础对象与关系，再展开具体分化。

只写指定结果文件；最终只回文件路径。完整上下文继承，模型与档位不可核验，不猜测具体配置。
