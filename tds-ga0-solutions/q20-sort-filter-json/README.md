# Q20 · Sort and Filter a JSON Product Catalog (0.5 marks)

## Question
Given 100 products `{category, price, name}`:
1. drop anything with `price < 117.71` *(threshold personalised)*
2. sort by **category A→Z**, then **price high→low**, then **name A→Z**
3. paste the result as **one minified JSON line**.

## Answer
54 products survived the filter in my version → submitted the minified array ✅
(Your product list is different, so run the script on yours.)

## Steps
1. Copy the JSON array from the question into `products.json`.
2. Run [`sort_filter.py`](sort_filter.py):
   ```bash
   python sort_filter.py products.json 117.71 > answer.json
   ```
3. Paste the single line from `answer.json` → **Check**.

### jq one-liner
```bash
jq -c '[.[] | select(.price >= 117.71)] | sort_by(.category, -.price, .name)' products.json
```

## Gotchas
- "Filter out price < X" means **keep `price >= X`** (equal stays in).
- Sort price **numerically**, descending — not as strings.
- Output must be minified (`separators=(",", ":")`), no spaces.
