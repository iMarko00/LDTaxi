#!/usr/bin/env python3
"""Generate the town landing pages (/taxi-<ort>/index.html) from TOWNS below.

Run from the repo root:  python3 tools/build-town-pages.py
Edit copy here, not in the generated HTML. Then update sitemap.xml lastmod.

German is rendered into the HTML (what Google indexes). EN/SR/RU are embedded as
#page-i18n JSON and applied by js/translate.js when a visitor picks a language.
Shared labels (nav, footer, town link pills) live in js/translate.js.
"""
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://www.ldtaxi.at"
PHONE_HREF = "tel:+436647991229"
PHONE = "0664 7991229"
GBP_URL = "https://www.google.com/search?kgmid=/g/11w3j1tlwx&q=LD+Taxi"
INSTAGRAM_URL = "https://www.instagram.com/ld.taxi/"
LANGS = ("de", "en", "sr", "ru")

PHOTOS = {
    "banner": {"src": "/assets/img/photos/ld-taxi-passat-banner.webp", "w": 928, "h": 928,
               "alt": "LD Taxi VW Passat neben dem LD-Taxi-Banner mit Telefonnummer und Leistungen"},
    "wash": {"src": "/assets/img/photos/ld-taxi-passat-waschstrasse.webp", "w": 928, "h": 928,
             "alt": "Der schwarze VW Passat von LD Taxi in der Waschstraße – das Auto ist immer gepflegt"},
    "driver": {"src": "/assets/img/photos/ld-taxi-fahrersicht.webp", "w": 736, "h": 980,
               "alt": "Blick vom Fahrersitz des LD Taxi auf eine Landstraße, Navigation am Armaturenbrett"},
    "rain": {"src": "/assets/img/photos/ld-taxi-passat-regen.webp", "w": 736, "h": 980,
             "alt": "Der schwarze VW Passat von LD Taxi bei Regen am Straßenrand"},
    "kreuzenstein": {"src": "/assets/img/photos/ld-taxi-passat-burg-kreuzenstein.webp", "w": 816, "h": 1088,
                     "alt": "Schwarzer VW Passat von LD Taxi vor der Burg Kreuzenstein in Leobendorf", "pos": "center 22%"},
}

# Template strings per language. {n} = town name in that language.
UI = {
    "de": dict(sub="24/7 erreichbar", bodyH="Ihr Taxi für {n}", destH="Häufige Fahrten",
               t1="Tag und Nacht erreichbar, auch an Wochenenden und Feiertagen.", stat2="Flughafen",
               t2="Transfers zum Flughafen Wien-Schwechat und zu weiteren Flughäfen in Österreich.",
               t3="Für Firmen: Fahrten buchen und gesammelt per Rechnung bezahlen.",
               nearH="Auch in der Umgebung unterwegs", ctaH="Taxi in {n} bestellen",
               ctaText="Rufen Sie an – wir sagen Ihnen sofort, wann wir bei Ihnen sind. Für geplante Fahrten können Sie uns auch",
               ctaLink="eine Anfrage senden", home="Startseite"),
    "en": dict(sub="Available 24/7", bodyH="Your taxi for {n}", destH="Popular rides",
               t1="Available day and night, including weekends and public holidays.", stat2="Airport",
               t2="Transfers to Vienna Airport (Schwechat) and other airports in Austria.",
               t3="For companies: book rides and pay for them together by invoice.",
               nearH="Also on the road nearby", ctaH="Book a taxi in {n}",
               ctaText="Give us a call – we'll tell you right away when we can be there. For planned rides you can also",
               ctaLink="send us a request", home="Home"),
    "sr": dict(sub="Доступни 24/7", bodyH="Ваш такси за {n}", destH="Честе вожње",
               t1="Доступни дању и ноћу, и викендом и празницима.", stat2="Аеродром",
               t2="Трансфери до аеродрома Беч-Швехат и других аеродрома у Аустрији.",
               t3="За фирме: резервишите вожње и платите их збирно по рачуну.",
               nearH="Возимо и у околини", ctaH="Наручите такси: {n}",
               ctaText="Позовите нас – одмах ћемо вам рећи када можемо да будемо код вас. За планиране вожње можете нам и",
               ctaLink="послати упит", home="Почетна"),
    "ru": dict(sub="На связи 24/7", bodyH="Ваше такси: {n}", destH="Популярные поездки",
               t1="На связи днём и ночью, в том числе в выходные и праздники.", stat2="Аэропорт",
               t2="Трансферы в аэропорт Вена-Швехат и другие аэропорты Австрии.",
               t3="Для компаний: бронируйте поездки и оплачивайте их одним счётом.",
               nearH="Также ездим поблизости", ctaH="Заказать такси: {n}",
               ctaText="Позвоните нам – мы сразу скажем, когда сможем быть у вас. Для запланированных поездок вы также можете",
               ctaLink="отправить заявку", home="Главная"),
}

