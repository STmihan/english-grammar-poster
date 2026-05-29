"""Convert english-grammar-poster.html to PDF using Playwright."""

from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent
HTML_FILE = ROOT / "english-grammar-poster.html"
PDF_FILE = ROOT / "english-grammar-poster.pdf"


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(HTML_FILE.as_uri())
        page.wait_for_timeout(2000)
        page.pdf(
            path=str(PDF_FILE),
            format="A2",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        browser.close()
    print(f"PDF saved to {PDF_FILE}")


if __name__ == "__main__":
    main()
