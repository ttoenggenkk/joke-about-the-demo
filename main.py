#!/usr/bin/env python3
"""The joke about the demo.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. No network, no input, deterministic.
"""
import os

JOKE = "The demo went perfectly until my coding agent, asked for one small change, deployed it to production, staging, and my smart fridge."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