TOWNS = [
    {
        "slug": "taxi-leobendorf", "photo": "kreuzenstein", "schema_name": "Leobendorf",
        "de": dict(
            name="Leobendorf",
            title="Taxi Leobendorf · 24/7 · LD Taxi · 0664 7991229",
            meta="Taxi in Leobendorf, Tresdorf, Ober- und Unterrohrbach: LD Taxi fährt rund um die Uhr – zum Bahnhof, nach Wien und zum Flughafen. Jetzt anrufen: 0664 7991229.",
            lead="Ob vom Bahnhof Leobendorf-Burg Kreuzenstein, aus Tresdorf oder aus Ober- und Unterrohrbach: LD Taxi holt Sie in der ganzen Gemeinde Leobendorf ab – Tag und Nacht.",
            body=["Leobendorf liegt direkt neben Korneuburg, unserem Standort. Deshalb sind wir meist schnell bei Ihnen, egal ob Sie früh morgens zum Flughafen müssen oder nach einem Abend in Wien sicher nach Hause wollen.",
                  "Gäste, die die Burg Kreuzenstein besuchen, bringen wir vom Bahnhof oder aus Wien direkt hinauf – und nach dem Besuch wieder zurück."],
            dest=["Bahnhof Leobendorf-Burg Kreuzenstein und Bahnhof Korneuburg", "Burg Kreuzenstein",
                  "Wien und Flughafen Wien-Schwechat", "Landesklinikum Korneuburg und Arzttermine in der Umgebung"]),
        "en": dict(
            name="Leobendorf",
            title="Taxi Leobendorf · 24/7 · LD Taxi · 0664 7991229",
            meta="Taxi in Leobendorf, Tresdorf, Oberrohrbach and Unterrohrbach: LD Taxi drives around the clock – to the station, to Vienna and to the airport. Call 0664 7991229.",
            lead="Whether from Leobendorf-Burg Kreuzenstein station, Tresdorf or Ober- and Unterrohrbach: LD Taxi picks you up anywhere in Leobendorf – day and night.",
            body=["Leobendorf is right next to Korneuburg, where we are based. That's why we are usually with you quickly – whether you need to get to the airport early in the morning or want to get home safely after an evening in Vienna.",
                  "Visiting Burg Kreuzenstein? We take you straight up from the station or from Vienna – and back again afterwards."],
            dest=["Leobendorf-Burg Kreuzenstein and Korneuburg stations", "Burg Kreuzenstein castle",
                  "Vienna and Vienna Airport (Schwechat)", "Korneuburg hospital and medical appointments nearby"]),
        "sr": dict(
            name="Леобендорф",
            title="Такси Леобендорф · 24/7 · LD Taxi · 0664 7991229",
            meta="Такси у Леобендорфу, Тресдорфу, Оберорбаху и Унтерорбаху: LD Taxi вози даноноћно – до станице, у Беч и на аеродром. Позовите 0664 7991229.",
            lead="Са станице Leobendorf-Burg Kreuzenstein, из Тресдорфа или из Обер- и Унтерорбаха: LD Taxi долази по вас било где у Леобендорфу – дању и ноћу.",
            body=["Леобендорф се налази одмах поред Корнојбурга, где смо смештени. Зато смо обично брзо код вас – било да рано ујутру морате на аеродром или после вечери у Бечу желите безбедно кући.",
                  "Посетиоце замка Кројценштајн возимо директно са станице или из Беча до замка – и после посете назад."],
            dest=["Станице Leobendorf-Burg Kreuzenstein и Korneuburg", "Замак Кројценштајн (Burg Kreuzenstein)",
                  "Беч и аеродром Беч-Швехат", "Болница у Корнојбургу и прегледи код лекара у околини"]),
        "ru": dict(
            name="Леобендорф",
            title="Такси Леобендорф · 24/7 · LD Taxi · 0664 7991229",
            meta="Такси в Леобендорфе, Тресдорфе, Оберорбахе и Унтерорбахе: LD Taxi работает круглосуточно – до вокзала, в Вену и в аэропорт. Звоните: 0664 7991229.",
            lead="Со станции Leobendorf-Burg Kreuzenstein, из Тресдорфа или из Обер- и Унтерорбаха: LD Taxi заберёт вас в любой точке Леобендорфа – днём и ночью.",
            body=["Леобендорф находится рядом с Корнойбургом, где мы базируемся. Поэтому обычно мы быстро у вас – нужно ли вам рано утром в аэропорт или вы хотите безопасно вернуться домой после вечера в Вене.",
                  "Гостей замка Кройценштайн мы отвезём прямо со станции или из Вены к замку – и обратно после визита."],
            dest=["Станции Leobendorf-Burg Kreuzenstein и Korneuburg", "Замок Кройценштайн (Burg Kreuzenstein)",
                  "Вена и аэропорт Вена-Швехат", "Больница Корнойбурга и визиты к врачу поблизости"]),
    },
    {
        "slug": "taxi-stockerau", "photo": "banner", "schema_name": "Stockerau",
        "de": dict(
            name="Stockerau",
            title="Taxi Stockerau · 24/7 · LD Taxi · 0664 7991229",
            meta="Taxi in Stockerau rund um die Uhr: Fahrten zum Bahnhof, nach Wien, zum Flughafen Wien-Schwechat und Rechnungsfahrten für Firmen. LD Taxi: 0664 7991229.",
            lead="LD Taxi fährt Sie in Stockerau rund um die Uhr – vom Bahnhof Stockerau, aus dem Zentrum oder direkt von Ihrer Haustür.",
            body=["Stockerau ist die größte Stadt im Bezirk Korneuburg und für uns eine tägliche Strecke. Wir übernehmen Einzelfahrten innerhalb der Stadt genauso wie Fahrten nach Wien oder zum Flughafen.",
                  "Für Betriebe in Stockerau bieten wir Fahrten auf Rechnung an – praktisch für Geschäftspartner, Mitarbeiter oder Botendienste."],
            dest=["Bahnhof Stockerau", "Wien und Flughafen Wien-Schwechat",
                  "Korneuburg und alle Gemeinden im Bezirk", "Firmenfahrten und Botendienste auf Rechnung"]),
        "en": dict(
            name="Stockerau",
            title="Taxi Stockerau · 24/7 · LD Taxi · 0664 7991229",
            meta="Taxi in Stockerau around the clock: rides to the station, to Vienna, to Vienna Airport and invoiced rides for companies. LD Taxi: 0664 7991229.",
            lead="LD Taxi drives you around Stockerau day and night – from Stockerau station, from the town centre or straight from your front door.",
            body=["Stockerau is the largest town in the Korneuburg district and part of our daily routes. We handle short rides within town just as well as trips to Vienna or the airport.",
                  "For businesses in Stockerau we offer rides on account – handy for business partners, staff or courier jobs."],
            dest=["Stockerau station", "Vienna and Vienna Airport (Schwechat)",
                  "Korneuburg and every municipality in the district", "Company rides and courier jobs on account"]),
        "sr": dict(
            name="Штокерау",
            title="Такси Штокерау · 24/7 · LD Taxi · 0664 7991229",
            meta="Такси у Штокерауу даноноћно: вожње до станице, у Беч, на аеродром Беч-Швехат и вожње по рачуну за фирме. LD Taxi: 0664 7991229.",
            lead="LD Taxi вас вози по Штокерауу даноноћно – са станице Stockerau, из центра или директно испред ваших врата.",
            body=["Штокерау је највећи град у округу Корнојбург и део наших свакодневних рута. Возимо кратке вожње по граду, као и до Беча или аеродрома.",
                  "За фирме у Штокерауу нудимо вожње по рачуну – практично за пословне партнере, запослене или курирске услуге."],
            dest=["Станица Stockerau", "Беч и аеродром Беч-Швехат",
                  "Корнојбург и све општине у округу", "Пословне вожње и курирске услуге по рачуну"]),
        "ru": dict(
            name="Штоккерау",
            title="Такси Штоккерау · 24/7 · LD Taxi · 0664 7991229",
            meta="Такси в Штоккерау круглосуточно: поездки до вокзала, в Вену, в аэропорт Вена-Швехат и поездки по счёту для компаний. LD Taxi: 0664 7991229.",
            lead="LD Taxi возит вас по Штоккерау круглосуточно – с вокзала Stockerau, из центра или прямо от вашей двери.",
            body=["Штоккерау – крупнейший город округа Корнойбург и часть наших ежедневных маршрутов. Мы выполняем короткие поездки по городу так же, как и поездки в Вену или в аэропорт.",
                  "Для компаний в Штоккерау мы предлагаем поездки по счёту – удобно для деловых партнёров, сотрудников или курьерских заданий."],
            dest=["Вокзал Stockerau", "Вена и аэропорт Вена-Швехат",
                  "Корнойбург и все общины округа", "Деловые поездки и курьерские услуги по счёту"]),
    },
    {
        "slug": "taxi-klosterneuburg", "photo": "rain", "schema_name": "Klosterneuburg",
        "de": dict(
            name="Klosterneuburg",
            title="Taxi Klosterneuburg · 24/7 · LD Taxi · 0664 7991229",
            meta="Taxi in Klosterneuburg rund um die Uhr: Fahrten zum Bahnhof, nach Wien, zum Flughafen Wien-Schwechat und ins Weinviertel. LD Taxi: 0664 7991229.",
            lead="Ob Stift Klosterneuburg, Kierling, Kritzendorf oder Weidling: LD Taxi holt Sie in ganz Klosterneuburg ab – rund um die Uhr.",
            body=["Klosterneuburg liegt auf der anderen Donauseite, gehört für uns aber selbstverständlich zum Einsatzgebiet. Wir fahren Sie nach Wien, zum Flughafen oder über die Donau nach Korneuburg und Stockerau.",
                  "Für Geschäftsreisende, etwa zum ISTA in Maria Gugging, fahren wir auch auf Rechnung."],
            dest=["Stift Klosterneuburg und Bahnhof Klosterneuburg-Kierling", "Wien und Flughafen Wien-Schwechat",
                  "Korneuburg, Stockerau und das Weinviertel", "Geschäftsfahrten auf Rechnung, z. B. zum ISTA in Maria Gugging"]),
        "en": dict(
            name="Klosterneuburg",
            title="Taxi Klosterneuburg · 24/7 · LD Taxi · 0664 7991229",
            meta="Taxi in Klosterneuburg around the clock: rides to the station, to Vienna, to Vienna Airport and into the Weinviertel. LD Taxi: 0664 7991229.",
            lead="Klosterneuburg Abbey, Kierling, Kritzendorf or Weidling: LD Taxi picks you up anywhere in Klosterneuburg – around the clock.",
            body=["Klosterneuburg is on the other side of the Danube, but of course it's part of our service area. We take you to Vienna, to the airport or across the Danube to Korneuburg and Stockerau.",
                  "For business travellers, for example to ISTA in Maria Gugging, we also drive on account."],
            dest=["Klosterneuburg Abbey and Klosterneuburg-Kierling station", "Vienna and Vienna Airport (Schwechat)",
                  "Korneuburg, Stockerau and the Weinviertel", "Business rides on account, e.g. to ISTA in Maria Gugging"]),
        "sr": dict(
            name="Клостернојбург",
            title="Такси Клостернојбург · 24/7 · LD Taxi · 0664 7991229",
            meta="Такси у Клостернојбургу даноноћно: вожње до станице, у Беч, на аеродром Беч-Швехат и у Вајнфиртел. LD Taxi: 0664 7991229.",
            lead="Манастир Клостернојбург, Кирлинг, Крицендорф или Вајдлинг: LD Taxi долази по вас било где у Клостернојбургу – даноноћно.",
            body=["Клостернојбург је на другој обали Дунава, али наравно спада у наше подручје. Возимо вас у Беч, на аеродром или преко Дунава у Корнојбург и Штокерау.",
                  "За пословна путовања, на пример до ISTA у Марија Гугингу, возимо и по рачуну."],
            dest=["Манастир Клостернојбург и станица Klosterneuburg-Kierling", "Беч и аеродром Беч-Швехат",
                  "Корнојбург, Штокерау и Вајнфиртел", "Пословне вожње по рачуну, нпр. до ISTA у Марија Гугингу"]),
        "ru": dict(
            name="Клостернойбург",
            title="Такси Клостернойбург · 24/7 · LD Taxi · 0664 7991229",
            meta="Такси в Клостернойбурге круглосуточно: поездки до вокзала, в Вену, в аэропорт Вена-Швехат и в Вайнфиртель. LD Taxi: 0664 7991229.",
            lead="Монастырь Клостернойбург, Кирлинг, Крицендорф или Вайдлинг: LD Taxi заберёт вас в любой точке Клостернойбурга – круглосуточно.",
            body=["Клостернойбург находится на другом берегу Дуная, но, конечно, входит в нашу зону обслуживания. Мы отвезём вас в Вену, в аэропорт или через Дунай в Корнойбург и Штоккерау.",
                  "Для деловых поездок, например в ISTA в Мария-Гуггинге, мы также ездим по счёту."],
            dest=["Монастырь Клостернойбург и вокзал Klosterneuburg-Kierling", "Вена и аэропорт Вена-Швехат",
                  "Корнойбург, Штоккерау и Вайнфиртель", "Деловые поездки по счёту, например в ISTA в Мария-Гуггинге"]),
    },
    {
        "slug": "taxi-hagenbrunn", "photo": "wash", "schema_name": "Hagenbrunn",
        "de": dict(
            name="Hagenbrunn",
            title="Taxi Hagenbrunn · 24/7 · LD Taxi · 0664 7991229",
            meta="Taxi in Hagenbrunn rund um die Uhr: Fahrten nach Wien, zum Flughafen Wien-Schwechat und im ganzen Bezirk Korneuburg. LD Taxi: 0664 7991229.",
            lead="Von Hagenbrunn nach Wien, zum Flughafen oder zum Einkaufen: LD Taxi ist rund um die Uhr für Sie erreichbar.",
            body=["Hagenbrunn liegt an der Stadtgrenze zu Wien. Wir fahren Sie nach Floridsdorf, in die Innenstadt oder zum Flughafen Wien-Schwechat – und holen Sie nachts auch wieder ab.",
                  "Auch für kurze Wege, etwa zum Einkaufen nach Gerasdorf oder zum Arzt nach Korneuburg, sind wir da."],
            dest=["Wien-Floridsdorf und Wien-Innenstadt", "Flughafen Wien-Schwechat",
                  "Einkaufen in Gerasdorf", "Korneuburg und der ganze Bezirk"]),
        "en": dict(
            name="Hagenbrunn",
            title="Taxi Hagenbrunn · 24/7 · LD Taxi · 0664 7991229",
            meta="Taxi in Hagenbrunn around the clock: rides to Vienna, to Vienna Airport and across the Korneuburg district. LD Taxi: 0664 7991229.",
            lead="From Hagenbrunn to Vienna, to the airport or to the shops: LD Taxi is available around the clock.",
            body=["Hagenbrunn sits right on the Vienna city border. We take you to Floridsdorf, the city centre or Vienna Airport – and pick you up again at night.",
                  "We're also there for short trips, such as shopping in Gerasdorf or a doctor's appointment in Korneuburg."],
            dest=["Vienna-Floridsdorf and central Vienna", "Vienna Airport (Schwechat)",
                  "Shopping in Gerasdorf", "Korneuburg and the whole district"]),
        "sr": dict(
            name="Хагенбрун",
            title="Такси Хагенбрун · 24/7 · LD Taxi · 0664 7991229",
            meta="Такси у Хагенбруну даноноћно: вожње у Беч, на аеродром Беч-Швехат и по целом округу Корнојбург. LD Taxi: 0664 7991229.",
            lead="Из Хагенбруна у Беч, на аеродром или у куповину: LD Taxi је доступан даноноћно.",
            body=["Хагенбрун се налази на самој граници Беча. Возимо вас у Флоридсдорф, у центар града или на аеродром Беч-Швехат – и ноћу вас поново покупимо.",
                  "Ту смо и за кратке вожње, на пример у куповину у Герасдорф или код лекара у Корнојбург."],
            dest=["Беч-Флоридсдорф и центар Беча", "Аеродром Беч-Швехат",
                  "Куповина у Герасдорфу", "Корнојбург и цео округ"]),
        "ru": dict(
            name="Хагенбрунн",
            title="Такси Хагенбрунн · 24/7 · LD Taxi · 0664 7991229",
            meta="Такси в Хагенбрунне круглосуточно: поездки в Вену, в аэропорт Вена-Швехат и по всему округу Корнойбург. LD Taxi: 0664 7991229.",
            lead="Из Хагенбрунна в Вену, в аэропорт или за покупками: LD Taxi на связи круглосуточно.",
            body=["Хагенбрунн расположен прямо на границе Вены. Мы отвезём вас во Флоридсдорф, в центр города или в аэропорт Вена-Швехат – и ночью заберём обратно.",
                  "Мы также выполняем короткие поездки, например за покупками в Герасдорф или к врачу в Корнойбург."],
            dest=["Вена-Флоридсдорф и центр Вены", "Аэропорт Вена-Швехат",
                  "Покупки в Герасдорфе", "Корнойбург и весь округ"]),
    },
    {
        "slug": "taxi-enzersfeld", "photo": "driver", "schema_name": "Enzersfeld im Weinviertel",
        "de": dict(
            name="Enzersfeld im Weinviertel", short="Enzersfeld",
            title="Taxi Enzersfeld im Weinviertel · 24/7 · LD Taxi",
            meta="Taxi in Enzersfeld im Weinviertel rund um die Uhr: Fahrten nach Korneuburg, Wien und zum Flughafen Wien-Schwechat. LD Taxi: 0664 7991229.",
            lead="LD Taxi holt Sie in Enzersfeld im Weinviertel ab – rund um die Uhr, auch spätabends und am Wochenende.",
            body=["In Enzersfeld fährt der Bus nicht immer dann, wenn Sie ihn brauchen. Wir bringen Sie zum Bahnhof Korneuburg, nach Wien oder direkt zum Flughafen.",
                  "Für Heurigenabende im Weinviertel holen wir Sie auch wieder ab, damit das Auto zu Hause bleiben kann."],
            dest=["Bahnhof Korneuburg", "Wien und Flughafen Wien-Schwechat",
                  "Heurigen und Veranstaltungen im Weinviertel", "Arzttermine und Landesklinikum Korneuburg"]),
        "en": dict(
            name="Enzersfeld im Weinviertel", short="Enzersfeld",
            title="Taxi Enzersfeld im Weinviertel · 24/7 · LD Taxi",
            meta="Taxi in Enzersfeld im Weinviertel around the clock: rides to Korneuburg, Vienna and Vienna Airport. LD Taxi: 0664 7991229.",
            lead="LD Taxi picks you up in Enzersfeld im Weinviertel – around the clock, late at night and at weekends too.",
            body=["In Enzersfeld the bus doesn't always run when you need it. We take you to Korneuburg station, to Vienna or straight to the airport.",
                  "After an evening at a Heuriger in the Weinviertel we'll pick you up again, so the car can stay at home."],
            dest=["Korneuburg station", "Vienna and Vienna Airport (Schwechat)",
                  "Heurigen and events in the Weinviertel", "Medical appointments and Korneuburg hospital"]),
        "sr": dict(
            name="Енцерсфелд",
            title="Такси Енцерсфелд · 24/7 · LD Taxi",
            meta="Такси у Енцерсфелду (Weinviertel) даноноћно: вожње у Корнојбург, Беч и на аеродром Беч-Швехат. LD Taxi: 0664 7991229.",
            lead="LD Taxi долази по вас у Енцерсфелд – даноноћно, и касно увече и викендом.",
            body=["У Енцерсфелду аутобус не вози увек онда када вам треба. Возимо вас до станице Korneuburg, у Беч или директно на аеродром.",
                  "После вечери на хеуригеру у Вајнфиртелу поново вас покупимо, да ауто може да остане код куће."],
            dest=["Станица Korneuburg", "Беч и аеродром Беч-Швехат",
                  "Хеуригери и догађаји у Вајнфиртелу", "Прегледи код лекара и болница у Корнојбургу"]),
        "ru": dict(
            name="Энцерсфельд",
            title="Такси Энцерсфельд · 24/7 · LD Taxi",
            meta="Такси в Энцерсфельде (Weinviertel) круглосуточно: поездки в Корнойбург, Вену и в аэропорт Вена-Швехат. LD Taxi: 0664 7991229.",
            lead="LD Taxi заберёт вас в Энцерсфельде – круглосуточно, в том числе поздно вечером и в выходные.",
            body=["В Энцерсфельде автобус ходит не всегда тогда, когда он нужен. Мы отвезём вас на вокзал Korneuburg, в Вену или прямо в аэропорт.",
                  "После вечера в хойригере в Вайнфиртеле мы заберём вас обратно – машина может остаться дома."],
            dest=["Вокзал Korneuburg", "Вена и аэропорт Вена-Швехат",
                  "Хойригеры и мероприятия в Вайнфиртеле", "Визиты к врачу и больница Корнойбурга"]),
    },
]

