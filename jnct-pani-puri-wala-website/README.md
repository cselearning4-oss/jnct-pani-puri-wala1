# JNCT Pani Puri Wala

A mobile-friendly Flask website for JNCT Pani Puri Wala.

## Run on Windows
```powershell
cd C:\pani-puri-website
python -m pip install -r requirements.txt
python app.py
```
Then open:
- PC: http://127.0.0.1:5000
- Phone on the same Wi-Fi: http://YOUR-PC-IP:5000

## Deploy publicly on Render
1. Create a GitHub repository and upload all files in this folder.
2. On Render, create a new Web Service from that GitHub repository.
3. Render detects `render.yaml`, or enter:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. Deploy. Render will give you a public HTTPS address.

The site uses the real pani-puri photo supplied by the owner and an original JNCT chef mascot.
