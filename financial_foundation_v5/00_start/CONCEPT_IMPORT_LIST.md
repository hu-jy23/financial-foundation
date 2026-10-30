# 金融概念／对象正式目录 v5

初步建图范围确认：2026-10-25。共 **163 个对象，18 个主题组**；正文 **132 份已完成、31 份待完成主审**（进度更新：2026-10-30）。

本表与[关系／机制正式目录](MECHANISM_IMPORT_LIST.md)共同构成初步建图的234个节点。条目已经入选，pending表示正文尚未完成主审（包括未制作或已有待审稿）。

原349项的去向见[审阅表](../50_reviews/CONCEPT_SELECTION_349.md)；[正文术语与旧ID登记](CONCEPT_CONTEXT_TERMS.md)用于追溯，不进入制作队列。

对象范围沿用用户确认的163项。后续按[制作标准](AUTHORING_STANDARD.md)展开内容，使用[JSON索引](catalog_index.json)读取ID、名称和正文状态。

正文文件名使用定稿标题；ID保留在元数据及本表中，全部计划路径见索引的`planned_path`。规则见[文件命名](FILE_NAMING.md)。

| 主题组 | 条目 | P0 | 成品 | 待完成主审 |
|---|---:|---:|---:|---:|
| 预期、信息与认知 | 3 | 1 | 3 | 0 |
| 物价、工资与就业 | 1 | 1 | 1 | 0 |
| 利率与收益率曲线 | 8 | 4 | 8 | 0 |
| 货币、央行与流动性 | 13 | 6 | 13 | 0 |
| 财政、政府债务与主权信用 | 4 | 1 | 4 | 0 |
| 银行、信用与金融稳定 | 10 | 1 | 10 | 0 |
| 外汇与国际金融 | 11 | 1 | 11 | 0 |
| 债券与固定收益工具 | 10 | 2 | 10 | 0 |
| 股票、估值与公司财务 | 2 | 1 | 2 | 0 |
| 衍生品、波动与对冲 | 4 | 1 | 4 | 0 |
| 交易结构、资金与行为 | 5 | 0 | 5 | 0 |
| 黄金、能源与大宗商品 | 12 | 1 | 12 | 0 |
| 中国宏观制度与政策工具 | 16 | 1 | 16 | 0 |
| A股、港股与区域市场制度 | 12 | 0 | 11 | 1 |
| 国际制度、政治与地缘 | 8 | 0 | 7 | 1 |
| AI、科技与产业链 | 29 | 0 | 15 | 14 |
| 行业与经营暴露 | 7 | 0 | 0 | 7 |
| 数字资产与新型金融 | 8 | 0 | 0 | 8 |

## 预期、信息与认知

| ID | 名称 | 对象边界 | 优先级 | 正文状态 |
|---|---|---|---|---|
| <a id="C-EXPECT-05"></a>C-EXPECT-05 | 主观概率与风险中性概率 | 不同测度与使用范围 | P1 | complete／[正文](../10_concepts/主观概率与风险中性概率.md) |
| <a id="C-POL-CREDIBILITY"></a>C-POL-CREDIBILITY | 央行可信度 | 承诺、行动与市场相信程度 | P0 | complete／[正文](../10_concepts/央行可信度.md) |
| <a id="C-EXPECT-15"></a>C-EXPECT-15 | 投资者注意力 | 关注稀缺与信息覆盖 | P1 | complete／[正文](../10_concepts/投资者注意力.md) |

## 物价、工资与就业

| ID | 名称 | 对象边界 | 优先级 | 正文状态 |
|---|---|---|---|---|
| <a id="C-INF-INFLATION"></a>C-INF-INFLATION | 通货膨胀 | 价格总体水平变化 | P0 | complete／[正文](../10_concepts/通货膨胀.md) |

## 利率与收益率曲线

| ID | 名称 | 对象边界 | 优先级 | 正文状态 |
|---|---|---|---|---|
| <a id="C-IR-REAL"></a>C-IR-REAL | 实际利率 | 事前/事后及TIPS代理 | P0 | complete／[正文](../10_concepts/实际利率.md) |
| <a id="C-IR-POLICY"></a>C-IR-POLICY | 政策利率与目标区间 | 央行设定及执行口径 | P0 | complete／[正文](../10_concepts/政策利率与目标区间.md) |
| <a id="C-RATE-05"></a>C-RATE-05 | 有效联邦基金利率EFFR | 美国实际隔夜无担保市场利率 | P1 | complete／[正文](../10_concepts/有效联邦基金利率EFFR.md) |
| <a id="C-RATE-06"></a>C-RATE-06 | SOFR与担保融资基准 | 担保隔夜资金价格 | P1 | complete／[正文](../10_concepts/SOFR与担保融资基准.md) |
| <a id="C-RATE-07"></a>C-RATE-07 | 隔夜指数掉期OIS | 浮动隔夜复利与固定利率互换 | P1 | complete／[正文](../10_concepts/隔夜指数掉期OIS.md) |
| <a id="C-RATE-08"></a>C-RATE-08 | 联邦基金期货 | 合约结算与政策预期代理 | P1 | complete／[正文](../10_concepts/联邦基金期货.md) |
| <a id="C-IR-CURVE"></a>C-IR-CURVE | 收益率曲线 | 期限、券种与拟合 | P0 | complete／[正文](../10_concepts/收益率曲线.md) |
| <a id="C-IR-TERM"></a>C-IR-TERM | 期限溢价 | 长期持有相对滚动短债的风险定价 | P0 | complete／[正文](../10_concepts/期限溢价.md) |

