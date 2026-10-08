# 内容归哪（职责划分）

## 判定表
- 全局总则（你是谁 / 语言 / 工作方式 / 环境）→ CLAUDE.md（入口；规则细节索引到 rules/）
- 按主题的行为约束 → rules/<主题>.md（一主题一文件；只对某类文件生效的带 paths: 按需加载）
- 多步可复用流程 / 想用词触发 → skills/
- 隔离副任务（审查/安全/测试）→ agents/（只回摘要）
- 必须无条件阻断或放行 → settings.json 的 permissions / hooks（硬约束，不是靠自觉）
- 具体项目的「事实/教训」→ 项目 memory/（本机私有、只载索引、按需）

## 记忆 vs 规则
- CLAUDE.md/rules = 你写的「指令/规则」：进 git、团队共享、每次加载
- memory = Claude 自动写的「学习/事实」：本机私有、只载索引、按需
- 反复纠正 / 团队决策才固化进 rules/CLAUDE.md；调试怪癖、会变的模式留该项目 memory
- 跨项目复用的事实（本机工具 / 环境 / 通用偏好）→ 全局 CLAUDE.md 对应段；不要写进项目 memory

## 密钥（API key / token / PAT）
- 本地备份：`~/.claude/token.txt`（本机私有，不进 git）。
- 使用处用平台 secret：n8n credential、GitHub Actions secrets、MCP 配置的 env/headers。
- 绝不进代码、绝不进 rules/CLAUDE.md/memory（这些可能进 git 或团队共享）。
- **文件层兜底**：密钥文件要 gitignore 防护（全局 `.gitignore` 排除 `token.txt`/`.env`/`*.key` 等）——「不进代码」不等于「不进 git」，两层都要。

> 同名不混淆：code-review 标准在 rules/code-review.md，跑流程用 /code-review skill，隔离执行用 code-reviewer agent。

## 精简（铁律）
- memory/rules 只写「换会话后还需要、代码/git 推不出来的」关键事实或硬约束。
- 一句话能说清的硬约束，不写散文、不写案例过程；单次案例下沉 memory，别塞全局规则。
- 过筛判据：移除这条 Claude 会犯错吗？不会就删。
- 总量红线：CLAUDE.md <200 行（最佳 ~60）；skill 正文 <500 行。但 minimal ≠ short——规则削太薄会让行为不正确，200 行是平衡点、不是越短越好。
- 事实/方案变了就标 DEPRECATED 或直接删，别留「已变但没标」的过时信息。
- 定期体检瘦身（删重复、删过时、删被覆盖的），别让冗余累积。