ICON_PHONE = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
LANG_SWITCH = '<div class="language-switch" role="group" aria-label="Sprache wählen" data-i18n-aria="languageLabel"><button type="button" data-language="de" lang="de" aria-label="Deutsch" aria-pressed="true">DE</button><span aria-hidden="true">/</span><button type="button" data-language="en" lang="en" aria-label="English" aria-pressed="false">EN</button><span aria-hidden="true">/</span><button type="button" data-language="sr" lang="sr-Cyrl" aria-label="Српски (ћирилица)" aria-pressed="false">СР</button><span aria-hidden="true">/</span><button type="button" data-language="ru" lang="ru" aria-label="Русский" aria-pressed="false">РУ</button></div>'

e = html.escape


def copy_for(t, lang):
    """Flat key -> text map for one language (what translate.js applies)."""
    c, ui = t[lang], UI[lang]
    n = c["name"]
    short = c.get("short", n)
    out = {
        "pageTitle": c["title"], "pageMeta": c["meta"],
        "townH1": f"Taxi {n}" if lang in ("de", "en") else f"Такси {n}",
        "townSub": ui["sub"], "townLead": c["lead"],
        "townBodyH": ui["bodyH"].format(n=short), "townDestH": ui["destH"],
        "townT1": ui["t1"], "townStat2": ui["stat2"], "townT2": ui["t2"], "townT3": ui["t3"],
        "townNearH": ui["nearH"], "townCtaH": ui["ctaH"].format(n=short),
        "townCtaText": ui["ctaText"], "townCtaLink": ui["ctaLink"], "townHome": ui["home"],
    }
    for i, p in enumerate(c["body"]):
        out[f"townBody{i}"] = p
    for i, d in enumerate(c["dest"]):
        out[f"townDest{i}"] = d
    return out


