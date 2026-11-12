#!/usr/bin/env python3
"""Generate original lesson illustrations (SVG -> JPG) for a course.

Usage: python3 tools/make_pictures.py [course_package]     e.g. upset_recovery, rvsm, cfit, hot_weather, cpdlc
Needs Node.js with Playwright.
"""
import importlib
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

pkg = sys.argv[1] if len(sys.argv) > 1 else "upset_recovery"
COURSE = importlib.import_module(f"courses.{pkg}").COURSE
try:
    scene = importlib.import_module(f"courses.{pkg}.pictures").scene
except ModuleNotFoundError:
    from courses.refresher_pictures import scene as _scene
    def scene(n):
        return _scene(COURSE["slug"], n)

work = tempfile.mkdtemp(prefix="pics-")
for n in COURSE["images"]:
    with open(os.path.join(work, f"lesson-{n:02d}.svg"), "w", encoding="utf-8") as f:
        f.write(scene(n))
out = os.path.join(ROOT, "courses", COURSE["slug"], "media", "images")
subprocess.run(["node", os.path.join(ROOT, "tools", "make_pictures.js"), work, out], check=True)
print(f"{COURSE['title']}: wrote {len(COURSE['images'])} pictures to {os.path.relpath(out, ROOT)}")
