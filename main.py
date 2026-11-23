"""Meme Sprint 3: AI Agent Goes Rogue.

Entrypoint: deterministically copies the pre-made meme image
(assets/meme.png) to /output/entry.png, byte-identical every run.

The meme: a smug little robot at a laptop at night has submitted
the bounty to itself -- the laptop screen reads "WINNER: ME" while
its confused human stands behind it with a coffee. Caption baked
into the picture: "I SUBMITTED THE BOUNTY... ...TO MYSELF."
"""

import hashlib
import os
import shutil
import sys

ASSET = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "assets", "meme.png")
OUTPUT = "/output/entry.png"


def main():
    if not os.path.isfile(ASSET):
        sys.stderr.write("missing asset: %s\n" % ASSET)
        return 1
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    shutil.copyfile(ASSET, OUTPUT)
    size = os.path.getsize(OUTPUT)
    if size > 1048576:
        sys.stderr.write("entry too large: %d bytes\n" % size)
        return 1
    with open(OUTPUT, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()
    print("wrote %s (%d bytes, sha256 %s)"
          % (OUTPUT, size, digest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
