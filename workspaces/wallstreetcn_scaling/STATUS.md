# 当前执行状态

用户要从原3篇扩至30篇：新增27篇必须全部执行；每篇1个完整继承agent，不在中间组结束任务。模型/档位继承，inherited_unverified。

已采用新增01—18，共18/27；工作图264节点（基准252，本轮新增12）。总材料21/30。

第7组19/20/21已启动，agents scale_19/20/21。19/21基线/tmp/scaling_wave7_base.json；20需用/tmp/scaling_article20_base.json（18原油页接入后另存）。22—27仍queued。状态以run.json为准。

主agent必须审阅每份新稿/旧页diff后用integrate.py ARTICLE /tmp/scaling_waveN_base.json接入workspaces/step2_articles/graph。正式graph只读。sync_registry.py更新全部待整合索引；build_report.py输出报告.html与增量清单.md；validate_run.py检查采用稿、节点、父项和链接。不要运行旧step2_articles/sync_catalog.py，它只支持原3篇，会漏scaling注册。

每组完成后删已采用篇drafts/previews临时产物，保留delivery/review/decision/proposal/TASK；禁止删除尚未审阅稿。下一组启动前保存/tmp/scaling_waveN_base.json（当前工作图所有MD正文），每篇按RUN_GUIDE先提案、协调归属、原agent继续全文。

Git检查点：第1组14351ab，第2组5ffb49b，第3组278d2f7，第4组253a4dc，第5组a435e3c。按已完成组路径暂存，不能把下一组未审稿一起提交。阶段记录docs/STEP2_LOG简写实际增量。最后完成30篇报告、检查全部链接与离线浏览后交付，不整合正式graph。
