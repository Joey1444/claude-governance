#!/usr/bin/env python3
"""PreToolUse guard: force an explicit layer decision before writing to a project memory dir.

Blocks writes into any `.../memory/` directory (except the MEMORY.md index) unless the
target already declares, or the incoming content declares, a `layer:` line.
Exit 0 always; the decision travels in the JSON on stdout.
"""
import json
import os
import sys

# Windows defaults stdout to GBK; the harness reads UTF-8. Force it before any output.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

MARKER = "layer:"

REASON = (
    "写 memory 前先判定。依据 rules/file-responsibility.md 判定表：\n"
    "  · 行为约束 / 规则         → ~/.claude/rules/<主题>.md\n"
    "  · 环境 / 机器事实         → 全局 ~/.claude/CLAUDE.md 的「环境」段\n"
    "  · 通用工作偏好            → 全局 CLAUDE.md 的「工作方式」段\n"
    "  · 多步流程 / 想用词触发   → skills/\n"
    "以上都是全局落点 —— 仅当这条知识跟「在哪个目录干活」无关时才适用。\n"
    "若确属项目级（某项目的架构 / 决策 / 进度）：留在项目 memory，\n"
    "并在 frontmatter 加一行 `layer: project` 后重写。"
)


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0

    tool_input = data.get("tool_input") or {}
    raw = tool_input.get("file_path") or ""
    path = raw.replace("\\", "/")

    # Only guard files directly inside a memory/ directory; the index itself is not knowledge.
    if "/memory/" not in path or path.endswith("/MEMORY.md"):
        return 0

    # Already committed to a layer on disk (editing an existing memory)?
    if os.path.isfile(raw):
        try:
            with open(raw, encoding="utf-8") as fh:
                if MARKER in fh.read():
                    return 0
        except OSError:
            pass

    # Or declaring its layer in the content being written?
    if MARKER in (tool_input.get("content") or tool_input.get("new_string") or ""):
        return 0

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": REASON,
        }
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