def schema(t):
    url = f"{SITE}/{t['slug']}/"
    return json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "TaxiService",
                "@id": f"{url}#service",
                "name": f"Taxi {t['schema_name']}",
                "url": url,
                "provider": {"@id": f"{SITE}/#business"},
                "areaServed": {"@type": "City", "name": t["schema_name"]},
                "availableChannel": {"@type": "ServiceChannel", "servicePhone": {"@type": "ContactPoint", "telephone": "+43 664 7991229", "contactType": "Taxibestellung", "hoursAvailable": "Mo-Su 00:00-23:59"}},
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "LD Taxi", "item": f"{SITE}/"},
                    {"@type": "ListItem", "position": 2, "name": f"Taxi {t['schema_name']}", "item": url},
                ],
            },
        ],
    }, ensure_ascii=False, indent=2)


def page(t):
    de = copy_for(t, "de")
    i18n = json.dumps({lang: copy_for(t, lang) for lang in LANGS}, ensure_ascii=False).replace("</", "<\\/")
    slug = t["slug"]
    pills = '<li><a href="/" data-i18n="town_home">Taxi Korneuburg</a></li>' + "".join(
        f'<li><a href="/{o["slug"]}/" data-i18n="town_{o["slug"]}">Taxi {e(o["de"].get("short", o["de"]["name"]))}</a></li>'
        for o in TOWNS if o is not t
    )
    body = "".join(f'<p data-i18n="townBody{i}">{e(p)}</p>' for i, p in enumerate(t["de"]["body"]))
    dests = "".join(f'<li data-i18n="townDest{i}">{e(d)}</li>' for i, d in enumerate(t["de"]["dest"]))
    p = PHOTOS[t["photo"]]
    pos = f' style="object-position: {p['pos']}"' if p.get("pos") else ""
    photo = f'<figure class="town-photo"><img src="{p["src"]}" width="{p["w"]}" height="{p["h"]}" alt="{e(p["alt"])}"{pos} loading="eager" decoding="async"></figure>'
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0E0E10">
<meta name="description" content="{e(de['pageMeta'])}">
<title>{e(de['pageTitle'])}</title>
<link rel="canonical" href="{SITE}/{slug}/">
<meta property="og:type" content="website">
<meta property="og:locale" content="de_AT">
<meta property="og:site_name" content="LD Taxi">
<meta property="og:url" content="{SITE}/{slug}/">
<meta property="og:title" content="{e(de['pageTitle'])}">
<meta property="og:description" content="{e(de['pageMeta'])}">
<meta property="og:image" content="{SITE}{p['src']}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/img/LDTaxi_logo_klein.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;800;900&amp;family=Inter:wght@400;500;600&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/redesign.css?v=20261112-3">
<link rel="stylesheet" href="/css/town.css?v=20261112-4">
<script type="application/ld+json">
{schema(t)}
</script>
<script type="application/json" id="page-i18n">{i18n}</script>
<script src="/js/translate.js?v=20261112-3" defer></script>
</head>
<body class="town-page" data-page="town">
<a class="skip-link" href="#main" data-i18n="skip">Zum Inhalt</a>
<header class="site-header container">
<a class="brand" href="/" aria-label="LD Taxi – Startseite" data-i18n-aria="homeLabel"><span class="brand-badge">LD</span><span>Taxi</span></a>
<div class="header-actions"><nav aria-label="Hauptnavigation" data-i18n-aria="navLabel"><a href="/#leistungen" data-i18n="navServices">Leistungen</a><a href="/#kontakt" data-i18n="contact">Kontakt</a></nav><a class="button primary header-call" href="{PHONE_HREF}">{ICON_PHONE}<span data-i18n="call">Anrufen</span></a></div>
</header>
<main id="main">
<section class="town-hero section"><div class="container town-grid has-photo">
<div class="town-copy">
<nav class="breadcrumb" aria-label="Brotkrümelnavigation"><a href="/">LD Taxi</a><span aria-hidden="true">/</span><span data-i18n="townH1">{e(de['townH1'])}</span></nav>
<h1><span data-i18n="townH1">{e(de['townH1'])}</span><span class="accent" data-i18n="townSub">{e(de['townSub'])}</span></h1>
<p class="hero-description" data-i18n="townLead">{e(de['townLead'])}</p>
<a class="town-call" href="{PHONE_HREF}">{ICON_PHONE}<span>{PHONE}</span></a>
</div>
{photo}
</div></section>
<div class="checker" aria-hidden="true"></div>
<section class="section town-body"><div class="container town-columns">
<div><h2 data-i18n="townBodyH">{e(de['townBodyH'])}</h2>{body}</div>
<div><h2 data-i18n="townDestH">{e(de['townDestH'])}</h2><ul class="town-list">{dests}</ul></div>
</div></section>
<section class="section benefits"><div class="container"><h2 data-i18n="whyHeading">Rund um die Uhr. Ohne Umwege.</h2><div class="benefit-grid"><div><p class="stat">24/7</p><p data-i18n="townT1">{e(de['townT1'])}</p></div><div><p class="stat" data-i18n="townStat2">{e(de['townStat2'])}</p><p data-i18n="townT2">{e(de['townT2'])}</p></div><div><p class="stat" data-i18n="invoice">Auf Rechnung</p><p data-i18n="townT3">{e(de['townT3'])}</p></div></div>
<div class="area"><h3 data-i18n="townNearH">{e(de['townNearH'])}</h3><ul class="town-links">{pills}</ul></div></div></section>
<section class="section town-cta"><div class="container"><h2 data-i18n="townCtaH">{e(de['townCtaH'])}</h2><p class="intro-copy"><span data-i18n="townCtaText">{e(de['townCtaText'])}</span> <a href="/#kontakt" data-i18n="townCtaLink">{e(de['townCtaLink'])}</a>.</p><a class="contact-number" href="{PHONE_HREF}">{ICON_PHONE}<span>{PHONE}</span></a><p class="contact-links"><a href="{GBP_URL}" rel="noopener" target="_blank" data-i18n="googleReviews">Bewertungen auf Google</a><a href="{INSTAGRAM_URL}" rel="noopener" target="_blank">Instagram</a></p></div></section>
</main>
<footer class="site-footer"><div class="container footer-inner"><p data-i18n="footer">© LD Taxi · Taxi im Bezirk Korneuburg</p><div class="footer-links"><a href="/" data-i18n="townHome">{e(de['townHome'])}</a><a href="{GBP_URL}" rel="noopener" target="_blank">Google</a><a href="/impressum.html" data-i18n="legal">Impressum</a>{LANG_SWITCH}</div></div></footer>
<div class="mobile-call"><a class="button primary" href="{PHONE_HREF}">{ICON_PHONE}<span data-i18n="callNow">Jetzt Taxi rufen</span></a></div>
</body>
</html>
"""


if __name__ == "__main__":
    for t in TOWNS:
        out = ROOT / t["slug"] / "index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(page(t), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))
