import json
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA = json.loads((Path(__file__).parent.parent / "q-vercel-latency.json").read_text())


def percentile(values, q):
    v = sorted(values)
    pos = (len(v) - 1) * q
    lo = int(pos)
    frac = pos - lo
    return v[lo] + frac * (v[lo + 1] - v[lo]) if lo + 1 < len(v) else v[lo]


@app.post("/{path:path}")
async def latency(request: Request, path: str = ""):
    body = await request.json()
    regions = body.get("regions", [])
    threshold = body.get("threshold_ms", 180)
    out = []
    for region in regions:
        recs = [r for r in DATA if r["region"] == region]
        if not recs:
            out.append({"region": region, "avg_latency": 0, "p95_latency": 0, "avg_uptime": 0, "breaches": 0})
            continue
        lat = [r["latency_ms"] for r in recs]
        up = [r["uptime_pct"] for r in recs]
        out.append({
            "region": region,
            "avg_latency": round(sum(lat) / len(lat), 2),
            "p95_latency": round(percentile(lat, 0.95), 2),
            "avg_uptime": round(sum(up) / len(up), 3),
            "breaches": sum(1 for x in lat if x > threshold),
        })
    return JSONResponse({"regions": out}, headers={"Access-Control-Allow-Origin": "*"})


@app.get("/{path:path}")
def health(path: str = ""):
    return {"ok": True, "records": len(DATA)}
