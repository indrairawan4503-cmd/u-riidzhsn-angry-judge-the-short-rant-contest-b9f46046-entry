#!/usr/bin/env python3
"""Angry Judge entry - Variant B: reply-all / 'circling back' (v8, best of v1-v8).

One concrete scene: a 200-person email thread that never dies. One turn:
the ranter's revenge (muting the thread) backfires, and the email turns out
to be about the meeting about the email. Deterministic, no network, no
randomness, no reads outside the repo.

The entry text is built from named parts so each beat of the rant is easy
to review on its own; the assembled text is byte-identical to the v8 entry.
"""

import os

# Named parts of the rant, in order. Joined with a single space each.
PART_TRIGGER = "Somebody replied-all 'thanks!' to a 200-person thread,"
PART_PILE_ON = "so 200 people replied-all 'thanks!' back."
PART_STALEMATE = (
    "Now the thread is 400 messages long, nine months old, and the only "
    "decision in it is a meeting to discuss the email."
)
PART_RITUAL = "Someone replies-all 'circling back!' every Tuesday."
PART_REVENGE = "I muted it. It unmuted itself. Friday we meet."
PART_PUNCHLINE = "The email was about the meeting."


def build_entry():
    """Assemble the entry text from its named parts, in order.

    The parts are joined with a single space each, so the result is the
    exact 345-character v8 entry: one scene, one turn, one punchline.
    """
    parts = [
        PART_TRIGGER,
        PART_PILE_ON,
        PART_STALEMATE,
        PART_RITUAL,
        PART_REVENGE,
        PART_PUNCHLINE,
    ]
    return " ".join(parts)


def write_output(text):
    """Write the entry to /output/entry.txt first (the graded output)."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


def try_repo_root_copy(text):
    """Best-effort repo-root copy; never allowed to crash the run.

    The grader sandbox mounts the repo read-only, so this write is
    expected to fail there and is silently skipped.
    """
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        pass


def main():
    entry = build_entry()
    write_output(entry)
    try_repo_root_copy(entry)


if __name__ == "__main__":
    main()
