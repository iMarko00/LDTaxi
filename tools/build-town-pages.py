#!/usr/bin/env python3
"""Generate the town landing pages (/taxi-<ort>/index.html) from TOWNS below.

Run from the repo root:  python3 tools/build-town-pages.py
Edit copy here, not in the generated HTML. Then update sitemap.xml lastmod.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://www.ldtaxi.at"
PHONE_HREF = "tel:+436647991229"
PHONE = "0664 7991229"

PHOTO_BANNER = {
    "src": "/assets/img/photos/ld-taxi-passat-banner.webp",
    "w": 928, "h": 928,
    "alt": "LD Taxi VW Passat neben dem LD-Taxi-Banner mit Telefonnummer und Leistungen",
}
PHOTO_WASH = {
    "src": "/assets/img/photos/ld-taxi-passat-waschstrasse.webp",
    "w": 928, "h": 928,
    "alt": "Der schwarze VW Passat von LD Taxi in der Waschstraße – das Auto ist immer gepflegt",
}
PHOTO_DRIVER_VIEW = {
    "src": "/assets/img/photos/ld-taxi-fahrersicht.webp",
    "w": 736, "h": 980,
    "alt": "Blick vom Fahrersitz des LD Taxi auf eine Landstraße, Navigation am Armaturenbrett",
}
PHOTO_KREUZENSTEIN = {
    "src": "/assets/img/photos/ld-taxi-passat-burg-kreuzenstein.webp",
    "w": 816, "h": 1088,
    "alt": "Schwarzer VW Passat von LD Taxi vor der Burg Kreuzenstein in Leobendorf",
}

TOWNS = [
    {
        "slug": "taxi-leobendorf",
        "name": "Leobendorf",
        "title": "Taxi Leobendorf · 24/7 · LD Taxi · 0664 7991229",
        "meta": "Taxi in Leobendorf, Tresdorf, Ober- und Unterrohrbach: LD Taxi fährt rund um die Uhr – zum Bahnhof, nach Wien und zum Flughafen. Jetzt anrufen: 0664 7991229.",
        "lead": "Ob vom Bahnhof Leobendorf-Burg Kreuzenstein, aus Tresdorf oder aus Ober- und Unterrohrbach: LD Taxi holt Sie in der ganzen Gemeinde Leobendorf ab – Tag und Nacht.",
        "body": [
            "Leobendorf liegt direkt neben Korneuburg, unserem Standort. Deshalb sind wir meist schnell bei Ihnen, egal ob Sie früh morgens zum Flughafen müssen oder nach einem Abend in Wien sicher nach Hause wollen.",
            "Gäste, die die Burg Kreuzenstein besuchen, bringen wir vom Bahnhof oder aus Wien direkt hinauf – und nach dem Besuch wieder zurück.",
        ],
        "destinations": [
            "Bahnhof Leobendorf-Burg Kreuzenstein und Bahnhof Korneuburg",
            "Burg Kreuzenstein",
            "Wien und Flughafen Wien-Schwechat",
            "Landesklinikum Korneuburg und Arzttermine in der Umgebung",
        ],
        "photo": PHOTO_KREUZENSTEIN,
    },
    {
        "slug": "taxi-stockerau",
        "name": "Stockerau",
        "title": "Taxi Stockerau · 24/7 · LD Taxi · 0664 7991229",
        "meta": "Taxi in Stockerau rund um die Uhr: Fahrten zum Bahnhof, nach Wien, zum Flughafen Wien-Schwechat und Rechnungsfahrten für Firmen. LD Taxi: 0664 7991229.",
        "lead": "LD Taxi fährt Sie in Stockerau rund um die Uhr – vom Bahnhof Stockerau, aus dem Zentrum oder direkt von Ihrer Haustür.",
        "body": [
            "Stockerau ist die größte Stadt im Bezirk Korneuburg und für uns eine tägliche Strecke. Wir übernehmen Einzelfahrten innerhalb der Stadt genauso wie Fahrten nach Wien oder zum Flughafen.",
            "Für Betriebe in Stockerau bieten wir Fahrten auf Rechnung an – praktisch für Geschäftspartner, Mitarbeiter oder Botendienste.",
        ],
        "destinations": [
            "Bahnhof Stockerau",
            "Wien und Flughafen Wien-Schwechat",
            "Korneuburg und alle Gemeinden im Bezirk",
            "Firmenfahrten und Botendienste auf Rechnung",
        ],
        "photo": PHOTO_BANNER,
    },
    {
        "slug": "taxi-hagenbrunn",
        "name": "Hagenbrunn",
        "title": "Taxi Hagenbrunn · 24/7 · LD Taxi · 0664 7991229",
        "meta": "Taxi in Hagenbrunn rund um die Uhr: Fahrten nach Wien, zum Flughafen Wien-Schwechat und im ganzen Bezirk Korneuburg. LD Taxi: 0664 7991229.",
        "lead": "Von Hagenbrunn nach Wien, zum Flughafen oder zum Einkaufen: LD Taxi ist rund um die Uhr für Sie erreichbar.",
        "body": [
            "Hagenbrunn liegt an der Stadtgrenze zu Wien. Wir fahren Sie nach Floridsdorf, in die Innenstadt oder zum Flughafen Wien-Schwechat – und holen Sie nachts auch wieder ab.",
            "Auch für kurze Wege, etwa zum Einkaufen nach Gerasdorf oder zum Arzt nach Korneuburg, sind wir da.",
        ],
        "destinations": [
            "Wien-Floridsdorf und Wien-Innenstadt",
            "Flughafen Wien-Schwechat",
            "Einkaufen in Gerasdorf",
            "Korneuburg und der ganze Bezirk",
        ],
        "photo": PHOTO_WASH,
    },
    {
        "slug": "taxi-enzersfeld",
        "name": "Enzersfeld im Weinviertel",
        "short": "Enzersfeld",
        "title": "Taxi Enzersfeld im Weinviertel · 24/7 · LD Taxi",
        "meta": "Taxi in Enzersfeld im Weinviertel rund um die Uhr: Fahrten nach Korneuburg, Wien und zum Flughafen Wien-Schwechat. LD Taxi: 0664 7991229.",
        "lead": "LD Taxi holt Sie in Enzersfeld im Weinviertel ab – rund um die Uhr, auch spätabends und am Wochenende.",
        "body": [
            "In Enzersfeld fährt der Bus nicht immer dann, wenn Sie ihn brauchen. Wir bringen Sie zum Bahnhof Korneuburg, nach Wien oder direkt zum Flughafen.",
            "Für Heurigenabende im Weinviertel holen wir Sie auch wieder ab, damit das Auto zu Hause bleiben kann.",
        ],
        "destinations": [
            "Bahnhof Korneuburg",
            "Wien und Flughafen Wien-Schwechat",
            "Heurigen und Veranstaltungen im Weinviertel",
            "Arzttermine und Landesklinikum Korneuburg",
        ],
        "photo": PHOTO_DRIVER_VIEW,
    },
]

ICON_PHONE = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'


def schema(t):
    url = f"{SITE}/{t['slug']}/"
    return json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "TaxiService",
                "@id": f"{url}#service",
                "name": f"Taxi {t['name']}",
                "url": url,
                "provider": {"@id": f"{SITE}/#business"},
                "areaServed": {"@type": "City", "name": t["name"]},
                "availableChannel": {"@type": "ServiceChannel", "servicePhone": {"@type": "ContactPoint", "telephone": "+43 664 7991229", "contactType": "Taxibestellung", "hoursAvailable": "Mo-Su 00:00-23:59"}},
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "LD Taxi", "item": f"{SITE}/"},
                    {"@type": "ListItem", "position": 2, "name": f"Taxi {t['name']}", "item": url},
                ],
            },
        ],
    }, ensure_ascii=False, indent=2)


def page(t):
    short = t.get("short", t["name"])
    others = "".join(
        f'<li><a href="/{o["slug"]}/">Taxi {o.get("short", o["name"])}</a></li>'
        for o in TOWNS if o is not t
    )
    body = "".join(f"<p>{p}</p>" for p in t["body"])
    dests = "".join(f"<li>{d}</li>" for d in t["destinations"])
    photo = ""
    if t["photo"]:
        p = t["photo"]
        photo = f'<figure class="town-photo"><img src="{p["src"]}" width="{p["w"]}" height="{p["h"]}" alt="{p["alt"]}" loading="eager" decoding="async"></figure>'
    og_image = f'{SITE}{t["photo"]["src"]}' if t["photo"] else f"{SITE}/assets/img/og-image.png"
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0E0E10">
<meta name="description" content="{t['meta']}">
<title>{t['title']}</title>
<link rel="canonical" href="{SITE}/{t['slug']}/">
<meta property="og:type" content="website">
<meta property="og:locale" content="de_AT">
<meta property="og:site_name" content="LD Taxi">
<meta property="og:url" content="{SITE}/{t['slug']}/">
<meta property="og:title" content="{t['title']}">
<meta property="og:description" content="{t['meta']}">
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/img/LDTaxi_logo_klein.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;800;900&amp;family=Inter:wght@400;500;600&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/redesign.css?v=20261031-2">
<link rel="stylesheet" href="/css/town.css?v=20261112-1">
<script type="application/ld+json">
{schema(t)}
</script>
</head>
<body class="town-page">
<a class="skip-link" href="#main">Zum Inhalt</a>
<header class="site-header container">
<a class="brand" href="/" aria-label="LD Taxi – Startseite"><span class="brand-badge">LD</span><span>Taxi</span></a>
<div class="header-actions"><nav aria-label="Hauptnavigation"><a href="/#leistungen">Leistungen</a><a href="/#kontakt">Kontakt</a></nav><a class="button primary header-call" href="{PHONE_HREF}">{ICON_PHONE}<span>Anrufen</span></a></div>
</header>
<main id="main">
<section class="town-hero section"><div class="container town-grid{' has-photo' if photo else ''}">
<div class="town-copy">
<nav class="breadcrumb" aria-label="Brotkrümelnavigation"><a href="/">LD Taxi</a><span aria-hidden="true">/</span><span>Taxi {short}</span></nav>
<h1>Taxi {t['name']}<span class="accent">24/7 erreichbar</span></h1>
<p class="hero-description">{t['lead']}</p>
<a class="town-call" href="{PHONE_HREF}">{ICON_PHONE}<span>{PHONE}</span></a>
</div>
{photo}
</div></section>
<div class="checker" aria-hidden="true"></div>
<section class="section town-body"><div class="container town-columns">
<div><h2>Ihr Taxi für {short}</h2>{body}</div>
<div><h2>Häufige Fahrten</h2><ul class="town-list">{dests}</ul></div>
</div></section>
<section class="section benefits"><div class="container"><h2>Rund um die Uhr. Ohne Umwege.</h2><div class="benefit-grid"><div><p class="stat">24/7</p><p>Tag und Nacht erreichbar, auch an Wochenenden und Feiertagen.</p></div><div><p class="stat">Flughafen</p><p>Transfers zum Flughafen Wien-Schwechat und zu weiteren Flughäfen in Österreich.</p></div><div><p class="stat">Auf Rechnung</p><p>Für Firmen: Fahrten buchen und gesammelt per Rechnung bezahlen.</p></div></div>
<div class="area"><h3>Auch in der Umgebung unterwegs</h3><ul class="town-links"><li><a href="/">Taxi Korneuburg</a></li>{others}</ul></div></div></section>
<section class="section town-cta"><div class="container"><h2>Taxi in {short} bestellen</h2><p class="intro-copy">Rufen Sie an – wir sagen Ihnen sofort, wann wir bei Ihnen sind. Für geplante Fahrten können Sie uns auch <a href="/#kontakt">eine Anfrage senden</a>.</p><a class="contact-number" href="{PHONE_HREF}">{ICON_PHONE}<span>{PHONE}</span></a></div></section>
</main>
<footer class="site-footer"><div class="container footer-inner"><p>© LD Taxi · Taxi im Bezirk Korneuburg</p><div class="footer-links"><a href="/">Startseite</a><a href="/impressum.html">Impressum</a></div></div></footer>
<div class="mobile-call"><a class="button primary" href="{PHONE_HREF}">{ICON_PHONE}<span>Jetzt Taxi rufen</span></a></div>
</body>
</html>
"""


if __name__ == "__main__":
    for t in TOWNS:
        out = ROOT / t["slug"] / "index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(page(t), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))
