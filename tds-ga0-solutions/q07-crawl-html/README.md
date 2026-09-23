# Q7 · Count crawled HTML files (1 mark)

## Question
Crawl <https://sanand0.github.io/tdsdata/crawl_html/>. How many HTML files begin with letters from **O to Z**?
*(the letter range is personalised)*

## Answer
**`55`** *(out of 106 HTML files in total)*

## Steps
### Option A — wget (what the course teaches)
```bash
wget --recursive --level=inf --no-parent --adjust-extension \
     --accept html,htm --directory-prefix=./crawl \
     https://sanand0.github.io/tdsdata/crawl_html/

# count files whose *name* starts with O..Z (case-insensitive), ignoring index.html
find crawl -type f -name "*.html" ! -name "index.html" -printf "%f\n" | grep -ci "^[o-z]"
```

### Option B — Python crawler
[`crawl_count.py`](crawl_count.py) does a breadth-first crawl, collects every `.html` link under the start URL
and counts by first letter of the file name.
```bash
pip install httpx beautifulsoup4
python crawl_count.py O Z
```

## Gotchas
- Count the **file name**, not the folder (`hospital/history.html` counts under **H**).
- Files live in sub-folders too — a non-recursive listing undercounts.
- Use `--level=inf` or a real BFS; the default wget depth (5) is fine here but don't rely on `--level=1`.
