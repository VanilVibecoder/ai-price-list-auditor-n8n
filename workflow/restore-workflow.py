#!/usr/bin/env python3
"""Restore the portable n8n workflow JSON from the compressed base64 artifact."""

from __future__ import annotations

import base64
import gzip
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "ai-price-list-auditor.json.gz.b64"
TARGET = ROOT / "ai-price-list-auditor.json"


def main() -> None:
    encoded = SOURCE.read_text(encoding="utf-8").strip()
    payload = gzip.decompress(base64.b64decode(encoded))
    TARGET.write_bytes(payload)
    print(f"Restored {TARGET} ({len(payload)} bytes)")


if __name__ == "__main__":
    main()
