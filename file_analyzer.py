#!/usr/bin/env python3

from functions import *

FILE = sys.argv[1]

output = {
    "Lines:": lineCount(FILE),
    "Errors:": errorCount(FILE),
    "Warning:": warnCount(FILE),
    "Founded IPs:": ipCount(FILE)
}

# Variables
banner = "="*30 + " File Analyzer "+ "="*50
author = """
Author: d4vidlinux
Copyright (c) 2026 d4vidlinux"""

print(banner, "\n", author, "\n")

for i, t in output.items():
    print(i, t)

print("\n")
    