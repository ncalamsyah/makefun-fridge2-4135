"""Fridge Roast: One Line, Biggest Laugh — make.fun bounty entry.

Writes a single roasting one-liner (1..200 chars, no newlines) to /output/entry.txt.
"""

from pathlib import Path

LINE = (
    "Your fridge isn't storage — it's a museum of good intentions, "
    "curated by mold, lit by guilt, and closed by denial."
)


def main() -> None:
    n = len(LINE)
    assert 1 <= n <= 200, f"LINE length {n} out of range (need 1..200)"
    assert "\n" not in LINE, "LINE must be a single line (no newline)"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
