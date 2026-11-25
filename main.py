"""Fridge Roast: One Line, Biggest Laugh — make.fun bounty entry."""

from pathlib import Path

LINE = (
    "Opening your fridge is like opening a cold case: everything's dated, "
    "nothing's solved, and the only witness is a half-dead lettuce."
)


def main() -> None:
    n = len(LINE)
    assert 1 <= n <= 200, f"LINE length {n} must be 1..200"
    assert "\n" not in LINE, "LINE must not contain a newline"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
