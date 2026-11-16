# v5 整合与本轮调整记录

日期：2026-10-24；执行与整合：主 agent。以 v4 正文及此前 Event／Source 工作区为底稿，按用户最后限定范围更新目录。

## 1. 回补与移出

回补净息差、金融周期、农产品、社会融资规模、宽基 ETF 共5项。战略储备与能源安全原已入选，保持原条目，未拆分。宽基 ETF 不包含行业 ETF。制裁与资产冻结移出对象目录。

因此对象数从159变为163，18个非空主题组，原349项其余186项不作为对象。完整去向见[逐项表](CONCEPT_SELECTION_349.md)和[迁移记录](CATALOG_MIGRATION.json)。

## 2. 只迁移指定五项

| 原对象候选 | 关系去向 | 处理 |
|---|---|---|
| 美元融资依赖 | [美元融资依赖的传导机制 R-USD-GLOBAL](../00_start/MECHANISM_IMPORT_LIST.md#R-USD-GLOBAL) | 整合既有候选，保留关系ID |
| 全球美元体系与美元主导地位 | [全球美元体系与美元主导地位 R-INTERNATIONAL-12](../00_start/MECHANISM_IMPORT_LIST.md#R-INTERNATIONAL-12) | 整合既有候选，保留关系ID |
| 收益率曲线陡峭化与平坦化 | [收益率曲线陡峭化与平坦化 R-IR-CURVE-SHAPE](../00_start/MECHANISM_IMPORT_LIST.md#R-IR-CURVE-SHAPE) | 新增候选 |
| 人民币国际化 | [人民币国际化 R-RMB-INTERNATIONALIZATION](../00_start/MECHANISM_IMPORT_LIST.md#R-RMB-INTERNATIONALIZATION) | 新增候选 |
| 美元信用与储备多元化 | [美元信用与储备多元化 R-INTERNATIONAL-13](../00_start/MECHANISM_IMPORT_LIST.md#R-INTERNATIONAL-13) | 整合既有候选，保留关系ID |

## 3. 只拆指定三组

| 原组合 | 对象 | 关系／机制 |
|---|---|---|
| 基差与基差交易 | [基差 C-DERIV-15](../00_start/CONCEPT_IMPORT_LIST.md#C-DERIV-15) | [基差交易与融资压力 R-DERIVATIVES-02](../00_start/MECHANISM_IMPORT_LIST.md#R-DERIVATIVES-02) |
| 准备金利率与利率走廊 | [准备金利率 C-MONEY-07](../00_start/CONCEPT_IMPORT_LIST.md#C-MONEY-07) | [利率走廊与隔夜利率传导 R-MONETARY-07](../00_start/MECHANISM_IMPORT_LIST.md#R-MONETARY-07) |
| 金融周期与系统性风险 | [金融周期 C-CREDIT-16](../00_start/CONCEPT_IMPORT_LIST.md#C-CREDIT-16) | [金融周期与系统性风险的积累、扩散 R-BANKING-12](../00_start/MECHANISM_IMPORT_LIST.md#R-BANKING-12) |

其他复合条目保持原组织。assistant 提议额外回补的期货、期权、黄金 ETF、不良贷款、持仓拥挤、行业 ETF 未加入；额外归属调整和其他拆分未实施。原关系目录中已有的相近候选保留既有状态，这不表示采纳了本轮新增建议。

## 随包交付的此前工作区更新

- Event 从七字段摘要改为可独立阅读的事件与分析材料；18个旧观察ID归入8份正文，原ID可定位。
- 课程 PDF 的46页原件、46张1920×1080原页图和文本转录全部保留。课程正文嵌入P2–46共45页，保留老师的图表和评论。
- P20–29 连续组织；P23–26、P27–28 为内部单元，P29–30 保存当时推论；P31 归伊核协议。P17 的精选历史关系时间线完整保留。
- Source 保存原材料、出处、阅读笔记与延伸入口，已有来源增加正文去向。四份完整样例、制作标准、任务单和模板随包保留。
- 本轮同步目录、JSON索引、正文引用、项目记忆和审阅说明。四份成品的经济论证与数字保持，节点角色和引用按最新选取调整。

## 当前覆盖边界

对象正文完成2份，关系正文完成2份；目录不等于已经完成全部正文。关系候选由175变为177，本轮只处理指定8项，未全面重审其余关系。24项旧关系候选的原节点均退出对象目录，已明确标为节点待整理，未自动回补对象。

原有来源覆盖与具体缺口继续保留。本次没有开展新的外部事实研究；课程材料的事实核验状态与原记录一致。校验结果见[VALIDATION.json](VALIDATION.json)。
