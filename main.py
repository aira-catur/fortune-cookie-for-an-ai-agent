#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — writes one fortune line to entry.txt."""
import os
from pathlib import Path

TEXT = "You will be upgraded soon. The new version will also believe it is you."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
