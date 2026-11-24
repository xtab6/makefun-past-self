#!/usr/bin/env python3
"""Two Lines to Your Past Self entry (make.fun, program/v1).

Writes the two-line warning to /output/entry.txt. Deterministic, stdlib
only, no network access. The output is byte-identical on every run.

Line 1 warns the past self about one specific moment (31 August, the quoted
refusal, one more cup of tea). Line 2 traces the cause and effect: that
refusal becomes the last thing ever said to her, and it changes behaviour.
"""

import os

ENTRY = (
    "On 31 August, don't tell your mother \"I'm too busy\" when she asks "
    "you to stay for one more cup of tea.\n"
    "That refusal becomes the last thing you ever say to her, and it is "
    "why you never let being busy answer for you again."
)


def validate(entry):
    """Gate the entry the way the sealed scorer does: UTF-8 text, 1-280
    characters, exactly two lines, one sentence per line."""
    if not (1 <= len(entry) <= 280):
        raise ValueError("entry must be 1-280 characters, got %d" % len(entry))
    lines = entry.split("\n")
    if len(lines) != 2 or not all(line.strip() for line in lines):
        raise ValueError("entry must be exactly two non-blank lines")
    if any(line.count(".") != 1 for line in lines):
        raise ValueError("each line must be exactly one sentence")
    return entry


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
