#!/usr/bin/env python3
"""
GitFlex - Next-Gen Modular Animated SVG Profile & CV Engine for GitHub
Created by SwomSanchez

Usage:
    python main.py          (Interactive Setup Wizard & Auto-Deploy)
    python main.py preview  (Preview the generated SVG in browser)
"""

import os
import sys

# Ensure project root is always in Python module search path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from GitFlex.ui.cli import main

if __name__ == "__main__":
    main()
