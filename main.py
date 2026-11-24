#!/usr/bin/env python3
"""Angry Judge entry - Variant B: reply-all / 'circling back' (v8, best of v1-v8).

One concrete scene: a 200-person email thread that never dies. One turn:
the ranter's revenge (muting the thread) backfires, and the email turns out
to be about the meeting about the email. Deterministic, no network, no
randomness, no reads outside the repo.
"""

import os

ENTRY = (
    "Somebody replied-all 'thanks!' to a 200-person thread, so 200 people "
    "replied-all 'thanks!' back. Now the thread is 400 messages long, nine "
    "months old, and the only decision in it is a meeting to discuss the "
    "email. Someone replies-all 'circling back!' every Tuesday. I muted it. "
    "It unmuted itself. Friday we meet. The email was about the meeting."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Optional repo-root copy only; the grader sandbox mounts the repo
    # read-only, so this must never crash the run.
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
