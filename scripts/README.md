# LISA Setup Scripts

This directory contains optional setup helpers for integrating LISA with OpenCode.

## Important safety note

`scripts/setup.sh` is side-effecting. It can:

- clone OpenCode into `$HOME/opencode-lisa`,
- install dependencies with Bun or npm,
- build OpenCode,
- copy LISA files into `$HOME/.lisa`,
- write OpenCode config/theme paths under `$HOME`.

For basic LISA inspection, **do not run this script**. Use the plain Python quickstart from the root README instead.

## Optional install

```bash
git clone https://github.com/breakingcircuits1337/lisa.git
cd lisa
./scripts/setup.sh
```

Options:

```bash
./scripts/setup.sh --help
./scripts/setup.sh --skip-lisa
./scripts/setup.sh --force
```

## Requirements

- Python 3 for LISA itself
- git
- Bun or npm only if you use the OpenCode setup script

## First LISA run after optional install

```bash
python3 ~/.lisa/bin/wake.py
```
