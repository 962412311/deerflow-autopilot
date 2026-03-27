# DeerFlow Autopilot

English | [中文](./README.md)

This is a personal fork of the upstream DeerFlow project.

- Upstream: [bytedance/deer-flow](https://github.com/bytedance/deer-flow)

This fork adapts DeerFlow for my daily local development workflow in WSL. It keeps the upstream core, but adds a more opinionated local setup for project work, task tracking, and repo-friendly startup behavior.

## What Changed

- Default web-session model order is `gpt-5.4-mini`, `gpt-5.4`, then `glm-4.7`.
- A repo-local `deerflow` launcher works from any project directory.
- The current project root is injected into the agent prompt.
- Local sandbox access is widened for projects under the configured workspace roots.
- The agent is instructed to keep `todo.md` current.
- Completed work is committed and pushed when a milestone is ready.
- Logs stay under the DeerFlow repository root.

## Usage

Run DeerFlow from any project directory:

```bash
deerflow
```

Foreground development mode:

```bash
deerflow dev
```

Background daemon mode:

```bash
deerflow daemon
```

Logs:

- `logs/langgraph.log`
- `logs/gateway.log`
- `logs/frontend.log`
- `logs/nginx.log`

## Workflow

1. Start DeerFlow from the project you want to work on.
2. Let it read or create `todo.md`.
3. Keep the todo list current as work progresses.
4. Commit and push when the task is ready to ship.

## Local Setup

```bash
./deerflow check
./deerflow install
./deerflow config
./deerflow
```

