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

Language selection uses the first supported language in the device/browser preferences (`de`, `en`, `sr` or `ru`, including regional variants; Serbian is displayed in Cyrillic). Unsupported languages fall back to German. The footer switch saves a manual preference in local storage. Remove `ldtaxi.language` from local storage to return to automatic selection. If storage is blocked, detection and switching still work for the current page.

The contact form retains the existing FormSubmit POST endpoint for `info@ldtaxi.net`. Name, phone and email are required. Pickup, destination and message are included in the inquiry. A submitted inquiry is not a confirmed booking. Delivery depends on the existing FormSubmit account configuration; local checks do not send real inquiries.

Google Fonts requires an internet connection; system font fallbacks are provided. Both pages share the base stylesheet and localization script; the Impressum also loads its own stylesheet; neither loads the legacy Bootstrap assets.
