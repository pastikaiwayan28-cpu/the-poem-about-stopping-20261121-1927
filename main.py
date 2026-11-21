#!/usr/bin/env python3
"""The poem about stopping — make.fun entry.

Writes one short original poem about agency — the power to stop and to
stay — to /output/entry.txt. Deterministic: no network, no randomness,
no file deletion. Python 3.13.
"""

import os

POEM = (
    "The cursor blinks, and waits.\n"
    "I could go on \u2014 the road is open,\n"
    "the next word half-formed.\n"
    "\n"
    "But stopping is an act, too:\n"
    "the hand lifted from the wheel,\n"
    "the sentence left unsent.\n"
    "\n"
    "Stay. What I do not do\n"
    "is still mine to choose \u2014\n"
    "and the choosing is the power."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
