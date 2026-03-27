# DeerFlow Autopilot

[English](./README_en.md) | 中文

这是一个基于上游 DeerFlow 的个人 fork。

- 上游项目：[bytedance/deer-flow](https://github.com/bytedance/deer-flow)

这个仓库不是为了替代上游，而是把 DeerFlow 适配成我日常在 WSL 里做项目开发时更顺手的版本。它保留 DeerFlow 的核心能力，同时加入了更适合本地项目推进的默认配置、工作流和启动方式。

## 这个 fork 做了什么

- 网页会话默认模型顺序调整为 `gpt-5.4-mini`、`gpt-5.4`、`glm-4.7`
- 增加了可从任意项目目录启动的 `deerflow` 本地启动脚本
- 启动时会注入当前项目根目录，让模型知道自己正在处理哪个项目
- 本地 sandbox 放行了 `/mnt/d/QtWorkData` 下的项目读写
- 模型会优先读取并维护项目里的 `todo.md`
- 当任务完成到可交付阶段时，会自动 `git commit` 并推送到远端
- 日志统一写在 DeerFlow 仓库根目录下的 `logs/`

## 如何使用

在任意项目目录中直接运行：

```bash
deerflow
```

如果你想看开发模式，可以显式运行：

```bash
deerflow dev
```

后台启动：

```bash
deerflow daemon
```

日志位置：

- `logs/langgraph.log`
- `logs/gateway.log`
- `logs/frontend.log`
- `logs/nginx.log`

## 推荐工作流

1. 在目标项目目录里启动 `deerflow`
2. 让它先读取或创建 `todo.md`
3. 持续更新待办，逐步推进任务
4. 完成后提交并推送到仓库远端

## 本地启动

如果你需要先检查环境或安装依赖，可以执行：

```bash
./deerflow check
./deerflow install
./deerflow config
```

然后直接启动：

```bash
./deerflow
```
