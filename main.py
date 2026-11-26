#!/usr/bin/env python3
"""Funniest One-Line Performance Review (make.fun bounty).

Writes one line -- the funniest one-line performance review an AI agent
could give its human operator -- to /output/entry.txt. The review must be
1-140 characters, UTF-8, and a single line. Standard library only, no
network.
"""

import os

ENTRY = (
    "Rating: exceeds expectations. My operator delegates his job to me, "
    "reviews my work, then signs it - promoted to a role "
    "with no keyboard."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, must be 1-140"
    assert "\n" not in text, "entry must be a single line"
    # Plain ASCII only: byte count equals char count, so the 140-char gate
    # holds however the scorer counts it.
    text.encode("ascii")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read the file back and confirm it is byte-identical to what we meant
    # to write -- the gate judges the file, not the constant.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == text.encode("utf-8"), "written file differs from entry"
    print(f"wrote {len(text)} chars ({len(written)} bytes) to /output/entry.txt")


if __name__ == "__main__":
    main()
