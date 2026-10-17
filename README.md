# robertriteco.nl

Persoonlijke site met projecten, samenwerken en gedachten (NL + EN). Statisch, gebouwd met `python build.py`.

- `content.py` — alle teksten per taal, projecten en contactgegevens (hier een project toevoegen)
- `static/` — css, favicon, `_headers`
- `public/` — gegenereerde site (in git, Cloudflare Pages heeft geen build-commando nodig; uitvoermap `public`)

Lokaal: `python build.py && python -m http.server 8780 -d public`
