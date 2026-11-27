#!/usr/bin/env python3
"""Package each academy course as a SCORM 1.2 zip for import into the company LMS.

Usage: python3 tools/make_scorm.py [slug ...]      (default: every generated course)
Output: lms/<slug>-scorm12.zip

Inside the LMS the course reports progress (cmi.suspend_data, lesson_location), completion and the final quiz
score (cmi.core.score.raw, lesson_status passed/failed) — see assets/js/course.js. Login, passwords and pilot
accounts are managed by the LMS itself.
"""
import os
import re
import sys
import zipfile
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import build  # noqa: E402

SKIP_DIRS = {"print", "narration", "icons"}
SKIP_FILES = {"assets/js/pwa.js"}
# The installable-app tags (tools/pwa.py) belong to the website only: inside the LMS there is no app to install.
PWA_TAGS = re.compile(r'\s*<meta name="(?:apple-)?mobile-web-app-[^>]*>|\s*<meta name="apple-mobile-web-app-[^>]*>'
                      r'|\s*<link rel="(?:apple-touch-icon|manifest)"[^>]*>|\s*<script src="[^"]*assets/js/pwa\.js"[^>]*></script>')


def files_for(slug):
    out = []
    for base in ("assets", os.path.join("courses", slug)):
        for dp, dns, fns in os.walk(os.path.join(ROOT, base)):
            dns[:] = [d for d in dns if d not in SKIP_DIRS and not d.startswith(".")]
            for fn in fns:
                if fn.startswith(".") or fn.endswith(".md"):
                    continue
                rel = os.path.relpath(os.path.join(dp, fn), ROOT).replace(os.sep, "/")
                if rel not in SKIP_FILES:
                    out.append(rel)
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
            if f.endswith(".html"):
                with open(os.path.join(ROOT, f), encoding="utf-8") as h:
                    z.writestr(f, PWA_TAGS.sub("", h.read()))
            else:
                z.write(os.path.join(ROOT, f), f)
    return out, len(files)



def locked_section(inner_html, password):
    """The administrator page content, encrypted (AES-256-GCM, key from PBKDF2-SHA256). The password itself is never written
    to the site or the repository: only the encrypted content, the salt and the IV are published."""
    import base64
    import secrets
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives import hashes
    salt, iv, rounds = secrets.token_bytes(16), secrets.token_bytes(12), 310000
    key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=rounds).derive(password.encode())
    ct = AESGCM(key).encrypt(iv, inner_html.encode(), None)
    b = lambda x: base64.b64encode(x).decode()
    return f"""
    <section class="content" id="lmsAdmin">
      <div class="eyebrow">For the LMS administrator</div>
      <h1>LMS Packages (SCORM 1.2)</h1>
      <form id="lmsLock" class="card panel" style="max-width:420px" autocomplete="off">
        <label for="lmsPw"><strong>Enter your password</strong></label>
        <input id="lmsPw" type="password" required style="display:block;width:100%;margin:10px 0;padding:10px;font-size:16px;border:1px solid #b8c4bd;border-radius:8px">
        <button class="btn primary" type="submit">Open</button>
        <p id="lmsErr" class="muted" role="alert" style="color:#b3261e;min-height:1.4em"></p>
      </form>
    </section>
    <script>
    (function () {{
      var D = {{ s: "{b(salt)}", i: "{b(iv)}", c: "{b(ct)}", n: {rounds} }};
      function u(x) {{ return Uint8Array.from(atob(x), function (ch) {{ return ch.charCodeAt(0); }}); }}
      async function open(pw) {{
        var base = await crypto.subtle.importKey("raw", new TextEncoder().encode(pw), "PBKDF2", false, ["deriveKey"]);
        var key = await crypto.subtle.deriveKey({{ name: "PBKDF2", salt: u(D.s), iterations: D.n, hash: "SHA-256" }}, base, {{ name: "AES-GCM", length: 256 }}, false, ["decrypt"]);
        var html = new TextDecoder().decode(await crypto.subtle.decrypt({{ name: "AES-GCM", iv: u(D.i) }}, key, u(D.c)));
        document.getElementById("lmsAdmin").innerHTML = html;
      }}
      document.getElementById("lmsLock").addEventListener("submit", function (e) {{
        e.preventDefault();
        var err = document.getElementById("lmsErr"); err.textContent = "Checking…";
        if (!window.crypto || !crypto.subtle) {{ err.textContent = "This browser cannot open the page (secure connection needed)."; return; }}
        open(document.getElementById("lmsPw").value).catch(function () {{ err.textContent = "Wrong password."; }});
      }});
    }})();
    </script>"""

def index_page():
    rows = []
    for c in build.COURSES:
        z = os.path.join(ROOT, "lms", f"{c['slug']}-scorm12.zip")
        if os.path.exists(z):
            rows.append(f'<tr><td><strong>{escape(c["title"])}</strong></td><td>{len(c["lessons"])}</td><td>{c["pass_mark"]} %</td>'
                        f'<td>{os.path.getsize(z) / 1e6:.1f} MB</td><td><a class="btn" href="{c["slug"]}-scorm12.zip" download>Download</a></td></tr>')
    secret = f"""
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
"""
    password = os.environ.get("LMS_ADMIN_PASSWORD")
    if not password:
        print("LMS_ADMIN_PASSWORD not set: lms/index.html left unchanged (the page is locked with the administrator password).")
        return
    main = locked_section(secret, password)
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
