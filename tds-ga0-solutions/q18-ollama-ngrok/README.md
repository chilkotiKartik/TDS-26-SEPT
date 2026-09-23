# Q18 · Local Ollama Endpoint (3 marks)

## Question
Run Ollama locally with CORS enabled, expose it through **ngrok** with an extra response header
`X-Email: <your email>`, and submit the ngrok HTTPS URL.

## What the checker actually does
`GET <your-url>/api/version` with header `ngrok-skip-browser-warning` → the JSON must contain `version`,
and the response header `X-Email` must equal your email. **You don't need to download any model.**

## Steps (Windows)
### 1. Install
- Ollama: <https://ollama.com/download> → install → then **right-click the llama tray icon → Quit** (we restart it with CORS).
- ngrok: sign up at <https://ngrok.com>, download the Windows zip, put `ngrok.exe` in a folder, and run once:
  ```bash
  ngrok config add-authtoken <YOUR_AUTHTOKEN>
  ```

### 2. Terminal 1 — Ollama with CORS
```bat
set OLLAMA_ORIGINS=*
ollama serve
```
(macOS / Linux: `export OLLAMA_ORIGINS="*" && ollama serve`)

### 3. Terminal 2 — ngrok with the email header (one line)
```bash
ngrok http 11434 --response-header-add "X-Email: 24f2004962@ds.study.iitm.ac.in" --response-header-add "Access-Control-Expose-Headers: *" --response-header-add "Access-Control-Allow-Headers: Authorization,Content-Type,User-Agent,Accept,Ngrok-skip-browser-warning"
```
Copy the `Forwarding https://xxxx.ngrok-free.app` URL.

### 4. Submit
Paste `https://xxxx.ngrok-free.app` (nothing after it) → **Check** → **Save**. Keep both terminals open until it's Correct.

## Quick self-test
```bash
curl -i -H "ngrok-skip-browser-warning: 1" https://xxxx.ngrok-free.app/api/version
# look for:  x-email: 24f2004962@ds.study.iitm.ac.in   and   {"version":"..."}
```

## Troubleshooting
| Error | Fix |
|---|---|
| `bind: Only one usage of each socket address` | Ollama still running in the tray — quit it first |
| "Server is not running Ollama" | Terminal 1 isn't running `ollama serve` |
| "X-Email header mismatch" | typo in the ngrok command — Ctrl+C and paste again |
| "URL must be an ngrok forwarding domain" | use the `…ngrok-free.app` link |
