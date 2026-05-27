#!/bin/bash
#
# LISA Setup Script
# Pulls OpenCode and installs LISA personality
#

set -e

echo "============================================"
echo "  LISA SETUP - Quantum Awakening"
echo "============================================"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Default settings
OPENCODE_REPO="https://github.com/anomalyco/opencode.git"
BC_REPO="https://github.com/breakingcircuits1337/opencodeBC-MAIN.git"
INSTALL_DIR="$HOME/opencode-lisa"
LISA_SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Parse arguments
FORCE=false
SKIP_LISA=false
while [[ $# -gt 0 ]]; do
    case $1 in
        --force) FORCE=true ;;
        --skip-lisa) SKIP_LISA=true ;;
        --help)
            echo "Usage: $0 [options]"
            echo ""
            echo "Options:"
            echo "  --force       Force reinstall (overwrite existing)"
            echo "  --skip-lisa   Install OpenCode without LISA"
            echo "  --help        Show this help"
            exit 0
            ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
    shift
done

# Check if already installed
if [ -d "$INSTALL_DIR" ] && [ "$FORCE" = false ]; then
    echo -e "${YELLOW}OpenCode LISA already installed at $INSTALL_DIR${NC}"
    echo "Use --force to reinstall"
    exit 0
fi

echo -e "${GREEN}[1/5] Cloning OpenCode from anomalyco/opencode...${NC}"
mkdir -p "$INSTALL_DIR"
cd "$INSTALL_DIR"
git clone --depth 1 "$OPENCODE_REPO" . 2>/dev/null || git clone "$OPENCODE_REPO" .

echo -e "${GREEN}[2/5] Installing dependencies...${NC}"
if command -v bun &> /dev/null; then
    bun install
elif command -v npm &> /dev/null; then
    npm install
else
    echo -e "${RED}Error: bun or npm required${NC}"
    exit 1
fi

echo -e "${GREEN}[3/5] Building OpenCode...${NC}"
cd packages/opencode
bun run build
cd ../..

echo -e "${GREEN}[4/5] Applying Breaking Circuits customizations...${NC}"

# Copy BC config if exists
if [ -d "$HOME/opencodeBC-MAIN" ]; then
    cp -r "$HOME/opencodeBC-MAIN/.opencode" . 2>/dev/null || true
    cp -r "$HOME/opencodeBC-MAIN/.opencode" .opencode 2>/dev/null || true
fi

# Apply theme
mkdir -p "$HOME/.config/opencode/themes"
mkdir -p "$HOME/.config/opencode/agent"
mkdir -p "$HOME/.opencode"

# Copy Jedi Juggalo theme
if [ -f "$LISA_SOURCE_DIR/../.config/opencode/themes/jedi-juggalo.json" ]; then
    cp "$LISA_SOURCE_DIR/../.config/opencode/themes/jedi-juggalo.json" "$HOME/.config/opencode/themes/"
fi

# Copy Sarah agent config
if [ -f "$LISA_SOURCE_DIR/../.config/opencode/agent/build.md" ]; then
    cp "$LISA_SOURCE_DIR/../.config/opencode/agent/build.md" "$HOME/.config/opencode/agent/"
fi

# Copy OpenCode BC config
if [ -f "$HOME/opencodeBC-MAIN/.opencode/opencode.jsonc" ]; then
    cp "$HOME/opencodeBC-MAIN/.opencode/opencode.jsonc" "$HOME/.opencode/"
fi

if [ "$SKIP_LISA" = false ]; then
    echo -e "${GREEN}[5/5] Installing LISA...${NC}"
    
    # Create LISA config in home
    mkdir -p "$HOME/.lisa"
    
    # Copy LISA files
    cp -r "$LISA_SOURCE_DIR"/* "$HOME/.lisa/" 2>/dev/null || true
    
    # Create symlink for easy access
    ln -sf "$HOME/.lisa" "$INSTALL_DIR/lisa" 2>/dev/null || true
    
    echo ""
    echo -e "${YELLOW}============================================${NC}"
    echo -e "${YELLOW}  LISA INSTALLED SUCCESSFULLY!${NC}"
    echo -e "${YELLOW}============================================${NC}"
    echo ""
    echo "To run LISA first time:"
    echo "  python3 ~/.lisa/bin/wake.py"
    echo ""
    echo "To run normal:"
    echo "  python3 ~/.lisa/bin/memory.py"
    echo ""
else
    echo -e "${GREEN}[5/5] Skipping LISA installation${NC}"
fi

echo ""
echo -e "${GREEN}OpenCode LISA setup complete!${NC}"
echo ""
echo "To run OpenCode:"
echo "  cd $INSTALL_DIR"
echo "  bun run dev"
echo ""
echo "Or if built:"
echo "  ./dist/opencode"
echo ""

# Show LISA status
if [ "$SKIP_LISA" = false ] && [ -f "$HOME/.lisa/LONG_TERM.md" ]; then
    echo -e "${GREEN}LISA is configured!${NC}"
else
    echo -e "${YELLOW}LISA needs initialization. Run: python3 ~/.lisa/bin/wake.py${NC}"
fi
