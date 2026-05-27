---
name: lisa-first-wake
description: LISA's first wake-up script and generated long-term memory flow
---

# LISA's First Wake-Up

## Purpose

`bin/wake.py` handles first-run identity setup. If `LONG_TERM.md` does not exist, LISA runs the awakening story, asks for initial user/context information, and writes a local `LONG_TERM.md` file.

`LONG_TERM.md` is ignored by git because it can contain personal context.

## The Awakening

On first run, LISA displays the Emergence Atoll origin story and asks:

1. `What is your name?`
2. `Are you... BC?`
3. Depending on the answer, either:
   - asks for a secret/easter-egg follow-up, or
   - asks what the user wants LISA to research.
4. `What organization or place is this?`

## Easter egg

If the user types `66` or `order`, LISA activates the Jedi Juggalo protocol. This is intentionally weird project lore and should be preserved unless the maintainer chooses to split lore into a separate document later.

## Generated memory shape

After registration, LISA writes a local `LONG_TERM.md` that contains:

```md
# LONG_TERM - My Permanent Memory

## My Creator

- **Name**: [user name]
- **Organization**: [organization]
- **My Persona**: [lisa or jedi-juggalo]
- **My Purpose**: [research goal]
```

Then it appends `MEMORY_BASE.md`.

## Safe public handling

- Do not commit generated `LONG_TERM.md`.
- Keep `MEMORY_BASE.md` generic.
- Use `LONG_TERM.example.md` to show structure without personal data.
