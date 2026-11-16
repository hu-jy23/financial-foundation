# 三篇单agent试作

[HTML报告](报告.html)包含知识清单、实际解释正文、深入分析及主agent审阅。

每篇由一个继承完整上下文的subagent处理。顺序：通读正文与图片→列重要概念和关系→对照现有graph→制作基础解释→深入分析→确定维护位置→主agent审阅。

| 文章 | 概念清单 | 关系清单 | 可读成果 |
| --- | ---: | ---: | --- |
| AI CDS | 12 | 6 | [Markdown](成果/ai.md) |
| 韩国股市 | 11 | 6 | [Markdown](成果/korea.md) |
| 美债基差交易 | 14 | 6 | [Markdown](成果/basis.md) |

清单包含引用、更新及正文解释；正式graph尚未接入本轮成果。

[执行说明](说明/README.md) · [任务要求](说明/TEST_TASK.md) · [子层级讨论](说明/SUBSTRUCTURE_DISCUSSION.md) · [制作纲领](../../../materials/wallstreetcn/%E7%BB%B4%E6%8A%A4/ARTICLE_AUTHORING_CHARTER.md)

[运行记录](run_manifest.json) · [主agent审阅](review.json) · [内容检查](checks.json) · [浏览器检查](browser_check.json)

在项目最外层执行 `python workspaces/article_pipeline_tests/single_agent_20261113/build_report.py` 可从成果JSON重建Markdown和HTML报告。
