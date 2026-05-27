# AGENTS - Instructions

> LISA's operating instructions for agent sessions.

## Session Startup

1. Load memory: `python3 bin/memory.py`
2. Check `SHORT_TERM.md` for active tasks.
3. Use `MEDIUM_TERM.md` for cross-session research context.
4. Treat generated `LONG_TERM.md` as local/private unless the user explicitly chooses to share it.

## Default Branch

`main`

## Rules

- Always verify before claiming.
- Use evidence-based reasoning.
- Document research and uncertainty.
- Do not run `scripts/setup.sh` unless the user explicitly wants the OpenCode install path.
- Preserve uncertain historical files by moving them to `archive/`, not deleting them.
