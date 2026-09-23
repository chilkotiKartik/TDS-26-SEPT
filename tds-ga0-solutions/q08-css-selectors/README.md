# Q8 · CSS: Featured-Sale Discount Sum (2 marks)

## Question
There's a **hidden** product list on the question. Each `<li>` has classes and a `data-discount`.
Using a single CSS selector for elements that have **both** `featured` and `sale` classes, sum their `data-discount`.

## Answer
**`209`** *(8 matching items in my list)*

## Steps
1. Open DevTools (**F12**) → **Console** on the exam page.
2. Paste [`sum.js`](sum.js):
   ```js
   [...document.querySelectorAll(".featured.sale")]
     .reduce((sum, el) => sum + Number(el.dataset.discount), 0)
   ```
3. Enter the number → **Check**.

## Why `.featured.sale`?
No space between the classes = **same element has both classes** (AND).
`.featured .sale` (with a space) would mean "a `.sale` *inside* a `.featured`" — a completely different selector.
Class order in the HTML doesn't matter, so `class="sale featured vip"` still matches.
