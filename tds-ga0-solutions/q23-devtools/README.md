# Q23 · Use DevTools (1 mark)

## Question
"Just above this paragraph, there's a hidden input with a secret value. What is it?"

## Answer
**`eoko70fqtj`** *(personalised)* ✅

## Steps
1. Right-click the question text → **Inspect**.
2. In the **Elements** panel look just above the paragraph for `<input type="hidden" value="…">`.
3. Or, in the **Console**:
   ```js
   document.querySelectorAll('input[type="hidden"]').forEach(i => console.log(i.value))
   ```
4. Paste the value → **Check**.