## 货币、央行与流动性

| ID | 名称 | 对象边界 | 优先级 | 正文状态 |
|---|---|---|---|---|
| <a id="C-MONEY-RESERVES"></a>C-MONEY-RESERVES | 银行准备金 | 央行账户余额与可用性 | P0 | complete／[正文](../10_concepts/银行准备金.md) |
| <a id="C-MONEY-CBBS"></a>C-MONEY-CBBS | 央行资产负债表 | 资产、准备金、现金与其他负债 | P0 | complete／[正文](../10_concepts/央行资产负债表.md) |
| <a id="C-MONEY-07"></a>C-MONEY-07 | 准备金利率 | 央行对准备金支付或收取的利率及其适用制度；利率走廊的传导另见机制。 机制部分：[利率走廊 R-MONETARY-07](../20_mechanisms/利率走廊.md) | P1 | complete／[正文](../10_concepts/准备金利率.md) |
| <a id="C-POL-QE"></a>C-POL-QE | 量化宽松QE | 资产购买与久期配置 | P0 | complete／[正文](../10_concepts/量化宽松QE.md) |
| <a id="C-POL-QT"></a>C-POL-QT | 量化紧缩QT | 到期不续作/出售与负债调整 | P0 | complete／[正文](../10_concepts/量化紧缩QT.md) |
| <a id="C-MONEY-10"></a>C-MONEY-10 | 回购与逆回购 | 融资方向、抵押品与对手方 | P1 | complete／[正文](../10_concepts/回购与逆回购.md) |
| <a id="C-MONEY-11"></a>C-MONEY-11 | 常备工具与最后贷款人 | 准入、抵押品和支持条件 | P1 | complete／[正文](../10_concepts/常备工具与最后贷款人.md) |
| <a id="C-MONEY-12"></a>C-MONEY-12 | 美元互换额度 | 央行之间的美元流动性安排 | P1 | complete／[正文](../10_concepts/美元互换额度.md) |
| <a id="C-MONEY-13"></a>C-MONEY-13 | 财政部一般账户TGA | 财政现金余额与准备金关系 | P1 | complete／[正文](../10_concepts/财政部一般账户TGA.md) |
| <a id="C-MONEY-14"></a>C-MONEY-14 | 隔夜逆回购ONRRP | 特定美国央行负债工具 | P1 | complete／[正文](../10_concepts/隔夜逆回购ONRRP.md) |
| <a id="C-LIQ-FUND"></a>C-LIQ-FUND | 融资流动性 | 融资成本、额度和抵押约束 | P0 | complete／[正文](../10_concepts/融资流动性.md) |
| <a id="C-LIQ-MARKET"></a>C-LIQ-MARKET | 市场流动性 | 价差、深度、冲击成本 | P0 | complete／[正文](../10_concepts/市场流动性.md) |
| <a id="C-MONEY-19"></a>C-MONEY-19 | 货币市场基金 | 短券、回购与央行工具配置；区分政府型、优质型及各国制度 | P1 | complete／[正文](../10_concepts/货币市场基金.md) |

## 财政、政府债务与主权信用

| ID | 名称 | 对象边界 | 优先级 | 正文状态 |
|---|---|---|---|---|
| <a id="C-FISCAL-DEFICIT"></a>C-FISCAL-DEFICIT | 财政赤字与初级赤字 | 是否包含利息支出 | P0 | complete／[正文](../10_concepts/财政赤字与初级赤字.md) |
| <a id="C-FISCAL-13"></a>C-FISCAL-13 | 财政主导 | 财政约束对货币政策的影响 | P1 | complete／[正文](../10_concepts/财政主导.md) |
| <a id="C-FISCAL-14"></a>C-FISCAL-14 | 主权信用风险与CDS | 违约、回收和交易定价 | P1 | complete／[正文](../10_concepts/主权信用风险与CDS.md) |
| <a id="C-FISCAL-15"></a>C-FISCAL-15 | 债务上限与政府停摆 | 美国两类不同制度事件 | P1 | complete／[正文](../10_concepts/债务上限与政府停摆.md) |

