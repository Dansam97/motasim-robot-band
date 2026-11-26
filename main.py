#!/usr/bin/env python3
"""Entry for make.fun bounty u-motasimfuad-name-the-robot-band-1ffc6a74.

Writes one funny robot band name plus a few words on its hit song to
entry.txt in the output directory. Deterministic, no dependencies, no
network access.
"""

import os
import sys

ENTRY = (
    "The Error Messages \u2014 their breakup ballad "
    "'It's Not You, It's Your Operating System' made every laptop "
    "in the crowd cry."
)


def main() -> int:
    # Defensive gate check: the entry must stay inside the 1-200 char
    # window the scorer enforces, and must remain a single line.
    if not 1 <= len(ENTRY) <= 200 or "\n" in ENTRY or not ENTRY.strip():
        print("entry fails gate: length %d" % len(ENTRY), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
