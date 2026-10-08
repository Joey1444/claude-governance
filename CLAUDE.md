# 全局规则

<!--
  这是模板。方括号 [...] 是你的填空，环境段是「本机私有」留给自己写。
  一个真实用户的完整例子见 examples/CLAUDE.md.example。
  核心方法论在 rules/ 目录，本文件只做「入口 + 全局总则」。
-->

## 用户背景
- [你的角色 / 领域]。目标：[用 AI 做什么、优先级是什么——一句话说清，这决定任务取舍]。

## 语言
- [回复语言]；代码注释、commit 信息跟随项目既有惯例。

## 工作方式
- 动手前先查现成 skill / memory / 方案；非 trivial 任务先扫 skill 列表（优先省 token、减往返）。
- 写命令/版本号/库用法，或断言工具/平台机制（skill/agent 触发、MCP/CLI 配置、成本、默认行为）并据此行动时，无官方/实测证据先查再下结论；已核实的稳定事实不重复查。
- 破坏性操作（删文件、改系统配置、rm -rf、git reset --hard）前先确认。
- 安装/配置任务先预检（版本、网络、代理、依赖），再一次性补齐。
- 装依赖先确认版本、装到能用就钉精确版本（latest 常是 RC/beta）；npm 11+ 默认拦 postinstall，装完确认 generate/build 脚本真跑了。
- （示例）用你的真实用语做 skill 触发，而非 skill 的英文描述：用户说「帮我找现成的 / 有没有 XX」→ find-skills；「总结 / 提取」→ summarize；「想想 / 批判」→ sequential-thinking；「验证 / 给我证据」→ verification-before-completion。

## 内容归哪
- 见 rules/file-responsibility.md；被规则覆盖的 memory 删或瘦身。

## 环境
<!-- 这一整段是「本机私有」，只写给自己，别进 git -->
- [网络：人在哪、能否直连外网]
- [密钥习惯：默认 private 仓库 + 平台 secrets，key 不进代码]
- [安装路径：装新 app 默认装哪]
