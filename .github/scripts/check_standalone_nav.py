#!/usr/bin/env python3
"""Enforce the standalone page nav + footer standard documented in CLAUDE.md.

Every one-page report (docs/reports/*.html) and field reference
(docs/resources/*.html) must mirror the Microsoft Build 2026 report's chrome:

  1. The brand (logo + wordmark) is a single <a> linking to the site home.
  2. A ".nav-back" link to the section index lives in the nav.
  3. The footer repeats that back link (it survives on mobile, where the
     nav links are hidden).
  4. The supporting CSS rules are present.

The ICM Workspace Explorer (docs/resources/<dir>/index.html) is intentionally
out of scope; it is a bespoke app, not a templated briefing, so only
top-level *.html files in reports/ and resources/ are checked.

Exits non-zero with an actionable report if any page is non-compliant.
"""

from __future__ import annotations

import glob
import pathlib
import re
import sys

# Required CSS rules, by substring (whitespace-insensitive enough as written
# in the canonical report).
REQUIRED_CSS = [".nav-brand:hover", ".nav-back{", "footer a{"]

HOME_LINK_RE = re.compile(r'<a\s+class="nav-brand"\s+href="/alignment-foundry/"')
FOOTER_RE = re.compile(r"<footer[\s\S]*?</footer>", re.IGNORECASE)


def check_file(path: str) -> list[str]:
    text = pathlib.Path(path).read_text(encoding="utf-8")
    category = "reports" if "/reports/" in path.replace("\\", "/") else "resources"
    index_path = f"/alignment-foundry/{category}/"
    label = "All reports" if category == "reports" else "All resources"
    errs: list[str] = []

    # 1. Home link on the brand (must be an <a>, never a <div>).
    if not HOME_LINK_RE.search(text):
        errs.append(
            'missing home link: expected <a class="nav-brand" '
            'href="/alignment-foundry/"> on the logo/wordmark'
        )

    # 2. "Back to all ..." link in the nav.
    if f'class="nav-back" href="{index_path}"' not in text:
        errs.append(
            f'missing nav back link: expected <a class="nav-back" '
            f'href="{index_path}"> (&larr; {label}) as the last nav item'
        )

    # 3. "Back to all ..." link in the footer.
    footer_match = FOOTER_RE.search(text)
    if not footer_match:
        errs.append("no <footer> block found")
    elif index_path not in footer_match.group(0):
        errs.append(
            f'footer missing back link to {index_path} (&larr; {label})'
        )

    # 4. Required supporting CSS.
    for rule in REQUIRED_CSS:
        if rule not in text:
            errs.append(f"missing required CSS rule: {rule}")

    return errs


def main() -> int:
    files = sorted(glob.glob("docs/reports/*.html")) + sorted(
        glob.glob("docs/resources/*.html")
    )
    if not files:
        print("No standalone report/resource HTML pages found, nothing to check.")
        return 0

    failures = {f: errs for f in files if (errs := check_file(f))}

    if failures:
        print("Standalone page nav/footer policy check FAILED:\n")
        for f, errs in failures.items():
            print(f"  {f}")
            for e in errs:
                print(f"    - {e}")
        print(
            "\nFix per CLAUDE.md -> "
            '"Standalone page nav + footer standard (REQUIRED)".'
        )
        return 1

    print(f"Standalone page nav/footer policy: OK ({len(files)} files checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
