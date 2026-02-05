# Suspicious URL Detector 
This is a very simple Python project that checks if a URL might be **suspicious** or used in phishing.

I made this to learn more about cybersecurity and how bad URLs trick people.

# What It Does

- Checks if the URL uses an IP address
- Looks for dangerous symbols like `@`
- Warns if the URL is super long
- Flags words like "login", "bank", "verify", etc.

# How To Run

1. Make sure you have Python 3 installed
2. Download `detector.py`
3. Run it in your terminal:

```bash
python detector.py

type a url like: https://www.google.com

Example Output:
This URL looks OK( no red flags found)
