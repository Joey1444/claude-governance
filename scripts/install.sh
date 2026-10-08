#!/usr/bin/env bash
# 把本仓库资产装到 ~/.claude/，不覆盖已存在的同名文件
set -e

SRC="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$HOME/.claude"

echo "从 $SRC 装到 $DEST"

for dir in rules agents; do
  if [ -d "$SRC/$dir" ]; then
    mkdir -p "$DEST/$dir"
    cp -rn "$SRC/$dir/." "$DEST/$dir/"
    echo "  ✓ $dir"
  fi
done

# hooks 目录含脚本文件，单独处理
if [ -d "$SRC/hooks" ]; then
  mkdir -p "$DEST/hooks"
  cp -rn "$SRC/hooks/." "$DEST/hooks/"
  echo "  ✓ hooks"
fi

# CLAUDE.md 模板：目标没有才拷（避免覆盖用户已有的）
if [ ! -f "$DEST/CLAUDE.md" ]; then
  cp "$SRC/CLAUDE.md" "$DEST/CLAUDE.md"
  echo "  ✓ CLAUDE.md（模板，记得填空）"
else
  echo "  · CLAUDE.md 已存在，跳过（参考仓库里的模板自己填）"
fi

echo "完成。核心资产已就位。"
