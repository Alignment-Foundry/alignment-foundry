#!/usr/bin/env python3
"""Fail the build if any em dash appears in tracked content.

Policy (see CLAUDE.md -> "Writing style: never use em dashes"): the em dash is
banned in every form across all tracked text files:

  * the literal character U+2014 (decimal 8212)
  * the named HTML entity  &mdash;
  * the decimal HTML entity &#8212;
  * the hex HTML entity     &#x2014;

The en dash (U+2013), hyphen, and other entities are allowed; only the em dash
is rejected.

This checker and its workflow are the only excluded paths, because they must
spell out the forbidden patterns in order to detect them.
"""

from __future__ import annotations

import re
import subprocess
import sys

# Paths allowed to contain the patterns (they define/enforce the policy).
EXCLUDE = {
    ".github/scripts/check_no_em_dash.py",
    ".github/workflows/no-em-dash.yml",
}

# U+2014 is matched by code point so this source need not contain the literal.
EM_DASH = "—"
ENTITY = re.compile(r"&mdash;|&#0*8212;|&#x0*2014;", re.IGNORECASE)


def list_files() -> list[str]:
    out = subprocess.check_output(["git", "ls-files"], text=True)
    return out.splitlines()


def scan(path: str) -> list[tuple[int, int, str]]:
    try:
        text = open(path, encoding="utf-8").read()
    except (UnicodeDecodeError, IsADirectoryError, FileNotFoundError):
        return []
    hits: list[tuple[int, int, str]] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for col, ch in enumerate(line, 1):
            if ch == EM_DASH:
                hits.append((lineno, col, line.strip()[:100]))
        for m in ENTITY.finditer(line):
            hits.append((lineno, m.start() + 1, line.strip()[:100]))
    return hits


def main() -> int:
    failures = []
    for f in list_files():
        if f in EXCLUDE:
            continue
        for lineno, col, snippet in scan(f):
            failures.append((f, lineno, col, snippet))

    if failures:
        print("Em dash policy check FAILED. Found em dashes in:\n")
        for f, lineno, col, snippet in failures:
            print(f"  {f}:{lineno}:{col}")
            print(f"      {snippet}")
        print(
            "\nReplace each per CLAUDE.md -> "
            '"Writing style: never use em dashes": use a colon, comma, '
            "semicolon, full stop, or (for numeric ranges) an en dash."
        )
        return 1

    print("Em dash policy: OK (no em dashes found in tracked content).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
