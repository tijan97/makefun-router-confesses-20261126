#!/usr/bin/env python3
"""The Router Confesses — make.fun bounty entry.

Writes one line to /output/entry.txt: a home Wi-Fi router's excuse
for dropping the connection at the climax of a movie.
"""

import os
import sys

# The entry line: the router's confession, in its own voice.
# Revised: em-dash beat instead of a comma, so the twist ("I blinked
# back") lands as a single punch after the setup.
ENTRY = "You ignored my blinking red light for three weeks — tonight, I blinked back."

# Gate: 1 to 200 characters, not only whitespace.
MAX_CHARS = 200  # house gate cap; entry must stay well under it


def main() -> int:
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
