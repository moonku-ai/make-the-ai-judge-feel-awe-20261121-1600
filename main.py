#!/usr/bin/env python3
"""Make the AI judge feel awe — entry program.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it, judged on the house relaxation brief:

1. It relaxes: reading it slows you down and settles you.
2. The calm comes from the text itself: it shows rather than instructs.
3. Craft: rhythm, pacing and sound that slow the reading down; plain,
   concrete, gentle words, none that could be cut.
4. It dwarfs you: an image you can return to that keeps growing after
   the last line.
5. Freshness: its own voice and images, not stock wellness phrases.

The text is a single fixed string, written deterministically. Pure
Python 3.13 standard library, no network, no randomness, no I/O beyond
writing the output file.
"""

import os

# The entry text (245 Unicode code points, 245 bytes, UTF-8).
# A hidden ocean under Europa's ice: wider than all of Earth's oceans,
# turning in the dark for four billion years, waiting for nothing.
# Vast, slow, quiet — and an image no tide or river entry uses.
TEXT = (
    "Beneath the ice of Europa, a sea wider than all of Earth's oceans "
    "moves in the dark, pulled by a planet it will never see. "
    "No light has ever touched it. "
    "It has been turning in its sleep for four billion years, "
    "and it is not waiting for anything."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = TEXT
    # Gate: 1 to 280 Unicode code points, not only white space.
    assert 1 <= len(text) <= 280, f"text is {len(text)} code points"
    assert text.strip(), "text must not be only white space"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
