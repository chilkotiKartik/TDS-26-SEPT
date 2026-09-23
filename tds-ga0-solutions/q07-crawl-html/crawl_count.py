import sys
from collections import deque
from urllib.parse import urljoin, urldefrag

import httpx
from bs4 import BeautifulSoup

ROOT = "https://sanand0.github.io/tdsdata/crawl_html/"
lo, hi = (sys.argv[1].lower(), sys.argv[2].lower()) if len(sys.argv) > 2 else ("o", "z")

seen, html_files = set(), set()
queue = deque([ROOT])
with httpx.Client(follow_redirects=True, timeout=20) as client:
    while queue:
        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)
        r = client.get(url)
        if r.status_code != 200:
            continue
        for a in BeautifulSoup(r.text, "html.parser").select("a[href]"):
            link = urldefrag(urljoin(url, a["href"]))[0].split("?")[0]
            if not link.startswith(ROOT):
                continue
            if link.endswith((".html", ".htm")):
                html_files.add(link)
                queue.append(link)
            elif link.endswith("/"):
                queue.append(link)

names = [u.rsplit("/", 1)[-1] for u in html_files]
matching = [n for n in names if lo <= n[0].lower() <= hi]
print(f"total html files: {len(names)}")
print(f"files starting {lo.upper()}-{hi.upper()}: {len(matching)}")
