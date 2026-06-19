"""
TASK 3: Task Automation with Python Scripts — CodeAlpha Python Internship
Goal: Automate small real-life repetitive tasks.
Key Concepts: os, shutil, re, requests, file handling

This file contains all 3 automation scripts:
  A) Move .jpg files to a new folder
  B) Extract email addresses from a .txt file
  C) Scrape the title of a webpage and save it
"""

import os
import re
import shutil
import requests
from html.parser import HTMLParser


# ═══════════════════════════════════════════════════════════════
# SCRIPT A: Move .jpg Files to a New Folder
# ═══════════════════════════════════════════════════════════════

def move_jpg_files(source_folder=".", destination_folder="jpg_files"):
    """
    Scan `source_folder` for .jpg / .jpeg files and move them
    all into `destination_folder` (created automatically if absent).
    """
    print("\n" + "=" * 50)
    print("  📁  SCRIPT A: Move JPG Files")
    print("=" * 50)

    if not os.path.isdir(source_folder):
        print(f"  ❌ Source folder not found: '{source_folder}'")
        return

    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    jpg_files = [
        f for f in os.listdir(source_folder)
        if f.lower().endswith((".jpg", ".jpeg")) and
           os.path.isfile(os.path.join(source_folder, f))
    ]

    if not jpg_files:
        print("  ⚠️  No .jpg / .jpeg files found in the source folder.")
        return

    moved = 0
    for filename in jpg_files:
        src = os.path.join(source_folder, filename)
        dst = os.path.join(destination_folder, filename)
        # Avoid overwriting: rename if file already exists at destination
        if os.path.exists(dst):
            base, ext = os.path.splitext(filename)
            dst = os.path.join(destination_folder, f"{base}_copy{ext}")
        shutil.move(src, dst)
        print(f"  ✅ Moved: {filename} → {destination_folder}/")
        moved += 1

    print(f"\n  Done! {moved} file(s) moved to '{destination_folder}/'")


# ═══════════════════════════════════════════════════════════════
# SCRIPT B: Extract Email Addresses from a .txt File
# ═══════════════════════════════════════════════════════════════

def extract_emails(input_file="input.txt", output_file="emails_found.txt"):
    """
    Read `input_file`, find all email addresses using regex,
    and save unique results to `output_file`.
    """
    print("\n" + "=" * 50)
    print("  📧  SCRIPT B: Extract Email Addresses")
    print("=" * 50)

    if not os.path.isfile(input_file):
        # Create a demo input file so the script can be tested immediately
        demo_content = (
            "Contact us at support@codealpha.tech or info@example.com.\n"
            "You can also reach out to hello.world@gmail.com and\n"
            "admin@company.org for more details.\n"
            "Duplicate test: support@codealpha.tech again.\n"
            "Invalid: notanemail@, @missinguser.com\n"
        )
        with open(input_file, "w") as f:
            f.write(demo_content)
        print(f"  ℹ️  '{input_file}' not found — created a demo file for testing.")

    with open(input_file, "r") as f:
        text = f.read()

    # Regex pattern for email addresses
    email_pattern = r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, text)
    unique_emails = sorted(set(emails))

    if not unique_emails:
        print("  ⚠️  No email addresses found.")
        return

    with open(output_file, "w") as f:
        f.write(f"Emails extracted from: {input_file}\n")
        f.write(f"Total unique emails found: {len(unique_emails)}\n")
        f.write("-" * 40 + "\n")
        for email in unique_emails:
            f.write(email + "\n")

    print(f"  Found {len(unique_emails)} unique email(s):")
    for email in unique_emails:
        print(f"    • {email}")
    print(f"\n  💾 Saved to '{output_file}'")


# ═══════════════════════════════════════════════════════════════
# SCRIPT C: Scrape Webpage Title and Save It
# ═══════════════════════════════════════════════════════════════

class TitleParser(HTMLParser):
    """Simple HTML parser to extract the <title> tag content."""

    def __init__(self):
        super().__init__()
        self._in_title = False
        self.title = None

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "title":
            self._in_title = True

    def handle_data(self, data):
        if self._in_title and self.title is None:
            self.title = data.strip()

    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self._in_title = False


def scrape_title(url="https://www.python.org", output_file="scraped_title.txt"):
    """
    Fetch the page at `url`, extract its <title>, and save it to `output_file`.
    """
    print("\n" + "=" * 50)
    print("  🌐  SCRIPT C: Scrape Webpage Title")
    print("=" * 50)
    print(f"  Fetching: {url}")

    try:
        headers = {"User-Agent": "Mozilla/5.0 (CodeAlpha Python Bot)"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"  ❌ Failed to fetch page: {e}")
        return

    parser = TitleParser()
    parser.feed(response.text)
    title = parser.title or "No title found"

    print(f"  ✅ Page title: '{title}'")

    with open(output_file, "w") as f:
        f.write(f"URL   : {url}\n")
        f.write(f"Title : {title}\n")

    print(f"  💾 Saved to '{output_file}'")


# ═══════════════════════════════════════════════════════════════
# MAIN MENU
# ═══════════════════════════════════════════════════════════════

def main():
    print("\n" + "=" * 50)
    print("  🤖  TASK AUTOMATION SCRIPTS — CodeAlpha")
    print("=" * 50)
    print("  A) Move .jpg files to a folder")
    print("  B) Extract emails from a text file")
    print("  C) Scrape a webpage title")
    print("  D) Run ALL scripts")
    print("=" * 50)

    choice = input("\n  Choose option (A/B/C/D): ").strip().upper()

    if choice == "A":
        src = input("  Source folder path (press Enter for current dir): ").strip() or "."
        dst = input("  Destination folder name (default: jpg_files): ").strip() or "jpg_files"
        move_jpg_files(src, dst)

    elif choice == "B":
        inp = input("  Input .txt file (default: input.txt): ").strip() or "input.txt"
        out = input("  Output file (default: emails_found.txt): ").strip() or "emails_found.txt"
        extract_emails(inp, out)

    elif choice == "C":
        url = input("  URL to scrape (default: https://www.python.org): ").strip() or "https://www.python.org"
        out = input("  Output file (default: scraped_title.txt): ").strip() or "scraped_title.txt"
        scrape_title(url, out)

    elif choice == "D":
        move_jpg_files()
        extract_emails()
        scrape_title()

    else:
        print("  ⚠️  Invalid option. Please run again and choose A, B, C, or D.")

    print("\n  Automation complete! ✅\n")


if __name__ == "__main__":
    main()
