"""Volledige schermafbeeldingen van de site ter controle (licht/donker, desktop/mobiel). Gebruik: python tools/check.py"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    for name, scheme, w, url in [("home-licht", "light", 1280, "/"), ("home-donker", "dark", 1280, "/"), ("home-mobiel", "light", 390, "/"),
                                  ("project", "light", 1280, "/projecten/doorzicht/"), ("samenwerken", "light", 1280, "/samenwerken/")]:
        ctx = b.new_context(viewport={"width": w, "height": 900}, color_scheme=scheme)
        pg = ctx.new_page(); pg.goto("http://localhost:8780" + url, wait_until="networkidle"); pg.wait_for_timeout(600)
        over = pg.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
        pg.screenshot(path=str(OUT / f"{name}.png"), full_page=True)
        print(name, "overflow", over)
        ctx.close()
    b.close()
