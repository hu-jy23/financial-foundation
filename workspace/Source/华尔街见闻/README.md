# 华尔街见闻本地材料库

本轮已保存206篇正文及770处正文插图，全部取得；图片文件769份，同篇重复引用共用文件。图片化的表格按原图保留。

打开[index.html](index.html)浏览和筛选文章；[CATALOG.md](CATALOG.md)提供文字目录。[采集方案](维护/PROPOSAL.md)记录抽样、格式选择和采集标准。[制作纲领](维护/ARTICLE_AUTHORING_CHARTER.md)说明通用制作思想；[AI CDS阅读草案](维护/SOURCE_TO_GRAPH_PLAN.md)保留具体分析示例。[最新试作报告](实验_20261113_基础与分析/报告.html)汇总AI CDS、韩国股市及美债基差交易三篇成果，每篇一个继承上下文的agent，先制作基础知识再深入分析；[本轮说明](实验_20261113_基础与分析/说明/README.md)记录执行顺序。[前轮报告](实验_20261113/报告.html)保留两篇各6次试作的比较。选文清单、采集脚本、检索数据库和检查记录集中放在`维护/`。

[三篇成品阅读报告](../../tmp_Workspace/step2_delivery_20261113/阅读报告.html)展示独立工作图中的新增、更新正文；[制作归属](../../tmp_Workspace/step2_delivery_20261113/制作说明.md)说明各页职责，尚未整合main。

每篇存放于`SourcePost/<文章标题>/`，ID保留在元数据中。Windows不支持的文件名字符替换为对应全角字符。

- `article.html`：离线阅读入口，正文图片按原顺序显示，可点击查看完整尺寸。
- `assets/`：正文图片文件，图像中的表格也保存在这里。
- `article.md`：供agent阅读和编辑的Markdown正文，保留标题、加粗、引用、列表、原文链接及本地图片；图题和注释保持原顺序。图片中的文字及数值需要查看图片。
- `raw.json`：公开接口此次响应原件，保留原始正文和来源字段。
- `metadata.json`：署名、页面显示日期、取得时间、原地址、资源校验和缺件情况。

`维护/manifest.json`汇总保存状态，`维护/validation.json`合并文件与浏览器检查，`维护/library.sqlite`索引Markdown全文，检索结果指向MD文件。浏览器入口的搜索覆盖标题、署名、主题和选文理由；全文搜索使用下面的命令。

从项目最外层目录执行：

```bash
# 全文检索；支持中文和英文短语
python Source/华尔街见闻/维护/library.py search '供应商融资'
python Source/华尔街见闻/维护/library.py search 'CDS' --limit 20

# 继续采集，复用已取得的原件和图片
python Source/华尔街见闻/维护/library.py acquire

# 按ID重试；原件已成功保存时不重新抓取网页版本
python Source/华尔街见闻/维护/library.py acquire --ids 3784900

# 从已保存的HTML重建Markdown，不联网
python Source/华尔街见闻/维护/library.py reformat

# 重建目录和SQLite；检查正文、图像、校验值及本地链接
python Source/华尔街见闻/维护/library.py build
python Source/华尔街见闻/维护/library.py validate
```

采集依赖Python的`requests`、`beautifulsoup4`、`Pillow`、`markdown-it-py`、支持FTS5 trigram的SQLite；Markdown转换使用Pandoc。直接阅读HTML不需要运行服务或安装这些依赖。迁移时保留整个材料库；单篇文件夹可以单独阅读，返回总目录和跨文章的本地链接需要保留原目录关系。

完整状态指当前取得版本的公开正文和正文插图齐备。页面显示日期不保证是最初发布时间；署名可能是编辑，观点归属以正文为准。平台配音、头像、封面、评论及链接出去的其他作品不在采集范围。原文、原图保留，下载不等于精读或核实结论。
