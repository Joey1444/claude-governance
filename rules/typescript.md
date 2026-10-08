---
paths:
  - "**/*.ts"
  - "**/*.tsx"
---
# TypeScript 规范

## 类型
- 导出函数、公共 API、组件 props 必须写显式参数 + 返回类型；局部变量让 TS 推断。
- 对象形状用 `interface`（可扩展/实现）；联合、交叉、映射、工具类型用 `type`。
- 优先字符串字面量联合，不用 `enum`（除非需要互操作）。
- 禁用 `any`；外部/不可信输入用 `unknown` 再 `instanceof` 收窄；依赖调用方的类型用泛型。

## React
- 组件 props 用具名 `interface`，不用 `React.FC`；回调 props 写显式类型。

## 不可变
- 用展开运算符做不可变更新，参数标 `Readonly<T>`，别原地 mutate。

## 错误处理
- async/await + try-catch；catch 的 `error` 是 `unknown`，先 `instanceof Error` 收窄再取 message。

## 校验与数据
- 表单/外部输入用 Zod 校验，从 schema `z.infer` 出类型。
- 数据访问走 repository/服务层，别把调用散落在组件/页面里。
- API 返回统一形状 `{ success, data?, error? }`。

## 红线
- 生产代码禁止 `console.log`，用日志库。
- 密钥只走 `process.env.*`，绝不硬编码进源码。
