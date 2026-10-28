# B066 研究与交审记录

实际执笔：/root/full_b066；模型gpt-6-astra，medium；2026-10-28。仅制作TASK指定三条；没有派子agent、改共享索引或操作Git。

## 输入与研究问题

已完整读TASK、COMMON_TASK、README、AUTHORING_STANDARD、REVIEW_CHECKLIST、NODE_SELECTION_GUIDE、机制模板、黄金／国债供给两完整样例、ACQUISITION_SHORTLIST。长输出截断后补读财政样例中后部和来源清单前半。catalog_index按分组items读取本批机制及全部指定对象；PATHS核对了全部对象链接。

研究先围绕下列问题展开：

- 新闻：新增事实、重复触达和重复计价怎样区分？有限关注为何没有被套利立即消除？经典公司公告研究能否外推到近年宏观新闻？
- 涨跌停：价格边界怎样使同一消息跨日反映？排队订单能否跨日保留、收盘价格是否可执行？2026年规则与旧的5%风险警示股说法有何变化？
- 基差：现券、期货、回购分别怎样记账？haircut与保证金怎样形成现金需求？2025年的相对价值平仓是否都可叫基差交易？

## 原文核读及失败替代

R-MARKET-11：

1. DellaVigna—Pollet作者公开2008-02-02稿，https://sdellavi.com/pdf/earnfr080204.pdf 。已读导论、模型命题、II样本、III股票反应及Table II讨论。论文主样本1995-01至2006-06，143,583次公告；即时0—1、延迟2—75交易日；15%、70%、8%均保存为作者概括的组间相对差异，不是个股回报百分点。没有采用工作稿中61.87%与0.6287的文字／公式不一致。
2. Tetlock正式2011 PDF由哥大教授页指向https://business.columbia.edu/sites/default/files-efs/pubfiles/3099/Tetlock%20Fit%20to%20Reprint%2010%2010.pdf ，web超时、urllib返回403。替代亲读作者大学公开2008年2月稿https://www.columbia.edu/~pt2238/papers/Tetlock_SSRN_Fit_to_Reprint.pdf ，印刷页1—15和附录相关信号模型。正文明确两版本不混用。27bp与−2bp来自2008稿Table III正文解释；其中新闻接近度是间接指标。2011仅核哥大正式摘要文本相似度口径，不声称核其表格。
3. Kroner 2025-022，https://www.federalreserve.gov/econres/feds/files/2025022pap.pdf ，PDF稿日2025-02-18、发布月2025-03；主样本2009-07-01至2023-07-12，读导论、Section 2竞争解释、3.1、5.1—5.2。新闻文章量在此用于注意力代理，而非独立事实次数。没有保存未读完整表的资产价格弹性。2024—2026公司联合数据仍未取得。

R-MARKET-13：

1. https://www.sse.com.cn/lawandrules/sselawsrules2025/stocks/exchange/c/c_20260424_10816482.shtml 通知和附件1。附件原URL：https://www.sse.com.cn/lawandrules/sselawsrules2025/stocks/exchange/c/10816482/files/e3a3b98e36894edca77841837936e006.docx 。web不支持DOCX，urllib成功下载/tmp/b066_sse.docx，用zip/XML抽取/tmp/b066_sse.txt。核读3.1.4—3.1.5、3.3.13—3.3.18、3.4—3.5、3.7、6.6、11.9；没有依据搜索摘要代替条文。
2. 2026-04-24官方修订说明https://www.sse.com.cn/aboutus/mediacenter/hotandd/c/c_20260424_10816474.shtml ：主板风险警示5%改10%、7月6日施行、盘后适用扩大。附件3暂缓条款未取得，正文没有笼统宣布全部条款实施。
3. Bao Qi原文https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0287548 。PMC入口正文访问遇captcha，改PLOS。读制度、假设、5.1、5.2及Table2解释、摘要结论。次日异常收益0.24/−0.76、−3.37/−0.68%；前后样本不是随机同类事件。5.1原文事件数量有明显前后矛盾（1537/942和2530/2406，1042/329和1210/774并列），正文明确不采用矛盾数量。磁吸结论仅按原论文所检验命题保留，不外推其他时期。

R-DERIVATIVES-02：

1. 2024-03-08 FEDS Note https://www.federalreserve.gov/econres/notes/feds-notes/quantifying-treasury-cash-futures-basis-trades-20240308.html ，读OABNOC、交割选择权、净回购与TRACE、Table1及近期测量比较。2023-09的2600亿TRACE、5740亿净回购、9130亿期货空头为不同代理，不能相加。来源正式作者名Glicoes。
2. CFTC咨询小组2024-12-10材料https://www.cftc.gov/media/11671/mrac121024_TreasuryCashFuturesBasisTradeReport/download ：II—III操作供需、IV作用、V风险PDF页4—12。不把小组建议当监管规则；其CTD最低市值简写不采用。没有逐项采用管理建议部分。
3. Monin 2026-06-22 https://www.federalreserve.gov/econres/notes/feds-notes/decomposing-hedge-funds-u-s-treasury-exposures-20260622.html ：导论、分解说明、基差复兴、掉期利差；数据至2025-09。约8300亿、35%和2.4万亿口径相容但为四舍五入；2025-04约600亿退出系swap spread，非现金期货基差。未复算附录分类算法。
4. Patel 2026年1月https://www.chicagofed.org/publications/chicago-fed-letter/2026/516 ：期货、转换因子、需求、杠杆、结论。其以期货空头代理超过1万亿不取作真实基差规模；第二篇清算情景未读，正文没有声称清算成本一定提高到某数。

## 算例与自查

- 新闻100→110、初始106为假设估值，明示非可观测内在价值。
- 涨停10→11→12.10为10%逐日复利，连续两日涨停累计21%。第二日重新申报，不能写作原订单原优先权跨日保留。
- 基差假设1亿/1.01亿，全部成本80万，利润20万；haircut2%+IM100万，至少占用300万，20/300=6.67%持有期而非年化。缓冲未包含并明确指出。
- 抵押压力：1亿×98%=9800万；9900万×96%=9504万；须补296万。明确现金补足不等于全部损失，避免与盯市损失重复记账。
- 三篇各两logic锚点，来源锚点和引用匹配，对象链接已逐项对PATHS；YAML保持draft，reviewed_by:null。没有新建Event/Source。

## 交审与需主审处

首个完整交审稿均在本批同名FIRST_DRAFT逐字冻结。main预审通知后R-MARKET-11、R-MARKET-13没有正文修改。R-DERIVATIVES-02为此轮首次交审。

请重点审：新闻2008与2011版本分离和近期Kroner研究的角色边界；涨跌停日度论文的选择偏差和2026制度截止；基差损益式的含息价格／票息记账及交割结算说明。全部指定node_ids保持不变，没有范围细化。
