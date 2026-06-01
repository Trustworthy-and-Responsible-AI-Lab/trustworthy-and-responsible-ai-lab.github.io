#!/usr/bin/env python3
"""
After running fetch_thumbnails.py, run this to add thumbnail: paths to publications.yml.
Run from the TRUE-Lab root directory:
    python3 scripts/update_yaml_thumbs.py
"""

import yaml, os, re

PAPERS_DIR = "assets/images/papers"
YAML_FILE  = "_data/publications.yml"

def slugify(text):
    s = re.sub(r'[^a-z0-9]+', '-', text.lower().strip())
    return s[:55].strip('-')

with open(YAML_FILE) as f:
    raw = f.read()

with open(YAML_FILE) as f:
    data = yaml.safe_load(f)

all_pubs = (data.get('preprints') or []) + (data.get('papers') or [])
updated = 0

for pub in all_pubs:
    title = pub.get('title', '')
    slug  = slugify(title)
    dest  = f"{PAPERS_DIR}/{slug}.jpg"

    if not os.path.exists(dest):
        continue

    thumb_yaml_path = f"/assets/images/papers/{slug}.jpg"

    # Only add if not already set
    if pub.get('thumbnail') == thumb_yaml_path:
        continue

    # Find the title line in raw YAML and insert thumbnail after it
    # Use a conservative regex to find this specific entry
    escaped = re.escape(title[:60])
    pattern = rf'(  - title: "{escaped}[^"]*"\n)'
    replacement = rf'\1    thumbnail: "{thumb_yaml_path}"\n'
    new_raw, n = re.subn(pattern, replacement, raw, count=1)

    if n == 1:
        raw = new_raw
        updated += 1
        print(f"  added: {slug}.jpg")
    else:
        print(f"  WARN  could not find in YAML: {title[:60]}")

with open(YAML_FILE, 'w') as f:
    f.write(raw)

print(f"\nUpdated {updated} entries in {YAML_FILE}")
