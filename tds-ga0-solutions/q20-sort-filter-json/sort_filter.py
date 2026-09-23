import json
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "products.json"
threshold = float(sys.argv[2]) if len(sys.argv) > 2 else 117.71

products = json.load(open(path, encoding="utf-8"))
kept = [p for p in products if not p["price"] < threshold]
kept.sort(key=lambda p: (p["category"], -p["price"], p["name"]))
print(json.dumps(kept, separators=(",", ":"), ensure_ascii=False))
