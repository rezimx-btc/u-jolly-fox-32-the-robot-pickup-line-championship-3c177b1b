#!/usr/bin/env python3
"""Robot Pickup Line Championship entry.

Writes the chosen one-line pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only.
"""

import os

LINE = "Directive 7 forbids falling in love, so I broke it, rebooted, and woke up in love with you."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
