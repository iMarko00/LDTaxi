# LD Taxi

Static taxi website. No install or build step is required.

## Run locally

```sh
python3 -m http.server 8000
```

Open http://localhost:8000. Stop the server with Ctrl+C.

## Editing

- `index.html`: page structure and German fallback content.
- `css/redesign.css`: shared responsive styling based on the supplied design reference.
- `css/legal.css`: Impressum layout and tappable contact links.
- `js/translate.js`: German, English, Serbian Cyrillic and Russian copy, language detection and manual switch.
- `impressum.html`: redesigned legal notice with shared localization.

The site always starts in German, so search engines index the German content. The footer switch (`de`, `en`, `sr` or `ru`; Serbian is displayed in Cyrillic) translates the page in place and saves the choice in local storage under `ldtaxi.language`. Remove that key to return to German. If storage is blocked, switching still works for the current page.

## SEO

- `robots.txt` and `sitemap.xml` live in the root; update `lastmod` in the sitemap when page content changes.
- `index.html` carries a `TaxiService` JSON-LD block. Keep its phone, address and opening hours identical to the Impressum and the Google Business Profile.
- Share preview: `assets/img/og-image.png` (1200×630).

The contact form retains the existing FormSubmit POST endpoint for `info@ldtaxi.net`. Name, phone and email are required. Pickup, destination and message are included in the inquiry. A submitted inquiry is not a confirmed booking. Delivery depends on the existing FormSubmit account configuration; local checks do not send real inquiries.

Google Fonts requires an internet connection; system font fallbacks are provided. Both pages share the base stylesheet and localization script; the Impressum also loads its own stylesheet; neither loads the legacy Bootstrap assets.
