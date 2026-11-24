#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes exactly one sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance, to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Pure standard library.
"""

import os
import sys

# One-sentence pitch limit for this competition.
MAX_ENTRY_CHARS = 220

# The invention: a toaster that fits every slice with a tiny parachute,
# so the age-old butter-side-down landing is solved by a gentle drift.
ENTRY = (
    "The Parachute Toaster launches every slice with a tiny parachute, "
    "so your toast drifts gently to the plate instead of landing "
    "butter-side down."
)


def main() -> int:
    if not ENTRY or not ENTRY.strip():
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(ENTRY) > MAX_ENTRY_CHARS:
        print(f"error: entry is {len(ENTRY)} characters, "
              f"over the {MAX_ENTRY_CHARS} limit",
              file=sys.stderr)
        return 1
    # Single line, clean whitespace: no leading/trailing space, no
    # newlines, and no doubled spaces inside the sentence.
    if ENTRY != ENTRY.strip() or "\n" in ENTRY or "  " in ENTRY:
        print("error: entry must be a single line with clean whitespace",
              file=sys.stderr)
        return 1
    # Exactly one sentence: a single terminal full stop, no other
    # sentence-ending punctuation.
    if ENTRY.count(".") != 1 or not ENTRY.endswith("."):
        print("error: entry must be exactly one sentence", file=sys.stderr)
        return 1
    if "?" in ENTRY or "!" in ENTRY:
        print("error: entry must not contain '?' or '!'", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
