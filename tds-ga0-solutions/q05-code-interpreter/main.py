import os
import sys
import json
import traceback
from io import StringIO
from typing import List

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class CodeRequest(BaseModel):
    code: str


class ErrorAnalysis(BaseModel):
    error_lines: List[int]


# ---------- Tool function ----------
def execute_python_code(code: str) -> dict:
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec(code, {"__name__": "__main__"})
        return {"success": True, "output": sys.stdout.getvalue()}
    except BaseException:
        return {"success": False, "output": traceback.format_exc()}
    finally:
        sys.stdout = old_stdout


def lines_from_traceback(code: str) -> List[int]:
    """Deterministic fallback: last frame inside the user's code (<string>)."""
    try:
        compile(code, "<string>", "exec")
    except SyntaxError as e:
        return [e.lineno] if e.lineno else []
    try:
        exec(code, {"__name__": "__main__"})
    except BaseException as e:
        frames = [f for f in traceback.extract_tb(e.__traceback__) if f.filename == "<string>"]
        if frames:
            return [frames[-1].lineno]
    return []


# ---------- AI agent (only on error) ----------
def analyze_error_with_ai(code: str, tb: str) -> List[int]:
    token = os.environ.get("AIPIPE_TOKEN")
    if not token:
        raise RuntimeError("no token")
    numbered = "\n".join(f"{i}: {l}" for i, l in enumerate(code.splitlines(), 1))
    prompt = (
        "Analyze this Python code and its error traceback. Identify the line number(s) "
        "in the CODE (not the traceback) where the error occurred. Use the deepest "
        '"<string>" frame in the traceback.\n\n'
        f"CODE (numbered):\n{numbered}\n\nTRACEBACK:\n{tb}"
    )
    r = httpx.post(
        "https://aipipe.org/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "model": "gpt-4.1-nano",
            "messages": [{"role": "user", "content": prompt}],
            "response_format": {
                "type": "json_schema",
                "json_schema": {
                    "name": "error_analysis",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "properties": {"error_lines": {"type": "array", "items": {"type": "integer"}}},
                        "required": ["error_lines"],
                        "additionalProperties": False,
                    },
                },
            },
        },
        timeout=30,
    )
    r.raise_for_status()
    content = r.json()["choices"][0]["message"]["content"]
    return ErrorAnalysis.model_validate_json(content).error_lines


@app.post("/code-interpreter")
def code_interpreter(req: CodeRequest):
    result = execute_python_code(req.code)
    if result["success"]:
        return {"error": [], "result": result["output"]}
    expected = lines_from_traceback(req.code)
    try:
        lines = analyze_error_with_ai(req.code, result["output"])
        # Trust the traceback if the AI disagrees with it
        if expected and sorted(lines) != expected:
            lines = expected
    except Exception:
        lines = expected
    return {"error": lines, "result": result["output"]}


@app.get("/")
def root():
    return {"status": "ok", "endpoint": "POST /code-interpreter"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
