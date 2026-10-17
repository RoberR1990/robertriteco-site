"""Maakt static/og.png (1200x630, deelafbeelding voor LinkedIn). Playwright + Edge."""
from pathlib import Path
from playwright.sync_api import sync_playwright

HTML = """<!doctype html><meta charset=utf-8>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,500..800&family=IBM+Plex+Mono:wght@500&display=swap" rel=stylesheet>
<style>
body{margin:0;width:1200px;height:630px;background:#2B3DE0;color:#fff;font-family:Archivo,Arial;display:flex;flex-direction:column;justify-content:space-between;padding:64px 72px;box-sizing:border-box}
.n{font:700 46px Archivo;font-stretch:118%;letter-spacing:-.01em}
h1{margin:0;font:700 78px/1.04 Archivo;font-stretch:112%;letter-spacing:-.015em;max-width:760px}
.s{font:500 22px 'IBM Plex Mono';letter-spacing:.08em;text-transform:uppercase;opacity:.9}
svg{position:absolute;right:56px;top:150px;width:420px}
</style>
<div class=n>Robert Riteco</div>
<h1>Data en AI, samengebracht in slimme tools die werken.</h1>
<div class=s>robertriteco.nl</div>
<svg viewBox="0 0 360 230"><defs><clipPath id=c><circle cx=130 cy=115 r=100 /></clipPath></defs>
<circle cx=130 cy=115 r=100 fill=none stroke=#fff stroke-width=3 /><circle cx=230 cy=115 r=100 fill=none stroke=#fff stroke-width=3 />
<circle cx=230 cy=115 r=100 clip-path=url(#c) fill=#fff />
<g font-family=Archivo font-weight=700 font-size=20 fill=#fff text-anchor=middle><text x=80 y=122>Data</text><text x=280 y=122>AI</text></g>
<text x=180 y=120 text-anchor=middle font-family="IBM Plex Mono" font-size=12 fill=#2B3DE0 letter-spacing=1>TOOLS</text></svg>"""

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    pg = b.new_page(viewport={"width": 1200, "height": 630})
    pg.set_content(HTML, wait_until="networkidle")
    pg.wait_for_timeout(800)
    pg.screenshot(path=str(Path(__file__).parent.parent / "static" / "og.png"))
    b.close()
