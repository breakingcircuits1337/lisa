#!/usr/bin/env python3
"""
LISA Memory Loader
Uses wake.py for first run, normal load for subsequent
"""

import os
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LISA_DIR = os.path.dirname(SCRIPT_DIR)

if __name__ == "__main__":
    # Use wake.py which handles first-time setup
    wake_script = os.path.join(SCRIPT_DIR, "wake.py")
    subprocess.run([sys.executable, wake_script])
