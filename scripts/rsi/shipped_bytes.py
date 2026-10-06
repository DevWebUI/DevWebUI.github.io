"""Bytes a visitor downloads: the committed size at HEAD of the files the site serves. Prints shipped_bytes=<n>.

GitHub Pages serves the repo root with no build step. Counted: the pages (index.html, 404.html), the
images they load (icon.svg, favicon.ico, the screenshot-<width>.webp srcset copies), the social card
that crawlers and link unfurlers fetch (share-card.png), the brand mark (logo-dark.svg) and the
discovery files (llms*.txt, pricing.md, robots.txt, sitemap.xml).
Not counted: docs/, scripts/, dot-folders, README.md, and the full-size image masters that
scripts/optimize_images.py derives the served copies from. No page loads a master, so shrinking or
deleting one changes nothing a visitor downloads.
"""
import subprocess

SERVED = (".html", ".css", ".js", ".mjs", ".svg", ".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".ico",
          ".woff", ".woff2", ".json", ".webmanifest", ".xml", ".txt", ".md")
SKIP_DIRS = ("docs", "scripts")
SKIP_FILES = ("README.md",)
# Source masters for scripts/optimize_images.py (master != output there). The page loads the derived
# copies, never these. favicon.ico is rewritten in place and is served, so it is not listed here.
MASTERS = ("screenshot.png",)
listing = subprocess.run(["git", "ls-tree", "-r", "-l", "-z", "HEAD"], capture_output=True, check=True).stdout
total = 0
for entry in listing.split(b"\0"):
    if not entry:
        continue
    meta, path = entry.decode("utf-8", "replace").split("\t", 1)
    size = meta.split()[3]
    parts = path.split("/")
    if size == "-" or not path.lower().endswith(SERVED):
        continue
    if any(p.startswith(".") for p in parts) or parts[0] in SKIP_DIRS or path in SKIP_FILES:
        continue
    if path in MASTERS:
        continue
    total += int(size)
print(f"shipped_bytes={total}")
