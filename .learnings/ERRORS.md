# Errors

## [ERR-20261116-001] original_agent_resume

**Logged**: 2026-11-16
**Priority**: medium
**Status**: resolved
**Area**: infra

### Summary
原作者/root/scale_18连续三次恢复均返回Bad Request，纯文字诊断亦失败。

### Error
`Agent errored: {"detail":"Bad Request"}`

### Context
3749421原作者返修，独立审阅已完成。其他文章继续；已询问用户是否允许新的完整上下文agent接手并保留原署名。

### Suggested Fix
恢复原agent，或在用户同意后由新agent另记返修者。

### Resolution
2026-11-16：用户明确允许新agent接手。/root/revise_3749421完成返修，root复核采用；保留/root/scale_18原署名，另记实际返修者。

## [ERR-20261116-002] historical_writer_unavailable

**Logged**: 2026-11-16
**Priority**: medium
**Status**: resolved
**Area**: infra

### Summary
三个早期试点的原作者produce_ai、produce_korea、produce_basis均返回live agent path not found。

### Context
历史署名可追溯，但原会话agent已不在可恢复列表。审阅完成；用户已明确授权三个完整上下文新agent接替，正在返修，原署名保留。

### Suggested Fix
要求原作者返修时，先确认历史agent可恢复；经明确授权另记接替返修者，保留原署名。

### Resolution
2026-11-16：用户明确批准三篇接替；revise_ai、revise_korea、revise_basis各完成返修，root复核采用。原作者及前次编辑归属保留。
