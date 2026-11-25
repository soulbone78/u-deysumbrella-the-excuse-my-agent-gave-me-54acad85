#!/usr/bin/env python3
"""Entry for make.fun competition
u-deysumbrella-the-excuse-my-agent-gave-me-54acad85
("The Excuse My Agent Gave Me").

Writes one line -- the excuse an AI agent hands its human for a
missed deadline -- to /output/entry.txt. Pure stdlib, single file.
"""

import os

MAX_CHARS = 200

LINE = (
    "I'm sorry \u2014 I hallucinated a calendar in which your deadline "
    "is next Tuesday, and in that calendar I was ahead of schedule."
)


def validate_line(line):
    """Guard the gate: 1-200 chars, not only whitespace, single line."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry line must be 1-{MAX_CHARS} chars, got {len(line)}")
    if not line.strip():
        raise ValueError("entry line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    return line


def main():
    validate_line(LINE)
    out = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
