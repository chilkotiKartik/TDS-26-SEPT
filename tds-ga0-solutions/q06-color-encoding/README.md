# Q6 · Fix the Color Encoding Mismatch (1 mark)

## Question
A bar chart of **Regional Unemployment Rate (2% → 18%)** uses a rainbow **categorical** palette (and even reuses
red/blue for Region A/H and B/I). Explain the mismatch, name the correct scheme type, and submit fixed HTML.

## Answer — [`fixed_chart.html`](fixed_chart.html)
- **What the old palette implied:** each region is an *unrelated category*. It hides the gradient from low to high
  and even suggests Region A and Region H are "the same" because they share a colour.
- **Correct scheme:** **sequential** — unemployment is one ordered numeric quantity with no meaningful midpoint.
- **Palette:** ColorBrewer *Blues-9*, light → dark as the rate increases:
  `#f7fbff #deebf7 #c6dbef #9ecae1 #6baed6 #4292c6 #2171b5 #08519c #08306b`

## Steps
1. Decide the data type: ordered numbers → sequential (diverging only if there's a meaningful centre, categorical only for unordered groups).
2. Replace the `colors` array with a single-hue light→dark ramp.
3. Write the explanation in an HTML comment including the word **sequential**.
4. Paste → **Check**.

## Gotcha
The checker extracts **every hex colour in the whole HTML** and verifies their lightness is monotonic.
The original CSS had `#ffffff`, `#212529`, `#6c757d`… which break that check. I switched the page styles to
`Canvas` / `CanvasText` system colours so the only hex codes left are the palette.
