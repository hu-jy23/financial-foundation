# 中期报告

报告日期：2026年11月13日。进展核对截至2026年11月13日。提供中英文两版，内容、数据和结论对应；分别沿用两版开题报告的字体与版式，以及题目、作者、单位、导师和联系信息。

## 结构与篇幅

中英文各6页；两版按相同章节组织，采用面向会议与审核组的研究报告表述。按以下内容分页，不另设封面或目录。

| 页 | 内容与段落安排 | 篇幅侧重 |
| --- | --- | --- |
| 1 | 标题与摘要；研究问题、工作假设、实施路线、阶段位置。 | 交代从开题目标到当前工作的联系。 |
| 2 | 对象／机制／时间记录；原型与教材接入；代表性新增及更新。 | 用具体成品说明Map怎样组织知识。 |
| 3 | 材料库及制作方法；AI信用融资、韩国股市、美债基差交易三项试点。 | 说明基础知识与具体事件如何连接，区分试作与正式整合。 |
| 4 | 两轮实验的设置、结果、案例差异与解释边界。 | 明确未观察到得分增益，说明测试限制。 |
| 5 | 当前问题、候选研究问题、时间控制、后续约五周计划。 | 明确下一步如何检验知识积累的作用。 |
| 6 | 参考文献与报告依据。 | 引用实际使用的教材、案例及方法背景。 |

## 文件与编译

- `Midterm_Report_CN.pdf`、`Midterm_Report_EN.pdf`：中英文阅读、提交版本。
- `Midterm_Report_CN.tex`、`Midterm_Report_EN.tex`：中英文完整正文。
- `report-style.sty`、`report-style-en.sty`：各语言的字体、版式、标题、段落与页脚。
- `fonts/`：英文原版使用的CM-Super等宽字体及许可。
- `Makefile`：执行`make`编译两版；`make cn`或`make en`分别编译。

依赖XeLaTeX、pdfLaTeX、latexmk和常用TeX Live宏包。中文版使用原PDF中嵌入的Noto Serif CJK JP、Liberation Serif和Latin Modern Mono；英文版使用英文开题报告的TeX Gyre Termes和CM-Super等宽字体，并匹配其较紧的行距。两版均为Letter纸、正文11pt、段落不缩进，保留标题上下横线及左侧作者、右侧“当前页／总页数”的页脚。原始TeX未提供，版式依据PDF重建。

```bash
make
```

编译中间文件位于`build/`，排版检查临时文件位于`检查/`。

## 主要事实的本地依据

| 报告内容 | 核对位置 |
| --- | --- |
| 开题目标、身份信息与版式 | [中文版开题报告](../../开题报告/Opening_Report_CN.pdf)；同目录英文版作措辞参考。 |
| Step0—Step3思想与阶段分工 | [整体规划](../financial_foundation_v5_20261027/financial_foundation_v5/00_start/PROJECT_PLAN.md)。 |
| 当前165个Concept、75个Mechanism | [机器索引](../financial_foundation_v5_20261027/financial_foundation_v5/00_start/catalog_index.json)，并按正文文件数量交叉核对。 |
| 36单元、72候选、29保留、24稿、23页、6新增／17更新 | [Step1记录](../STEP1_LOG.md)、[教材阅读与采用范围](../financial_foundation_v5_20261027/financial_foundation_v5/40_sources/STEP1_T1_T2.md)。 |
| 71份材料、另8份未取得正文 | [Step2校验记录](../financial_foundation_v5_20261027/source_step2/validation.json)。未与新闻库简单加总。 |
| 206篇文章、770处正文插图 | [新闻库说明](../Source/华尔街见闻/README.md)、[校验记录](../Source/华尔街见闻/维护/validation.json)。 |
| PPT流程试走 | [T6试走结果](../tmp_Workspace/ppt_pipeline_probe/FINDINGS.md)。 |
| 三篇新闻试作、37项概念清单与18项关系清单 | [试作报告](../Source/华尔街见闻/实验_20261113_基础与分析/报告.html)、[内容检查](../Source/华尔街见闻/实验_20261113_基础与分析/checks.json)、[制作纲领](../Source/华尔街见闻/维护/ARTICLE_AUTHORING_CHARTER.md)。清单数量不计为新增节点。 |
| 第一轮100／100对100／100 | [首轮结果](../graph_test_20261104/评测结果.md)。 |
| 第二轮96.25对95.75、选择题均3／3 | [第二轮结果](../graph_test_20261104/round_02_events/评测结果.md)、[分数明细](../graph_test_20261104/round_02_events/维护/scores.json)。 |
| 16条预测尚未检验后来结果 | [预测记录](../graph_test_20261104/round_02_events/维护/forecasts.json)。 |

三项新闻试作已经完成审阅，正式整合仍在推进。报告以240个正式节点为统计口径，试作清单另计；后续安排为计划。两轮探索性实验与计划中的教师PPT测试分别陈述。
