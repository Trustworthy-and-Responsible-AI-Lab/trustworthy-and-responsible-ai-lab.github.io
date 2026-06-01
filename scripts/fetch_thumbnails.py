#!/usr/bin/env python3
"""
Fetch paper first-page thumbnails from arXiv / open-access PDFs.
Run from the TRUE-Lab root directory:
    python3 scripts/fetch_thumbnails.py
"""

import yaml, subprocess, os, re, time, sys, urllib.request, urllib.error

PAPERS_DIR  = "assets/images/papers"
YAML_FILE   = "_data/publications.yml"
TEMP_PDF    = "/tmp/_thumb_paper.pdf"
TEMP_PREFIX = "/tmp/_thumb_page"

# ------------------------------------------------------------------
def slugify(text):
    s = re.sub(r'[^a-z0-9]+', '-', text.lower().strip())
    return s[:55].strip('-')

def extract_arxiv_id(url):
    m = re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})', url or "")
    return m.group(1) if m else None

def get_pdf_url(pub):
    """Return (url, label) for the most accessible PDF, or (None, None)."""
    links = pub.get('links') or {}
    pdf   = links.get('pdf', '') or ''
    arxiv = links.get('arxiv', '') or ''

    for url in [arxiv, pdf]:
        aid = extract_arxiv_id(url)
        if aid:
            return f"https://arxiv.org/pdf/{aid}", f"arXiv:{aid}"

    # USENIX / MLR / OpenReview direct PDFs
    for url in [pdf]:
        if any(h in url for h in ['usenix.org', 'mlr.press',
                                   'openreview.net', 'isca-archive.org',
                                   'link.springer.com', 'dl.acm.org',
                                   'ieeexplore.ieee.org']):
            if url.endswith('.pdf') or '/pdf' in url:
                return url, "direct"

    return None, None

def download_pdf(url, dest, retries=2):
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent":
                         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"}
            )
            with urllib.request.urlopen(req, timeout=40) as resp:
                content = resp.read()
            if len(content) < 5000:   # too small → probably an error page
                return False
            with open(dest, 'wb') as f:
                f.write(content)
            return True
        except Exception as e:
            if attempt < retries:
                time.sleep(3)
            else:
                print(f"    download error: {e}")
    return False

def pdf_to_jpeg(pdf_path, out_path, dpi=150):
    try:
        result = subprocess.run(
            ['pdftoppm', '-f', '1', '-l', '1', '-jpeg',
             '-r', str(dpi), pdf_path, TEMP_PREFIX],
            capture_output=True, timeout=30
        )
        for candidate in [f"{TEMP_PREFIX}-1.jpg", f"{TEMP_PREFIX}-01.jpg"]:
            if os.path.exists(candidate):
                os.rename(candidate, out_path)
                return True
    except Exception as e:
        print(f"    pdftoppm error: {e}")
    return False

# ------------------------------------------------------------------
def main():
    os.makedirs(PAPERS_DIR, exist_ok=True)

    with open(YAML_FILE) as f:
        data = yaml.safe_load(f)

    all_pubs = (data.get('preprints') or []) + (data.get('papers') or [])
    total = len(all_pubs)
    done, skipped, failed = 0, 0, 0

    for i, pub in enumerate(all_pubs, 1):
        title  = pub.get('title', '')
        slug   = slugify(title)
        dest   = f"{PAPERS_DIR}/{slug}.jpg"
        label  = f"[{i}/{total}]"

        if os.path.exists(dest):
            print(f"{label} skip (exists): {slug}")
            skipped += 1
            continue

        pdf_url, src_label = get_pdf_url(pub)
        if not pdf_url:
            print(f"{label} no public PDF — {title[:60]}")
            skipped += 1
            continue

        print(f"{label} {src_label}  {title[:55]}...")

        if not download_pdf(pdf_url, TEMP_PDF):
            print(f"    FAILED (download)")
            failed += 1
            continue

        if pdf_to_jpeg(TEMP_PDF, dest):
            size_kb = os.path.getsize(dest) // 1024
            print(f"    OK  {slug}.jpg  ({size_kb} KB)")
            done += 1
        else:
            print(f"    FAILED (convert)")
            failed += 1

        # Clean temp
        for f in [TEMP_PDF] + [f"{TEMP_PREFIX}-{s}.jpg" for s in ['1','01']]:
            if os.path.exists(f):
                os.remove(f)

        time.sleep(1.5)   # polite to servers

    print(f"\nDone: {done} new  |  {skipped} skipped  |  {failed} failed")
    print(f"\nNext step — run update_yaml_thumbs.py to add thumbnail: fields to publications.yml")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    main()
