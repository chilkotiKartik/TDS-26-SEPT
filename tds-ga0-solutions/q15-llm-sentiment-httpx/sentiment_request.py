import httpx

response = httpx.post(
    "https://api.openai.com/v1/chat/completions",
    headers={
        "Authorization": "Bearer dummy_api_key",
        "Content-Type": "application/json",
    },
    json={
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "Analyze the sentiment of the following text and classify it as GOOD, BAD, or NEUTRAL.",
            },
            {"role": "user", "content": "8  cic Eb5Mx Xsuk8b1Pxt  5kFGdALCuw02rwCz n7K CmSP"},
        ],
    },
)
response.raise_for_status()
print(response.json()["choices"][0]["message"]["content"])
