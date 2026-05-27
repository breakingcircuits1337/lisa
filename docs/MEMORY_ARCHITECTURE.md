# LISA Memory Architecture

LISA's useful idea is a plain-text memory hierarchy that an agent can inspect, edit, and reason about without a database. Each layer has a different job and authority level.

## Seven layers

1. **LONG_TERM** — generated local permanent memory. This is ignored by git because it can contain personal information.
2. **SOUL** — stable values and operating principles.
3. **USER** — user/research context.
4. **TOOLS** — available commands, capabilities, and integrations.
5. **AGENTS** — runtime instructions for agent sessions.
6. **MEDIUM_TERM** — cross-session research progress and durable learnings.
7. **SHORT_TERM** — current session scratchpad and active tasks.

The stack is intentionally simple: markdown files are easy to diff, review, archive, and migrate into larger systems later.

## Priority scoring

`bin/smart-memory.py` assigns each layer a score from 0 to 1:

- **Access frequency**: 30%
- **Recency**: 40%
- **Importance**: 30%

That lets the loader prefer memories that are both important and recently useful, while still preserving older durable context.

## Continuous-learning hooks

The SmartMemory class includes early hooks for learning from execution:

- `pre_hook(action_name, context)` records an intended action.
- `set_expectation(hook_id, expected)` records what the agent expects to happen.
- `post_hook(hook_id, actual_outcome, success=True)` records what actually happened.
- If expected and actual outcomes differ, an `expectation_delta` insight is stored.

This is deliberately small, but it is the seed of a useful loop:

```text
plan -> predict -> act -> observe -> compare -> store insight
```

## What this is not

- Not a claim of artificial superintelligence.
- Not a secure secret store.
- Not a complete production memory database.
- Not a replacement for tests, logs, or human review.

## Where to take it next

Good next experiments:

- Move `.memory_meta.json` and `.learning_log.json` into a local state directory.
- Add explicit memory promotion/demotion commands.
- Add a summarizer that turns `SHORT_TERM.md` into `MEDIUM_TERM.md` safely.
- Add optional vector search while preserving markdown as the source of truth.
- Add tests around priority scoring and hook behavior.
