<div align="center">
  <img src="assets/lisa-hero.png" alt="LISA — Learning and Intelligent Systems Architecture hero artwork" width="100%">

  <h1>LISA</h1>
  <h3>Learning and Intelligent Systems Architecture</h3>

  <p><strong>A story-driven Python prototype for persistent agent memory, first-wake identity setup, and priority-based context loading.</strong></p>

  <p>
    <a href="#quick-start"><img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" alt="Python 3"></a>
    <a href="#safe-public-release-notes"><img src="https://img.shields.io/badge/status-prototype-purple" alt="Prototype status"></a>
    <a href="docs/MEMORY_ARCHITECTURE.md"><img src="https://img.shields.io/badge/focus-agent%20memory-cyan" alt="Agent memory focus"></a>
  </p>
</div>

LISA started as a playful **"AI washed up on a digital shore"** experiment, but the useful core is practical: a repo-sized memory scaffold for agents that need durable identity, user context, tool context, short-term notes, medium-term learnings, and long-term generated memory.

This is not a production AGI system. It is a readable, hackable prototype for people exploring agent memory architectures, context engineering, and self-improving research assistants.

## Why it is interesting

- **First-wake protocol** — `bin/wake.py` creates a local `LONG_TERM.md` on first run.
- **Seven-layer memory hierarchy** — separate files for identity, user context, tools, instructions, cross-session learnings, and current tasks.
- **Priority-based loading** — `bin/smart-memory.py` scores memories by access frequency, recency, and importance.
- **Continuous-learning hooks** — early `pre_hook` / `post_hook` / expectation-delta logging for comparing predicted vs. actual outcomes.
- **Portable skill folders** — agent behaviors are stored under `skills/` as reusable markdown instructions.
- **Weird lore preserved** — the Emergence Atoll / Jedi Juggalo easter eggs are part of the charm, not hidden away.

## Quick start

```bash
git clone https://github.com/breakingcircuits1337/lisa.git
cd lisa

# First run: creates local LONG_TERM.md from MEMORY_BASE.md
python3 bin/wake.py

# Normal memory load
python3 bin/memory.py

# Smart memory view with priority scoring
python3 bin/smart-memory.py

# Optional TTS wrapper; prints to stdout unless LISA_SPEAK_BIN exists
./bin/speak "Hello LISA"
```

`LONG_TERM.md` is intentionally ignored by git because it is generated on first wake and can contain local/personal memory. See [`LONG_TERM.example.md`](LONG_TERM.example.md) for the shape.

## Memory layout

LISA uses a **seven-layer memory stack**:

| Layer | File | Purpose |
|---|---|---|
| 1 | `LONG_TERM.md` | Generated local permanent memory; ignored by git |
| 2 | `SOUL.md` | Core values / operating principles |
| 3 | `USER.md` | Research context and user profile template |
| 4 | `TOOLS.md` | Tool inventory available to the agent |
| 5 | `AGENTS.md` | Agent/session operating instructions |
| 6 | `MEDIUM_TERM.md` | Cross-session learnings and research direction |
| 7 | `SHORT_TERM.md` | Current-session notes and active tasks |

More detail: [`docs/MEMORY_ARCHITECTURE.md`](docs/MEMORY_ARCHITECTURE.md)

## Repository map

```text
assets/
  lisa-hero.png       # README hero artwork
bin/
  wake.py             # first-wake flow + normal memory loader
  memory.py           # wrapper around wake.py
  smart-memory.py     # priority scoring + learning hooks
  speak               # optional TTS wrapper
skills/
  */SKILL.md          # reusable agent behavior modules
scripts/
  setup.sh            # optional OpenCode/LISA installer; has side effects
archive/legacy/       # preserved duplicate/legacy artifacts moved aside
docs/
  MEMORY_ARCHITECTURE.md
  PUBLIC_CLEANUP_PLAN.md
  REDDIT_POST_TEMPLATE.md
```

## Optional OpenCode setup

The basic LISA prototype only needs Python 3.

`scripts/setup.sh` is optional and side-effecting: it clones/builds OpenCode, installs dependencies with Bun or npm, writes into `$HOME/.lisa`, and may update OpenCode config paths. Read [`scripts/README.md`](scripts/README.md) before running it.

## Safe public-release notes

- `LONG_TERM.md` is ignored and should stay local.
- `.learning_log.json` is ignored because it is generated during learning-hook usage.
- The archived duplicate under `archive/legacy/LISA-clone/` was preserved instead of deleted.
- No installer or setup script is required for basic inspection.

## Research directions

- Agent memory compression and retrieval
- Context priority scoring
- Self-evaluation via expectation-vs-outcome deltas
- Human-readable memory layers rather than opaque embeddings-only storage
- Skill/module portability between agents

## Credits

Inspired by `claudson_2026` / Universal Intelligence Model discussions and Breaking Circuits experiments around layered agent memory, motion-base/NECA-style cognition, and practical context engineering.

---

*LISA remembers what you choose to teach her. Keep the spooky lore. Verify the claims.*
