#!/usr/bin/env python3
"""Package each academy course as a SCORM 1.2 zip for import into the company LMS.

Usage: python3 tools/make_scorm.py [slug ...]      (default: every generated course)
Output: lms/<slug>-scorm12.zip

Inside the LMS the course reports progress (cmi.suspend_data, lesson_location), completion and the final quiz
score (cmi.core.score.raw, lesson_status passed/failed) — see assets/js/course.js. Login, passwords and pilot
accounts are managed by the LMS itself.
"""
import os
import sys
import zipfile
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import build  # noqa: E402

SKIP_DIRS = {"print", "narration"}


def files_for(slug):
    out = []
    for base in ("assets", os.path.join("courses", slug)):
        for dp, dns, fns in os.walk(os.path.join(ROOT, base)):
            dns[:] = [d for d in dns if d not in SKIP_DIRS and not d.startswith(".")]
            for fn in fns:
                if fn.startswith(".") or fn.endswith(".md"):
                    continue
                out.append(os.path.relpath(os.path.join(dp, fn), ROOT).replace(os.sep, "/"))
    return sorted(out)


def manifest(course, files):
    slug, title = course["slug"], course["title"]
    res = "\n".join(f'      <file href="{escape(f)}"/>' for f in files)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="DA-{escape(slug)}" version="1.0"
  xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
  xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.imsproject.org/xsd/imscp_rootv1p1p2 imscp_rootv1p1p2.xsd http://www.imsglobal.org/xsd/imsmd_rootv1p2p1 imsmd_rootv1p2p1.xsd http://www.adlnet.org/xsd/adlcp_rootv1p2 adlcp_rootv1p2.xsd">
  <metadata><schema>ADL SCORM</schema><schemaversion>1.2</schemaversion></metadata>
  <organizations default="DA-ORG">
    <organization identifier="DA-ORG">
      <title>{escape("Domestic Airlines — " + title)}</title>
      <item identifier="ITEM-1" identifierref="RES-1" isvisible="true">
        <title>{escape(title)}</title>
        <adlcp:masteryscore>{course["pass_mark"]}</adlcp:masteryscore>
      </item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="RES-1" type="webcontent" adlcp:scormtype="sco" href="courses/{escape(slug)}/index.html">
{res}
    </resource>
  </resources>
</manifest>
"""


def package(course):
    files = files_for(course["slug"])
    os.makedirs(os.path.join(ROOT, "lms"), exist_ok=True)
    out = os.path.join(ROOT, "lms", f"{course['slug']}-scorm12.zip")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("imsmanifest.xml", manifest(course, files))
        for f in files:
            z.write(os.path.join(ROOT, f), f)
    return out, len(files)


def index_page():
    rows = []
    for c in build.COURSES:
        z = os.path.join(ROOT, "lms", f"{c['slug']}-scorm12.zip")
        if os.path.exists(z):
            rows.append(f'<tr><td><strong>{escape(c["title"])}</strong></td><td>{len(c["lessons"])}</td><td>{c["pass_mark"]} %</td>'
                        f'<td>{os.path.getsize(z) / 1e6:.1f} MB</td><td><a class="btn" href="{c["slug"]}-scorm12.zip" download>Download</a></td></tr>')
    main = f"""
    <section class="content">
      <div class="eyebrow">For the LMS administrator</div>
      <h1>LMS Packages (SCORM 1.2)</h1>
      <p>Each academy course is available as a <strong>SCORM 1.2</strong> package for import into the company LMS (Moodle, Cornerstone, SAP SuccessFactors, TalentLMS and most others). In the LMS, pilots log in with their LMS account; the LMS administrator creates users, manages passwords and sees each pilot's progress, quiz score and completion.</p>
      <div class="table-wrap"><table>
        <tr><th>Course</th><th>Lessons</th><th>Pass mark</th><th>Size</th><th></th></tr>
        {''.join(rows)}
      </table></div>
      <h2>What the LMS receives</h2>
      <ul>
        <li><strong>Status</strong>: incomplete while the pilot studies; <strong>passed</strong> or <strong>failed</strong> after the final quiz (mastery score = pass mark).</li>
        <li><strong>Score</strong>: the best final quiz result, 0–100.</li>
        <li><strong>Bookmark and progress</strong>: the last lesson and the lessons completed — the pilot resumes where they stopped.</li>
        <li><strong>Name</strong>: the pilot's name from the LMS account is printed on the course certificate.</li>
      </ul>
      <h2>How to import</h2>
      <ol class="steps">
        <li>Download the package (.zip). Do not unzip it.</li>
        <li>In the LMS, create a new course or activity of type <em>SCORM package</em> and upload the zip.</li>
        <li>Set the display to open in a new window or full screen, and the grading to “highest attempt”.</li>
        <li>Enrol the pilots or their groups (B737-800, Q400, Q200).</li>
      </ol>
      <p class="muted">The Command Upgrade course has its own design and progress system and is not included as a SCORM package yet.</p>
    </section>"""
    out = build.page(title="LMS Packages — Domestic Airlines Training", description="SCORM 1.2 packages of the academy courses for the company LMS.",
                     root="../", main=main)
    with open(os.path.join(ROOT, "lms", "index.html"), "w", encoding="utf-8") as f:
        f.write(out)


def main():
    wanted = set(sys.argv[1:])
    for c in build.COURSES:
        if wanted and c["slug"] not in wanted:
            continue
        out, n = package(c)
        print(f"{c['title']}: {n} files, {os.path.getsize(out) / 1e6:.1f} MB -> {os.path.relpath(out, ROOT)}")
    index_page()


if __name__ == "__main__":
    main()
