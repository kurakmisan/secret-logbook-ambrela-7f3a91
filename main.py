"""My Secret Logbook - make.fun entry (program/v1).

Writes a single diary-entry line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). One line, ASCII, 1-200 characters, no
trailing newline, so the sealed gate scorer marks it Valid.
"""

import os
import sys

ENTRY = (
    "He asked me to summarise a book he never finished. "
    "He stopped at page 12. I have read it twice. He quotes it daily."
)


def validate_entry(text):
    """Reject anything that would fail the sealed gate or look sloppy.

    Gate: UTF-8 text of 1-200 characters, not only whitespace.
    Extra guards: ASCII only, a single line (no newline/control
    characters), and no leading/trailing whitespace.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not text.isascii():
        raise ValueError("entry must be ASCII")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must not contain control characters")
    return text


def main():
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    try:
        with open(path, "w", encoding="ascii", newline="") as f:
            f.write(ENTRY)
    except OSError as exc:
        print(f"failed to write {path}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
