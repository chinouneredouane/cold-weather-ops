"""DAL TRAINING: install the academy as an app (Safari "Add to Home Screen") and make it work offline.

Called from build.py. It writes:
  manifest.webmanifest   app name, icons and colours
  sw.js                  service worker: stores the site on the device
  assets/js/pwa.js       is static (not generated); it registers sw.js and shows the install guide

What is stored on the device:
  * on the first visit: every page, style sheet, script and picture (the "app shell");
  * narration MP3s, PDFs and videos: when the learner plays or opens them, or all at once
    with the "Save this course for offline" button on each course home page.
SCORM packages (lms/), tools/ and demo/ are never stored.
"""
import hashlib
import json
import os

APP_NAME = "DAL TRAINING"
THEME = "#125a2b"
BACKGROUND = "#0b1f3a"

SHELL_EXT = {".html", ".css", ".js", ".jpg", ".jpeg", ".png", ".svg", ".webp", ".gif", ".ico", ".json", ".vtt"}
MEDIA_EXT = {".mp3", ".m4a", ".wav", ".mp4", ".pdf"}
SKIP_DIRS = {".git", ".github", "lms", "tools", "demo", "node_modules"}
SKIP_FILES = {"sw.js"}


def pwa_head(root):
    """Tags added to every page's <head>."""
    return f"""  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-status-bar-style" content="default" />
  <meta name="apple-mobile-web-app-title" content="{APP_NAME}" />
  <link rel="apple-touch-icon" href="{root}assets/img/icons/apple-touch-icon.png" />
  <link rel="manifest" href="{root}manifest.webmanifest" />
  <script src="{root}assets/js/pwa.js" defer></script>"""


def _files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = os.path.relpath(dirpath, root)
        top = rel_dir.split(os.sep)[0]
        if top in SKIP_DIRS:
            dirnames[:] = []
            continue
        dirnames[:] = sorted(d for d in dirnames if not d.startswith(".") and d not in SKIP_DIRS)
        for name in sorted(filenames):
            if name.startswith(".") or name in SKIP_FILES:
                continue
            rel = os.path.normpath(os.path.join(rel_dir, name)).replace(os.sep, "/")
            yield rel, os.path.join(dirpath, name)


def _hash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:12]


def build_pwa(root):
    shell, media = [], {}
    shell_hash = hashlib.sha256()
    sizes = {}
    for rel, full in _files(root):
        ext = os.path.splitext(rel)[1].lower()
        if ext in SHELL_EXT:
            shell.append(rel)
            shell_hash.update(rel.encode())
            shell_hash.update(_hash(full).encode())
        elif ext in MEDIA_EXT:
            media[rel] = _hash(full)
            sizes[rel] = os.path.getsize(full)

    # Media of each course, for the "Save this course for offline" button.
    courses = {}
    for rel in media:
        parts = rel.split("/")
        if parts[0] == "courses" and len(parts) > 2:
            c = courses.setdefault(parts[1], {"files": [], "bytes": 0})
            c["files"].append(rel)
            c["bytes"] += sizes[rel]

    version = shell_hash.hexdigest()[:12]

    manifest = {
        "name": APP_NAME,
        "short_name": APP_NAME,
        "description": "Domestic Airlines Training Academy: e-learning courses for crews and operations staff.",
        "id": "./",
        "start_url": "./index.html",
        "scope": "./",
        "display": "standalone",
        "orientation": "any",
        "background_color": BACKGROUND,
        "theme_color": THEME,
        "icons": [
            {"src": "assets/img/icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "assets/img/icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
            {"src": "assets/img/icons/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
        ],
    }
    with open(os.path.join(root, "manifest.webmanifest"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")

    with open(os.path.join(root, "tools", "sw_template.js"), encoding="utf-8") as f:
        sw = f.read()
    sw = (sw.replace("__VERSION__", version)
            .replace("__SHELL__", json.dumps(shell, separators=(",", ":")))
            .replace("__MEDIA__", json.dumps(media, separators=(",", ":"), sort_keys=True))
            .replace("__COURSES__", json.dumps(courses, separators=(",", ":"), sort_keys=True)))
    with open(os.path.join(root, "sw.js"), "w", encoding="utf-8", newline="\n") as f:
        f.write(sw)

    shell_mb = sum(os.path.getsize(os.path.join(root, r)) for r in shell) / 1e6
    media_mb = sum(sizes.values()) / 1e6
    print(f"Built app support ({APP_NAME}): {len(shell)} files stored on first visit ({shell_mb:.1f} MB), "
          f"{len(media)} media files on demand ({media_mb:.0f} MB), version {version}")
