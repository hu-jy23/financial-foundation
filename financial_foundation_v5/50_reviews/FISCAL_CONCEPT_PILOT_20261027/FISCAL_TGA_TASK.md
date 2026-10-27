# 国债供给机制关联Concepts试产任务 — 2026-10-27

用户要求：GPT-6-Astra，medium，每个subagent最多三个条目；main只新写一个。当前v5已确认163个对象＋71个机制，原完整包版本3。
Workspace: /workspace/scratch/d173ad0a8827/fiscal_pilot/financial_foundation_v5
Review directory: 50_reviews/FISCAL_CONCEPT_PILOT_20261027

每篇是独立完整的heavy concept：定义→内部含义/构成/过程（公式讲清对象、单位和假设）→相近边界→观测口径→自身历史/关键预期→入选关系及角色→可追溯来源/具体缺口。不要只写国债机制的附注，不设机械字数下限；解释需要充分连贯，不能用免责声明串或表格标签代替。历史中事实、当时专业判断、本库条件推演与后来结果分别有归属。重要数字主动检索并核对其真正含义。

先完整阅读：00_start/README.md、AUTHORING_STANDARD.md、BATCH_TASK.md、REVIEW_CHECKLIST.md、NODE_SELECTION_GUIDE.md、templates/CONCEPT_TEMPLATE.md；现有实际利率、期限溢价、政策利率concept；国债供给机制；catalog_index.json中相关ID与关系；40_sources/ACQUISITION_SHORTLIST.md及SOURCES_FISCAL.md。旧成品的解释方法可参考，不能机械抄框架或当作内容上限。

亲自主动web检索并打开原始资料。制度/数字以财政部、联储、央行、IMF等原始资料核对；理论阅读原论文/教材具体章节，研究结论保留条件，不能将机制可能性当已识别的单一因果。来源清单说明真实阅读范围、作者日期、页码/章节、访问问题。仅取得目录不算读正文。可用足够解释概念的历史证据；清楚声明截止，禁止依记忆写当前政策/最新数字。源文件已有材料可用作检索入口，但要自行核关键来源。

本轮不创建/修改Event或Source。新来源直接在每篇文末用独立唯一前缀登记，并正文锚点引用；研究记录放本任务review目录。不得更改共享索引、README、规范、旧正文或另一位作者的文件。其他本批新页路径见OUTPUT_PATHS.json；未写节点链接正式目录锚点；不新增/改名/恢复已排除节点。只链接选定机制且说明本对象角色。

YAML: id,type,title,status:draft,draft_author实际agent路径,model:gpt-6-astra,reasoning_effort:medium,reviewed_by:null,updated:2026-10-27,evidence_as_of真实历史截止,source_ids。标题后简写作者和资料范围。每篇交付时保存完整首次提交稿为review目录中的ID_FIRST_DRAFT.md。main通读逐篇并复核关键来源；有实质问题会退回作者修改，首稿保留。汇报只给文件路径、缺口和需审阅问题，不粘全文。不另派subagent，不上传。

## 你的条目（2篇）
- C-FISCAL-DEFICIT《财政赤字与初级赤字》→10_concepts/C-FISCAL-DEFICIT_fiscal_primary_deficit.md
- C-MONEY-13《财政部一般账户TGA》→10_concepts/C-MONEY-13_treasury_general_account.md
额外输出 FISCAL_TGA_AGENT_NOTES.md。

财政篇重点：收入/支出/利息的预算口径与符号；赤字流量、债务存量、净借款和总发行之间的桥；初级余额和利息、债务/GDP动态的条件及 stock-flow adjustments；名义美元/占GDP、财政年/自然年、现金/权责口径。用实际预算记录和预测版本解释对象。区分美联邦口径与一般政府，必要时简明说明国际对照。
TGA篇重点：联储负债/财政部资产；税收、支出、发债交割如何改变TGA、准备金和私人存款，明确交易对手/资金来源/ON RRP差异，不能每次发债一律按一比一永久抽走准备金。现金缓冲与债务上限阶段、每日财报/周报/季度融资估计的日期口径；2023和2025现金起点/重建与借款对账可选。两个对象边界各自完整，避免重复大段。
