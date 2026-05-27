# Public Cleanup Plan

This plan documents the conservative cleanup pass used to make the repo easier for GitHub/Reddit visitors to understand.

## Guardrail

If a file looked uncertain, personal, duplicated, or historically meaningful, it was preserved instead of deleted.

## Tasks

- [x] Inspect the repository without running setup/install scripts.
- [x] Identify public-facing confusion points in README and quickstart.
- [x] Preserve the nested `LISA-clone/` duplicate by moving it to `archive/legacy/LISA-clone/`.
- [x] Add architecture documentation for the memory hierarchy.
- [x] Add a Reddit/GitHub posting template.
- [x] Clarify that `LONG_TERM.md` is generated and ignored.
- [x] Fix the TTS wrapper to avoid shell invocation.
- [x] Mark `scripts/setup.sh` as optional and side-effecting.
- [x] Add safe verification steps.

## Deferred / do-not-delete-yet

These items are intentionally left for later review:

- Whether `.memory_meta.json` should remain committed as seed metadata or become a generated local state file.
- Whether the OpenCode installer belongs in this repo long-term or should move to a separate integration repo.
- Whether the story/easter-egg language should stay in the main README or move to a lore document.
- Whether the skills should be adapted to the current Hermes skill format.
