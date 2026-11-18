"""Entry program for the make.fun news-image-20261117 bounty.

Ships the finished front page: a deterministic, byte-for-byte copy of
entry.png into the output directory. Standard library only, no network,
no timestamps, no randomness -- two runs produce identical bytes.
"""

import os
import shutil
import sys
from pathlib import Path


def entrypoint() -> int:
    base = Path(__file__).resolve().parent
    picture = base / "entry.png"
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", base / "out"))
    target.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(picture, target / "entry.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(entrypoint())