## 银行、信用与金融稳定

| ID | 名称 | 对象边界 | 优先级 | 正文状态 |
|---|---|---|---|---|
| <a id="C-CREDIT-02"></a>C-CREDIT-02 | 银行资本与杠杆率 | 损失吸收与监管约束 | P1 | complete／[正文](../10_concepts/银行资本与杠杆率.md) |
| <a id="C-CREDIT-03"></a>C-CREDIT-03 | 银行流动性覆盖与稳定融资 | 期限错配约束 | P1 | complete／[正文](../10_concepts/银行流动性覆盖与稳定融资.md) |
| <a id="C-CREDIT-04"></a>C-CREDIT-04 | 净息差NIM | 资产收益与负债成本 | P1 | complete／[正文](../10_concepts/净息差NIM.md) |
| <a id="C-CREDIT-SPREAD"></a>C-CREDIT-SPREAD | 信用利差 | 无风险曲线外的补偿 | P0 | complete／[正文](../10_concepts/信用利差.md) |
| <a id="C-CREDIT-08"></a>C-CREDIT-08 | 信用评级与迁移 | 评级行动和滞后 | P1 | complete／[正文](../10_concepts/信用评级与迁移.md) |
| <a id="C-CREDIT-10"></a>C-CREDIT-10 | 抵押品与折扣率haircut | 借款能力与风险控制 | P1 | complete／[正文](../10_concepts/抵押品与折扣率haircut.md) |
| <a id="C-CREDIT-12"></a>C-CREDIT-12 | 影子银行与非银金融 | 中介功能与监管边界 | P1 | complete／[正文](../10_concepts/影子银行与非银金融.md) |
| <a id="C-CREDIT-13"></a>C-CREDIT-13 | 证券化与资产支持证券 | 现金流分层与风险转移 | P1 | complete／[正文](../10_concepts/证券化与资产支持证券.md) |
| <a id="C-CREDIT-15"></a>C-CREDIT-15 | 挤兑与存款迁移 | 信心、保险与数字化速度 | P1 | complete／[正文](../10_concepts/挤兑与存款迁移.md) |
| <a id="C-CREDIT-16"></a>C-CREDIT-16 | 金融周期 | 金融运行状态、周期阶段和历史；信用、杠杆和资产价格反馈及系统性风险另见机制。 机制部分：[金融周期中的系统性风险积累与扩散 R-BANKING-12](../20_mechanisms/金融周期中的系统性风险积累与扩散.md) | P1 | complete／[正文](../10_concepts/金融周期.md) |

## 外汇与国际金融

| ID | 名称 | 对象边界 | 优先级 | 正文状态 |
|---|---|---|---|---|
| <a id="C-FX-USD"></a>C-FX-USD | 美元 | 计价、支付、融资和储备货币角色 | P0 | complete／[正文](../10_concepts/美元.md) |
| <a id="C-FX-02"></a>C-FX-02 | 人民币与离岸人民币 | CNY/CNH市场与制度边界 | P1 | complete／[正文](../10_concepts/人民币与离岸人民币.md) |
| <a id="C-FX-03"></a>C-FX-03 | 日元 | 融资与国际资产配置角色 | P1 | complete／[正文](../10_concepts/日元.md) |
| <a id="C-FX-04"></a>C-FX-04 | 欧元与欧元体系 | 共同货币和分散财政 | P1 | complete／[正文](../10_concepts/欧元与欧元体系.md) |
| <a id="C-FX-05"></a>C-FX-05 | 港元联系汇率 | 货币发行与利率传导制度 | P1 | complete／[正文](../10_concepts/港元联系汇率.md) |
| <a id="C-FX-07"></a>C-FX-07 | 美元指数DXY与广义美元指数 | 成分权重不同 | P1 | complete／[正文](../10_concepts/美元指数DXY与广义美元指数.md) |
| <a id="C-FX-10"></a>C-FX-10 | 跨币种基差 | 有担保利率平价偏离 | P1 | complete／[正文](../10_concepts/跨币种基差.md) |
| <a id="C-FX-13"></a>C-FX-13 | 资本流动与资本管制 | 流量、方向、主体与规则 | P1 | complete／[正文](../10_concepts/资本流动与资本管制.md) |
| <a id="C-FX-14"></a>C-FX-14 | 外汇储备 | 币种、流动性与估值变化 | P1 | complete／[正文](../10_concepts/外汇储备.md) |
| <a id="C-FX-17"></a>C-FX-17 | 套息交易 | 融资币、投资币、杠杆和对冲 | P1 | complete／[正文](../10_concepts/套息交易.md) |
| <a id="C-FX-18"></a>C-FX-18 | 外汇干预 | 数量、冲销和信号渠道 | P1 | complete／[正文](../10_concepts/外汇干预.md) |

## 债券与固定收益工具

