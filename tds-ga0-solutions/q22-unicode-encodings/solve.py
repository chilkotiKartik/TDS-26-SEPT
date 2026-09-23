import csv

SYMBOLS = {"Š", "œ", "†"}  # <- change to the symbols in your question
FILES = [
    ("data1.csv", "cp1252", ","),
    ("data2.csv", "utf-8", ","),
    ("data3.txt", "utf-16", "\t"),
]

total = 0
matches = 0
for name, enc, sep in FILES:
    with open(name, encoding=enc, newline="") as f:
        for row in csv.DictReader(f, delimiter=sep):
            if row["symbol"].strip() in SYMBOLS:
                total += float(row["value"])
                matches += 1

print("matching rows:", matches)
print("sum:", int(total) if total.is_integer() else total)
