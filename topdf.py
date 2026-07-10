from playwright.sync_api import sync_playwright

html_path = "index.html"

with sync_playwright() as p:
    browser = p.chromium.launch()

    page = browser.new_page(
        viewport={
            "width": 794,
            "height": 1123
        }
    )

    page.goto(f"file:///{html_path}")

    page.pdf(
        path="resume.pdf",
        format="A4",
        print_background=True,
        margin={
            "top": "12mm",
            "bottom": "12mm",
            "left": "12mm",
            "right": "12mm"
        }
    )

    browser.close()