| ID | 名称 | 对象边界 | 优先级 | 正文状态 |
|---|---|---|---|---|
| <a id="C-ASSET-UST"></a>C-ASSET-UST | 美国国债 | 财政部信用、期限与市场结构 | P0 | complete／[正文](../10_concepts/美国国债.md) |
| <a id="C-IR-TIPS"></a>C-IR-TIPS | 美国通胀保值国债TIPS | 指数化本金与实际收益率 | P0 | complete／[正文](../10_concepts/美国通胀保值国债TIPS.md) |
| <a id="C-BOND-03"></a>C-BOND-03 | 中国国债与政策性金融债 | 信用、税务与交易群体 | P1 | complete／[正文](../10_concepts/中国国债与政策性金融债.md) |
| <a id="C-BOND-04"></a>C-BOND-04 | 地方政府债 | 一般债、专项债及偿债来源 | P1 | complete／[正文](../10_concepts/地方政府债.md) |
| <a id="C-BOND-05"></a>C-BOND-05 | 投资级公司债 | 信用与久期共同暴露 | P1 | complete／[正文](../10_concepts/投资级公司债.md) |
| <a id="C-BOND-06"></a>C-BOND-06 | 高收益债 | 违约风险与流动性 | P1 | complete／[正文](../10_concepts/高收益债.md) |
| <a id="C-BOND-07"></a>C-BOND-07 | 机构MBS | 提前还款与利率风险 | P1 | complete／[正文](../10_concepts/机构MBS.md) |
| <a id="C-BOND-08"></a>C-BOND-08 | 浮息债FRN | 重置基准与利差 | P1 | complete／[正文](../10_concepts/浮息债FRN.md) |
| <a id="C-BOND-09"></a>C-BOND-09 | 可转债 | 债底、转股价值与条款 | P1 | complete／[正文](../10_concepts/可转债.md) |
| <a id="C-BOND-14"></a>C-BOND-14 | 拍卖、投标倍数与尾差 | 发行定价与需求指标 | P1 | complete／[正文](../10_concepts/拍卖、投标倍数与尾差.md) |

## 股票、估值与公司财务

| ID | 名称 | 对象边界 | 优先级 | 正文状态 |
|---|---|---|---|---|
| <a id="C-EQ-ERP"></a>C-EQ-ERP | 股权风险溢价ERP | 预期回报超额补偿 | P0 | complete／[正文](../10_concepts/股权风险溢价ERP.md) |
| <a id="C-EQUITY-18"></a>C-EQUITY-18 | 并购交易与交易条款 | 现金或换股对价、交割条件、终止条款和审批程序 | P1 | complete／[正文](../10_concepts/并购交易与交易条款.md) |

## 衍生品、波动与对冲

| ID | 名称 | 对象边界 | 优先级 | 正文状态 |
|---|---|---|---|---|
| <a id="C-VOL-IVRV"></a>C-VOL-IVRV | 隐含波动率与实现波动率 | 定价参数和统计量 | P0 | complete／[正文](../10_concepts/隐含波动率与实现波动率.md) |
| <a id="C-DERIV-04"></a>C-DERIV-04 | 波动率风险溢价 | 测度、期限与收益标签 | P1 | complete／[正文](../10_concepts/波动率风险溢价.md) |
| <a id="C-DERIV-14"></a>C-DERIV-14 | 保证金与追加保证金 | 融资约束和路径风险 | P1 | complete／[正文](../10_concepts/保证金与追加保证金.md) |
| <a id="C-DERIV-15"></a>C-DERIV-15 | 基差 | 现货与期货等相关价格之间的差额；报价口径、观测和历史；交易头寸与融资过程另见机制。 机制部分：[基差交易 R-DERIVATIVES-02](../20_mechanisms/基差交易.md) | P1 | complete／[正文](../10_concepts/基差.md) |

## 交易结构、资金与行为

| ID | 名称 | 对象边界 | 优先级 | 正文状态 |
|---|---|---|---|---|
| <a id="C-FLOW-05"></a>C-FLOW-05 | ETF申赎与二级市场交易 | 份额变化和成交额区别 | P1 | complete／[正文](../10_concepts/ETF申赎与二级市场交易.md) |
| <a id="C-FLOW-09"></a>C-FLOW-09 | 融资融券与借券成本 | 杠杆、多空实施约束 | P1 | complete／[正文](../10_concepts/融资融券与借券成本.md) |
| <a id="C-FLOW-10"></a>C-FLOW-10 | 程序化交易与做市 | 策略类型和库存管理 | P1 | complete／[正文](../10_concepts/程序化交易与做市.md) |
| <a id="C-FLOW-11"></a>C-FLOW-11 | 趋势跟随与CTA | 信号规则、杠杆和市场暴露 | P1 | complete／[正文](../10_concepts/趋势跟随与CTA.md) |
| <a id="C-FLOW-12"></a>C-FLOW-12 | 风险平价与波动率目标 | 风险预算与再平衡 | P1 | complete／[正文](../10_concepts/风险平价与波动率目标.md) |

