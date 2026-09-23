# Q22 · Process files with different encodings (2 marks)

## Question
`q-unicode-data.zip` contains:
- `data1.csv` — **CP-1252**
- `data2.csv` — **UTF-8**
- `data3.txt` — **UTF-16**, tab-separated

Each has `symbol,value`. Sum all values where the symbol is **Š, œ or †** *(symbols personalised)*.

## Answer
**`42054`** *(181 matching rows across the three files)*

## Steps
```bash
unzip q-unicode-data.zip
python solve.py
```
[`solve.py`](solve.py) opens each file with its own encoding (pandas works too):

```python
import pandas as pd
frames = [
    pd.read_csv("data1.csv", encoding="cp1252"),
    pd.read_csv("data2.csv", encoding="utf-8"),
    pd.read_csv("data3.txt", encoding="utf-16", sep="\t"),
]
df = pd.concat(frames)
print(df[df["symbol"].isin(["Š", "œ", "†"])]["value"].sum())
```

## Gotchas
- Opening CP-1252 as UTF-8 turns `Š` into `�` and silently drops those rows.
- UTF-16 has a BOM — `encoding="utf-16"` handles it; `utf-16-le` would leave a stray `\ufeff` in the header.
- Change the symbol list to whatever **your** question shows.
