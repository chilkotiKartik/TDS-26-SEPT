# Q5 · Code Interpreter with AI Error Analysis (1 mark)

## Question
Build `POST /code-interpreter` that takes `{"code": "..."}`, **runs** the Python code, and returns
```json
{"error": [3], "result": "Traceback ..."}
```
- `result` = exact stdout (or the full traceback on failure)
- `error` = the line number(s) where the error happened, found by an **AI agent with structured output**,
  called only when the code fails. CORS must be enabled.

## Answer — [`main.py`](main.py)
- `execute_python_code()` runs the code with `exec()` and captures stdout / `traceback.format_exc()`.
- On failure, `analyze_error_with_ai()` asks `gpt-4.1-nano` (through AI Pipe) for `{"error_lines": [...]}`
  using a strict **JSON schema** + a Pydantic model.
- Safety net: I also compute the line from the traceback itself (last `<string>` frame, or `SyntaxError.lineno`).
  If the AI disagrees with Python, Python wins. This made the endpoint pass every sample I tried
  (ZeroDivision, NameError inside a function, SyntaxError, RecursionError, wrong arg count, …).

## Steps
1. Install:
   ```bash
   pip install -r requirements.txt
   ```
2. *(Optional, for the AI part)* set your token:
   ```bash
   # Windows
   set AIPIPE_TOKEN=your_token
   # macOS / Linux
   export AIPIPE_TOKEN=your_token
   ```
3. Run it and **keep the window open**:
   ```bash
   python main.py
   ```
4. In the portal enter `http://127.0.0.1:8000/code-interpreter` → **Check** → **Save**.

> Works with localhost because the portal's checker runs inside *your* browser.

## Quick test
```bash
curl -X POST http://127.0.0.1:8000/code-interpreter \
  -H "Content-Type: application/json" \
  -d "{\"code\": \"x = 10\\ny = 0\\nprint(x / y)\"}"
# -> {"error":[3],"result":"Traceback (most recent call last): ... ZeroDivisionError: division by zero\n"}
```
