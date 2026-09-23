# Q10 · Write a FastAPI server to serve data (3 marks)

## Question
Serve `q-fastapi.csv` (`studentId,class`) at `/api`:
- `/api` → all students `{"students": [{"studentId": 1, "class": "1A"}, …]}` in CSV order
- `/api?class=1A&class=1B` → only those classes, **still in CSV order**
- CORS enabled for GET from any origin

## Answer — [`main.py`](main.py)
The trick is `List[str] = Query(alias="class")` — `class` is a Python keyword, and a plain `str`
parameter would only keep the *last* `class=` value. Filtering the original list (instead of looping over
the requested classes) keeps CSV order automatically.

## Steps (Windows)
1. Install Python from python.org — **tick "Add python.exe to PATH"**.
2. Make a folder, put `main.py` in it, and download **your** `q-fastapi.csv` from the question into the same folder.
3. In that folder's address bar type `cmd` → Enter, then:
   ```bash
   pip install fastapi uvicorn
   python main.py
   ```
   You should see `Loaded 2000 students` and `Uvicorn running on http://127.0.0.1:8000`. Keep it open.
4. Sanity check in a browser: <http://127.0.0.1:8000/api?class=1A>
5. Portal answer: `http://127.0.0.1:8000/api` → **Check** → **Save**.

## Troubleshooting
| Problem | Fix |
|---|---|
| `python is not recognized` | Re-install Python with "Add to PATH" ticked |
| `No such file: q-fastapi.csv` | CSV must be in the same folder and named exactly `q-fastapi.csv` |
| Saved as `main.py.txt` | In Notepad's *Save As* pick **All Files (\*.\*)** |
| "Failed to fetch" | Server window closed, or Brave Shields blocking localhost — turn Shields off for the exam site |
