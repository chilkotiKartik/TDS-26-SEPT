# Q19 · Replace across files (2 marks)

## Question
Unzip `q-replace-across-files.zip` into a new folder, replace every **IITM** (any case) with **IIT Madras** in all
files **without changing line endings**, and report `cat * | sha256sum`.

## Answer
```
ac09a205682af5f8082a51bb37ce6e68deab345f39a682ba42388187c951afd5  -
```
*(10 files, file0.txt … file9.txt — your hash will differ)*

## Steps — [`solve.sh`](solve.sh)
```bash
mkdir replaced && cd replaced
unzip ../q-replace-across-files.zip
sed -i 's/iitm/IIT Madras/gI' *
cat * | sha256sum
```

## Gotchas
- The `I` flag in `s/…/…/gI` = case-insensitive (GNU sed). On macOS use `gsed` or
  `perl -pi -e 's/iitm/IIT Madras/gi' *`.
- **Never** open and re-save the files in Notepad/VS Code — they may convert `\r\n` ↔ `\n` and the hash changes.
- `sed -i` keeps line endings as they are, which is exactly what we want.
