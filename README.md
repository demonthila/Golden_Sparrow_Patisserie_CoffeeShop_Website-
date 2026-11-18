# Golden Sparrow Patisserie – Website

Hand-coded static website (HTML, CSS, JavaScript – no frameworks) for Golden Sparrow Patisserie, East Village, Sunbury VIC.
Built by NovaLink Innovations.

## Pages
- `index.html` – Home
- `menu.html` – Menu (no prices, by client request)
- `about.html` – Our story
- `faq.html` – FAQ

## Editing
Business details, hours, menu items and FAQs live in `build.py`. Edit them, then run:

```bash
python3 build.py
```

All four pages are regenerated. If opening hours change, also update `HOURS` near the top of `assets/main.js` (it powers the "Open today" badge).

## To do
- Replace photo placeholders with real or stock photos
- Replace sample menu items with the client's menu PDF
- Add the real logo (placeholder sparrow mark for now)

## Deploy
Hostinger Git deployment from the `main` branch to `vv.novalinkinnovations.com`, with auto-deploy on push.
