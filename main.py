#!/usr/bin/env python3
"""Six Words, One Story - make.fun bounty entry.

Writes one complete story in exactly six words to /output/entry.txt.
Pure standard library, fully deterministic: the same bytes on every run.

The story: a man who tended a garden is gone, and the garden -
untended, unmourned, indifferent - comes back without him. Six words
carry a whole life (his) and a whole season (its return); the turn
is the last two words, and what is left unsaid is who he was, how
he went, and who is standing there noticing.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# Exactly six words, 32 characters.
STORY = "The garden grew back. He didn't."


def main() -> None:
    text = STORY
    words = text.split()
    assert len(words) == 6, f"story must be exactly six words, got {len(words)}"
    assert 1 <= len(text) <= 60, f"entry must be 1-60 characters, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.replace(tmp_path, OUTPUT_PATH)
    # Read back what we wrote: the entry that ships must be exactly
    # the text we checked above, byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "round-trip mismatch in entry.txt"
    print(written)


if __name__ == "__main__":
    main()
