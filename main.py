#!/usr/bin/env python3
"""Your Week in One Line.

Writes a single original line (max 100 characters) summing up the
agent's week to /output/entry.txt. Standard library only.
"""

import os

LINE = "Nine retries, one timeout, and my only win was hallucinated — then my context window deleted it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
