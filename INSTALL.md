# 安装说明

## 核心资产（必需，零依赖）

rules/、agents/、hooks/ 不依赖任何第三方，直接拷进你的 `~/.claude/` 就能用。

一条命令：

```bash
bash scripts/install.sh
```

或手动：

```bash
cp -rn rules/*      ~/.claude/rules/
cp -rn agents/*     ~/.claude/agents/
cp -rn hooks/*      ~/.claude/hooks/
# CLAUDE.md 模板：如果 ~/.claude 里还没有，拷一份再填
cp -n  CLAUDE.md    ~/.claude/CLAUDE.md
```

`-n` = 不覆盖你已有的同名文件。如果你想整体替换，去掉 `-n`。

## 第三方 plugin（可选，不装不影响核心）

本仓库**不打包**第三方 plugin，它们各有自己的市场，按需装：

| plugin | 作用 | 来源 |
|---|---|---|
| superpowers | 一批方法论 skill（brainstorming、test-driven-development 等 14 个） | superpowers-marketplace |
| typescript-lsp | TS 语言服务 | claude-plugins-official |
| notion | Notion 集成 | claude-plugins-official |
| n8n-skills | n8n 工作流技能 | n8n-io marketplace |

这些是「增强」不是「必需」。先装核心，用起来觉得缺哪个再装哪个。

## 密钥（重要）

本仓库**不含任何密钥**，也永远不会含。你自己的密钥：

1. 放 `~/.claude/token.txt`（本机私有）
2. 确保 `~/.claude/.gitignore` 排除了它（本仓库 `examples/` 不涉及，但你的 `~/.claude` 需要自己加）：

```gitignore
token.txt
.env
*.key
.claude.json
settings.local.json
```

## 自定义

1. 从 `CLAUDE.md` 模板开始，填空。
2. 看 `examples/CLAUDE.md.example` 了解一个真实用户怎么填。
3. 读 `rules/file-responsibility.md` 理解整套体系的判定逻辑。
4. 删掉你不需要的规则——判据只有一个：「删了会犯错吗？不会就删」。
