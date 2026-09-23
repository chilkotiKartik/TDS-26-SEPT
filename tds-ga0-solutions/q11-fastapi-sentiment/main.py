import re
from typing import List

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

HAPPY = set('''love loved loving happy happiest happiness joy joyful excited excitement thrilled amazing
awesome great fantastic wonderful best perfect perfectly grateful blessed delighted overjoyed ecstatic
proud bliss smiling smile grinning celebrating celebrate beautiful spectacular incredible incredibly
fortunate lucky energized alive dream winning won win promotion exceeded glad pleased enjoy enjoyed
brilliant excellent superb terrific cheerful elated radiating bursting accomplished opportunity
surprise engagement vacation hoping yay good nice'''.split())

SAD = set('''sad sadness worst terrible horrible awful hate hated heartbroken devastated depressed
depression lonely alone abandoned failed fail failure lost lose loss regret disappointed disappointing
disappointment rejected layoffs passed died death pain painful crying cry tears hopeless miserable
unhappy upset struggling struggle worse bad broken ended badly falling apart grief grieving nobody hurt
suffering sorrow gloomy anxious scared afraid angry frustrated tragic tragedy sick diagnosis cancelled
canceled missed stolen fired accident traumatized defeated empty shattered betrayal betrayed burdened
problems unfortunately worried exhausted ruined'''.split())


def classify(text: str) -> str:
    low = text.lower()
    words = re.findall(r"[a-z']+", low)
    h = sum(w in HAPPY for w in words)
    s = sum(w in SAD for w in words)
    # idioms that word counting gets wrong
    if "tears of joy" in low or "cloud nine" in low:
        h += 2
    if h > s:
        return "happy"
    if s > h:
        return "sad"
    return "neutral"


class SentimentRequest(BaseModel):
    sentences: List[str]


@app.post("/sentiment")
def sentiment(req: SentimentRequest):
    return {"results": [{"sentence": s, "sentiment": classify(s)} for s in req.sentences]}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