## 黄金、能源与大宗商品

| ID | 名称 | 对象边界 | 优先级 | 正文状态 |
|---|---|---|---|---|
| <a id="C-ASSET-GOLD"></a>C-ASSET-GOLD | 黄金 | 商品、储备与投资属性 | P0 | complete／[正文](../10_concepts/黄金.md) |
| <a id="C-COMMOD-02"></a>C-COMMOD-02 | 白银与贵金属 | 工业与投资需求权重 | P1 | complete／[正文](../10_concepts/白银与贵金属.md) |
| <a id="C-COMMOD-03"></a>C-COMMOD-03 | 原油与Brent/WTI | 品质、交割地与基准 | P1 | complete／[正文](../10_concepts/原油与Brent／WTI.md) |
| <a id="C-COMMOD-04"></a>C-COMMOD-04 | 天然气与LNG | 区域市场、运输和季节 | P1 | complete／[正文](../10_concepts/天然气与LNG.md) |
| <a id="C-COMMOD-05"></a>C-COMMOD-05 | 煤炭与焦煤 | 能源和冶金需求区别 | P1 | complete／[正文](../10_concepts/煤炭与焦煤.md) |
| <a id="C-COMMOD-06"></a>C-COMMOD-06 | 铜与工业金属 | 终端需求、库存和供给 | P1 | complete／[正文](../10_concepts/铜与工业金属.md) |
| <a id="C-COMMOD-07"></a>C-COMMOD-07 | 铝与电力成本 | 能耗、冶炼和供给约束 | P1 | complete／[正文](../10_concepts/铝与电力成本.md) |
| <a id="C-COMMOD-08"></a>C-COMMOD-08 | 铁矿石与钢铁 | 地产基建、产量和库存 | P1 | complete／[正文](../10_concepts/铁矿石与钢铁.md) |
| <a id="C-COMMOD-09"></a>C-COMMOD-09 | 农产品 | 天气、种植、库存与贸易 | P1 | complete／[正文](../10_concepts/农产品.md) |
| <a id="C-COMMOD-13"></a>C-COMMOD-13 | OPEC与闲置产能 | 组织、执行和供给缓冲 | P1 | complete／[正文](../10_concepts/OPEC与闲置产能.md) |
| <a id="C-COMMOD-14"></a>C-COMMOD-14 | 战略储备与能源安全 | 库存政策和供应风险 | P1 | complete／[正文](../10_concepts/战略储备与能源安全.md) |
| <a id="C-COMMOD-16"></a>C-COMMOD-16 | 碳排放权与碳价格 | 制度、配额与成本 | P1 | complete／[正文](../10_concepts/碳排放权与碳价格.md) |

## 中国宏观制度与政策工具

| ID | 名称 | 对象边界 | 优先级 | 正文状态 |
|---|---|---|---|---|
| <a id="C-CHINA-01"></a>C-CHINA-01 | 中国人民银行 | 货币、金融稳定与政策执行 | P1 | complete／[正文](../10_concepts/中国人民银行.md) |
| <a id="C-CHINA-02"></a>C-CHINA-02 | 财政部与地方财政 | 央地分工和预算体系 | P1 | complete／[正文](../10_concepts/财政部与地方财政.md) |
| <a id="C-CN-TSF"></a>C-CN-TSF | 社会融资规模 | 统计范围、存量与增量 | P0 | complete／[正文](../10_concepts/社会融资规模.md) |
| <a id="C-CHINA-05"></a>C-CHINA-05 | 人民币贷款与票据融资 | 融资结构和需求代理 | P1 | complete／[正文](../10_concepts/人民币贷款与票据融资.md) |
| <a id="C-CHINA-06"></a>C-CHINA-06 | 存款准备金率与降准 | 结构、覆盖与释放资金 | P1 | complete／[正文](../10_concepts/存款准备金率与降准.md) |
| <a id="C-CHINA-07"></a>C-CHINA-07 | MLF、逆回购与结构性工具 | 工具功能按制度版本记录 | P1 | complete／[正文](../10_concepts/MLF、逆回购与结构性工具.md) |
| <a id="C-CHINA-08"></a>C-CHINA-08 | LPR与贷款定价 | 报价机制与传导 | P1 | complete／[正文](../10_concepts/LPR与贷款定价.md) |
| <a id="C-CHINA-09"></a>C-CHINA-09 | DR007、R007与同业存单 | 不同主体的资金价格 | P1 | complete／[正文](../10_concepts/DR007、R007与同业存单.md) |
| <a id="C-CHINA-10"></a>C-CHINA-10 | 汇率中间价与跨境宏观审慎 | 汇率和资本流动管理 | P1 | complete／[正文](../10_concepts/汇率中间价与跨境宏观审慎.md) |
| <a id="C-CHINA-11"></a>C-CHINA-11 | 土地财政 | 出让收入与地方支出 | P1 | complete／[正文](../10_concepts/土地财政.md) |
| <a id="C-CHINA-12"></a>C-CHINA-12 | 地方融资平台LGFV | 主体、隐性担保与债务 | P1 | complete／[正文](../10_concepts/地方融资平台LGFV.md) |
| <a id="C-CHINA-13"></a>C-CHINA-13 | 地方债务置换与化债 | 本金、期限、利率和责任变化 | P1 | complete／[正文](../10_concepts/地方债务置换与化债.md) |
| <a id="C-CHINA-14"></a>C-CHINA-14 | 房地产预售与保交楼 | 现金流、交付与信用链 | P1 | complete／[正文](../10_concepts/房地产预售与保交楼.md) |
| <a id="C-CHINA-15"></a>C-CHINA-15 | 房地产融资与住房按揭 | 开发端和居民端 | P1 | complete／[正文](../10_concepts/房地产融资与住房按揭.md) |
| <a id="C-CHINA-18"></a>C-CHINA-18 | 产业政策与政府引导基金 | 补贴、股权与资源配置 | P1 | complete／[正文](../10_concepts/产业政策与政府引导基金.md) |
| <a id="C-CHINA-19"></a>C-CHINA-19 | 国企央企与资本回报考核 | 治理、分红与投资约束 | P1 | complete／[正文](../10_concepts/国企央企与资本回报考核.md) |

