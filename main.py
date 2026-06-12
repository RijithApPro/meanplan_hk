"""
Entry point for the Bosch Speiseplan PDF parser.

Usage:
    python main.py [path/to/menu.pdf]

Defaults to 'menu_de.pdf' in the same directory if no argument is given.
Outputs: menu_week.md and menu_week.json alongside the PDF.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from parser import parse_menu, menu_to_markdown


def main() -> None:
    pdf_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "menu_de.pdf"

    if not pdf_path.exists():
        print(f"[ERROR] PDF not found: {pdf_path}")
        sys.exit(1)

    print(f"[INFO] Parsing {pdf_path} …")
    data = parse_menu(str(pdf_path))

    out_dir   = pdf_path.parent
    md_path   = out_dir / "menu_week.md"
    json_path = out_dir / "menu_week.json"

    md_path.write_text(menu_to_markdown(data), encoding="utf-8")
    print(f"[OK]   Markdown  → {md_path}")

    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK]   JSON      → {json_path}")


if __name__ == "__main__":
    main()

