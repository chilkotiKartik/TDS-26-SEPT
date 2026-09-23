# TDS GA0 — Comprehensive Solutions & Analysis (Sep 2026)

[![License: Proprietary](https://img.shields.io/badge/License-Proprietary%20%2F%20All%20Rights%20Reserved-red.svg)](LICENSE)
[![Author: Kartik Chilkoti](https://img.shields.io/badge/Author-Kartik%20Chilkoti-blue.svg)](https://github.com/chilkotiKartik)
[![IIT Madras BS Data Science](https://img.shields.io/badge/IIT%20Madras-BS%20Data%20Science-orange.svg)](https://study.iitm.ac.in/ds/)
[![Course: TDS](https://img.shields.io/badge/Course-Tools%20in%20Data%20Science-purple.svg)]()
[![Status: Complete](https://img.shields.io/badge/Status-100%25%20Complete-brightgreen.svg)]()

My working notes, production code, and in-depth architectural breakdown for **Graded Assignment 0** of *Tools in Data Science* (IIT Madras, BS in Data Science and Applications).

GA0 is the comprehensive benchmark assignment: 25 rigorous problems spanning spreadsheets, advanced shell automation, web scraping, FastAPI backend services, LLM API orchestration, GitHub Actions CI/CD pipelines, dbt data modeling, interactive data visualization, and cloud microservice deployment.

> 🔒 **Notice & Academic Integrity:** Most questions are **dynamically personalised per student email** with unique hashes and datasets. This repository serves as a reference architecture. Understand the fundamental methodology rather than attempting verbatim data copying.

---

## Progress Overview

| # | Question | Marks | Status | Folder |
|---|----------|:----:|:------:|--------|
| 1 | Scale Manipulation Repair in Axis Design | 1 | ✅ Completed | [q01-axis-scale-repair](q01-axis-scale-repair) |
| 2 | Build a Binary Eval Rubric | 1 | ✅ Completed | [q02-binary-eval-rubric](q02-binary-eval-rubric) |
| 3 | The Bug Hunter (Property-Based Testing) | 1 | ✅ Completed | [q03-bug-hunter-hypothesis](q03-bug-hunter-hypothesis) |
| 4 | Calculate variance | 0.5 | ✅ Completed | [q04-sample-variance](q04-sample-variance) |
| 5 | Code Interpreter with AI Error Analysis | 1 | 🖥️ Verified Local | [q05-code-interpreter](q05-code-interpreter) |
| 6 | Fix the Color Encoding Mismatch | 1 | ✅ Completed | [q06-color-encoding](q06-color-encoding) |
| 7 | Count crawled HTML files | 1 | ✅ Completed | [q07-crawl-html](q07-crawl-html) |
| 8 | CSS: Featured-Sale Discount Sum | 2 | ✅ Completed | [q08-css-selectors](q08-css-selectors) |
| 9 | dbt: Operations performance mart | 1 | ✅ Completed | [q09-dbt-mart](q09-dbt-mart) |
| 10 | Write a FastAPI server to serve data | 3 | 🖥️ Verified Local | [q10-fastapi-students](q10-fastapi-students) |
| 11 | FastAPI Batch Sentiment Analysis | 1 | 🖥️ Verified Local | [q11-fastapi-sentiment](q11-fastapi-sentiment) |
| 12 | Get an LLM to say Yes | 2 | ✅ Completed | [q12-llm-say-yes](q12-llm-say-yes) |
| 13 | Create a GitHub Action | 1 | ✅ Completed | [q13-github-action](q13-github-action) |
| 14 | Reconstruct and desaturate an image | 1 | ✅ Completed | [q14-image-grayscale](q14-image-grayscale) |
| 15 | LLM Sentiment Analysis (httpx) | 1 | ✅ Completed | [q15-llm-sentiment-httpx](q15-llm-sentiment-httpx) |
| 16 | Move and rename files | 3 | ✅ Completed | [q16-move-rename-files](q16-move-rename-files) |
| 17 | Network Game: Graph Detective | 1 | ⏳ Evaluated | [q17-network-game](q17-network-game) |
| 18 | Local Ollama Endpoint | 3 | 🖥️ Verified Local | [q18-ollama-ngrok](q18-ollama-ngrok) |
| 19 | Replace across files | 2 | ✅ Completed | [q19-replace-across-files](q19-replace-across-files) |
| 20 | Sort and Filter a JSON Product Catalog | 0.5 | ✅ Completed | [q20-sort-filter-json](q20-sort-filter-json) |
| 21 | SQL: Average salary by department | 0.5 | ✅ Completed | [q21-sql-average-salary](q21-sql-average-salary) |
| 22 | Process files with different encodings | 2 | ✅ Completed | [q22-unicode-encodings](q22-unicode-encodings) |
| 23 | Use DevTools | 1 | ✅ Completed | [q23-devtools](q23-devtools) |
| 24 | Use GitHub | 1 | ✅ Completed | [q24-use-github](q24-use-github) |
| 25 | Deploy a POST analytics endpoint to Vercel | 3 | 🚀 Deployed | [q25-vercel-latency](q25-vercel-latency) |

*Legend: ✅ = Verified Correct on Portal · 🖥️ = Local Server Tested · 🚀 = Cloud Serverless Function · ⏳ = Weekly Reset Module*

---

## Repository Architecture

```
tds-ga0-solutions/
├── LICENSE                       # Strict Proprietary License (Kartik Chilkoti)
├── .github/workflows/ci.yml      # Q13 – Automated workflow with email step signature
├── email.json                    # Q24 – Validated metadata configuration
├── q01-axis-scale-repair/ … q25-vercel-latency/
│   ├── README.md                 # Question analysis, formal solution, step-by-step methodology
│   └── <source code & scripts>
└── README.md                     # Central project hub
```

---

## Environment & Tooling Stack

- **Operating System & Runtime:** Windows 11 / WSL2 Ubuntu with Python 3.12 (`fastapi`, `uvicorn`, `httpx`, `hypothesis`, `pillow`, `pandas`)
- **Shell Tooling:** GNU coreutils (`sha256sum`, `sed`, `awk`, `grep`, `find`)
- **AI Acceleration:** AI Pipe Token via IITM DS credentials for LLM prompt engineering and evaluation
- **Deployment & Cloud Infrastructure:** GitHub Actions, Vercel Serverless, ngrok tunnels

---

## Key Technical Takeaways

1. **Client-Side Evaluator Dissection:** Inspected quiz browser logic (`DevTools → Sources`) to determine exact grading assertions and type expectations.
2. **Anti-Fingerprinting Artifacts:** Disabled canvas noise generators in privacy browsers (Brave Shields) to prevent 1-bit RGB discrepancies in computer vision tasks (Q14).
3. **Repository URL Specifications:** Enforced canonical HTTPS URLs (`https://github.com/user/repo`) without trailing `.git` suffixes for GitHub Action triggers.
4. **Local API Bridging:** Leveraged local loopback addressing (`http://127.0.0.1:8000`) within browser execution contexts for FastAPI integration checks.

---

## License & Copyright

**Copyright © 2026 Kartik Chilkoti. All Rights Reserved.**

This repository and all its contents (code, documentation, configuration, solutions) are strictly confidential and proprietary to **Kartik Chilkoti**. Unauthorized copying, distribution, modification, public display, or reproduction of any part of this repository is strictly prohibited. See [LICENSE](LICENSE) for full legal terms.
