# Q15 · LLM Sentiment Analysis with httpx (1 mark)

## Question
Write a Python program that uses **httpx** to POST to OpenAI's chat completions API with:
- a dummy `Authorization` header, model `gpt-4o-mini`
- **message 1 (system):** analyse sentiment as GOOD, BAD or NEUTRAL
- **message 2 (user):** *exactly* the given random text

My text was: `8  cic Eb5Mx Xsuk8b1Pxt  5kFGdALCuw02rwCz n7K CmSP` *(personalised — note the double spaces)*

## Answer — [`sentiment_request.py`](sentiment_request.py) ✅

## Steps
1. Copy **your** random text from the question exactly (keep double spaces).
2. Paste it into the user message, paste the whole program → **Check**.

## Gotcha
My first submission used a variable `text = "..."` and `{"role": "user", "content": text}`.
The checker (which reads the code, it doesn't run it) couldn't resolve the variable and grabbed some other string.
Putting the **literal string directly inside the user message** fixed it.
