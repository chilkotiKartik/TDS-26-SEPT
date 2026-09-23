# Q25 · Deploy a POST analytics endpoint to Vercel (3 marks)

## Question
Deploy a Python endpoint on **Vercel** that accepts
```json
{"regions": ["apac", "amer"], "threshold_ms": 179}
```
and returns, per region, from the telemetry in `q-vercel-latency.json`:
`avg_latency` (mean), `p95_latency` (95th percentile), `avg_uptime` (mean), `breaches` (count above threshold).
CORS must allow POST from any origin, and the hostname must end with `vercel.app`.

## Answer — [`api/index.py`](api/index.py)
- FastAPI app, catch-all `POST` route (works at `/api/latency` or anywhere), explicit `Access-Control-Allow-Origin: *`.
- **p95** uses linear interpolation — the same formula as the checker:
  `pos = (n − 1) × 0.95`, then interpolate between the two neighbouring sorted values
  (same as `numpy.percentile(x, 95)` default).
- Rounds latency to 2 decimals, uptime to 3 — matching the checker.
- Response shape: `{"regions": [{"region": "apac", "avg_latency": …, "p95_latency": …, "avg_uptime": …, "breaches": …}, …]}`

## Folder layout
```
q25-vercel-latency/
├── api/index.py
├── q-vercel-latency.json     <- download YOUR copy from the question
├── requirements.txt
└── vercel.json               <- rewrites every path to api/index
```

## Steps
1. Install Node.js (LTS) from nodejs.org, then:
   ```bash
   npm install -g vercel
   vercel login
   ```
2. Download `q-vercel-latency.json` from the question into this folder.
3. From this folder:
   ```bash
   vercel --prod
   ```
   Answers: set up & deploy → **Y**, link to existing → **N**, accept defaults.
4. It prints `Production: https://<name>.vercel.app`.
5. Submit `https://<name>.vercel.app/api/latency` → **Check** → **Save**.

## Test after deploying
```bash
curl -X POST https://<name>.vercel.app/api/latency \
  -H "Content-Type: application/json" \
  -d "{\"regions\":[\"apac\",\"amer\"],\"threshold_ms\":179}"
```

## Gotchas
- Forgetting to include the JSON file in the deploy → 500 error (it must sit next to `vercel.json`).
- Vercel preview URLs may be behind "Deployment Protection" — use the **production** URL or turn protection off
  in Project → Settings.
