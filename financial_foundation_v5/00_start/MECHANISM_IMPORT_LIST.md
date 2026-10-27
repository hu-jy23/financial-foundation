# 金融关系／机制正式目录 v5

初步建图范围确认：2026-10-25。共 **71 个关系／机制，16 个主题组**；正文 **2 份已完成、69 份待制作**。

本表只列已确认入选的关系。原177项的勾叉与最终名称见[完整审阅表](../50_reviews/MECHANISM_SELECTION_177.md)，未入选106项见[旧ID登记](MECHANISM_ARCHIVE.md)。

名称采用已修订版本，并恢复用户确认的36项原名。恢复名称不改变勾叉；其中未入选者仍保留在审阅记录中。

关联对象均来自正式对象目录；其余变量放在正文术语栏。未完成条目的关联对象为初始研究入口，具体逻辑组在制作时依据材料细化。

节点范围已确定；pending表示正文待制作。命名、解释与研究要求见[制作标准](AUTHORING_STANDARD.md)，结构化数据见[索引](catalog_index.json)。

| 主题组 | 条目 | P0 | 成品 | 待制作 |
|---|---:|---:|---:|---:|
| 测量、恒等式与预期 | 1 | 1 | 0 | 1 |
| 货币政策与利率传导 | 9 | 5 | 0 | 9 |
| 增长、就业与通胀机制 | 1 | 0 | 0 | 1 |
| 财政与债务机制 | 6 | 2 | 1 | 5 |
| 信用与金融稳定机制 | 9 | 3 | 0 | 9 |
| 跨境、美元与汇率机制 | 10 | 3 | 0 | 10 |
| 股票与公司定价机制 | 2 | 1 | 0 | 2 |
| 资金流与市场微观结构 | 7 | 0 | 0 | 7 |
| 衍生品与波动机制 | 6 | 1 | 0 | 6 |
| 黄金与跨资产机制 | 3 | 2 | 1 | 2 |
| 能源与商品机制 | 3 | 1 | 0 | 3 |
| 中国信用、地产与财政传导 | 7 | 2 | 0 | 7 |
| 中国资产与政策机制 | 1 | 0 | 0 | 1 |
| 科技与AI产业机制 | 2 | 0 | 0 | 2 |
| 政治、制度与长期变化 | 2 | 0 | 0 | 2 |
| 数字资产传导 | 2 | 0 | 0 | 2 |

## 测量、恒等式与预期

