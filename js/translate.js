/* Shared copy and language selection. No link or form behavior is intercepted. */
(() => {
  'use strict';
  const messages = {
  "de": {
    "navServices": "Leistungen",
    "backHome": "Zur Startseite",
    "companyInfo": "Unternehmen",
    "companyName": "Firmenname",
    "companyActivity": "Unternehmensgegenstand",
    "transportCompany": "Transportunternehmen",
    "companyAddress": "Firmensitz",
    "legalTitle": "Impressum · LD Taxi",
    "legalMeta": "Impressum von LD Taxi: Firmeninformationen, Anschrift und Kontakt in Korneuburg.",
    "contact": "Kontakt",
    "call": "Anrufen",
    "region": "Taxi im Bezirk Korneuburg",
    "heroFirst": "Sie kennen das Ziel.",
    "heroSecond": "Wir kennen den Weg!",
    "heroText": "Einzelfahrten, Flughafentransfer, Shuttle- und Botendienst – rund um die Uhr für Sie unterwegs.",
    "callNow": "Jetzt Taxi rufen",
    "request": "Fahrt anfragen",
    "available": "24/7 erreichbar",
    "order": "Taxi bestellen",
    "services": "Dienstleistungen",
    "servicesHeading": "Fünf Wege, ans Ziel zu kommen.",
    "servicesIntro": "Wir wissen, dass Transportbedürfnisse keine Uhrzeiten kennen. Verlassen Sie sich daher 24/7 auf LD Taxi für Ihre Fahrten.",
    "service1": "Einzelfahrten",
    "description1": "Bequem von A nach B – ob zum wichtigen Geschäftstermin oder einfach sicher nach Hause. Wir stehen Ihnen zur Verfügung.",
    "service2": "Flughafentransfer",
    "description2": "Von Wien bis Salzburg: Transfers zu den wichtigsten Flughäfen Österreichs. Beginnen oder beenden Sie Ihre Reise stressfrei.",
    "service3": "Shuttleservice",
    "description3": "Bei Veranstaltungen sind wir da: Wir befördern Sie und Ihre Gäste – ob Sie teilnehmen oder selbst organisieren.",
    "service4": "Botendienst",
    "description4": "Pakete oder Dokumente von A nach B? Dafür haben wir den professionellen Botendienst.",
    "service5": "Rechnungsfahrten",
    "description5": "Firmen buchen bei LD Taxi und bekommen die Kosten später in Rechnung gestellt. Rechtzeitig buchen für eine stressfreie Fahrt.",
    "whyHeading": "Rund um die Uhr. Ohne Umwege.",
    "hoursText": "Transportbedürfnisse kennen keine Uhrzeiten. Wir auch nicht – Tag und Nacht für Sie erreichbar.",
    "airports": "Wien–Salzburg",
    "airportsText": "Flughafentransfers zu den wichtigsten Flughäfen Österreichs, komfortabel und bequem.",
    "invoice": "Auf Rechnung",
    "invoiceText": "Für Firmen: Fahrten buchen, pünktlich ankommen und später bequem per Rechnung bezahlen.",
    "contactHeading": "Kontaktieren Sie uns.",
    "contactText": "Rufen Sie einfach an oder senden Sie uns Ihre Anfrage. Wir planen Ihre nächste Fahrt.",
    "contactNote": "24/7 erreichbar · Taxi im Bezirk Korneuburg",
    "name": "Name",
    "telephone": "Telefon",
    "email": "E-Mail",
    "pickup": "Abholort",
    "destination": "Ziel",
    "message": "Nachricht",
    "send": "Anfrage senden",
    "footer": "© LD Taxi · Taxi im Bezirk Korneuburg",
    "legal": "Impressum",
    "skip": "Zum Inhalt",
    "homeLabel": "LD Taxi – Startseite",
    "navLabel": "Hauptnavigation",
    "languageLabel": "Sprache wählen",
    "formLabel": "Fahrt anfragen",
    "formNote": "Mit dem Senden wird Ihre Anfrage über FormSubmit übermittelt. Eine Fahrt ist erst nach unserer Bestätigung gebucht.",
    "title": "LD Taxi · Taxi im Bezirk Korneuburg · 24/7",
    "meta": "LD Taxi im Bezirk Korneuburg: Einzelfahrten, Flughafentransfer, Shuttle- und Botendienst. Rund um die Uhr erreichbar unter 0664 7991229."
  },
  "en": {
    "navServices": "Services",
    "backHome": "Back to home",
    "companyInfo": "Company information",
    "companyName": "Company name",
    "companyActivity": "Business activity",
    "transportCompany": "Transportation company",
    "companyAddress": "Registered address",
    "legalTitle": "Legal notice · LD Taxi",
    "legalMeta": "LD Taxi legal notice: company information, address and contact details in Korneuburg.",
    "contact": "Contact",
    "call": "Call us",
    "region": "Taxi in the Korneuburg district",
    "heroFirst": "Your destination.",
    "heroSecond": "Our expertise!",
    "heroText": "Single trips, airport transfers, shuttle and courier services – on the road for you, around the clock.",
    "callNow": "Call a taxi now",
    "request": "Request a ride",
    "available": "Available 24/7",
    "order": "Book a taxi",
    "services": "Our services",
    "servicesHeading": "Five ways to get you there.",
    "servicesIntro": "We understand that transportation needs have no time constraints. Rely on LD Taxi 24/7 for your rides.",
    "service1": "Single trips",
    "description1": "Get from A to B comfortably – whether you have an important business meeting or simply need a safe ride home. We’re here to help.",
    "service2": "Airport transfers",
    "description2": "From Vienna to Salzburg: transfers to Austria’s main airports. Start or end your journey without the stress.",
    "service3": "Shuttle service",
    "description3": "Count on us for your events. Our shuttle service transports you and your guests, whether you’re attending or organizing.",
    "service4": "Courier service",
    "description4": "Packages or documents that need to get from A to B? Our professional courier service has you covered.",
    "service5": "For companies",
    "description5": "Book your business trips with LD Taxi and have the costs invoiced to your company later. Book ahead for a stress-free journey.",
    "whyHeading": "Around the clock. All the way.",
    "hoursText": "Transportation needs have no time constraints. Neither do we – reach us day or night.",
    "airports": "Vienna–Salzburg",
    "airportsText": "Comfortable, convenient transfers to Austria’s main airports.",
    "invoice": "By invoice",
    "invoiceText": "For companies: book a ride, arrive on time, and conveniently pay by invoice later.",
    "contactHeading": "Let’s plan your ride.",
    "contactText": "Give us a call or send us your inquiry. We’ll help plan your next ride.",
    "contactNote": "Available 24/7 · Taxi in the Korneuburg district",
    "name": "Name",
    "telephone": "Phone",
    "email": "Email",
    "pickup": "Pickup location",
    "destination": "Destination",
    "message": "Message",
    "send": "Send inquiry",
    "footer": "© LD Taxi · Taxi in the Korneuburg district",
    "legal": "Legal notice",
    "skip": "Skip to content",
    "homeLabel": "LD Taxi – Home",
    "navLabel": "Main navigation",
    "languageLabel": "Choose language",
    "formLabel": "Request a ride",
    "formNote": "Your inquiry is sent through FormSubmit. Your ride is only booked once we confirm it.",
    "title": "LD Taxi · Taxi in the Korneuburg district · 24/7",
    "meta": "LD Taxi in the Korneuburg district: single trips, airport transfers, shuttle and courier services. Call us around the clock on +43 664 7991229."
  }
};
  const storageKey = 'ldtaxi.language';
  const supported = language => Object.hasOwn(messages, language);
  function deviceLanguage() {
    const preferences = navigator.languages?.length ? navigator.languages : [navigator.language || 'de'];
    for (const locale of preferences) {
      const language = locale.toLowerCase().split(/[-_]/)[0];
      if (supported(language)) return language;
    }
    return 'de';
  }
  function savedLanguage() {
    try {
      const language = localStorage.getItem(storageKey);
      return supported(language) ? language : null;
    } catch { return null; }
  }
  function applyLanguage(language) {
    const copy = messages[language];
    document.documentElement.lang = language;
    const isLegalPage = document.body.dataset.page === 'legal';
    document.title = isLegalPage ? copy.legalTitle : copy.title;
    document.querySelector('meta[name="description"]').content = isLegalPage ? copy.legalMeta : copy.meta;
    document.querySelectorAll('[data-i18n]').forEach(element => {
      const key = element.dataset.i18n;
      if (Object.hasOwn(copy, key)) element.textContent = copy[key];
    });
    document.querySelectorAll('[data-i18n-aria]').forEach(element => {
      element.setAttribute('aria-label', copy[element.dataset.i18nAria]);
    });
    document.querySelectorAll('[data-language]').forEach(button => {
      button.setAttribute('aria-pressed', String(button.dataset.language === language));
    });
    const subject = document.querySelector('input[name="_subject"]');
    if (subject) subject.value = language === 'de' ? 'LD Taxi – Fahrtanfrage' : 'LD Taxi – Ride inquiry';
  }
  document.querySelectorAll('[data-language]').forEach(button => {
    button.addEventListener('click', () => {
      const language = button.dataset.language;
      if (!supported(language)) return;
      try { localStorage.setItem(storageKey, language); } catch { /* Device selection still works without storage. */ }
      applyLanguage(language);
    });
  });
  window.addEventListener('languagechange', () => {
    if (!savedLanguage()) applyLanguage(deviceLanguage());
  });
  applyLanguage(savedLanguage() || deviceLanguage());
})();
