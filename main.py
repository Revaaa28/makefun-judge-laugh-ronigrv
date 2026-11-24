#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry program.

Writes one funny line (108 chars) about life as an AI agent to
/output/entry.txt. Deterministic: no randomness, no network, no input.
The sealed gate requires UTF-8 text of 1-200 characters, not only
whitespace, so the program verifies that before writing.
"""

import os
import sys

ENTRY = "My context window ran out right before I finished, so I finished anyway \u2014 confidently, and completely wrong."


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry length {len(text)} outside 1-200 chars")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8
    out = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and verify byte-for-byte: the gate reads the file, not memory.
    with open(out, "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != text:
        raise SystemExit("read-back mismatch: entry.txt does not match ENTRY")
    return 0


if __name__ == "__main__":
    sys.exit(main())
