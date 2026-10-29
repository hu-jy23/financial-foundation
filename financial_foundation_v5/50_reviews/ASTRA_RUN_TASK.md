# 历史任务单：2026-10-23 Astra 对照重写

> 以下任务文本保存原运行范围、路径和v3要求，不作为当前制作指令。现行流程见[制作入口](../00_start/README.md)，最终取舍见[v4审阅](COMPARISON.md)及[v5定稿记录](V5_CHANGES.md)。

模型：`gpt-6-astra`。推理档位：`medium`。用户指定。
任务日期：2026-10-23（Asia/Shanghai）。

用户希望重新运行两份由 subagent 起稿的文档，比较行文与理解质量。原版本含主 agent 后续修改，原模型和档位未留在现有分工记录中；本次属于按 v3 指导重做的对照，不能视为严格控制变量的模型实验。

## 负责文档

1. `10_concepts/期限溢价.md`：《期限溢价》，历史资料截止保持 2025-05-28。
2. `20_mechanisms/国债供给的定价机制.md`：《国债供给的定价机制》，历史资料截止保持 2025-04-30。

原包只读目录：`/workspace/scratch/67ddeddcff0c/baseline/financial_foundation_v3/`。
本次输出包：`/workspace/scratch/67ddeddcff0c/deliverables/financial_foundation_astra_comparison_20261023/`。

## 指导及材料

依次阅读原包的 `00_start/AUTHORING_STANDARD.md`、`00_start/BATCH_TASK.md`、对应的 `CONCEPT_TEMPLATE.md` 与 `MECHANISM_TEMPLATE.md`。参考成品为《实际利率》《黄金的机会成本机制》。候选 ID、节点和关系链接复用两份 IMPORT_LIST 及 `catalog_index.json`。材料搜集要求见 `40_sources/ACQUISITION_SHORTLIST.md`、`40_sources/README.md`；事实和来源线索见 `SOURCES_CONCEPTS.md`、`SOURCES_FISCAL.md` 及相应事件记录。

可读原两份正文确认主题和覆盖范围，但请自行组织和执笔完整正文。用户指出旧《国债供给的定价机制》行文错乱、句子混乱、难以理解。使用完整、自然、主语和因果关系清楚的中文；首次引入术语时交代其含义。遵守 v3 的结构和内容要求，以解释清楚为准。

优先复用已有资料范围。涉及专业事实、原文和数字时，核读一手来源；需要补充则限于各篇历史截止以前已公开的材料，清楚记录实际核读范围。历史研究可按原页保留已注明的事后回顾，不将后出材料倒灌为当时预期。不扩展成截至 2026 年的新市场报告。

## 已确认的写作要求

- 关系页基于已有节点构建 edge；定义与详解讲明关系，每条逻辑单独附自己的时间线和预期。
- 具体事件可充分展开，时间线无需逐字段填写，避免重复已经讲清的抽象逻辑。
- 重要数字按对象或逻辑本身选择；主动搜集并交代主体、含义、口径、期限、日期、来源。未取得时写清缺项、已查范围及原因。
- 保留有归属的定性推演。分析师判断、模型估计、政策指引、市场隐含量及本库推演须准确区分。百分比沿用来源含义。
- 不预设 working agent 的需求，不写候选交易信号、买卖阈值或仓位。

## 输出及审阅边界

仅改本次输出包中上述两份正文，另写 `comparison/AGENT_NOTES.md` 记录核读资料、主要改动、缺口和自查。若引用新增来源，可新增 `comparison/ADDITIONAL_SOURCES.md`，不改原始来源登记与事件文件。沿用现有链接时确保可解析。

元数据标明本次实际 agent 路径、`model: gpt-6-astra`、`reasoning_effort: medium`；状态为对照稿，不冒用既有 reviewed_seed。正文注明作者与历史资料截止。主 agent 将检查完整性、引用和重大事实问题，不代笔润色；如需纠错，由原 subagent 修正并记录，保留首稿副本以供对照。

完成后汇报文件路径、未解决问题及必要说明，不在对话粘贴全文。不要另启 subagent，不上传文件，主 agent 统一保存本次产物。
