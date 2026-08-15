import sys
import os
from datetime import datetime
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright

if len(sys.argv) < 2:
    print("Usage: python detonate.py <URL>")
    sys.exit(1)

URL = sys.argv[1]

os.makedirs("/app/screenshots", exist_ok=True)
os.makedirs("/app/reports", exist_ok=True)

timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

screenshot_file = f"/app/screenshots/{timestamp}.png"
report_file = f"/app/reports/{timestamp}.txt"

print("=" * 50)
print("PHISHING URL DETONATION")
print("=" * 50)
print(f"[+] URL: {URL}")

try:
    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ]
        )

        page = browser.new_page()

        response = page.goto(
            URL,
            wait_until="domcontentloaded",
            timeout=30000
        )

        final_url = page.url
        title = page.title()

        status = response.status if response else "Unknown"

        print(f"[+] HTTP Status: {status}")
        print(f"[+] Final URL: {final_url}")
        print(f"[+] Page Title: {title}")

        page.screenshot(
            path=screenshot_file,
            full_page=True
        )

        browser.close()

    parsed = urlparse(final_url)

    report = f"""
PHISHING URL DETONATION REPORT
==============================

Analysis Time UTC:
{timestamp}

Original URL:
{URL}

Final URL:
{final_url}

Domain:
{parsed.netloc}

HTTP Status:
{status}

Page Title:
{title}

Screenshot:
{os.path.basename(screenshot_file)}

Result:
Browser successfully loaded the URL.
"""

except Exception as e:

    print(f"[!] Navigation error: {e}")

    report = f"""
PHISHING URL DETONATION REPORT
==============================

Analysis Time UTC:
{timestamp}

Original URL:
{URL}

Result:
Navigation failed.

Error:
{e}
"""

with open(report_file, "w") as f:
    f.write(report)

print(f"[+] Report: {report_file}")
print(f"[+] Screenshot: {screenshot_file}")
print("[+] Analysis complete")
