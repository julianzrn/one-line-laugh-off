"""Entry for make.fun competition: u-zkhiel-one-line-laugh-off-714618ae.

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

CASUALTY = "My houseplant died while I was on a trip "
CONFESSION = "learning how to take better care of myself."

ENTRY = CASUALTY + CONFESSION


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry line to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
