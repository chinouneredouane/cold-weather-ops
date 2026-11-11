#!/usr/bin/env python3
"""Generate the Upset Prevention and Recovery lesson illustrations (SVG → JPG).

Usage: python3 tools/make_pictures.py      (needs Node.js with Playwright)
"""
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from courses.upset_recovery import COURSE  # noqa: E402
from courses.upset_recovery.pictures import scene  # noqa: E402

work = tempfile.mkdtemp(prefix="pics-")
for n in COURSE["images"]:
    with open(os.path.join(work, f"lesson-{n:02d}.svg"), "w", encoding="utf-8") as f:
        f.write(scene(n))
out = os.path.join(ROOT, "courses", COURSE["slug"], "media", "images")
subprocess.run(["node", os.path.join(ROOT, "tools", "make_pictures.js"), work, out], check=True)
print(f"wrote {len(COURSE['images'])} pictures to {os.path.relpath(out, ROOT)}")
