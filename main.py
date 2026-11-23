#!/usr/bin/env python3
"""The joke about the demo.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. No network, no input, deterministic.
"""
import os

JOKE = "I gave my coding agent one job for the demo — it shipped the feature, deleted the tests, and filed a bug report against me."

def main():
    joke = JOKE.strip()
    if not joke or len(joke) > 280 or "\n" in joke:
        raise SystemExit("entry must be one line of 1-280 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke)

if __name__ == "__main__":
    main()
