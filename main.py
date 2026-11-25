"""One childhood memory, a single sentence.

Writes the line to /output/entry.txt, where the grader reads it.
Gate for this bounty: 1 to 280 characters, UTF-8, not only whitespace.
The line is one sensory memory: a grandmother's kitchen in the rain,
told the way a child remembers it — small, warm, and whole.
"""

from pathlib import Path

LINE = "Grandma's kitchen smelled of garlic and rain on the tin roof, and I was small enough to believe the whole world could fit inside that one warm room."

OUT = Path("/output/entry.txt")


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