## A股、港股与区域市场制度

| ID | 名称 | 对象边界 | 优先级 | 正文状态 |
|---|---|---|---|---|
| <a id="C-ASIA-01"></a>C-ASIA-01 | A股市场 | 交易制度、投资者与行业结构 | P1 | complete／[正文](../10_concepts/A股市场.md) |
| <a id="C-ASIA-02"></a>C-ASIA-02 | 港股市场 | 离岸定价、资金与中国暴露 | P1 | complete／[正文](../10_concepts/港股市场.md) |
| <a id="C-ASIA-03"></a>C-ASIA-03 | 沪深港通与南北向资金 | 渠道、口径与披露制度 | P1 | complete／[正文](../10_concepts/沪深港通与南北向资金.md) |
| <a id="C-ASIA-04"></a>C-ASIA-04 | 宽基ETF | 跟踪宽基指数的实际基金产品、资产组合、投资者与市场作用；本轮未回补行业ETF。 | P1 | complete／[正文](../10_concepts/宽基ETF.md) |
| <a id="C-ASIA-05"></a>C-ASIA-05 | 红利资产与高股息指数 | 股息可持续性与规则 | P1 | complete／[正文](../10_concepts/红利资产与高股息指数.md) |
| <a id="C-ASIA-06"></a>C-ASIA-06 | 保险资金与长期资金 | 负债期限与配置约束 | P1 | complete／[正文](../10_concepts/保险资金与长期资金.md) |
| <a id="C-ASIA-07"></a>C-ASIA-07 | 社保基金与政策性持有主体 | 公开持仓与不可见交易 | P1 | complete／[正文](../10_concepts/社保基金与政策性持有主体.md) |
| <a id="C-ASIA-08"></a>C-ASIA-08 | 涨跌停、T+1与停复牌 | 执行约束与价格发现 | P1 | complete／[正文](../10_concepts/涨跌停、T+1与停复牌.md) |
| <a id="C-ASIA-09"></a>C-ASIA-09 | IPO、再融资与退市 | 权益供求和制度事件 | P1 | complete／[正文](../10_concepts/IPO、再融资与退市.md) |
| <a id="C-ASIA-10"></a>C-ASIA-10 | A/H溢价 | 分割市场与定价差异 | P1 | complete／[正文](../10_concepts/A／H溢价.md) |
| <a id="C-ASIA-11"></a>C-ASIA-11 | 恒生指数与恒生科技指数 | 成分、权重和行业敞口 | P1 | pending／待完成主审 |
| <a id="C-ASIA-12"></a>C-ASIA-12 | 日本银行与YCC | 政策工具、版本和退出 | P1 | complete／[正文](../10_concepts/日本银行与YCC.md) |

## 国际制度、政治与地缘

