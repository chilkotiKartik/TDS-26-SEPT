import csv
from typing import List

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# keep rows in the exact CSV order
students = []
with open("q-fastapi.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        students.append({"studentId": int(row["studentId"]), "class": row["class"]})


@app.get("/api")
def get_students(class_: List[str] = Query(default=[], alias="class")):
    if not class_:
        return {"students": students}
    wanted = set(class_)
    return {"students": [s for s in students if s["class"] in wanted]}


if __name__ == "__main__":
    import uvicorn

    print("Loaded", len(students), "students")
    uvicorn.run(app, host="127.0.0.1", port=8000)
