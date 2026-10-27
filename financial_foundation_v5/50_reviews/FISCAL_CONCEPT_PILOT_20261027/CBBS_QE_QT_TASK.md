# 国债供给机制关联Concepts试产任务 — 2026-10-27

用户要求：GPT-6-Astra，medium，每个subagent最多三个条目；main只新写一个。当前v5已确认163个对象＋71个机制，原完整包版本3。
Workspace: /workspace/scratch/d173ad0a8827/fiscal_pilot/financial_foundation_v5
Review directory: 50_reviews/FISCAL_CONCEPT_PILOT_20261027

每篇是独立完整的heavy concept：定义→内部含义/构成/过程（公式讲清对象、单位和假设）→相近边界→观测口径→自身历史/关键预期→入选关系及角色→可追溯来源/具体缺口。不要只写国债机制的附注，不设机械字数下限；解释需要充分连贯，不能用免责声明串或表格标签代替。历史中事实、当时专业判断、本库条件推演与后来结果分别有归属。重要数字主动检索并核对其真正含义。

先完整阅读：00_start/README.md、AUTHORING_STANDARD.md、BATCH_TASK.md、REVIEW_CHECKLIST.md、NODE_SELECTION_GUIDE.md、templates/CONCEPT_TEMPLATE.md；现有实际利率、期限溢价、政策利率concept；国债供给机制；catalog_index.json中相关ID与关系；40_sources/ACQUISITION_SHORTLIST.md及SOURCES_FISCAL.md。旧成品的解释方法可参考，不能机械抄框架或当作内容上限。

亲自主动web检索并打开原始资料。制度/数字以财政部、联储、央行、IMF等原始资料核对；理论阅读原论文/教材具体章节，研究结论保留条件，不能将机制可能性当已识别的单一因果。来源清单说明真实阅读范围、作者日期、页码/章节、访问问题。仅取得目录不算读正文。可用足够解释概念的历史证据；清楚声明截止，禁止依记忆写当前政策/最新数字。源文件已有材料可用作检索入口，但要自行核关键来源。

本轮不创建/修改Event或Source。新来源直接在每篇文末用独立唯一前缀登记，并正文锚点引用；研究记录放本任务review目录。不得更改共享索引、README、规范、旧正文或另一位作者的文件。其他本批新页路径见OUTPUT_PATHS.json；未写节点链接正式目录锚点；不新增/改名/恢复已排除节点。只链接选定机制且说明本对象角色。

YAML: id,type,title,status:draft,draft_author实际agent路径,model:gpt-6-astra,reasoning_effort:medium,reviewed_by:null,updated:2026-10-27,evidence_as_of真实历史截止,source_ids。标题后简写作者和资料范围。每篇交付时保存完整首次提交稿为review目录中的ID_FIRST_DRAFT.md。main通读逐篇并复核关键来源；有实质问题会退回作者修改，首稿保留。汇报只给文件路径、缺口和需审阅问题，不粘全文。不另派subagent，不上传。

## 你的条目（3篇）
- C-MONEY-CBBS《央行资产负债表》→10_concepts/C-MONEY-CBBS_central_bank_balance_sheet.md
- C-POL-QE《量化宽松QE》→10_concepts/C-POL-QE_quantitative_easing.md
- C-POL-QT《量化紧缩QT》→10_concepts/C-POL-QT_quantitative_tightening.md
额外输出 CBBS_QE_QT_AGENT_NOTES.md。

CBBS重点：资产/准备金/现金/TGA/逆回购/其他负债与资本的会计结构；买券、贷款、财政现金转移和现金需求的示意分录；准备金不直接等于公众存款或可贷资金；负债构成、付息成本/递延资产和估值口径；H4.1时点/均值与国别差异。
QE重点：作为政策安排的资产购买、流量/存量/再投资/期限结构；非银行卖券与银行卖券会计差异，组合再平衡/信号/市场运作渠道；购债、常规储备管理购买和危机流动性工具的边界；历史政策安排与原论文效果区分。
QT重点：到期不续作/主动出售、上限/实际赎回、机构MBS提前偿还、负债调整路径；准备金/ONRRP/TGA背景；缩表减速和终止怎样与政策利率分开理解；2017—2019和2022—2025实际安排，可止于明确历史日期；财政部私人净市场借款已含SOMA赎回，不能重复加QT。
三篇共享定义需一致，但各篇自足，互相指路分工。研究每篇至足够质量再交付，不为赶工缩成摘要。
