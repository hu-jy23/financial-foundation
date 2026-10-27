---
id: C-IR-POLICY
type: concept
title: 政策利率与目标区间
status: draft
draft_author: "/root/policy_concept"
model: gpt-6-astra
reasoning_effort: medium
reviewed_by: null
updated: 2026-10-27
evidence_as_of: 2024-12-18
source_ids: [S-POLICY-01, S-POLICY-02, S-POLICY-03, S-POLICY-04, S-POLICY-05, S-POLICY-06, S-POLICY-07, S-POLICY-08, S-POLICY-09, S-POLICY-10, S-POLICY-11, S-POLICY-12, S-POLICY-13, S-POLICY-14, S-POLICY-15, S-POLICY-16, S-POLICY-17, S-POLICY-18]
---

# 政策利率与目标区间

> 独立执笔：`/root/policy_concept`，GPT-6-Astra，medium；2026-10-27 首稿，待主 agent 审阅。历史事实覆盖至 **2024-12-18**，中国制度比较采用 **2024年7—8月**口径；来源访问日期为2026-10-27。本页不报告制作日的政策利率。

## 概念定义

政策利率是央行为实现物价稳定、就业等政策目标，选择并调控的关键利率。它可以表现为对某个短期市场利率设定的目标，也可以表现为央行在特定操作中直接给出的利率。目标区间则是央行希望相关市场利率运行的范围：它表达政策决策，同时给执行部门一个可以检查的操作目标。不同央行选择的工具、市场和期限不同，不能只凭“政策利率”这个名称把各国数字当成同一种报价。[S-POLICY-01](#S-POLICY-01)、[S-POLICY-13](#S-POLICY-13)

在本页重点讨论的美国制度中，联邦公开市场委员会（FOMC）设定**联邦基金利率目标区间**，美元隔夜联邦基金市场的成交结果用有效联邦基金利率（EFFR）概括。前者是政策选择，后者是市场交易的统计值；美联储还通过准备金利率和公开市场操作，把交易利率引导到目标区间内。因而，“美联储利率是多少”需要先说明问的是目标上下限、目标中点、EFFR，还是某项操作工具利率。[S-POLICY-02](#S-POLICY-02)、[S-POLICY-04](#S-POLICY-04)

## 概念详解

### 从政策意图到成交利率：两项相接的工作

政策决策解决的是“短期货币价格应当处于什么水平”。FOMC评估就业、通胀及前景风险，决定维持、提高或降低目标区间，并解释未来判断所依赖的信息。操作执行解决的是“如何让这个决定成为市场上的资金价格”。目标公布后，银行不会因此自动以区间中点成交；美联储必须让相关机构面对与目标一致的存放、借出和融资选择。

在2019年确认、2024年仍采用的充裕准备金框架下，FOMC设定联邦基金目标区间并向纽约联储公开市场交易台下达指令；美联储理事会设定准备金余额利率（IORB）。交易台依指令开展操作。会议声明主要说明政策立场，配套的实施说明（Implementation Note）列明具体工具利率、生效日和操作安排。两份文件合读，才能把“决策宣布”与“开始执行”分开。例如2024年9月18日宣布降息，配套实施说明列明相关操作和IORB调整从9月19日起生效。[S-POLICY-05](#S-POLICY-05)、[S-POLICY-15](#S-POLICY-15)

### 目标区间、中点和有效利率分别表达什么

设目标下限为 \(L\)、上限为 \(U\)，中点为 \(m=(L+U)/2\)，宽度为 \(w=U-L\)。这些量均按年化百分比表示。若目标区间是4.75%—5.00%，中点为4.875%，区间宽度为0.25个百分点，即25个基点（bp）。中点是由上下限算出的摘要，方便比较政策位置；它不是另外一项存贷款利率，也不表示美联储要求每笔交易恰好在4.875%成交。

联邦基金交易是美国境内存款类机构从其他存款类机构及部分其他主体借入美元的无担保交易，主要期限是隔夜。EFFR根据符合口径的隔夜交易计算。在2016年3月1日起采用的方法中，纽约联储将FR 2420报告的交易按利率排序，按金额累计到50%处的利率形成成交量加权中位数，再按规定取整发布。它既不是区间中点，也不是把所有交易利率简单平均。日内可以存在高于或低于EFFR的交易，EFFR在区间内也不表示每笔成交都在区间内。[S-POLICY-02](#S-POLICY-02)、[S-POLICY-03](#S-POLICY-03)

目标区间因此是一项需要执行的政策目标，并非法律上禁止市场越过的价格边界。把目标画成一个带状区域、把EFFR画成一条成交统计曲线，可以分别观察“央行选择了什么”和“市场实现了什么”。若EFFR偏离，首先应区分政策目标是否改变，还是资金供求和执行条件出现变化。

### 为什么调整IORB能够引导市场利率

准备金是银行等合资格机构在联储持有的余额。IORB是美联储对合资格余额支付的利率。对一家可以获得IORB的银行而言，把资金留在联储能够取得一种低信用风险、可用于流动性管理的回报；若向另一家机构隔夜出借，银行就要比较借款人的风险、交易成本与这项替代回报。IORB提高后，银行出借资金所要求的回报通常随之提高，其他短期资金价格也受到向上的牵引。[S-POLICY-04](#S-POLICY-04)

这个过程解释了IORB为何有利率下方支撑作用，也解释了它为何不构成所有交易的硬下限。并不是所有资金出借方都有资格赚取IORB。联邦住房贷款银行等机构可能愿意以低于IORB的利率出借；有资格取得IORB的银行则可能借入这些资金，再存放于联储。中介的资产负债表成本、监管成本和交易条件，使价差不一定被完全消除。美联储2024年7月的研究据此解释了联邦基金市场中不同出借方、借入方及其交易动机；不能把EFFR低于IORB直接理解为执行失灵。[S-POLICY-06](#S-POLICY-06)

隔夜逆回购工具（ON RRP）扩大了这种替代投资选择的覆盖范围：符合资格的货币市场基金等机构可以把现金通过有证券支持的隔夜交易交给联储，并取得规定回报。它们与私人借款人议价时，就多了一个可比较的去处。IORB与ON RRP共同支持短端利率控制，ON RRP不是面向所有投资者的无限制存款账户，其资格和限额以当时操作规则为准。[S-POLICY-04](#S-POLICY-04)、[S-POLICY-07](#S-POLICY-07)

这些操作利率与目标上下限之间的距离可以调整。2024年9月19日实施的组合是目标4.75%—5.00%、IORB 4.90%、ON RRP报价4.80%；IORB不等于上限，ON RRP也不等于下限。若为保持EFFR稳定而改变工具利率相对目标区间的位置，这可以是技术性调整，不能仅看某个工具上调了几bp就判定FOMC额外收紧了政策。[S-POLICY-15](#S-POLICY-15)

### 准备金稀缺与充裕，为什么需要不同的执行办法

在金融危机前的稀缺准备金框架中，银行对结算和满足准备金要求的余额有需求，而系统余额供给相对有限。额外投放或回收准备金会明显改变银行在市场借款的迫切程度，美联储通过公开市场操作调整供给，使市场利率接近政策目标。这里，数量调节是实现价格目标的重要日常手段。[S-POLICY-06](#S-POLICY-06)

大规模资产购买以后，准备金增多。只要余额仍处在充裕区域，通常规模的准备金变化对边际借款需求的影响较小，单靠日常微调数量难以像此前那样控制利率。操作重心于是转向管理利率：改变银行持有准备金及其他合资格主体存放隔夜资金的回报。所谓“充裕”，是指供给足以使利率对准备金数量变化不太敏感，并非一个永远不变的美元金额。银行支付需求、流动性管理和其他联储负债变化，仍会影响需要维持多少准备金。[S-POLICY-04](#S-POLICY-04)、[S-POLICY-07](#S-POLICY-07)

这样可以同时理解两个事实：充裕准备金与较高政策利率可以并存，因为央行提高了持有准备金的报酬；维持充裕准备金又仍需管理资产负债表，因为一旦供给逼近需求较陡的区域，资金利率会更容易受数量扰动。目标区间描述短率的政策设置，资产负债表规模和构成则是另一组政策与执行安排，二者有联系，却没有固定的一对一换算。[S-POLICY-05](#S-POLICY-05)

### 加息25bp、利率上升25%、政策变得限制性，是三个判断

1 bp等于0.01个百分点。**假设算例**：利率从4.00%升至4.25%，增加0.25个百分点，亦即25bp；相对原水平的增幅是 \(0.25/4.00=6.25\%\)，不是25%。若一个宽度25bp的目标区间整体上移25bp，上下限各升25bp，中点也升25bp，宽度不变。新闻中的“加息25bp”通常指这种水平变化，应以原公告为准。

上调目标表示央行提高了这项名义短率的政策设置；“限制性”则判断这种设置是否对需求和通胀形成抑制，涉及预期通胀、均衡实际利率、信用条件及传导时滞。2015年12月FOMC就在加息后仍将政策描述为宽松。只看名义利率为正或本次方向向上，无法完成政策立场的判断。[S-POLICY-09](#S-POLICY-09) 购买力口径见[实际利率 C-IR-REAL](C-IR-REAL_real_interest_rate.md)。

### 区间下限与有效下限不能混为一谈

目标区间下限，是某次决策选定的一个数字；零利率下限／有效下限，讨论的是继续压低名义利率会面临什么约束。现金本身不支付负利息，存款或安全短债收益率若过低，持有人可能改持现金。但持有、运输和保管现金也有成本，因此经济上的有效下限不必精确等于0%，不同制度下也未必相同。[S-POLICY-01](#S-POLICY-01)

美国2008年与2020年采用0%—0.25%目标区间，体现的是相应时点接近下限的政策选择，不是把全世界名义利率的最小值写成一条自然定律。短率继续下调的空间受限时，央行仍可通过未来政策沟通、资产购买等工具影响较长期融资条件；此时单独一个目标区间更难概括全部政策力度。[S-POLICY-05](#S-POLICY-05)、[S-POLICY-08](#S-POLICY-08)、[S-POLICY-11](#S-POLICY-11)

## 相近概念与适用边界

| 对象或口径 | 本页需要保留的区别 |
|---|---|
| [有效联邦基金利率EFFR C-RATE-05](../00_start/CONCEPT_IMPORT_LIST.md#C-RATE-05) | 隔夜无担保交易的统计结果；目标区间是政策指定的范围。完整市场结构与序列细节归该对象。 |
| [准备金利率 C-MONEY-07](../00_start/CONCEPT_IMPORT_LIST.md#C-MONEY-07) | 央行直接支付的管理利率，是执行工具；与政策目标相连，但不等于目标上限或中点。 |
| [收益率曲线 C-IR-CURVE](../00_start/CONCEPT_IMPORT_LIST.md#C-IR-CURVE)与[期限溢价 C-IR-TERM](C-IR-TERM_term_premium.md) | 两年、十年收益率是对应期限资产的市场价格，包含未来短率路径及风险补偿，不能把今天的政策率复制到每个期限。 |
| [实际利率 C-IR-REAL](C-IR-REAL_real_interest_rate.md) | 把名义回报与相关期间的物价变化联系起来。政策率是名义隔夜口径，减去当前CPI同比并不能自动得到规范的未来实际投资回报。 |
| [MLF、逆回购与结构性工具 C-CHINA-07](../00_start/CONCEPT_IMPORT_LIST.md#C-CHINA-07) | 中国的不同期限与用途的央行工具须按制度时期辨认，不能统称为一个“央行利率”。 |

长期市场利率会在会议之前变化，因为投资者在给一段未来现金流定价，已经需要判断这段时间内的政策路径。例如明天到期的隔夜资金，与未来两年不断到期再投资的资金，受一次会议及后续会议的影响不同。即使本次目标未变，关于未来路径的新信息仍可能改变两年收益率；即使本次降息，远期路径或期限溢价上升也可能抵消长债收益率下行。这是期限结构的经济含义，完整条件与证据见[货币政策冲击的期限结构传导](../00_start/MECHANISM_IMPORT_LIST.md#R-POL-CURVE)。

### 中国对照：先识别哪项利率承担政策信号

人民银行2024年8月9日发布的第二季度货币政策执行报告，在专栏2说明：7天期逆回购操作利率已基本承担主要政策利率功能；7月22日起采用固定利率、数量招标，并从1.80%下调10bp至1.70%。这样由央行明示操作价格，再按操作安排处理需求数量，减少了操作利率波动与政策信号之间的混淆。[S-POLICY-13](#S-POLICY-13)

同一报告解释，2019年LPR改革初期，报价主要参考1年期MLF利率；随着框架调整，MLF的政策利率色彩逐步淡化，LPR更多参考短期政策利率。这个历史转变说明，对“中国降息”的判断应明确是哪项工具、什么日期。LPR是贷款定价参考，DR007等是货币市场成交指标，它们都不应直接改名为美联储式的目标区间。完整工具、报价和市场口径分别见[央行工具](../00_start/CONCEPT_IMPORT_LIST.md#C-CHINA-07)、[LPR与贷款定价](../00_start/CONCEPT_IMPORT_LIST.md#C-CHINA-08)、[DR007、R007与同业存单](../00_start/CONCEPT_IMPORT_LIST.md#C-CHINA-09)。此处只描述2024年报告所载阶段，不把它扩充为2026年的完整框架。[S-POLICY-13](#S-POLICY-13)

## 观测与数据口径

| 要观察的内容 | 优先资料和读取方法 | 需要保留的区别 |
|---|---|---|
| 已作出的政策决定 | FOMC声明；记录宣布日、目标上下限、调整幅度和表述 | 声明中的未来判断不是已经发生的调整。 |
| 决定怎样执行 | 同日实施说明；记录各工具利率、执行主体和生效日 | 当日宣布不等于当日所有隔夜交易已按新参数发生。 |
| 市场是否实现目标 | 纽约联储EFFR、成交量及分位数；与相同交易日有效的区间比较 | EFFR通常下一营业日纽约时间约9时发布；观测日与可知日分开。 |
| 官员对未来路径的判断 | SEP利率点阵、表1与脚注 | 年末目标中点／目标水平，不是全年均值；个体适当政策判断不等于委员会承诺。 |
| 市场对政策的预期 | 对应日期的利率衍生品报价或调查原表 | 价格隐含路径、受访者中位数、最可能结果和概率分布各有含义；需要合约、期限和转换方法。 |

EFFR的长期比较还需处理方法变化：2016年3月1日前后，数据源和计算方法改变。纽约联储现行方法页还规定数据不足时的替代处理、同日修订及滞后补充统计；后来取得的补充统计可能与最初公布值不同。事件研究应保留当时实际可见的版本，而不是把今天下载的数据自动视为当时信息。[S-POLICY-03](#S-POLICY-03)

预期的读取有一个重要层次：**预期什么水平**与**预期如何到达该水平**不同。年末目标中点4.4%的预测，没有唯一指定中间每次会议的时间和幅度，也没有给出未来一整年的平均资金成本。若用它解释某个期限资产，就必须补中间路径。SEP参加者包括理事与储备银行行长，其个体判断汇总也不能直接代替金融市场边际投资者的预期。[S-POLICY-16](#S-POLICY-16)

## 本对象的历史

以下选择的是目标形式、执行框架和预期口径发生重要变化的片段。各段保存相应时点的政策制定者判断；没有取得会前市场分布的地方，不判断政策动作“超出市场预期”多少。

### 2008-12-16：从单点表达转向0%—0.25%的目标区间

此前10月29日的声明仍采用1.00%的单点目标；12月16日FOMC宣布设立0%—0.25%联邦基金利率目标区间。声明把经济活动进一步转弱、金融市场压力和通胀压力回落放在一起，预计疲弱经济状况会使特别低的利率维持一段时间，但没有给出确定的退出日期。目标采取区间形式并接近零，政策沟通同时转向资产购买等其他工具。[S-POLICY-08](#S-POLICY-08)

这段历史的意义是：政策短率仍是一个清楚可识别的对象，但目标处于低位以后，只记录“维持利率”会遗漏其他政策变化。低目标水平与采用区间形式是两项可分别观察的制度／状态特征，不能把区间宽度解释成央行对下一次利率决定的概率分布。

### 2015-12-16宣布、12-17实施：离开下限并不要求先回到稀缺准备金

FOMC把目标区间提高到0.25%—0.50%。当时委员会认为就业状况已有显著改善，并有合理信心相信通胀将在中期回到2%；同时预计后续加息只能是渐进的，实际路径取决于新的经济信息，并认为加息后的政策仍属宽松。这是委员会当时的条件性判断，不是对未来会议次数的承诺。[S-POLICY-09](#S-POLICY-09)

实施说明规定，自12月17日起，法定和超额准备金余额利率均为0.50%，ON RRP报价为0.25%；同时继续到期国债滚动及相关证券本金再投资。也就是说，此次加息主要通过调整资金的替代回报执行，并未先靠大幅压缩资产持有把系统带回危机前的稀缺准备金状态。[S-POLICY-10](#S-POLICY-10)

**较晚材料记录的结果**：2016年2月22日FEDS Notes回顾，在剔除年末交易日的比较中，多数联邦基金成交从加息前约11—15bp移至加息后约32—37bp；前窗为2015年12月3—16日，后窗为12月17日至2016年1月4日。这里是交易分布的位置，不是EFFR每日取值，也不是当时已知的预测。它显示管理利率变化如何进入实际成交，同时保留了成交并非集中于目标中点一个数字的事实。[S-POLICY-18](#S-POLICY-18)

### 2018—2019：政策区间、工具位置与准备金条件须分别记录

2018年6月FOMC将目标区间上移25bp，但准备金利率只提高20bp至1.95%，使其位于区间上限下方5bp。美联储7月货币政策报告解释，这是为了让此前靠近上限的EFFR运行得更靠近区间中部。一次会议里可以同时发生政策加息和执行参数的技术调整，不能把20bp与25bp的差异误读为两套相互矛盾的政策决定。[S-POLICY-17](#S-POLICY-17)

2019年1月30日，FOMC明确表示将继续采用充裕准备金制度，以管理利率为主要短率控制手段。**后来研究对当年压力的回顾**：2024年7月FEDS Notes记录，2019年9月17日EFFR为2.30%，高于当日2.00%—2.25%的目标区间；当日SOFR为5.25%。这些是不同市场的利率，不应把回购市场峰值当作联邦基金政策利率。这个片段说明，宣布采用充裕框架并不免除持续检查准备金供求和市场联动的职责。[S-POLICY-05](#S-POLICY-05)、[S-POLICY-06](#S-POLICY-06)

### 2020-03-15：同样的低区间，伴随新的经济条件与退出条件

疫情冲击下，FOMC于当日17:00 EDT宣布将目标区间降至0%—0.25%，并预计维持到其确信经济已度过冲击、重新走向就业与物价目标为止。这里的期限由经济条件界定，没有确定的日历终点。0%—0.25%与2008年数值相同，冲击、金融状态及政策沟通却不相同，因此同一目标数字不能替代对政策背景的阅读。[S-POLICY-11](#S-POLICY-11)

准备金付息的名称也有历史变化：2021年7月29日起，单一IORB取代此前的IORR与IOER称谓。因此阅读2015年实施说明时应保留其当时名称，而不是把现行缩写倒填进历史公告。[S-POLICY-12](#S-POLICY-12)

### 2022-09-21：目标上调是已发生事实，继续加息是当时判断

当日14:00 EDT，FOMC把目标区间从7月决定的2.25%—2.50%提高至3.00%—3.25%，即上移75bp，并预计继续上调将是适当的。声明同时强调通胀高企，并继续减少国债、机构债和机构MBS持有量。3.00%—3.25%是本次决定的名义政策水平；“继续上调”是委员会对后续方向的判断，原声明没有给出终点利率或每次会议的固定步长。对黄金或长债的分析若要进一步使用实际利率和未来路径，仍需对应期限的额外证据。[S-POLICY-14](#S-POLICY-14)

### 2024-09-18及12-18：降息、路径预测和后来端点的不同身份

9月18日14:00 EDT，FOMC把目标区间下调50bp至4.75%—5.00%，理由涉及通胀进展和风险平衡。9月19日起生效的IORB 4.90%及ON RRP 4.80%，是把该决定落实到资金市场的执行参数。二者均非9月18日EFFR的观测值。[S-POLICY-15](#S-POLICY-15)

同日SEP表1中，参加者对2024、2025年末适当联邦基金利率的预测中位数分别是4.4%、3.4%；6月相应中位数为5.1%、4.1%。这些是对年末目标中点或目标水平的个体判断汇总。它们说明官员所评估的适当路径发生了变化，但既不是会前市场预期，也不能据此推出每位官员都主张同一条降息路径。[S-POLICY-16](#S-POLICY-16)

**后来结果，2024-12-18**：FOMC又宣布下调25bp至4.25%—4.50%。该区间中点4.375%取一位小数为4.4%，与9月SEP中2024年末中位数在这个精度上相容。此处仅核到12月18日的政策决定，没有重建全年每日EFFR或9月以后各人的预测修订；数值相容不等于预测全过程准确，也不能据此倒推9月的市场定价。[S-POLICY-15](#S-POLICY-15)、[S-POLICY-16](#S-POLICY-16)

## 涉及的关系

| 关系入口 | 本对象在其中的作用 |
|---|---|
| [黄金的机会成本机制 R-GOLD-REALRATES，逻辑2](../20_mechanisms/R-GOLD-REALRATES_real_rates_gold.md#logic-2) | 政策利率及未来路径是名义短端输入；与预期通胀共同关系到实际替代回报，再进入[黄金](C-ASSET-GOLD_gold.md)的持有比较。政策目标本身不等于黄金机会成本的完整测量。 |
| [货币政策冲击的期限结构传导 R-POL-CURVE](../00_start/MECHANISM_IMPORT_LIST.md#R-POL-CURVE) | 区分本次目标调整和未来路径信息，解释不同期限市场利率如何反应。 |
| [央行公告的政策效应与信息效应 R-POL-INFORMATION](../00_start/MECHANISM_IMPORT_LIST.md#R-POL-INFORMATION) | 央行公告同时包含政策选择与经济判断；已执行的降息不能单独确定市场把经济前景上修还是下修。 |
| [利率走廊 R-MONETARY-07](../00_start/MECHANISM_IMPORT_LIST.md#R-MONETARY-07) | 本对象给出要实现的利率目标；该机制进一步解释各设施价格、机构资格与准备金供求怎样约束市场成交。 |

## 来源与待补问题

下列为本轮直接核读的一手资料及教材章节，来源ID仅在本页登记，不另建Source／Event。阅读范围与访问失败记录另见[执笔笔记](../50_reviews/CONCEPT_PILOT_20261027/POLICY_AGENT_NOTES.md)。

<a id="S-POLICY-01"></a>
- **S-POLICY-01**：Bindseil、Fotia，*Introduction to Central Banking*第3章[Conventional Monetary Policy](https://link.springer.com/chapter/10.1007/978-3-030-70884-9_3)，2021-05-19，pp.29–51。本次抽读§3.1.1、§3.1.2.1及§3.2—3.3相关段落；主要采用操作目标和现金下限解释，不声称通读全章。网页有关美国地板制起点存在年代疑点，未采用。
<a id="S-POLICY-02"></a>
- **S-POLICY-02**：纽约联储，[Effective Federal Funds Rate](https://www.newyorkfed.org/markets/reference-rates/effr)，动态方法入口，页面未列固定初发日；读取定义、FR 2420与公布时点，不提取最新行情。
<a id="S-POLICY-03"></a>
- **S-POLICY-03**：纽约联储，[Additional Information about Reference Rates](https://www.newyorkfed.org/markets/reference-rates/additional-information-about-reference-rates)，动态规则页，初发日未取得；读取EFFR/OBFR的Primary Data Inputs、Calculation Methodology、Details on Publication and Revisions及应急处理段落。现时方法核读不代表取得历年原始版本。
<a id="S-POLICY-04"></a>
- **S-POLICY-04**：美联储，Ihrig、Senyuz、Weinbach，[Implementing Monetary Policy in an “Ample-Reserves” Regime: The Basics](https://www.federalreserve.gov/econres/notes/feds-notes/implementing-monetary-policy-in-an-ample-reserves-regime-the-basics-note-1-of-3-20200701.html)，2020-07-01；正文准备金需求、管理利率、技术调整段落，图1—2附近文字，未提取图表序列。
<a id="S-POLICY-05"></a>
- **S-POLICY-05**：FOMC，[Statement Regarding Monetary Policy Implementation and Balance Sheet Normalization](https://www.federalreserve.gov/newsevents/pressreleases/monetary20190130c.htm)，2019-01-30 14:00 EST；声明全文。
<a id="S-POLICY-06"></a>
- **S-POLICY-06**：Anderson、Na，[The Recent Evolution of the Federal Funds Market and its Dynamics during Reductions of the Federal Reserve’s Balance Sheet](https://www.federalreserve.gov/econres/notes/feds-notes/the-recent-evolution-of-the-federal-funds-market-and-its-dynamics-during-reductions-of-fr-balance-sheet-20240711.html)，FEDS Notes，2024-07-11；Background、Participants and trading motivations及2017—2019缩表／2019-09-17段落。研究者解释与历史回顾，未复算图表。
<a id="S-POLICY-07"></a>
- **S-POLICY-07**：Eric LeSueur，纽约联储，[The Federal Reserve’s Monetary Policy Implementation Framework](https://tellerwindow.newyorkfed.org/2024/08/05/the-federal-reserve-and-its-monetary-policy-implementation-framework/)，2024-08-05；框架及How the Administered Rates Work正文。
<a id="S-POLICY-08"></a>
- **S-POLICY-08**：FOMC，[2008-12-16声明](https://www.federalreserve.gov/newsevents/pressreleases/monetary20081216b.htm)，2008-12-16，全文；另核[2008-10-29声明](https://www.federalreserve.gov/newsevents/pressreleases/monetary20081029a.htm)目标段，以确认此前单点1.00%。两页未列精确发布时刻。
<a id="S-POLICY-09"></a>
- **S-POLICY-09**：FOMC，[2015-12-16声明](https://www.federalreserve.gov/newsevents/pressreleases/monetary20151216a.htm)，2015-12-16，全文，尤其目标决定、渐进路径与再投资安排。
<a id="S-POLICY-10"></a>
- **S-POLICY-10**：美联储，[2015-12-16实施说明](https://www.federalreserve.gov/newsevents/pressreleases/20151216a1.htm)，2015-12-16发布，网页末次更新2015-12-17；操作指令及各工具生效日。
<a id="S-POLICY-11"></a>
- **S-POLICY-11**：FOMC，[2020-03-15声明](https://www.federalreserve.gov/newsevents/pressreleases/monetary20200315a.htm)，2020-03-15 17:00 EDT；目标决定、退出条件及工具安排。
<a id="S-POLICY-12"></a>
- **S-POLICY-12**：美联储，[IORB Frequently Asked Questions](https://www.federalreserve.gov/monetarypolicy/iorb-faqs.htm)；本文只采用标注2021-07-29的“What is the IORB rate?”及“Prior to the implementation…”两问，核实命名、生效日与此前付息制度；不以此页2025年新增问答扩展本文历史截止。
<a id="S-POLICY-13"></a>
- **S-POLICY-13**：人民银行，[2024年第二季度中国货币政策执行报告](https://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125957/5347949/2025100917195573922/2025081217013923839.pdf)，报告署期2024-08-09；印刷页11—14，专栏2在12—13页（PDF第18—19页）。URL含后续迁移目录日期，不替代报告署期。
<a id="S-POLICY-14"></a>
- **S-POLICY-14**：FOMC，[2022-09-21声明](https://www.federalreserve.gov/newsevents/pressreleases/monetary20220921a.htm)，2022-09-21 14:00 EDT；正文目标、持续加息判断和缩表段落；另核[2022-07-27声明](https://www.federalreserve.gov/newsevents/pressreleases/monetary20220727a.htm)目标段，作为75bp变化的比较基准。
<a id="S-POLICY-15"></a>
- **S-POLICY-15**：FOMC，[2024-09-18声明](https://www.federalreserve.gov/newsevents/pressreleases/monetary20240918a.htm)及[配套实施说明](https://www.federalreserve.gov/newsevents/pressreleases/monetary20240918a1.htm)，2024-09-18；[2024-12-18声明](https://www.federalreserve.gov/newsevents/pressreleases/monetary20241218a.htm)，2024-12-18 14:00 EST。分别核目标决定、IORB/ON RRP与生效日、12月目标端点。
<a id="S-POLICY-16"></a>
- **S-POLICY-16**：美联储，[September 2024 Summary of Economic Projections](https://www.federalreserve.gov/monetarypolicy/files/fomcprojtabl20240918.pdf)，2024-09-18 14:00 EDT；PDF第1—2页，说明、Table 1利率行及期限脚注。未重建逐人完整路径。
<a id="S-POLICY-17"></a>
- **S-POLICY-17**：美联储，[July 2018 Monetary Policy Report, Part 2](https://www.federalreserve.gov/monetarypolicy/2018-07-mpr-part2.htm)，2018-07-13；“The Federal Reserve’s implementation of monetary policy has continued smoothly”及“Interest on Reserves and Its Importance for Monetary Policy”专栏的技术调整段。
<a id="S-POLICY-18"></a>
- **S-POLICY-18**：美联储，[What Happened in Money Markets after the Fed’s December Rate Increase?](https://www.federalreserve.gov/econresdata/notes/feds-notes/2016/what-happened-in-money-markets-after-the-feds-december-rate-increase-20160222.html)，2016-02-22；隔夜市场段落、图3文字及窗口注释。网页注明图2于3月1日修订，本页没有使用图2数据。

**本轮具体缺口**：尚未取得上述会议前同一时间截面的期货／OIS报价、调查分布与完整转换参数。本轮已查会议声明、实施说明、SEP以及2015年实施后的官方研究；这些材料可证明政策动作、官员条件判断和部分事后执行结果，不能量化每次会议的会前市场预期差。历史报价与调查原表的专项提取未完成，因此正文不写“市场已定价几次”“降息概率多少”。中国比较只核到2024年报告，2024年后框架变动及全部配套工具未系统核读；这是本页选择的历史范围，不表示后来没有变化。
