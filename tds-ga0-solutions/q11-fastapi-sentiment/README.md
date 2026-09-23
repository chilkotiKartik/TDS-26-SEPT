# Q11 · FastAPI Batch Sentiment Analysis (1 mark)

## Question
`POST /sentiment` with `{"sentences": [...]}` → `{"results": [{"sentence": ..., "sentiment": "happy"|"sad"|"neutral"}, ...]}`
in the same order. The checker sends 10 random sentences; **7/10** correct = full marks. Any method allowed.

## Answer — [`main.py`](main.py)
A small **lexicon classifier**: count happy words vs sad words, plus two idiom overrides
("tears of joy", "cloud nine"). No model, no API key, instant responses.

I checked it against the quiz's own pool of ~99 test sentences (e.g. *"My pet passed away yesterday."* → sad,
*"The store opens at 9 AM."* → neutral, *"I'm on cloud nine!"* → happy) and it gets all of them right,
so 7/10 is very safe.

## Steps
1. Stop any other server using port 8000 (Ctrl + C in its window).
2. Put `main.py` in a folder, open `cmd` there:
   ```bash
   pip install fastapi uvicorn
   python main.py
   ```
3. Portal answer: `http://127.0.0.1:8000/sentiment` → **Check** → **Save**.

## Quick test
```bash
curl -X POST http://127.0.0.1:8000/sentiment -H "Content-Type: application/json" \
  -d "{\"sentences\": [\"I love this product!\", \"This is terrible.\", \"The meeting is at 3 PM.\"]}"
```

## Want a "real" model instead?
Swap `classify()` for an LLM call (AI Pipe / Ollama) with a prompt that must answer exactly one of the three labels.
The lexicon is just faster and deterministic for a 10-sentence check.
