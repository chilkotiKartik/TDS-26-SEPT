# Q13 · Create a GitHub Action (1 mark)

## Question
Create a GitHub Action in a repo where **one step's name contains your email**, trigger it, make sure it's the
most recent run, and submit the repo URL.

## Answer
- Workflow: [`../.github/workflows/ci.yml`](../.github/workflows/ci.yml) (also copied here as [`ci.yml`](ci.yml))
- Submitted: `https://github.com/chilkotiKartik/tds-ga0` ✅

```yaml
name: TDS GA0 action
on:
  push:
  workflow_dispatch:
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: 24f2004962@ds.study.iitm.ac.in
        run: echo "Hello, world!"
```

## Steps
1. github.com → **+ → New repository** → public, add README → Create.
2. **Add file → Create new file** → name it `.github/workflows/ci.yml` (the slashes create folders).
3. Paste the YAML (replace the email with yours) → **Commit changes**.
4. Open the **Actions** tab → wait for the green ✔ (~30 s).
5. Submit the repo URL.

## Gotcha — `No runs found`
I first pasted `https://github.com/chilkotiKartik/tds-ga0.git`. The checker parses `owner/repo` from the URL and
called the API for a repo literally named `tds-ga0.git` → *"No runs found"*. Remove the `.git`.

Every later commit triggers a new run (because of `on: push`), and since every run contains the email step,
it stays correct.
