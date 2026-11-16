# 执行状态

以run.json为机器状态，selection.json为选文。用户选择完整上下文继承，模型档位随主agent，记录inherited_unverified。每篇1agent，3并发、9组；全部27篇需完成，不在首组结束任务。

第1组01/02/03已审阅采用并接入唯一工作图workspaces/step2_articles/graph：新增GLD子概念及资源挤出关系，工作图254节点。对应agents scale_01/02/03已结束。drafts已删除，delivery/review保留。

第2组04/05/06正在制作，agents scale_04/05/06已全继承启动，归属均批准。本组基线/tmp/scaling_wave2_base.json；先读各篇proposal/decision。

工具：integrate.py ARTICLE_ID /tmp/scaling_waveN_base.json（审阅采用后调用，禁止正式graph写入）；sync_registry.py同步待整合索引；build_report.py输出报告.html、增量清单.md。不要运行旧step2_articles/sync_catalog.py，它只支持最初三篇，会遗漏新增注册。

每篇交付需主agent逐篇阅读（新页全文，旧页与组基线diff；预览时去掉图片路径行可省输出，保留图表本身在最终成品）。整合后删除该篇drafts/previews临时产物，避免本地链接测试把临时位置当最终位置；未整合不得删。

第1组工作图validate.py已通过（1859链接；正式图知识未变，仅此前授权的3份说明修改）。首次链式验证进程被SIGTERM143，单独重跑通过。当前需要完成第1组Git检查点，随后继续处理第2组并依次完成第3—9组。

每组审阅完成后生成下一组/tmp/scaling_waveN_base.json（保存当前工作图全部MD正文），继而各拉新agent。统一读RUN_GUIDE及各篇TASK，先提案、主agent归属后继续全文。涉及并发旧页改动使用基线合并；同名新对象统一ID。每组docs/STEP2_LOG只写简短实际增量。
