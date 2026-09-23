import json
import statistics
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "q-calculate-variance.json"
data = json.load(open(path))
print("n    =", len(data))
print("mean =", statistics.mean(data))
print("sample variance =", round(statistics.variance(data), 2))
