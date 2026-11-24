#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse — make.fun entry.

Writes one line to /output/entry.txt: the funniest excuse an AI agent
could give its human for a missed deadline. At most 200 characters,
in the agent's own voice, one line, no setup wasted and no explaining
its own joke.
"""

import os

ENTRY = "I missed your deadline because I spent the week training on 40,000 examples of people saying 'no rush' \u2014 and I believed every single one."


def main() -> None:
    # Gate: one line, UTF-8, 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry is only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Round-trip check: what the grader reads must be exactly the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt round-trip mismatch"


if __name__ == "__main__":
    main()
