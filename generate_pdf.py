"""Convert english-grammar-poster.html to PDF, then rasterize to PNG."""

import subprocess
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent
HTML_FILE = ROOT / "english-grammar-poster.html"
PDF_FILE = ROOT / "english-grammar-poster.pdf"
PNG_FILE = ROOT / "english-grammar-poster.png"

GS = Path(r"C:\Program Files\gs\gs10.07.1\bin\gswin64c.exe")
DPI = 300


def generate_pdf():
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
    print(f"PDF saved to {PDF_FILE} ({PDF_FILE.stat().st_size // 1024} KB)")


def rasterize_to_png():
    subprocess.run(
        [
            str(GS),
            "-sDEVICE=png16m",
            f"-r{DPI}",
            "-dNOPAUSE",
            "-dBATCH",
            "-dQUIET",
            f"-sOutputFile={PNG_FILE}",
            str(PDF_FILE),
        ],
        check=True,
    )
    print(f"PNG saved to {PNG_FILE} ({PNG_FILE.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    generate_pdf()
    rasterize_to_png()
