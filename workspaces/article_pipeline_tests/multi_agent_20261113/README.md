# 文章制作思想与子层级试作

- [HTML报告](报告.html)：主要发现、两篇文章比较、12份试作与内容样稿。
- [制作纲领](../../../materials/wallstreetcn/%E7%BB%B4%E6%8A%A4/ARTICLE_AUTHORING_CHARTER.md)：通用制作思想。
- [子层级讨论](说明/SUBSTRUCTURE_DISCUSSION.md)：何时注册、继承内容与维护收益。
- [测试说明](说明/README.md)：测试版标准、共同输入与交付范围。
- `成果/`：每篇6次试作的原始JSON，报告直接由其生成。
- `run_manifest.json`：文章与说明文件校验值、运行配置和状态。
- `review.json`：主agent汇总与逐份审阅意见。
- `result_check.json`、`browser_check.json`：文件、输入一致性及页面交互检查。

运行`python build_report.py`重建HTML，运行`python check_results.py`检查12份结果与冻结输入。可选运行`python check_browser.py`检查本地浏览器交互，需要Chrome、requests和websocket-client。正式graph不在本轮修改范围。


感觉同一片文章启动多个subagent并行效果一般。后面就用1个吧。理念方面，新闻作为Step2仍可以补充很多基本的概念/关系，所以基本的制作也不要拉下。可以先看基本的，比如先列出所有重要的概念。再按照你之前的纲领进一步提取。
举个例子，韩国股市这一篇，提取的概念就要include SOX，