| ID | 关系名称 | 关联对象 | 正文术语／相关关系 | 范围 | 优先级 | 正文状态 |
|---|---|---|---|---|---|---|
| <a id="R-MEAS-BEI"></a>R-MEAS-BEI | 通胀补偿的定价分解 | [美国通胀保值国债TIPS C-IR-TIPS](CONCEPT_IMPORT_LIST.md#C-IR-TIPS)；[市场流动性 C-LIQ-MARKET](CONCEPT_IMPORT_LIST.md#C-LIQ-MARKET) | [名义利率（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-IR-NOMINAL)；[盈亏平衡通胀率BEI（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-IR-BEI)；[通胀风险溢价（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-INFLATION-09) | 溢价和流动性成分 | P0 | pending／待制作 |

## 货币政策与利率传导

| ID | 关系名称 | 关联对象 | 正文术语／相关关系 | 范围 | 优先级 | 正文状态 |
|---|---|---|---|---|---|---|
| <a id="R-POL-CURVE"></a>R-POL-CURVE | 货币政策冲击的期限结构传导 | [政策利率与目标区间 C-IR-POLICY](../10_concepts/C-IR-POLICY_policy_rate_target_range.md)；[量化宽松QE C-POL-QE](../10_concepts/C-POL-QE_quantitative_easing.md)；[收益率曲线 C-IR-CURVE](CONCEPT_IMPORT_LIST.md#C-IR-CURVE)；[期限溢价 C-IR-TERM](../10_concepts/C-IR-TERM_term_premium.md) | [预期差与意外成分（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EXPECT-SURPRISE)；[前瞻指引（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EXPECT-13) | 目标利率、路径、资产购买分别识别 | P0 | pending／待制作 |
| <a id="R-POL-INFORMATION"></a>R-POL-INFORMATION | 央行公告的政策效应与信息效应 | [美联储与FOMC C-GLOBAL-01](CONCEPT_IMPORT_LIST.md#C-GLOBAL-01)；[政策利率与目标区间 C-IR-POLICY](../10_concepts/C-IR-POLICY_policy_rate_target_range.md)；[收益率曲线 C-IR-CURVE](CONCEPT_IMPORT_LIST.md#C-IR-CURVE) | [前瞻指引（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EXPECT-13)；[预期修正（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EXPECT-09)；[盈利预期与分析师修正（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EQUITY-09) | 增长信息和政策动作共同出现 | P0 | pending／待制作 |
| <a id="R-QE-DURATION"></a>R-QE-DURATION | QE的久期风险转移 | [量化宽松QE C-POL-QE](../10_concepts/C-POL-QE_quantitative_easing.md)；[央行资产负债表 C-MONEY-CBBS](../10_concepts/C-MONEY-CBBS_central_bank_balance_sheet.md)；[期限溢价 C-IR-TERM](../10_concepts/C-IR-TERM_term_premium.md) | [债务期限结构与净久期供给（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FISCAL-DURATION)；[久期、修正久期与DV01（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-BOND-DURATION) | 期限供给、信号与市场功能 | P0 | pending／待制作 |
| <a id="R-QT-LIQ"></a>R-QT-LIQ | QT与准备金、ONRRP及资金市场 | [量化紧缩QT C-POL-QT](../10_concepts/C-POL-QT_quantitative_tightening.md)；[央行资产负债表 C-MONEY-CBBS](../10_concepts/C-MONEY-CBBS_central_bank_balance_sheet.md)；[银行准备金 C-MONEY-RESERVES](CONCEPT_IMPORT_LIST.md#C-MONEY-RESERVES)；[隔夜逆回购ONRRP C-MONEY-14](CONCEPT_IMPORT_LIST.md#C-MONEY-14)；[SOFR与担保融资基准 C-RATE-06](CONCEPT_IMPORT_LIST.md#C-RATE-06)；[融资流动性 C-LIQ-FUND](../10_concepts/C-LIQ-FUND_funding_liquidity.md) | — | 央行负债替代与稀缺性 | P0 | pending／待制作 |
| <a id="R-MONETARY-07"></a>R-MONETARY-07 | 利率走廊 | [银行准备金 C-MONEY-RESERVES](CONCEPT_IMPORT_LIST.md#C-MONEY-RESERVES)；[准备金利率 C-MONEY-07](CONCEPT_IMPORT_LIST.md#C-MONEY-07)；[常备工具与最后贷款人 C-MONEY-11](CONCEPT_IMPORT_LIST.md#C-MONEY-11)；[有效联邦基金利率EFFR C-RATE-05](CONCEPT_IMPORT_LIST.md#C-RATE-05)；[SOFR与担保融资基准 C-RATE-06](CONCEPT_IMPORT_LIST.md#C-RATE-06) | — | 准备金利率、常备工具与准备金供给如何共同影响隔夜市场利率；区分走廊与地板制度。 | P1 | pending／待制作 |
| <a id="R-TGA-RESERVES"></a>R-TGA-RESERVES | TGA收支对准备金的影响 | [财政部一般账户TGA C-MONEY-13](../10_concepts/C-MONEY-13_treasury_general_account.md)；[央行资产负债表 C-MONEY-CBBS](../10_concepts/C-MONEY-CBBS_central_bank_balance_sheet.md)；[银行准备金 C-MONEY-RESERVES](CONCEPT_IMPORT_LIST.md#C-MONEY-RESERVES)；[隔夜逆回购ONRRP C-MONEY-14](CONCEPT_IMPORT_LIST.md#C-MONEY-14) | [国债总发行与净发行（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FISCAL-07) | 现金流和负债替代 | P0 | pending／待制作 |
| <a id="R-MONETARY-09"></a>R-MONETARY-09 | 货币基金在ONRRP与国库券之间的配置 | [隔夜逆回购ONRRP C-MONEY-14](CONCEPT_IMPORT_LIST.md#C-MONEY-14)；[货币市场基金 C-MONEY-19](CONCEPT_IMPORT_LIST.md#C-MONEY-19)；[美国国债 C-ASSET-UST](CONCEPT_IMPORT_LIST.md#C-ASSET-UST)；[回购与逆回购 C-MONEY-10](CONCEPT_IMPORT_LIST.md#C-MONEY-10) | [国债总发行与净发行（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FISCAL-07) | 货币基金替代配置 | P1 | pending／待制作 |
| <a id="R-MONETARY-10"></a>R-MONETARY-10 | 利率上调与存款迁移 | [政策利率与目标区间 C-IR-POLICY](../10_concepts/C-IR-POLICY_policy_rate_target_range.md)；[货币市场基金 C-MONEY-19](CONCEPT_IMPORT_LIST.md#C-MONEY-19)；[挤兑与存款迁移 C-CREDIT-15](CONCEPT_IMPORT_LIST.md#C-CREDIT-15)；[净息差NIM C-CREDIT-04](CONCEPT_IMPORT_LIST.md#C-CREDIT-04) | [广义货币与存款（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MONEY-03) | 存款beta和货币基金替代 | P1 | pending／待制作 |
| <a id="R-IR-CURVE-SHAPE"></a>R-IR-CURVE-SHAPE | 收益率曲线陡峭化与平坦化 | [收益率曲线 C-IR-CURVE](CONCEPT_IMPORT_LIST.md#C-IR-CURVE)；[政策利率与目标区间 C-IR-POLICY](../10_concepts/C-IR-POLICY_policy_rate_target_range.md)；[期限溢价 C-IR-TERM](../10_concepts/C-IR-TERM_term_premium.md)；[美国国债 C-ASSET-UST](CONCEPT_IMPORT_LIST.md#C-ASSET-UST) | — | 短端政策路径、长端预期与期限溢价怎样改变曲线斜率；区分不同期限和牛熊变化。 | P1 | pending／待制作 |

## 增长、就业与通胀机制

| ID | 关系名称 | 关联对象 | 正文术语／相关关系 | 范围 | 优先级 | 正文状态 |
|---|---|---|---|---|---|---|
| <a id="R-GROWTH-04"></a>R-GROWTH-04 | 工资—价格反馈 | [通货膨胀 C-INF-INFLATION](CONCEPT_IMPORT_LIST.md#C-INF-INFLATION)；[央行可信度 C-POL-CREDIBILITY](CONCEPT_IMPORT_LIST.md#C-POL-CREDIBILITY) | [工资增长（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-INFLATION-10)；[单位劳动成本（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-INFLATION-13)；[服务、商品与住房通胀（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-INFLATION-07)；[通胀预期（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-INF-EXPECT)；[预期锚定（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EXPECT-11) | 议价制度与预期锚定 | P1 | pending／待制作 |

## 财政与债务机制

| ID | 关系名称 | 关联对象 | 正文术语／相关关系 | 范围 | 优先级 | 正文状态 |
|---|---|---|---|---|---|---|
| <a id="R-FISCAL-LONGYIELD"></a>R-FISCAL-LONGYIELD | 国债供给的定价机制 | [财政赤字与初级赤字 C-FISCAL-DEFICIT](../10_concepts/C-FISCAL-DEFICIT_fiscal_primary_deficit.md)；[财政部一般账户TGA C-MONEY-13](../10_concepts/C-MONEY-13_treasury_general_account.md)；[融资流动性 C-LIQ-FUND](../10_concepts/C-LIQ-FUND_funding_liquidity.md)；[期限溢价 C-IR-TERM](../10_concepts/C-IR-TERM_term_premium.md)；[央行资产负债表 C-MONEY-CBBS](../10_concepts/C-MONEY-CBBS_central_bank_balance_sheet.md)；[量化宽松QE C-POL-QE](../10_concepts/C-POL-QE_quantitative_easing.md)；[量化紧缩QT C-POL-QT](../10_concepts/C-POL-QT_quantitative_tightening.md)；[实际利率 C-IR-REAL](../10_concepts/C-IR-REAL_real_interest_rate.md) | [国债总发行与净发行（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FISCAL-07)；[债务期限结构与净久期供给（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FISCAL-DURATION)；[久期、修正久期与DV01（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-BOND-DURATION)；[基金流量与资产配置（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-07)；[风险偏好与避险需求（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-14)；[利差与汇率对冲成本（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FX-08)；[产出缺口（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MAC-OUTPUTGAP)；[政策反应函数（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-POL-REACTION) | 从发行期限和央行持仓推到私人久期承接，再讨论期限溢价与收益率 | P0 | complete／[正文](../20_mechanisms/R-FISCAL-LONGYIELD_fiscal_long_yields.md) |
| <a id="R-FISCAL-DEBTDYN"></a>R-FISCAL-DEBTDYN | 政府债务动态 | [财政赤字与初级赤字 C-FISCAL-DEFICIT](../10_concepts/C-FISCAL-DEFICIT_fiscal_primary_deficit.md) | [债务占GDP比率（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FISCAL-05)；[政府利息负担（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FISCAL-06)；[名义GDP与实际GDP（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MACRO-01)；[债务可持续性（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FISCAL-11) | 口径一致的债务可持续性 | P0 | pending／待制作 |
| <a id="R-FISCAL-07"></a>R-FISCAL-07 | 国债供给与抵押品便利收益定价 | [美国国债 C-ASSET-UST](CONCEPT_IMPORT_LIST.md#C-ASSET-UST)；[抵押品与折扣率haircut C-CREDIT-10](CONCEPT_IMPORT_LIST.md#C-CREDIT-10)；[回购与逆回购 C-MONEY-10](CONCEPT_IMPORT_LIST.md#C-MONEY-10) | [国债总发行与净发行（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FISCAL-07)；[在券与老券on/off-the-run（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-BOND-15) | 安全资产的抵押服务与流动性价值须同商品的物理便利收益区分 | P1 | pending／待制作 |
| <a id="R-FISCAL-08"></a>R-FISCAL-08 | 债务上限风险的短券定价 | [债务上限与政府停摆 C-FISCAL-15](CONCEPT_IMPORT_LIST.md#C-FISCAL-15)；[财政部一般账户TGA C-MONEY-13](../10_concepts/C-MONEY-13_treasury_general_account.md)；[美国国债 C-ASSET-UST](CONCEPT_IMPORT_LIST.md#C-ASSET-UST)；[主权信用风险与CDS C-FISCAL-14](CONCEPT_IMPORT_LIST.md#C-FISCAL-14)；[货币市场基金 C-MONEY-19](CONCEPT_IMPORT_LIST.md#C-MONEY-19) | — | 到期时点和支付风险 | P1 | pending／待制作 |
| <a id="R-FISCAL-10"></a>R-FISCAL-10 | 财政主导与通胀预期 | [财政主导 C-FISCAL-13](CONCEPT_IMPORT_LIST.md#C-FISCAL-13)；[央行可信度 C-POL-CREDIBILITY](CONCEPT_IMPORT_LIST.md#C-POL-CREDIBILITY) | [政府利息负担（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FISCAL-06)；[债务期限结构与净久期供给（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FISCAL-DURATION)；[通胀预期（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-INF-EXPECT) | 制度、债务期限与央行约束 | P1 | pending／待制作 |
| <a id="R-FISCAL-11"></a>R-FISCAL-11 | 主权信用与银行资产负债表反馈 | [主权信用风险与CDS C-FISCAL-14](CONCEPT_IMPORT_LIST.md#C-FISCAL-14)；[银行资本与杠杆率 C-CREDIT-02](CONCEPT_IMPORT_LIST.md#C-CREDIT-02)；[挤兑与存款迁移 C-CREDIT-15](CONCEPT_IMPORT_LIST.md#C-CREDIT-15) | [商业银行资产负债表（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CREDIT-01)；[财政空间（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FISCAL-12) | 本国债持仓及救助预期 | P1 | pending／待制作 |

## 信用与金融稳定机制

| ID | 关系名称 | 关联对象 | 正文术语／相关关系 | 范围 | 优先级 | 正文状态 |
|---|---|---|---|---|---|---|
| <a id="R-BANKING-01"></a>R-BANKING-01 | 银行信贷的资本约束 | [银行资本与杠杆率 C-CREDIT-02](CONCEPT_IMPORT_LIST.md#C-CREDIT-02) | [商业银行资产负债表（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CREDIT-01)；[不良贷款与拨备（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CREDIT-14)；[贷款标准与贷款需求（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CREDIT-05) | 资本损失、风险权重和融资 | P1 | pending／待制作 |
| <a id="R-BANKING-02"></a>R-BANKING-02 | 银行负债成本、资产重定价与息差 | [净息差NIM C-CREDIT-04](CONCEPT_IMPORT_LIST.md#C-CREDIT-04)；[政策利率与目标区间 C-IR-POLICY](../10_concepts/C-IR-POLICY_policy_rate_target_range.md) | [商业银行资产负债表（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CREDIT-01)；[广义货币与存款（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MONEY-03)；[久期、修正久期与DV01（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-BOND-DURATION) | 固定/浮动、久期和存款beta | P1 | pending／待制作 |
| <a id="R-CREDIT-COLLATERAL"></a>R-CREDIT-COLLATERAL | 金融加速器 | [抵押品与折扣率haircut C-CREDIT-10](CONCEPT_IMPORT_LIST.md#C-CREDIT-10) | [住房价格与家庭净财富（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MACRO-17)；[贷款标准与贷款需求（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CREDIT-05)；[杠杆与去杠杆（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CREDIT-LEVERAGE)；[企业投资与资本开支（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MACRO-08) | 金融加速器 | P0 | pending／待制作 |
| <a id="R-LIQ-SPIRAL"></a>R-LIQ-SPIRAL | 保证金驱动的流动性螺旋 | [保证金与追加保证金 C-DERIV-14](CONCEPT_IMPORT_LIST.md#C-DERIV-14)；[抵押品与折扣率haircut C-CREDIT-10](CONCEPT_IMPORT_LIST.md#C-CREDIT-10)；[融资流动性 C-LIQ-FUND](../10_concepts/C-LIQ-FUND_funding_liquidity.md) | [杠杆与去杠杆（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CREDIT-LEVERAGE)；[持仓拥挤与集中度（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-08)；[价格冲击与市场容量（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-03) | 杠杆投资者和共同持仓 | P0 | pending／待制作 |
| <a id="R-BANKING-05"></a>R-BANKING-05 | 流动性错配下的挤兑机制 | [银行流动性覆盖与稳定融资 C-CREDIT-03](CONCEPT_IMPORT_LIST.md#C-CREDIT-03)；[挤兑与存款迁移 C-CREDIT-15](CONCEPT_IMPORT_LIST.md#C-CREDIT-15)；[市场流动性 C-LIQ-MARKET](CONCEPT_IMPORT_LIST.md#C-LIQ-MARKET) | [广义货币与存款（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MONEY-03)；[商业银行资产负债表（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CREDIT-01) | 赎回承诺、资产可售性 | P1 | pending／待制作 |
| <a id="R-DEBT-DEFLATION"></a>R-DEBT-DEFLATION | 债务通缩 | [通货膨胀 C-INF-INFLATION](CONCEPT_IMPORT_LIST.md#C-INF-INFLATION)；[金融周期 C-CREDIT-16](CONCEPT_IMPORT_LIST.md#C-CREDIT-16)；[抵押品与折扣率haircut C-CREDIT-10](CONCEPT_IMPORT_LIST.md#C-CREDIT-10) | [通缩与去通胀（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-INFLATION-02)；[名义量与实际量（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-BASIC-NOMREAL)；[杠杆与去杠杆（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CREDIT-LEVERAGE)；[住房价格与家庭净财富（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MACRO-17)；[家庭消费（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MACRO-06) | 收入价格下降、名义债固定 | P0 | pending／待制作 |
| <a id="R-BANKING-09"></a>R-BANKING-09 | 证券化中的风险转移与激励 | [证券化与资产支持证券 C-CREDIT-13](CONCEPT_IMPORT_LIST.md#C-CREDIT-13)；[银行资本与杠杆率 C-CREDIT-02](CONCEPT_IMPORT_LIST.md#C-CREDIT-02)；[影子银行与非银金融 C-CREDIT-12](CONCEPT_IMPORT_LIST.md#C-CREDIT-12) | [商业银行资产负债表（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CREDIT-01)；[违约概率与回收率（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CREDIT-07) | 分层、信息和监管 | P1 | pending／待制作 |
| <a id="R-BANKING-10"></a>R-BANKING-10 | 最后贷款人的危机干预 | [常备工具与最后贷款人 C-MONEY-11](CONCEPT_IMPORT_LIST.md#C-MONEY-11)；[抵押品与折扣率haircut C-CREDIT-10](CONCEPT_IMPORT_LIST.md#C-CREDIT-10)；[挤兑与存款迁移 C-CREDIT-15](CONCEPT_IMPORT_LIST.md#C-CREDIT-15)；[融资流动性 C-LIQ-FUND](../10_concepts/C-LIQ-FUND_funding_liquidity.md) | [商业银行资产负债表（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CREDIT-01) | 抵押、可得性和道德风险 | P1 | pending／待制作 |
| <a id="R-BANKING-12"></a>R-BANKING-12 | 金融周期中的系统性风险积累与扩散 | [金融周期 C-CREDIT-16](CONCEPT_IMPORT_LIST.md#C-CREDIT-16)；[抵押品与折扣率haircut C-CREDIT-10](CONCEPT_IMPORT_LIST.md#C-CREDIT-10)；[融资流动性 C-LIQ-FUND](../10_concepts/C-LIQ-FUND_funding_liquidity.md)；[市场流动性 C-LIQ-MARKET](CONCEPT_IMPORT_LIST.md#C-LIQ-MARKET)；[银行资本与杠杆率 C-CREDIT-02](CONCEPT_IMPORT_LIST.md#C-CREDIT-02) | — | 信用扩张、杠杆和资产价格反馈；抵押、融资及银行约束如何促成风险积累与扩散。 | P1 | pending／待制作 |

## 跨境、美元与汇率机制

| ID | 关系名称 | 关联对象 | 正文术语／相关关系 | 范围 | 优先级 | 正文状态 |
|---|---|---|---|---|---|---|
| <a id="R-FX-PARITY"></a>R-FX-PARITY | 利率平价 | [跨币种基差 C-FX-10](CONCEPT_IMPORT_LIST.md#C-FX-10) | [名义利率（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-IR-NOMINAL)；[名义汇率与实际汇率（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FX-06)；[利差与汇率对冲成本（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FX-08)；[远期汇率与掉期点（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FX-09) | 有担保/无担保条件分开 | P0 | pending／待制作 |
| <a id="R-USD-GLOBAL"></a>R-USD-GLOBAL | 美元融资依赖的传导机制 | [美元 C-FX-USD](CONCEPT_IMPORT_LIST.md#C-FX-USD)；[融资流动性 C-LIQ-FUND](../10_concepts/C-LIQ-FUND_funding_liquidity.md)；[跨币种基差 C-FX-10](CONCEPT_IMPORT_LIST.md#C-FX-10)；[信用利差 C-CREDIT-SPREAD](CONCEPT_IMPORT_LIST.md#C-CREDIT-SPREAD)；[股权风险溢价ERP C-EQ-ERP](CONCEPT_IMPORT_LIST.md#C-EQ-ERP) | — | 美元负债与收入币种错配、融资可得性及跨境资产定价；解释依赖如何形成并在融资收紧时传导。 | P0 | pending／待制作 |
| <a id="R-INTERNATIONAL-05"></a>R-INTERNATIONAL-05 | 美元互换额度对跨币种基差的影响 | [美元互换额度 C-MONEY-12](CONCEPT_IMPORT_LIST.md#C-MONEY-12)；[跨币种基差 C-FX-10](CONCEPT_IMPORT_LIST.md#C-FX-10)；[融资流动性 C-LIQ-FUND](../10_concepts/C-LIQ-FUND_funding_liquidity.md) | [商业银行资产负债表（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CREDIT-01)；相关关系：[美元融资依赖的传导机制 R-USD-GLOBAL](MECHANISM_IMPORT_LIST.md#R-USD-GLOBAL) | 流动性供给和机构约束 | P1 | pending／待制作 |
| <a id="R-JPY-CARRY"></a>R-JPY-CARRY | 日元套息交易的平仓反馈 | [日元 C-FX-03](CONCEPT_IMPORT_LIST.md#C-FX-03)；[套息交易 C-FX-17](CONCEPT_IMPORT_LIST.md#C-FX-17)；[隐含波动率与实现波动率 C-VOL-IVRV](CONCEPT_IMPORT_LIST.md#C-VOL-IVRV) | [利差与汇率对冲成本（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FX-08)；[杠杆与去杠杆（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CREDIT-LEVERAGE)；[价格冲击与市场容量（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-03) | 利差、汇率波动和杠杆 | P0 | pending／待制作 |
| <a id="R-INTERNATIONAL-07"></a>R-INTERNATIONAL-07 | 汇率对冲成本对跨境债券配置的影响 | [跨币种基差 C-FX-10](CONCEPT_IMPORT_LIST.md#C-FX-10)；[美国国债 C-ASSET-UST](CONCEPT_IMPORT_LIST.md#C-ASSET-UST)；[收益率曲线 C-IR-CURVE](CONCEPT_IMPORT_LIST.md#C-IR-CURVE) | [利差与汇率对冲成本（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FX-08)；[日本投资者海外资产配置（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-ASIA-13) | 对冲比例和负债币种 | P1 | pending／待制作 |
| <a id="R-INTERNATIONAL-09"></a>R-INTERNATIONAL-09 | 资本流出、储备干预与本币流动性 | [资本流动与资本管制 C-FX-13](CONCEPT_IMPORT_LIST.md#C-FX-13)；[外汇储备 C-FX-14](CONCEPT_IMPORT_LIST.md#C-FX-14)；[外汇干预 C-FX-18](CONCEPT_IMPORT_LIST.md#C-FX-18)；[银行准备金 C-MONEY-RESERVES](CONCEPT_IMPORT_LIST.md#C-MONEY-RESERVES) | [公开市场操作（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MONEY-06) | 是否冲销及资本管制 | P1 | pending／待制作 |
| <a id="R-INTERNATIONAL-12"></a>R-INTERNATIONAL-12 | 美元主导地位的形成与维持 | [美元 C-FX-USD](CONCEPT_IMPORT_LIST.md#C-FX-USD)；[国际支付与清算体系 C-GLOBAL-13](CONCEPT_IMPORT_LIST.md#C-GLOBAL-13)；[外汇储备 C-FX-14](CONCEPT_IMPORT_LIST.md#C-FX-14)；[美国国债 C-ASSET-UST](CONCEPT_IMPORT_LIST.md#C-ASSET-UST)；[美元互换额度 C-MONEY-12](CONCEPT_IMPORT_LIST.md#C-MONEY-12) | — | 支付、计价、融资与储备使用之间的联系，以及网络效应和路径依赖。 | P1 | pending／待制作 |
| <a id="R-INTERNATIONAL-13"></a>R-INTERNATIONAL-13 | 美元信用与储备多元化 | [美元 C-FX-USD](CONCEPT_IMPORT_LIST.md#C-FX-USD)；[外汇储备 C-FX-14](CONCEPT_IMPORT_LIST.md#C-FX-14)；[美国国债 C-ASSET-UST](CONCEPT_IMPORT_LIST.md#C-ASSET-UST)；[黄金 C-ASSET-GOLD](../10_concepts/C-ASSET-GOLD_gold.md)；[国际支付与清算体系 C-GLOBAL-13](CONCEPT_IMPORT_LIST.md#C-GLOBAL-13) | — | 美元信用、资产权利与储备配置变化；替代资产的流动性、收益和托管约束。 | P1 | pending／待制作 |
| <a id="R-INTERNATIONAL-14"></a>R-INTERNATIONAL-14 | 港元联系汇率与HIBOR传导 | [港元联系汇率 C-FX-05](CONCEPT_IMPORT_LIST.md#C-FX-05)；[资本流动与资本管制 C-FX-13](CONCEPT_IMPORT_LIST.md#C-FX-13)；[银行准备金 C-MONEY-RESERVES](CONCEPT_IMPORT_LIST.md#C-MONEY-RESERVES)；[政策利率与目标区间 C-IR-POLICY](../10_concepts/C-IR-POLICY_policy_rate_target_range.md)；[融资流动性 C-LIQ-FUND](../10_concepts/C-LIQ-FUND_funding_liquidity.md) | — | 资金流和货币发行局 | P1 | pending／待制作 |
| <a id="R-RMB-INTERNATIONALIZATION"></a>R-RMB-INTERNATIONALIZATION | 人民币国际化 | [人民币与离岸人民币 C-FX-02](CONCEPT_IMPORT_LIST.md#C-FX-02)；[资本流动与资本管制 C-FX-13](CONCEPT_IMPORT_LIST.md#C-FX-13)；[外汇储备 C-FX-14](CONCEPT_IMPORT_LIST.md#C-FX-14)；[国际支付与清算体系 C-GLOBAL-13](CONCEPT_IMPORT_LIST.md#C-GLOBAL-13)；[中国国债与政策性金融债 C-BOND-03](CONCEPT_IMPORT_LIST.md#C-BOND-03) | — | 人民币跨境结算、融资和储备使用的联系，以及支付渠道、资本流动制度与资产供给约束。 | P1 | pending／待制作 |

## 股票与公司定价机制

| ID | 关系名称 | 关联对象 | 正文术语／相关关系 | 范围 | 优先级 | 正文状态 |
|---|---|---|---|---|---|---|
| <a id="R-EQ-DIVIDEND"></a>R-EQ-DIVIDEND | 高股息资产的债券替代效应 | [红利资产与高股息指数 C-ASIA-05](CONCEPT_IMPORT_LIST.md#C-ASIA-05)；[投资级公司债 C-BOND-05](CONCEPT_IMPORT_LIST.md#C-BOND-05)；[保险资金与长期资金 C-ASIA-06](CONCEPT_IMPORT_LIST.md#C-ASIA-06) | [股息、分红率与回购（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EQUITY-08)；[名义利率（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-IR-NOMINAL) | 股息可持续性和利率 | P0 | pending／待制作 |
| <a id="R-EQUITY-14"></a>R-EQUITY-14 | 并购价差定价 | [并购交易与交易条款 C-EQUITY-18](CONCEPT_IMPORT_LIST.md#C-EQUITY-18) | [公司治理与控制权（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EQUITY-16)；[市场预期（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EXPECT-MARKET)；[名义利率（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-IR-NOMINAL)；[股票与股权索取权（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EQUITY-01) | 成交概率、期限与对价 | P1 | pending／待制作 |

## 资金流与市场微观结构

| ID | 关系名称 | 关联对象 | 正文术语／相关关系 | 范围 | 优先级 | 正文状态 |
|---|---|---|---|---|---|---|
| <a id="R-MARKET-04"></a>R-MARKET-04 | ETF申赎套利 | [ETF申赎与二级市场交易 C-FLOW-05](CONCEPT_IMPORT_LIST.md#C-FLOW-05)；[宽基ETF C-ASIA-04](CONCEPT_IMPORT_LIST.md#C-ASIA-04)；[融资流动性 C-LIQ-FUND](../10_concepts/C-LIQ-FUND_funding_liquidity.md) | [买卖价差与订单簿深度（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-01)；[价格冲击与市场容量（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-03) | 价差、篮子与执行成本 | P1 | pending／待制作 |
| <a id="R-MARKET-05"></a>R-MARKET-05 | 指数调整的被动资金效应 | [ETF申赎与二级市场交易 C-FLOW-05](CONCEPT_IMPORT_LIST.md#C-FLOW-05) | [股票指数与权重方法（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EQUITY-14)；[基金流量与资产配置（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-07)；[订单流失衡（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-02)；[价格冲击与市场容量（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-03) | 公告、实施和提前交易 | P1 | pending／待制作 |
| <a id="R-MARKET-07"></a>R-MARKET-07 | 波动率目标策略的顺周期反馈 | [风险平价与波动率目标 C-FLOW-12](CONCEPT_IMPORT_LIST.md#C-FLOW-12)；[隐含波动率与实现波动率 C-VOL-IVRV](CONCEPT_IMPORT_LIST.md#C-VOL-IVRV) | [杠杆与去杠杆（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CREDIT-LEVERAGE)；[订单流失衡（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-02)；[价格冲击与市场容量（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-03) | 目标波动、估计滞后和杠杆 | P1 | pending／待制作 |
| <a id="R-MARKET-08"></a>R-MARKET-08 | 风险平价与股债相关性变化 | [风险平价与波动率目标 C-FLOW-12](CONCEPT_IMPORT_LIST.md#C-FLOW-12)；[美国国债 C-ASSET-UST](CONCEPT_IMPORT_LIST.md#C-ASSET-UST)；[通货膨胀 C-INF-INFLATION](CONCEPT_IMPORT_LIST.md#C-INF-INFLATION)；[隐含波动率与实现波动率 C-VOL-IVRV](CONCEPT_IMPORT_LIST.md#C-VOL-IVRV) | [股票指数与权重方法（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EQUITY-14)；[总需求（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MACRO-05) | 风险预算与联合冲击 | P1 | pending／待制作 |
| <a id="R-MARKET-09"></a>R-MARKET-09 | CTA趋势跟随的价格反馈 | [趋势跟随与CTA C-FLOW-11](CONCEPT_IMPORT_LIST.md#C-FLOW-11) | [动量、反转与均值回归（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-13)；[杠杆与去杠杆（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CREDIT-LEVERAGE)；[价格冲击与市场容量（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-03)；[持仓拥挤与集中度（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-08) | 持仓、触发区间和市场容量 | P1 | pending／待制作 |
| <a id="R-MARKET-11"></a>R-MARKET-11 | 新闻传播、投资者注意力与价格延迟反应 | [投资者注意力 C-EXPECT-15](CONCEPT_IMPORT_LIST.md#C-EXPECT-15) | [信息集与可得时间（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EXPECT-INFO)；[市场情绪与新闻热度（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-16)；[预期修正（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EXPECT-09)；[动量、反转与均值回归（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-13) | 区分新增事实和重复传播的注意力效应，不把报道数量当作独立信息 | P1 | pending／待制作 |
| <a id="R-MARKET-13"></a>R-MARKET-13 | 涨跌停制度下的跨日价格发现 | [涨跌停、T+1与停复牌 C-ASIA-08](CONCEPT_IMPORT_LIST.md#C-ASIA-08) | [订单流失衡（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-02)；[买卖价差与订单簿深度（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-01)；[价格冲击与市场容量（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-03)；[预期差与意外成分（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EXPECT-SURPRISE) | 约束、排队和不可成交样本 | P1 | pending／待制作 |

## 衍生品与波动机制

| ID | 关系名称 | 关联对象 | 正文术语／相关关系 | 范围 | 优先级 | 正文状态 |
|---|---|---|---|---|---|---|
| <a id="R-DERIV-CARRY"></a>R-DERIV-CARRY | 现货期货持有成本定价 | [基差 C-DERIV-15](CONCEPT_IMPORT_LIST.md#C-DERIV-15) | [期货与远期（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-DERIV-01)；[名义利率（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-IR-NOMINAL)；[股息、分红率与回购（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EQUITY-08)；[便利收益与储存成本（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-COMMOD-11) | 融资、分红、储存与便利收益 | P0 | pending／待制作 |
| <a id="R-DERIVATIVES-02"></a>R-DERIVATIVES-02 | 基差交易 | [基差 C-DERIV-15](CONCEPT_IMPORT_LIST.md#C-DERIV-15)；[保证金与追加保证金 C-DERIV-14](CONCEPT_IMPORT_LIST.md#C-DERIV-14)；[抵押品与折扣率haircut C-CREDIT-10](CONCEPT_IMPORT_LIST.md#C-CREDIT-10)；[回购与逆回购 C-MONEY-10](CONCEPT_IMPORT_LIST.md#C-MONEY-10)；[融资流动性 C-LIQ-FUND](../10_concepts/C-LIQ-FUND_funding_liquidity.md) | — | 基差交易的现货与期货头寸、融资、抵押、保证金、收敛及退出过程。 | P1 | pending／待制作 |
| <a id="R-DERIVATIVES-03"></a>R-DERIVATIVES-03 | 做市商Gamma对冲的价格反馈 | [程序化交易与做市 C-FLOW-10](CONCEPT_IMPORT_LIST.md#C-FLOW-10) | [Delta与Gamma（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-DERIV-07)；[动态对冲与对冲误差（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-DERIV-17)；[订单流失衡（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-02)；[价格冲击与市场容量（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-03) | 净持仓符号与交易规则 | P1 | pending／待制作 |
| <a id="R-DERIVATIVES-06"></a>R-DERIVATIVES-06 | 波动率风险溢价与卖波收益风险 | [波动率风险溢价 C-DERIV-04](CONCEPT_IMPORT_LIST.md#C-DERIV-04)；[隐含波动率与实现波动率 C-VOL-IVRV](CONCEPT_IMPORT_LIST.md#C-VOL-IVRV)；[保证金与追加保证金 C-DERIV-14](CONCEPT_IMPORT_LIST.md#C-DERIV-14) | [隐含分布与尾部概率（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-DERIV-13)；[动态对冲与对冲误差（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-DERIV-17) | 尾部损失和交易成本 | P1 | pending／待制作 |
| <a id="R-DERIVATIVES-07"></a>R-DERIVATIVES-07 | 偏斜与尾部保险需求 | [隐含波动率与实现波动率 C-VOL-IVRV](CONCEPT_IMPORT_LIST.md#C-VOL-IVRV)；[波动率风险溢价 C-DERIV-04](CONCEPT_IMPORT_LIST.md#C-DERIV-04) | [偏斜skew与微笑smile（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-DERIV-06)；[隐含分布与尾部概率（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-DERIV-13)；[风险逆转与蝶式结构（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-DERIV-11)；[风险偏好与避险需求（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-14)；[持仓量与成交量（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-DERIV-16) | 供需、跳跃与持仓 | P1 | pending／待制作 |
| <a id="R-DERIVATIVES-10"></a>R-DERIVATIVES-10 | MBS负凸性引发的利率对冲反馈 | [机构MBS C-BOND-07](CONCEPT_IMPORT_LIST.md#C-BOND-07)；[收益率曲线 C-IR-CURVE](CONCEPT_IMPORT_LIST.md#C-IR-CURVE) | [凸性与负凸性（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-BOND-11)；[久期、修正久期与DV01（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-BOND-DURATION)；[动态对冲与对冲误差（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-DERIV-17) | 提前还款、久期和对冲方向 | P1 | pending／待制作 |

## 黄金与跨资产机制

| ID | 关系名称 | 关联对象 | 正文术语／相关关系 | 范围 | 优先级 | 正文状态 |
|---|---|---|---|---|---|---|
| <a id="R-GOLD-REALRATES"></a>R-GOLD-REALRATES | 黄金的机会成本机制 | [实际利率 C-IR-REAL](../10_concepts/C-IR-REAL_real_interest_rate.md)；[黄金 C-ASSET-GOLD](../10_concepts/C-ASSET-GOLD_gold.md)；[政策利率与目标区间 C-IR-POLICY](../10_concepts/C-IR-POLICY_policy_rate_target_range.md) | [名义利率（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-IR-NOMINAL)；[通胀预期（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-INF-EXPECT)；[风险偏好与避险需求（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-14)；[黄金ETF持仓与流量（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-GOLDETF)；相关关系：[美元信用与储备多元化 R-INTERNATIONAL-13](MECHANISM_IMPORT_LIST.md#R-INTERNATIONAL-13) | 以同期限实际回报为主线，区分美元、需求与流动性带来的共同冲击 | P0 | complete／[正文](../20_mechanisms/R-GOLD-REALRATES_real_rates_gold.md) |
| <a id="R-GOLD-03"></a>R-GOLD-03 | 央行购金与黄金需求结构 | [外汇储备 C-FX-14](CONCEPT_IMPORT_LIST.md#C-FX-14)；[黄金 C-ASSET-GOLD](../10_concepts/C-ASSET-GOLD_gold.md) | [央行与储备管理者（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-ACTOR-CB)；相关关系：[美元信用与储备多元化 R-INTERNATIONAL-13](MECHANISM_IMPORT_LIST.md#R-INTERNATIONAL-13) | 储备目标、披露与估计 | P1 | pending／待制作 |
| <a id="R-ASSET-STOCKBOND"></a>R-ASSET-STOCKBOND | 股债相关性与通胀/增长主导状态 | [美国国债 C-ASSET-UST](CONCEPT_IMPORT_LIST.md#C-ASSET-UST)；[通货膨胀 C-INF-INFLATION](CONCEPT_IMPORT_LIST.md#C-INF-INFLATION)；[期限溢价 C-IR-TERM](../10_concepts/C-IR-TERM_term_premium.md) | [股票指数与权重方法（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EQUITY-14)；[总需求（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MACRO-05)；[政策反应函数（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-POL-REACTION) | 冲击类型和政策反应 | P0 | pending／待制作 |

## 能源与商品机制

| ID | 关系名称 | 关联对象 | 正文术语／相关关系 | 范围 | 优先级 | 正文状态 |
|---|---|---|---|---|---|---|
| <a id="R-OIL-SHOCK"></a>R-OIL-SHOCK | 原油供给冲击的宏观传导 | [原油与Brent/WTI C-COMMOD-03](CONCEPT_IMPORT_LIST.md#C-COMMOD-03)；[OPEC与闲置产能 C-COMMOD-13](CONCEPT_IMPORT_LIST.md#C-COMMOD-13)；[通货膨胀 C-INF-INFLATION](CONCEPT_IMPORT_LIST.md#C-INF-INFLATION) | [商品库存与库存消费比（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-COMMOD-10)；[家庭消费（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MACRO-06) | 库存和需求弹性 | P0 | pending／待制作 |
| <a id="R-COMMODITY-03"></a>R-COMMODITY-03 | 库存与便利收益、期货曲线 | [原油与Brent/WTI C-COMMOD-03](CONCEPT_IMPORT_LIST.md#C-COMMOD-03)；[天然气与LNG C-COMMOD-04](CONCEPT_IMPORT_LIST.md#C-COMMOD-04)；[铜与工业金属 C-COMMOD-06](CONCEPT_IMPORT_LIST.md#C-COMMOD-06)；[农产品 C-COMMOD-09](CONCEPT_IMPORT_LIST.md#C-COMMOD-09) | [商品库存与库存消费比（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-COMMOD-10)；[便利收益与储存成本（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-COMMOD-11)；[升水、贴水与期货曲线（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-COMMOD-12)；[期货与远期（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-DERIV-01) | 交割地和可用库存 | P1 | pending／待制作 |
| <a id="R-COMMODITY-08"></a>R-COMMODITY-08 | 矿业投资与供给的周期反馈 | [铜与工业金属 C-COMMOD-06](CONCEPT_IMPORT_LIST.md#C-COMMOD-06) | [矿业资本开支与供给弹性（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-COMMOD-15)；[企业投资与资本开支（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MACRO-08)；[商品库存与库存消费比（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-COMMOD-10)；[盈利、收入与利润率（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EQ-EARNINGS) | 建设时滞、品位和需求 | P1 | pending／待制作 |

## 中国信用、地产与财政传导

| ID | 关系名称 | 关联对象 | 正文术语／相关关系 | 范围 | 优先级 | 正文状态 |
|---|---|---|---|---|---|---|
| <a id="R-CHINA-01"></a>R-CHINA-01 | 降准的资金与信贷传导 | [存款准备金率与降准 C-CHINA-06](CONCEPT_IMPORT_LIST.md#C-CHINA-06)；[银行准备金 C-MONEY-RESERVES](CONCEPT_IMPORT_LIST.md#C-MONEY-RESERVES)；[人民币贷款与票据融资 C-CHINA-05](CONCEPT_IMPORT_LIST.md#C-CHINA-05)；[DR007、R007与同业存单 C-CHINA-09](CONCEPT_IMPORT_LIST.md#C-CHINA-09) | [贷款标准与贷款需求（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CREDIT-05) | 银行约束和贷款需求 | P1 | pending／待制作 |
| <a id="R-CHINA-02"></a>R-CHINA-02 | 政策利率的LPR传导渠道 | [MLF、逆回购与结构性工具 C-CHINA-07](CONCEPT_IMPORT_LIST.md#C-CHINA-07)；[LPR与贷款定价 C-CHINA-08](CONCEPT_IMPORT_LIST.md#C-CHINA-08)；[DR007、R007与同业存单 C-CHINA-09](CONCEPT_IMPORT_LIST.md#C-CHINA-09)；[净息差NIM C-CREDIT-04](CONCEPT_IMPORT_LIST.md#C-CREDIT-04)；[人民币贷款与票据融资 C-CHINA-05](CONCEPT_IMPORT_LIST.md#C-CHINA-05) | — | 银行负债成本和信用分层 | P1 | pending／待制作 |
| <a id="R-CN-CREDIT"></a>R-CN-CREDIT | 社融结构、信用脉冲与实体需求 | [社会融资规模 C-CN-TSF](CONCEPT_IMPORT_LIST.md#C-CN-TSF)；[人民币贷款与票据融资 C-CHINA-05](CONCEPT_IMPORT_LIST.md#C-CHINA-05)；[地方政府债 C-BOND-04](CONCEPT_IMPORT_LIST.md#C-BOND-04) | [信用脉冲（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CHINA-04)；[企业投资与资本开支（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MACRO-08)；[家庭消费（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MACRO-06) | 政府/企业/居民分项 | P0 | pending／待制作 |
| <a id="R-CN-PROPERTY"></a>R-CN-PROPERTY | 房地产开发的现金流循环 | [房地产预售与保交楼 C-CHINA-14](CONCEPT_IMPORT_LIST.md#C-CHINA-14)；[房地产融资与住房按揭 C-CHINA-15](CONCEPT_IMPORT_LIST.md#C-CHINA-15)；[房地产开发与物业 C-SECTOR-06](CONCEPT_IMPORT_LIST.md#C-SECTOR-06) | [地产销售、库存与土地购置（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CHINA-16)；[经营现金流、资本开支与自由现金流（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EQUITY-04) | 预售、融资和交付 | P0 | pending／待制作 |
| <a id="R-CHINA-05"></a>R-CHINA-05 | 土地财政的基建融资机制 | [土地财政 C-CHINA-11](CONCEPT_IMPORT_LIST.md#C-CHINA-11)；[财政部与地方财政 C-CHINA-02](CONCEPT_IMPORT_LIST.md#C-CHINA-02) | [地产销售、库存与土地购置（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CHINA-16)；[建筑、建材与基建（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-SECTOR-07)；[预算、拨款与执行（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FISCAL-16) | 资金来源与项目执行 | P1 | pending／待制作 |
| <a id="R-CHINA-06"></a>R-CHINA-06 | 地方化债的资产负债表传导 | [地方债务置换与化债 C-CHINA-13](CONCEPT_IMPORT_LIST.md#C-CHINA-13)；[地方融资平台LGFV C-CHINA-12](CONCEPT_IMPORT_LIST.md#C-CHINA-12)；[地方政府债 C-BOND-04](CONCEPT_IMPORT_LIST.md#C-BOND-04) | [不良贷款与拨备（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CREDIT-14)；[建筑、建材与基建（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-SECTOR-07)；[经营现金流、资本开支与自由现金流（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EQUITY-04) | 债务置换和新增融资分开 | P1 | pending／待制作 |
| <a id="R-CHINA-12"></a>R-CHINA-12 | 存款迁移的债市传导 | [挤兑与存款迁移 C-CREDIT-15](CONCEPT_IMPORT_LIST.md#C-CREDIT-15)；[证券与资管业 C-SECTOR-03](CONCEPT_IMPORT_LIST.md#C-SECTOR-03)；[中国国债与政策性金融债 C-BOND-03](CONCEPT_IMPORT_LIST.md#C-BOND-03)；[DR007、R007与同业存单 C-CHINA-09](CONCEPT_IMPORT_LIST.md#C-CHINA-09) | [广义货币与存款（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MONEY-03)；[基金流量与资产配置（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-07) | 存款利率、理财和风险偏好 | P1 | pending／待制作 |

## 中国资产与政策机制

| ID | 关系名称 | 关联对象 | 正文术语／相关关系 | 范围 | 优先级 | 正文状态 |
|---|---|---|---|---|---|---|
| <a id="R-CHINA_MARKET-07"></a>R-CHINA_MARKET-07 | A/H溢价的市场分割机制 | [A/H溢价 C-ASIA-10](CONCEPT_IMPORT_LIST.md#C-ASIA-10)；[A股市场 C-ASIA-01](CONCEPT_IMPORT_LIST.md#C-ASIA-01)；[港股市场 C-ASIA-02](CONCEPT_IMPORT_LIST.md#C-ASIA-02)；[沪深港通与南北向资金 C-ASIA-03](CONCEPT_IMPORT_LIST.md#C-ASIA-03)；[人民币与离岸人民币 C-FX-02](CONCEPT_IMPORT_LIST.md#C-FX-02)；[港元联系汇率 C-FX-05](CONCEPT_IMPORT_LIST.md#C-FX-05) | — | 汇率、投资者和交易约束 | P1 | pending／待制作 |

## 科技与AI产业机制

| ID | 关系名称 | 关联对象 | 正文术语／相关关系 | 范围 | 优先级 | 正文状态 |
|---|---|---|---|---|---|---|
| <a id="R-TECH-03"></a>R-TECH-03 | 模型效率、推理成本与总算力需求 | [人工智能算力 C-TECH-01](CONCEPT_IMPORT_LIST.md#C-TECH-01)；[云服务与超大规模云厂商 C-TECH-03](CONCEPT_IMPORT_LIST.md#C-TECH-03)；[GPU与AI加速器 C-TECH-02](CONCEPT_IMPORT_LIST.md#C-TECH-02) | [AI模型能力与推理成本（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-TECH-12)；[AI应用收入与商业化（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-TECH-13) | 单位成本下降和需求弹性 | P1 | pending／待制作 |
| <a id="R-TECH-12"></a>R-TECH-12 | 平台网络效应 | [云服务与超大规模云厂商 C-TECH-03](CONCEPT_IMPORT_LIST.md#C-TECH-03) | [平台竞争与网络效应（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-TECH-16)；[AI应用收入与商业化（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-TECH-13)；[盈利、收入与利润率（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EQ-EARNINGS)；[估值倍数PE/PB/EV-EBITDA（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EQUITY-06) | 切换成本、开放生态与监管 | P1 | pending／待制作 |

## 政治、制度与长期变化

| ID | 关系名称 | 关联对象 | 正文术语／相关关系 | 范围 | 优先级 | 正文状态 |
|---|---|---|---|---|---|---|
| <a id="R-GEOPOLITICS-02"></a>R-GEOPOLITICS-02 | 关税的跨境成本分担 | [通货膨胀 C-INF-INFLATION](CONCEPT_IMPORT_LIST.md#C-INF-INFLATION)；[美元 C-FX-USD](CONCEPT_IMPORT_LIST.md#C-FX-USD)；[人民币与离岸人民币 C-FX-02](CONCEPT_IMPORT_LIST.md#C-FX-02) | [关税、配额与贸易壁垒（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-GLOBAL-08)；[生产者价格指数PPI（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-INFLATION-05)；[盈利、收入与利润率（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-EQ-EARNINGS)；[名义汇率与实际汇率（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FX-06)；[贸易余额与净出口（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MACRO-15) | 成本分担、替代和报复 | P1 | pending／待制作 |
| <a id="R-GEOPOLITICS-07"></a>R-GEOPOLITICS-07 | 养老金资产配置的人口结构约束 | [养老金与退休负债 C-SECTOR-13](CONCEPT_IMPORT_LIST.md#C-SECTOR-13) | [人口与劳动供给（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MACRO-14)；[久期、修正久期与DV01（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-BOND-DURATION)；[基金流量与资产配置（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FLOW-07)；[储蓄率（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MACRO-07) | 缴费、支付和负债期限 | P1 | pending／待制作 |

## 数字资产传导

| ID | 关系名称 | 关联对象 | 正文术语／相关关系 | 范围 | 优先级 | 正文状态 |
|---|---|---|---|---|---|---|
| <a id="R-CRYPTO-02"></a>R-CRYPTO-02 | 稳定币发行赎回对短券需求的影响 | [稳定币 C-CRYPTO-03](CONCEPT_IMPORT_LIST.md#C-CRYPTO-03)；[美国国债 C-ASSET-UST](CONCEPT_IMPORT_LIST.md#C-ASSET-UST)；[货币市场基金 C-MONEY-19](CONCEPT_IMPORT_LIST.md#C-MONEY-19) | [广义货币与存款（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-MONEY-03)；[国债总发行与净发行（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-FISCAL-07) | 储备结构和资金来源 | P1 | pending／待制作 |
| <a id="R-CRYPTO-04"></a>R-CRYPTO-04 | 永续合约的强平瀑布 | [加密资产杠杆与永续合约 C-CRYPTO-05](CONCEPT_IMPORT_LIST.md#C-CRYPTO-05)；[保证金与追加保证金 C-DERIV-14](CONCEPT_IMPORT_LIST.md#C-DERIV-14)；[市场流动性 C-LIQ-MARKET](CONCEPT_IMPORT_LIST.md#C-LIQ-MARKET)；[比特币 C-CRYPTO-01](CONCEPT_IMPORT_LIST.md#C-CRYPTO-01) | [杠杆与去杠杆（正文术语）](CONCEPT_CONTEXT_TERMS.md#C-CREDIT-LEVERAGE) | 资金费率、保证金和深度 | P1 | pending／待制作 |