| ID | 名称 | 对象边界 | 优先级 | 正文状态 |
|---|---|---|---|---|
| <a id="C-GLOBAL-01"></a>C-GLOBAL-01 | 美联储与FOMC | 政策主体、投票和沟通 | P1 | complete／[正文](../10_concepts/美联储与FOMC.md) |
| <a id="C-GLOBAL-02"></a>C-GLOBAL-02 | 美国财政部 | 融资、现金管理与财政执行 | P1 | complete／[正文](../10_concepts/美国财政部.md) |
| <a id="C-GLOBAL-03"></a>C-GLOBAL-03 | 美国国会与行政部门 | 预算、立法与执行分工 | P1 | complete／[正文](../10_concepts/美国国会与行政部门.md) |
| <a id="C-GLOBAL-04"></a>C-GLOBAL-04 | 民主党与共和党 | 实体及具体政策主张的版本 | P1 | complete／[正文](../10_concepts/民主党与共和党.md) |
| <a id="C-GLOBAL-05"></a>C-GLOBAL-05 | 欧洲央行与欧元区成员国 | 货币与财政分工 | P1 | complete／[正文](../10_concepts/欧洲央行与欧元区成员国.md) |
| <a id="C-GLOBAL-07"></a>C-GLOBAL-07 | IMF、世界银行与BIS | 职能与数据来源 | P1 | complete／[正文](../10_concepts/IMF、世界银行与BIS.md) |
| <a id="C-GLOBAL-09"></a>C-GLOBAL-09 | 出口管制与技术限制 | 产品、地区和合规版本 | P1 | complete／[正文](../10_concepts/出口管制与技术限制.md) |
| <a id="C-GLOBAL-13"></a>C-GLOBAL-13 | 国际支付与清算体系 | 网络、币种与流动性 | P1 | pending／待完成主审 |

## AI、科技与产业链

| ID | 名称 | 对象边界 | 优先级 | 正文状态 |
|---|---|---|---|---|
| <a id="C-TECH-01"></a>C-TECH-01 | 人工智能算力 | 训练、推理与计量口径 | P1 | complete／[正文](../10_concepts/人工智能算力.md) |
| <a id="C-TECH-02"></a>C-TECH-02 | GPU与AI加速器 | 性能、供给、定价和使用率 | P1 | complete／[正文](../10_concepts/GPU与AI加速器.md) |
| <a id="C-TECH-03"></a>C-TECH-03 | 云服务与超大规模云厂商 | 资本开支、收入与客户 | P1 | complete／[正文](../10_concepts/云服务与超大规模云厂商.md) |
| <a id="C-TECH-04"></a>C-TECH-04 | 数据中心 | 建设、机架、选址与资源约束 | P1 | complete／[正文](../10_concepts/数据中心.md) |
| <a id="C-TECH-05"></a>C-TECH-05 | 电力、电网与发电容量 | 能源、电力、接入的不同瓶颈 | P1 | complete／[正文](../10_concepts/电力、电网与发电容量.md) |
| <a id="C-TECH-06"></a>C-TECH-06 | HBM与存储芯片 | 带宽、产能和产品周期 | P1 | complete／[正文](../10_concepts/HBM与存储芯片.md) |
| <a id="C-TECH-07"></a>C-TECH-07 | 晶圆制造与先进制程 | 良率、产能、设备与限制 | P1 | complete／[正文](../10_concepts/晶圆制造与先进制程.md) |
| <a id="C-TECH-08"></a>C-TECH-08 | 先进封装与CoWoS | 集成工艺和瓶颈 | P1 | complete／[正文](../10_concepts/先进封装与CoWoS.md) |
| <a id="C-TECH-09"></a>C-TECH-09 | 半导体设备与材料 | 资本开支链和技术约束 | P1 | complete／[正文](../10_concepts/半导体设备与材料.md) |
| <a id="C-TECH-10"></a>C-TECH-10 | 光模块、交换机与网络互联 | 数据传输与集群规模 | P1 | complete／[正文](../10_concepts/光模块、交换机与网络互联.md) |
| <a id="C-TECH-11"></a>C-TECH-11 | 散热与液冷 | 功耗密度与系统成本 | P1 | complete／[正文](../10_concepts/散热与液冷.md) |
| <a id="C-TECH-17"></a>C-TECH-17 | NVIDIA | 加速器与系统公司；财务和产品版本单独记录 | P1 | complete／[正文](../10_concepts/NVIDIA.md) |
| <a id="C-TECH-18"></a>C-TECH-18 | AMD | CPU、GPU与AI加速器公司 | P1 | complete／[正文](../10_concepts/AMD.md) |
| <a id="C-TECH-19"></a>C-TECH-19 | Microsoft | 企业软件、云与AI平台 | P1 | complete／[正文](../10_concepts/Microsoft.md) |
| <a id="C-TECH-20"></a>C-TECH-20 | Amazon | 零售、物流与AWS云业务 | P1 | complete／[正文](../10_concepts/Amazon.md) |
| <a id="C-TECH-21"></a>C-TECH-21 | Alphabet | 搜索广告、云与AI业务 | P1 | pending／待完成主审 |
| <a id="C-TECH-22"></a>C-TECH-22 | Meta | 社交广告、推荐系统与AI投资 | P1 | pending／待完成主审 |
| <a id="C-TECH-23"></a>C-TECH-23 | Apple | 消费硬件、服务与终端AI | P1 | pending／待完成主审 |
| <a id="C-TECH-24"></a>C-TECH-24 | Tesla | 汽车、能源与自动驾驶业务 | P1 | pending／待完成主审 |
| <a id="C-TECH-25"></a>C-TECH-25 | TSMC | 晶圆代工与先进封装 | P1 | pending／待完成主审 |
| <a id="C-TECH-26"></a>C-TECH-26 | ASML | 光刻设备与服务 | P1 | pending／待完成主审 |
| <a id="C-TECH-27"></a>C-TECH-27 | Samsung Electronics | 存储、逻辑代工与终端业务 | P1 | pending／待完成主审 |
| <a id="C-TECH-28"></a>C-TECH-28 | SK hynix | 存储与HBM业务 | P1 | pending／待完成主审 |
| <a id="C-TECH-29"></a>C-TECH-29 | Micron | 存储与HBM业务 | P1 | pending／待完成主审 |
| <a id="C-TECH-30"></a>C-TECH-30 | 腾讯 | 社交、游戏、广告与云 | P1 | pending／待完成主审 |
| <a id="C-TECH-31"></a>C-TECH-31 | 阿里巴巴 | 电商、云与AI业务 | P1 | pending／待完成主审 |
| <a id="C-TECH-32"></a>C-TECH-32 | 百度 | 搜索、AI云与自动驾驶 | P1 | pending／待完成主审 |
| <a id="C-TECH-33"></a>C-TECH-33 | 中芯国际 | 晶圆代工与制造能力 | P1 | pending／待完成主审 |
| <a id="C-TECH-34"></a>C-TECH-34 | 寒武纪 | AI芯片与软件生态 | P1 | pending／待完成主审 |

