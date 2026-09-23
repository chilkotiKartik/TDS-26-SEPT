# Q4 · Calculate variance (0.5 marks)

## Question
Download `q-calculate-variance.json` (1000 measurements) and report the **sample variance** (N−1 denominator),
rounded to 2 decimals.

## Answer
**`133.45`** *(my file: n = 1000, mean = 31.137, variance = 133.4517…)*

## Steps
1. Click the `q-calculate-variance.json` button on the question to download it.
2. Run [`variance.py`](variance.py):
   ```bash
   python variance.py q-calculate-variance.json
   ```
3. Paste the rounded value → **Check**.

### Spreadsheet way
Import the JSON into Excel / Google Sheets as a column and use `=ROUND(VAR.S(A:A), 2)`.
(`VAR.P` / `statistics.pvariance` is the *population* variance — wrong for this question.)
