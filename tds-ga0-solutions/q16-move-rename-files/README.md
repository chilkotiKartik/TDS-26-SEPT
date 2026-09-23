# Q16 · Move and rename files (3 marks)

## Question
Extract `q-move-rename-files.zip`, **move** every file from all sub-folders into one empty folder, then rename each
file replacing every digit with the next one (`1→2`, `9→0`; `a1b9c.txt → a2b0c.txt`).
Report the output of `grep . * | LC_ALL=C sort | sha256sum`.

## Answer
```
648a6f117820fa41be9bfab9a556fe26b64045f554f7e3c3141768be5cb2cc76  -
```
*(29 files in my zip — your hash will differ)*

## Steps — [`solve.sh`](solve.sh) (Git Bash / WSL / macOS / Linux)
```bash
unzip q-move-rename-files.zip -d extracted
mkdir flat
find extracted -type f -exec mv {} flat/ \;
cd flat
for f in *; do
  new=$(echo "$f" | sed 'y/0123456789/1234567890/')
  [ "$f" != "$new" ] && mv -- "$f" "$new"
done
grep . * | LC_ALL=C sort | sha256sum
```

## Gotchas
- `sed 'y/…/…/'` transliterates **every** digit at once — doing `s/1/2/g` then `s/2/3/g` would chain and be wrong.
- `LC_ALL=C` matters: without it `sort` uses locale rules and the hash changes.
- Run it in **bash**, not PowerShell (`grep`/`sha256sum` behave differently or don't exist).
