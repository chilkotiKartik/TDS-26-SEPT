@echo off
REM Terminal 1: start Ollama with CORS open
set OLLAMA_ORIGINS=*
start "ollama" cmd /k ollama serve
timeout /t 3 >nul
REM Terminal 2: expose via ngrok with the email header
ngrok http 11434 --response-header-add "X-Email: 24f2004962@ds.study.iitm.ac.in" --response-header-add "Access-Control-Expose-Headers: *" --response-header-add "Access-Control-Allow-Headers: Authorization,Content-Type,User-Agent,Accept,Ngrok-skip-browser-warning"
