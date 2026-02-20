# LISA Setup Scripts

This directory contains scripts to set up LISA with OpenCode.

## Quick Install

```bash
# Clone LISA
git clone https://github.com/breakingcircuits1337/lisa.git

# Run setup
cd lisa
./scripts/setup.sh
```

## What It Does

1. Clones OpenCode from `anomalyco/opencode` (the original)
2. Installs dependencies
3. Builds OpenCode
4. Applies BC customizations (if available)
5. Installs LISA personality

## Requirements

- bun or npm
- git

## First Run

```bash
# Initialize LISA
python3 ~/.lisa/bin/wake.py
```

## Manual Setup

If you already have OpenCode:

```bash
# Add LISA
cp -r lisa ~/

# Initialize
python3 ~/.lisa/bin/wake.py
```
