# Q14 · Reconstruct and desaturate an image (1 mark)

## Question
`jigsaw.webp` (500×500) is scrambled into a 5×5 grid. Use the mapping table
(scrambled row/col → original row/col) to rebuild it, convert to grayscale with
**Y = 0.2126 R + 0.7152 G + 0.0722 B**, and upload a lossless PNG/WEBP. It must match **pixel-for-pixel**.

## Answer — [`rebuild.py`](rebuild.py) ✅
My mapping (`scrambled_row scrambled_col → original_row original_col`):

```
0 0→2 1   0 1→1 1   0 2→4 1   0 3→0 3   0 4→0 1
1 0→1 4   1 1→2 0   1 2→2 4   1 3→4 2   1 4→2 2
2 0→0 0   2 1→3 2   2 2→4 3   2 3→3 0   2 4→3 4
3 0→1 0   3 1→2 3   3 2→3 3   3 3→4 4   3 4→0 2
4 0→3 1   4 1→1 2   4 2→1 3   4 3→0 4   4 4→4 0
```

## Steps
1. Download `jigsaw.webp` from the question into this folder.
2. Edit `MAPPING` in `rebuild.py` if yours differs, then:
   ```bash
   pip install pillow
   python rebuild.py
   ```
3. Upload `reconstructed_grayscale.png` → **Check**.

## Gotchas
- **Rounding:** the checker uses JavaScript `Math.round` (0.5 always rounds up). Python's `round()` does
  banker's rounding (0.5 → even), so I use `int(y + 0.5)`.
- **Don't use `img.convert("L")`** — Pillow uses different coefficients (0.299/0.587/0.114).
- **Brave browser:** fingerprint protection adds ±1 noise to canvas reads, so the checker's comparison fails even
  for a perfect image. Lion icon → turn **Block fingerprinting** off for the exam site → reload → check again.
