#!/usr/bin/env python3
"""Validate the desktop-pet catalog."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog.json"
REQUIRED = {"name", "url", "category", "stack", "note"}


def main() -> int:
    entries = json.loads(CATALOG.read_text(encoding="utf-8"))
    if not isinstance(entries, list) or not entries:
        raise SystemExit("catalog.json must contain a non-empty list")

    seen_urls: set[str] = set()
    for index, entry in enumerate(entries, start=1):
        missing = REQUIRED - set(entry)
        if missing:
            raise SystemExit(f"entry {index} is missing fields: {sorted(missing)}")

        url = entry["url"]
        if not re.match(r"^https://github\.com/[^/]+/[^/]+$", url):
            raise SystemExit(f"entry {index} has a non-GitHub repo URL: {url}")
        if url in seen_urls:
            raise SystemExit(f"duplicate URL: {url}")
        seen_urls.add(url)

        if len(entry["note"]) < 20:
            raise SystemExit(f"entry {index} note is too short")

    print(f"validated {len(entries)} catalog entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
