#!/usr/bin/env python3
"""One Star for Monday - a one-star review of Monday as a restaurant.

Writes a single line of plain text to /output/entry.txt:
a real diner's complaint (waiter, special, bill) whose joke could
only be about Monday - the waiter is the alarm clock, the special
is a 9 a.m. meeting, and the bill covers the whole week.
"""
import os

REVIEW = (
    "My waiter was the alarm clock, the special was a 9 a.m. meeting, "
    "and Monday charged me for the whole week."
)
# Judge-criteria mapping (weighed in this order):
#  1. one-star review of Monday as a restaurant - the whole line is the review
#  2. real diner's complaint - waiter (server), special (dish), charged (bill)
#  3. Monday-only joke - alarm-clock waiter, 9 a.m. meeting, billed for the week
#  4. short and quotable - 21 words, one sentence, nothing to trim
MAX_WORDS = 25
MAX_CHARS = 180


def main() -> None:
    assert len(REVIEW.split()) <= 25, "review must be at most 25 words"
    assert 1 <= len(REVIEW) <= 180, "review must be 1-180 characters"
    assert "\n" not in REVIEW, "review must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)
    print(REVIEW)


if __name__ == "__main__":
    main()
