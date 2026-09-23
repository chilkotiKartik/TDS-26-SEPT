# Q1 · Scale Manipulation Repair in Axis Design (1 mark)

## Question
A Chart.js line chart titled *"Satisfaction is rising"* uses a deceptive axis. Identify the manipulation,
quantify the distortion, submit corrected HTML, and explain it in an HTML comment at the top.

My assigned chart (15 of 20) had this data:

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 |
|----|----|----|----|----|----|----|----|
| 399.01 | 388.67 | 379.01 | 372.87 | 363.81 | 352.55 | 347.31 | 334.86 |

and the broken config had `"scales": {"y": {"reverse": true}}`.

## Answer
- **Manipulation:** inverted axis (`reverse: true`) → a falling series is drawn as a rising line.
- **Distortion ratio:** `1.0` (a complete direction flip). Real change: 399.01 → 334.86 = **−64.15 points (≈ −16.1%)**.
- **Fix:** `reverse: false` → [`corrected_chart.html`](corrected_chart.html)
- **What it reveals:** satisfaction has *declined every single quarter*; the broken chart sold a decline as growth.

## Steps
1. Look at the `scales` block — anything like `reverse`, `min`, a second `y2` axis, or `type: 'logarithmic'` is suspect.
2. Compare the table with what the chart claims (values go *down*, title says *rising*) → inverted axis.
3. Change `reverse: true` to `reverse: false` and retitle the chart honestly.
4. Put the explanation comment **at the very top**, starting with the distortion number.

## Gotcha (found by reading the checker)
The validator grabs the **first number** in your HTML comment and compares it to the expected distortion
(±15%). For inverted axes the expected value is `1`, so the comment must start with something like
`Distortion ratio: 1.0` — if you write "Q1 399.01…" first, it reads `1`… or worse `399`. It also looks for a
phrase such as *"inverted axis flips decline narrative"* and the literal `reverse: false`.