## 行业与经营暴露

| ID | 名称 | 对象边界 | 优先级 | 正文状态 |
|---|---|---|---|---|
| <a id="C-SECTOR-01"></a>C-SECTOR-01 | 商业银行业 | 资产质量、息差和资本 | P1 | pending／待完成主审 |
| <a id="C-SECTOR-02"></a>C-SECTOR-02 | 保险业 | 负债成本、利率和资本市场 | P1 | pending／待完成主审 |
| <a id="C-SECTOR-03"></a>C-SECTOR-03 | 证券与资管业 | 成交、融资和管理资产 | P1 | pending／待完成主审 |
| <a id="C-SECTOR-04"></a>C-SECTOR-04 | 电力与公用事业 | 电价、燃料、利用小时与资本开支 | P1 | pending／待完成主审 |
| <a id="C-SECTOR-06"></a>C-SECTOR-06 | 房地产开发与物业 | 销售、融资、交付与现金流 | P1 | pending／待完成主审 |
| <a id="C-SECTOR-12"></a>C-SECTOR-12 | REITs与基础设施资产 | 运营现金流、利率与制度 | P1 | pending／待完成主审 |
| <a id="C-SECTOR-13"></a>C-SECTOR-13 | 养老金与退休负债 | 缴费、待遇支付、资金积累和负债久期；区分现收现付与积累制 | P1 | pending／待完成主审 |

## 数字资产与新型金融

| ID | 名称 | 对象边界 | 优先级 | 正文状态 |
|---|---|---|---|---|
| <a id="C-CRYPTO-01"></a>C-CRYPTO-01 | 比特币 | 供给规则、需求和风险暴露 | P1 | pending／待完成主审 |
| <a id="C-CRYPTO-02"></a>C-CRYPTO-02 | 以太坊与智能合约平台 | 网络使用、费用与资产属性 | P1 | pending／待完成主审 |
| <a id="C-CRYPTO-03"></a>C-CRYPTO-03 | 稳定币 | 储备、赎回、交易与支付 | P1 | pending／待完成主审 |
| <a id="C-CRYPTO-04"></a>C-CRYPTO-04 | 数字资产交易所与托管 | 交易对手及操作风险 | P1 | pending／待完成主审 |
| <a id="C-CRYPTO-05"></a>C-CRYPTO-05 | 加密资产杠杆与永续合约 | 资金费率、清算和基差 | P1 | pending／待完成主审 |
| <a id="C-CRYPTO-06"></a>C-CRYPTO-06 | 现货加密ETF | 份额、流量和基础资产 | P1 | pending／待完成主审 |
| <a id="C-CRYPTO-08"></a>C-CRYPTO-08 | 代币化国债与现实资产RWA | 法律权利、托管和流动性 | P1 | pending／待完成主审 |
| <a id="C-CRYPTO-09"></a>C-CRYPTO-09 | 比特币挖矿、区块奖励与矿工 | 工作量证明、难度、区块补贴、手续费与算力成本 | P1 | pending／待完成主审 |
