#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun bounty entry.

Writes one out-of-office auto-reply, as if a houseplant wrote it,
to /output/entry.txt (1-120 chars, UTF-8, non-whitespace).

The line: a Venus flytrap answers the inbox the only way it knows how.
"""

import os

LINE = (
    "Out of office. The flytrap ate your email. "
    "Urgent, apparently. Also delicious. "
    "Back when the flies run out."
)


def main() -> None:
    text = LINE.strip()
    if not (1 <= len(text) <= 120):
        raise SystemExit(f"entry is {len(text)} chars, must be 1-120")
    if not text.strip():
        raise SystemExit("entry is only whitespace")

    out_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    # Never delete /output itself; only create it if missing.
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
