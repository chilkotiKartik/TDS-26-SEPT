# Q24 · Use GitHub (1 mark)

## Question
Create a public repo, commit `email.json` containing `{"email": "24f2004962@ds.study.iitm.ac.in"}`, and submit its **raw** URL.

## Answer
- File: [`../email.json`](../email.json)
- Submitted: `https://raw.githubusercontent.com/chilkotiKartik/tds-ga0/main/email.json` ✅

## Steps
1. In your repo: **Add file → Create new file** → name `email.json`.
2. Content (exactly, with your email):
   ```json
   {"email": "24f2004962@ds.study.iitm.ac.in"}
   ```
3. **Commit changes**.
4. Open the file → click **Raw** → copy the `raw.githubusercontent.com/...` URL → submit.

### Command-line version
```bash
echo '{"email": "24f2004962@ds.study.iitm.ac.in"}' > email.json
git add email.json
git commit -m "Add email.json for TDS GA0"
git push
```
