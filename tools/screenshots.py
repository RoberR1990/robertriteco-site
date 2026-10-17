"""Maakt de schermafbeeldingen van de projecten (Playwright, chromium). Eenmalig: pip install playwright pillow."""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path(__file__).parent.parent / "static" / "img"
SHOTS = [
    ("raadzoeker", "https://raadzoeker.nl/", 3000, {"x": 0, "y": 0, "width": 1440, "height": 810}),
    ("doorzicht", "https://roberr1990.github.io/doorzicht/", 5000, {"x": 620, "y": 100, "width": 820, "height": 640}),
    ("bordenschouw", "https://roberr1990.github.io/bordenschouw/#kaart", 3000, {"x": 0, "y": 0, "width": 1440, "height": 810}),
]
only = sys.argv[1:]
with sync_playwright() as p:
    import glob, os
    exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    b = p.chromium.launch(executable_path=exe, args=["--use-gl=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"])
    for name, url, wait, clip in SHOTS:
        if only and name not in only:
            continue
        pg = b.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
        pg.add_init_script("try{localStorage.setItem('rz-welkom','1');localStorage.setItem('rz-tour-index','1')}catch(e){}")
        pg.goto(url, wait_until="networkidle")
        pg.wait_for_timeout(wait)
        pg.screenshot(path=str(OUT / f"{name}.jpg"), type="jpeg", quality=82, clip=clip)
        print(name, (OUT / f"{name}.jpg").stat().st_size // 1024, "kB")
        pg.close()
    b.close()
