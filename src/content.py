# -*- coding: utf-8 -*-
"""All page URLs and per-language copy used by build.py (new components only).
The long, finished sections (hero, promise, before/after, calculator, bio+process, contact form)
live as HTML partials in src/<lang>/*.html."""

LANGS = ['en', 'fr', 'it']
LOCALE = {'en': 'en_GB', 'fr': 'fr_FR', 'it': 'it_IT'}

# page key -> {lang: clean URL}.  Every page is a folder with index.html (Cloudflare Pages serves /x/ without rewrites).
PAGES = {
    'home':     {'en': '/',          'fr': '/fr/',                  'it': '/it/'},
    'services': {'en': '/services/', 'fr': '/fr/services/',         'it': '/it/servizi/'},
    'work':     {'en': '/work/',     'fr': '/fr/projets/',          'it': '/it/progetti/'},
    'about':    {'en': '/about/',    'fr': '/fr/a-propos/',         'it': '/it/chi-sono/'},
    'contact':  {'en': '/contact/',  'fr': '/fr/contact/',          'it': '/it/contatto/'},
    'privacy':  {'en': '/privacy/',  'fr': '/fr/confidentialite/',  'it': '/it/privacy/'},
    'cookies':  {'en': '/cookies/',  'fr': '/fr/cookies/',          'it': '/it/cookie/'},
}

# ───────────────────────── page meta ─────────────────────────
META = {
    'home': {
        'en': dict(title='Upmarkpro | More Calls Websites & Brand Identity for Local Trades',
                   desc='I design More Calls Websites, brand identities and Shopify stores for local trades — so you outrank competitors, get found and win more work.',
                   og_desc='I design brands, More Calls Websites and Shopify stores for local trade and service businesses — helping them outrank competitors, get found and win more work.',
                   tw_title='Upmarkpro | More Calls Websites & Brand Identity',
                   tw_desc='Website design, brand identity and Shopify stores for local trades. Look credible, get found, win the work.',
                   keywords='website design for trades, more calls website, brand identity design, Shopify store design, local business website, plumber website, electrician website, roofer website, local SEO, WhatsApp integration'),
        'fr': dict(title='Upmarkpro | Sites More Calls & identité de marque pour artisans locaux',
                   desc='Sites More Calls, identités de marque et boutiques Shopify pour artisans et prestataires locaux. Soyez trouvé et décrochez plus de chantiers.',
                   og_desc='Je crée des marques, des sites More Calls et des boutiques Shopify pour les artisans et prestataires locaux — pour devancer la concurrence, être trouvé et décrocher plus de travail.',
                   tw_title='Upmarkpro | Sites More Calls & identité de marque',
                   tw_desc='Design web, identité de marque et boutiques Shopify pour artisans locaux. Paraissez pro, soyez trouvé, décrochez le travail.',
                   keywords="design web artisans, site more calls, identité de marque, boutique Shopify, site entreprise locale, site plombier, site électricien, SEO local, intégration WhatsApp, Riviera française, Côte d'Azur"),
        'it': dict(title='Siti web per attività locali e imprese | Upmarkpro',
                   desc='Siti web veloci, immagine coordinata e scheda Google per attività locali, studi professionali ed e-commerce. Chiamami o scrivimi su WhatsApp.'),
    },
    'services': {
        'en': dict(title='Services: Website Design, Branding, Google & Shopify | Upmarkpro',
                   desc="Four services built to work together: More Calls website design, brand identity, Google visibility and Shopify stores. See exactly what's included."),
        'fr': dict(title='Services : sites web, identité de marque, Google et Shopify | Upmarkpro',
                   desc='Quatre services pensés pour fonctionner ensemble : sites More Calls, identité de marque, visibilité Google et boutiques Shopify. Voyez ce qui est inclus.'),
        'it': dict(title='Servizi: siti web, branding, Google e Shopify | Upmarkpro',
                   desc='Quattro servizi pensati per lavorare insieme: siti web, branding, visibilità su Google e negozi online Shopify. Scopri cosa è incluso.'),
    },
    'work': {
        'en': dict(title='Concept Projects for Real Industries | Upmarkpro',
                   desc='Six concept sites for schools, solar, dental, construction, barbers and events, built to show my approach. Switch between desktop and mobile.'),
        'fr': dict(title='Projets démonstratifs pour des secteurs réels | Upmarkpro',
                   desc='Six sites concept pour écoles, solaire, dentistes, bâtiment, barbiers et événements, créés pour montrer ma méthode. Passez du bureau au mobile.'),
        'it': dict(title='Progetti dimostrativi per settori reali | Upmarkpro',
                   desc='Sei siti concept per scuole, fotovoltaico, dentisti, edilizia, barbieri ed eventi, realizzati per mostrare il mio metodo. Passa da desktop a mobile.'),
    },
    'about': {
        'en': dict(title='About Upmarkpro: How I Work | Upmarkpro',
                   desc='Listen, strategy, design, delivery: how I work with local businesses, plus answers to the questions people ask before starting a website.'),
        'fr': dict(title='À propos et méthode de travail | Upmarkpro',
                   desc="Écoute, stratégie, design, livraison : ma façon de travailler avec les entreprises locales, et les réponses aux questions qu'on me pose avant de commencer."),
        'it': dict(title='Chi sono e come lavoro | Upmarkpro',
                   desc='Ascolto, strategia, design e consegna: come lavoro con le attività locali, più le risposte alle domande più frequenti prima di iniziare.'),
    },
    'contact': {
        'en': dict(title='Contact & Free Online Presence Audit | Upmarkpro',
                   desc='Send me your business name for a free summary of how you look on Google and the web, or tell me about your project. I reply within 24 hours.'),
        'fr': dict(title='Contact et audit gratuit de votre présence en ligne | Upmarkpro',
                   desc="Envoyez-moi le nom de votre entreprise pour un audit gratuit de votre présence sur Google et le web, ou parlez-moi de votre projet. Réponse sous 24 h."),
        'it': dict(title='Contatti e analisi gratuita | Upmarkpro',
                   desc="Mandami il nome della tua attività per un'analisi gratuita di come ti vedono su Google e sul web, oppure raccontami il progetto. Rispondo entro 24 ore."),
    },
}

# ───────────────────────── header / footer / dock ─────────────────────────
NAV = {
    'en': dict(services='Services', work='Work', about='About', contact='Contact', cta='Start a project', wa_aria='Chat on WhatsApp', menu='Menu'),
    'fr': dict(services='Services', work='Projets', about='À propos', contact='Contact', cta='Démarrer un projet', wa_aria='Discuter sur WhatsApp', menu='Menu'),
    'it': dict(services='Servizi', work='Progetti', about='Chi sono', contact='Contatto', cta='Analisi gratuita', wa_aria='Scrivimi su WhatsApp', menu='Menu'),
}
FOOT = {
    'en': dict(desc='Website design, brand identity and Shopify stores for local trades that want to look credible, get found and win more work.',
               cols=('Services', 'Navigate', 'Contact'), copy='© 2026 Upmarkpro. All rights reserved.', privacy='Privacy', cookies='Cookies', aria='Site footer', home='Home'),
    'fr': dict(desc='Design web, identité de marque et boutiques Shopify pour les artisans locaux qui veulent paraître crédibles, être trouvés et gagner plus de clients.',
               cols=('Services', 'Navigation', 'Contact'), copy='© 2026 Upmarkpro. Tous droits réservés.', privacy='Confidentialité', cookies='Cookies', aria='Pied de page', home='Accueil'),
    'it': dict(desc='Sito, immagine e Google per attività che vogliono sembrare affidabili, farsi trovare e lavorare di più.',
               cols=('Servizi', 'Navigazione', 'Contatti'), copy='© 2026 Upmarkpro. Tutti i diritti riservati.', privacy='Privacy', cookies='Cookie', aria='Piè di pagina', home='Home'),
}
DOCK = {
    'en': dict(aria='Quick contact', replies='Replies within 24h', quote='Get a quote'),
    'fr': dict(aria='Contact rapide', replies='Réponse sous 24 h', quote='Demander un devis'),
    'it': dict(aria='Contatto rapido', replies='Risposta entro 24 ore', quote='Richiedi un preventivo'),
}
DRAWER = {
    'en': dict(lang='Language', wa='WhatsApp', call='Call', mail='Email', cta='Get a free audit →', close='Close menu', menu='Menu'),
    'fr': dict(lang='Langue', wa='WhatsApp', call='Appeler', mail='Email', cta='Audit gratuit →', close='Fermer le menu', menu='Menu'),
    'it': dict(lang='Lingua', wa='WhatsApp', call='Chiama', mail='Email', cta='Analisi gratuita →', close='Chiudi il menu', menu='Menu'),
}
BACKTOP = {'en': 'Back to top', 'fr': 'Retour en haut', 'it': 'Torna su'}

# ───────────────────────── services ─────────────────────────
# order: website, brand, google, shopify
SERVICE_SHORT = {
    'en': ['Website Design', 'Brand Identity', 'Google Visibility', 'Shopify Stores'],
    'fr': ['Design Web', 'Identité de Marque', 'Visibilité Google', 'Boutiques Shopify'],
    'it': ['Siti web', 'Branding', 'Visibilità su Google', 'Negozi Shopify'],
}
SERVICES = {
    'en': [
        dict(title='More Calls Website Design',
             p='A fast, mobile-first website built to rank on Google and turn visitors into phone calls and booked jobs — not another site your competitors outrank.',
             chips=['Fast Load Speed', 'Mobile-First', 'Local SEO', 'Click-to-Call'],
             items=['Custom mobile-first design', 'Local SEO & Google Maps optimisation', 'Click-to-call & WhatsApp booking', 'Fast-loading, mobile-first pages', 'Service & location pages built to rank', 'Link to your Google Business Profile']),
        dict(title='Brand Identity',
             p='A complete brand system — logo, colour and typography — so your trucks, signage and socials finally look like the same credible business.',
             chips=['Logo Design', 'Color System', 'Typography', 'Print & Social'],
             items=['Logo design & usage guide', 'Brand colour palette', 'Typography system', 'Signage & print-ready assets', 'Social media templates', 'Brand guidelines document']),
        dict(title='Google Visibility',
             p='I get you found when someone searches for your service in your area.',
             chips=['Business Profile', 'Local Maps', 'Photos & Hours', 'Reviews'],
             items=['Google Business Profile setup or clean-up', 'Correct categories and services', 'Photos and opening hours', 'Link to your website', 'Tips for collecting reviews']),
        dict(title='Shopify Store Design',
             p='A Shopify store built to sell — for trades and local businesses selling products, parts or gift cards online, so customers buy from you instead of a competitor open 24/7.',
             chips=['Product Pages', 'Secure Checkout', 'Mobile Store', 'Inventory Setup'],
             items=['Custom Shopify theme design', 'Product & collection pages', 'Secure checkout & payments', 'Mobile-optimised store', 'Inventory & shipping setup']),
    ],
    'fr': [
        dict(title='More Calls Website Design',
             p='Un site rapide et mobile-first, conçu pour bien classer sur Google et transformer les visiteurs en appels et en rendez-vous — pas un site de plus que vos concurrents devancent.',
             chips=['Chargement Rapide', 'Mobile-First', 'SEO Local', 'Appel en 1 Clic'],
             items=['Design mobile-first sur mesure', 'Optimisation SEO local & Google Maps', 'Appel et réservation WhatsApp en 1 clic', 'Pages à chargement rapide, pensées pour mobile', 'Pages services & localités conçues pour être bien classées', 'Lien vers votre fiche Google Business']),
        dict(title='Identité de Marque',
             p='Un système de marque complet — logo, couleurs et typographie — pour que vos camions, votre enseigne et vos réseaux sociaux paraissent enfin être la même entreprise crédible.',
             chips=['Design Logo', 'Système de Couleurs', 'Typographie', 'Print & Social'],
             items=["Logo & guide d'usage", 'Palette de couleurs de marque', 'Système typographique', 'Supports prêts pour enseigne & print', 'Templates réseaux sociaux', 'Document de guidelines de marque']),
        dict(title='Visibilité sur Google',
             p="Je vous fais trouver quand quelqu'un cherche votre service dans votre zone.",
             chips=['Fiche Google', 'Google Maps', 'Photos et horaires', 'Avis'],
             items=['Création ou mise en ordre de la fiche Google Business', 'Catégories et services corrects', 'Photos et horaires', 'Lien vers votre site', 'Conseils pour récolter des avis']),
        dict(title='Boutique Shopify',
             p='Une boutique Shopify conçue pour vendre — pour les artisans et commerces locaux qui vendent des produits, pièces ou cartes cadeaux en ligne, pour que vos clients achètent chez vous plutôt que chez un concurrent ouvert 24/7.',
             chips=['Pages Produits', 'Paiement Sécurisé', 'Boutique Mobile', 'Configuration Stock'],
             items=['Thème Shopify sur mesure', 'Pages produits & collections', 'Paiement sécurisé', 'Boutique optimisée mobile', 'Configuration stock & livraison']),
    ],
    'it': [
        dict(title='Siti web',
             p='Un sito veloce, pensato per il telefono, che spiega cosa fai e trasforma le visite in chiamate e messaggi.',
             chips=['Design su misura', 'Google e Maps', 'Chiama e WhatsApp', 'Pagine per zone'],
             items=['Design su misura', 'Ottimizzazione per Google e Maps', 'Pulsanti Chiama e WhatsApp', 'Pagine per servizi e zone', 'Collegamento alla scheda Google']),
        dict(title='Branding',
             p='Logo, colori e caratteri coordinati, così furgone, insegna, biglietti e social sembrano la stessa azienda seria.',
             chips=['Logo', 'Palette colori', 'Caratteri', 'Stampa e social'],
             items=["Logo e regole d'uso", 'Palette colori', 'Caratteri', 'File pronti per la stampa', 'Modelli per i social']),
        dict(title='Visibilità su Google',
             p='Ti faccio trovare quando qualcuno cerca il tuo servizio nella tua zona.',
             chips=['Scheda Google', 'Categorie', 'Foto e orari', 'Recensioni'],
             items=['Creazione o sistemazione della scheda Google Business', 'Categorie e servizi corretti', 'Foto e orari', 'Collegamento al sito', 'Consigli per raccogliere recensioni']),
        dict(title='Negozi online Shopify',
             p='Un negozio online per vendere prodotti, ricambi o buoni regalo, anche quando sei chiuso.',
             chips=['Pagine prodotto', 'Pagamenti sicuri', 'Versione mobile', 'Spedizioni e magazzino'],
             items=['Tema Shopify su misura', 'Pagine prodotto e collezioni', 'Pagamenti sicuri', 'Versione mobile', 'Spedizioni e magazzino']),
    ],
}
SERVICE_META = [  # id, class, icon key, number
    ('website', 'svc-web', 'ico_web', '01'), ('brand', 'svc-brand', 'ico_brand', '02'),
    ('google', 'svc-brand', 'ico_google', '03'), ('shopify', 'svc-shop', 'ico_shop', '04'),
]
SERVICES_UI = {
    'en': dict(aria='Services', eyebrow='/ What I do', h='Four services. Built to work together.',
               sub='Website design, brand identity, Google visibility and Shopify stores — take one, or combine them all.',
               incl="What's included", explore='Explore all services & inclusions →', list_h='The four services', aria_sec='Services'),
    'fr': dict(aria='Services', eyebrow='/ Ce que je fais', h='Quatre services. Conçus pour fonctionner ensemble.',
               sub='Design web, identité de marque, visibilité Google et boutiques Shopify — prenez un service ou combinez-les tous.',
               incl='Voir le détail', explore='Découvrir tous les services et ce qui est inclus →', list_h='Les quatre services', aria_sec='Services'),
    'it': dict(aria='Servizi', eyebrow='/ Cosa faccio', h='Quattro servizi. Pensati per lavorare insieme.',
               sub='Siti web, branding, visibilità su Google e negozi online Shopify — scegline uno o combinali tutti.',
               incl='Inclusi', explore='Scopri tutti i servizi e cosa è incluso →', list_h='I quattro servizi', aria_sec='Servizi'),
}

PER_CHI = {
    'en': dict(label='/ Who I work for', aria='Who I work for', cards=[
        dict(icon='trades', badge='01 / LOCAL', title='Local businesses',
             tags=['Plumbers', 'Electricians', 'Tilers', 'Painters', 'Drywallers', 'Window fitters', 'HVAC', 'Gardeners', 'Restaurants & bars', 'Dental practices', 'Private schools', 'Language centres'],
             outcome_label='Primary focus', outcome_desc='Tap-to-call buttons, Google Maps visibility and quote requests from mobile.'),
        dict(icon='practices', badge='02 / FIRMS', title='Practices & firms',
             tags=['Solar companies', 'Construction firms', 'Architecture studios', 'Interior designers'],
             outcome_label='Primary focus', outcome_desc='A portfolio that shows your work, authority branding and qualified enquiries.'),
        dict(icon='online', badge='03 / DIGITAL', title='Online & freelance',
             tags=['Shopify e-commerce stores', 'Marketers', 'Independent professionals'],
             outcome_label='Primary focus', outcome_desc='Smooth checkout, fast landing pages and simple lead capture.'),
    ]),
    'fr': dict(label='/ Pour qui je travaille', aria='Pour qui je travaille', cards=[
        dict(icon='trades', badge='01 / LOCAL', title='Entreprises locales',
             tags=['Plombiers', 'Électriciens', 'Carreleurs', 'Peintres', 'Plaquistes', 'Menuisiers', 'Climatisation', 'Jardiniers', 'Restaurants et bars', 'Cabinets dentaires', 'Écoles privées', 'Centres de langues'],
             outcome_label='Priorité', outcome_desc='Appel en un geste, visibilité sur Google Maps et demandes de devis depuis le mobile.'),
        dict(icon='practices', badge='02 / CABINETS', title='Cabinets et entreprises',
             tags=['Entreprises de photovoltaïque', 'Entreprises du bâtiment', "Cabinets d'architecture", "Designers d'intérieur"],
             outcome_label='Priorité', outcome_desc="Un portfolio qui valorise vos réalisations, une image d'autorité et des demandes qualifiées."),
        dict(icon='online', badge='03 / EN LIGNE', title='En ligne et freelances',
             tags=['Boutiques e-commerce Shopify', 'Marketeurs', 'Indépendants'],
             outcome_label='Priorité', outcome_desc="Un paiement fluide, des pages d'atterrissage rapides et une capture de contacts simple."),
    ]),
    'it': dict(label='/ Per chi lavoro', aria='Per chi lavoro', cards=[
        dict(icon='trades', badge='01 / LOCALE', title='Attività locali',
             tags=['Idraulici', 'Elettricisti', 'Piastrellisti', 'Imbianchini', 'Cartongessisti', 'Serramentisti', 'Climatizzazione', 'Giardinieri', 'Ristoranti e bar', 'Studi dentistici', 'Scuole private', 'Centri linguistici'],
             outcome_label='Obiettivo principale', outcome_desc='Chiamata in un tocco, visibilità su Google Maps e richieste di preventivo da mobile.'),
        dict(icon='practices', badge='02 / STUDI', title='Studi e imprese',
             tags=['Aziende di fotovoltaico', 'Imprese edili', 'Studi di architettura', 'Interior designer'],
             outcome_label='Obiettivo principale', outcome_desc="Un portfolio che valorizza i tuoi lavori, un'immagine autorevole e richieste qualificate."),
        dict(icon='online', badge='03 / ONLINE', title='Online e freelance',
             tags=['Negozi e-commerce su Shopify', 'Marketer', 'Professionisti indipendenti'],
             outcome_label='Obiettivo principale', outcome_desc='Checkout fluido, landing page veloci e raccolta contatti semplice.'),
    ]),
}

# ───────────────────────── concept projects ─────────────────────────
CONCEPTS = {  # id -> data (order = display order on the Work page)
    'ifct': dict(url='https://ifct.vercel.app/',
                 niche=dict(it='Scuole', en='Schools', fr='Formation'),
                 title=dict(it='Centro di formazione — concept', en='Training centre — concept', fr='Centre de formation — concept')),
    'digitalpower': dict(url='https://digitalpower-seven.vercel.app/',
                 niche=dict(it='Fotovoltaico', en='Solar', fr='Photovoltaïque'),
                 title=dict(it='Azienda fotovoltaica — concept', en='Solar company — concept', fr='Entreprise photovoltaïque — concept')),
    'dental': dict(url='https://cabinet-dentaire-drmeriem-hamza.vercel.app/',
                 niche=dict(it='Dentisti', en='Dental', fr='Dentistes'),
                 title=dict(it='Studio dentistico — concept', en='Dental clinic — concept', fr='Cabinet dentaire — concept')),
    'ldbatiment': dict(url='https://ld-batiment-carrelage.vercel.app/',
                 niche=dict(it='Edilizia', en='Construction', fr='Bâtiment'),
                 title=dict(it='Impresa di piastrellatura — concept', en='Tiling company — concept', fr='Entreprise de carrelage — concept')),
    'bilelcoiff': dict(url='https://bilelcoiff.vercel.app/',
                 niche=dict(it='Barbieri', en='Barbers', fr='Barbiers'),
                 title=dict(it='Barbiere — concept', en='Barber shop — concept', fr='Barbier — concept')),
    'meryouma': dict(url='https://meryouma-events-3l2d.vercel.app/',
                 niche=dict(it='Eventi', en='Events', fr='Événements'),
                 title=dict(it='Organizzazione eventi — concept', en='Event company — concept', fr="Organisation d'événements — concept")),
}
FEATURED = ['bilelcoiff', 'digitalpower', 'dental']      # shown on the home page
WORK_UI = {
    'en': dict(aria='Concept projects', eyebrow='/ Portfolio', h='Concept projects',
               intro="Sites built to show my approach for real industries. My first clients' projects will appear here.",
               count='6 concept projects · 6 industries', view='View concept ↗', view_plain='View concept', note=None,
               preview='Preview ↑', pick=lambda t: f'Preview {t} in the viewer', alt='Preview of the concept site',
               disclaimer="Concept projects — built to show my approach on real industries. They are not client work and are not the official websites of the businesses they are based on.",
               all='View all 6 concept projects →', viewer='Concept site viewer', list_h='All concept projects'),
    'fr': dict(aria='Projets démonstratifs', eyebrow='/ Portfolio', h='Projets démonstratifs',
               intro='Des sites créés pour montrer ma méthode sur des secteurs réels. Les projets de mes premiers clients apparaîtront ici.',
               count='6 projets démonstratifs · 6 secteurs', view='Voir le concept ↗', view_plain='Voir le concept', note=None,
               preview='Aperçu ↑', pick=lambda t: f'Voir {t} dans la visionneuse', alt='Aperçu du site concept',
               disclaimer="Projets démonstratifs — créés pour montrer ma méthode sur des secteurs réels. Ce ne sont ni des projets clients ni les sites officiels des entreprises dont ils s'inspirent.",
               all='Voir les 6 projets démonstratifs →', viewer='Visionneuse des sites concept', list_h='Tous les projets démonstratifs'),
    'it': dict(aria='Progetti dimostrativi', eyebrow='/ Portfolio', h='Progetti dimostrativi',
               intro='Siti realizzati per mostrare il mio metodo su settori reali. I primi clienti in Italia avranno qui il loro progetto.',
               count='6 progetti dimostrativi · 6 settori', view='Vedi il concept ↗', view_plain='Vedi il concept', note='Sito in francese',
               preview='Anteprima ↑', pick=lambda t: f'Mostra {t} nel visualizzatore', alt='Anteprima del sito concept',
               disclaimer="Progetti dimostrativi — realizzati per mostrare il mio metodo su settori reali. Non sono lavori per clienti né i siti ufficiali delle attività a cui si ispirano.",
               all='Vedi tutti i 6 progetti dimostrativi →', viewer='Visualizzatore dei siti concept', list_h='Tutti i progetti dimostrativi'),
}

# ───────────────────────── about / faq / offer / cta ─────────────────────────
ABOUT_UI = {
    'en': dict(teaser_link='More about me →', aria='About'),
    'fr': dict(teaser_link='En savoir plus sur moi →', aria='À propos'),
    'it': dict(teaser_link='Scopri di più su di me →', aria='Chi sono'),
}
FIRST_CLIENTS = {  # Italian market only
    'it': dict(h='Prezzo dedicato ai primi clienti in Italia',
               p="Sto iniziando in Italia e cerco i primi 3 clienti. Per loro c'è un prezzo ridotto, in cambio di una recensione su Google e del permesso di mostrare il progetto qui.",
               aria='Primi clienti'),
}
FAQ = {
    'en': dict(aria='Frequently asked questions', eyebrow='/ FAQ', h='Frequently asked questions', qa=[
        ('How much does a website cost?', 'It depends on what you need. After a short call I send you a clear quote, no strings attached, and we talk it through.'),
        ('How long does it take?', 'It depends on the project: I tell you in the quote, before we start.'),
        ('Do you only work in my city?', 'No, I work remotely with businesses across Italy.'),
        ('Do I have to do anything?', 'Very little: you send me photos, services and information about your business. I take care of the rest.'),
        ('What happens after delivery?', 'I show you how to update the basic information and I stay available for changes and questions.'),
        ('Are the projects shown client work?', "No, they are concept projects built to show my work on real industries. My first clients' projects will appear here.")]),
    'fr': dict(aria='Questions fréquentes', eyebrow='/ FAQ', h='Questions fréquentes', qa=[
        ('Combien coûte un site ?', 'Cela dépend de ce dont vous avez besoin. Après un court appel, je vous envoie un devis clair, sans engagement, et nous en discutons ensemble.'),
        ('En combien de temps est-il prêt ?', "Cela dépend du projet : je vous l'indique dans le devis, avant de commencer."),
        ('Travaillez-vous seulement dans ma ville ?', "Non, je travaille à distance avec des entreprises dans toute l'Italie."),
        ('Dois-je faire quelque chose ?', "Peu : vous m'envoyez photos, services et informations sur votre activité. Je m'occupe du reste."),
        ('Que se passe-t-il après la livraison ?', 'Je vous explique comment mettre à jour les informations de base et je reste disponible pour les modifications et les questions.'),
        ('Les projets présentés sont-ils des projets clients ?', 'Non, ce sont des projets démonstratifs créés pour montrer mon travail sur des secteurs réels. Les projets de mes premiers clients apparaîtront ici.')]),
    'it': dict(aria='Domande frequenti', eyebrow='/ FAQ', h='Domande frequenti', qa=[
        ('Quanto costa un sito?', 'Dipende da cosa ti serve. Dopo una breve chiamata ti mando un preventivo chiaro, senza impegno, e ne parliamo insieme.'),
        ('In quanto tempo è pronto?', 'Dipende dal progetto: te lo indico nel preventivo, prima di iniziare.'),
        ('Lavori solo nella mia città?', 'No, lavoro a distanza con attività in tutta Italia.'),
        ('Devo fare qualcosa io?', 'Poco: mi mandi foto, servizi e informazioni sulla tua attività. Al resto penso io.'),
        ('Cosa succede dopo la consegna?', 'Ti spiego come aggiornare le informazioni base e resto disponibile per modifiche e domande.'),
        ('I progetti mostrati sono di clienti?', 'No, sono progetti dimostrativi realizzati per mostrare il mio lavoro su settori reali. I primi clienti italiani avranno qui il loro progetto.')]),
}
OFFER = {
    'en': dict(aria='Free audit', eyebrow='/ Free audit', h='Free audit of your online presence.',
               p='Send me your business name. Within 48 hours you get a short summary: how you look on Google and the web today, and 3 concrete things to improve. Free, no strings attached.',
               btn='Request the audit on WhatsApp →', small='I reply within 24 hours. No obligation, no jargon.',
               wa='Hello, I would like the free audit for my business: [business name, city]'),
    'fr': dict(aria='Audit gratuit', eyebrow='/ Audit gratuit', h='Audit gratuit de votre présence en ligne.',
               p="Envoyez-moi le nom de votre entreprise. Sous 48 heures, vous recevez un court récapitulatif : comment on vous voit aujourd'hui sur Google et sur le web, et 3 choses concrètes à améliorer. Gratuit et sans engagement.",
               btn="Demander l'audit sur WhatsApp →", small='Je réponds sous 24 heures. Aucune obligation, aucun jargon.',
               wa="Bonjour, je voudrais l'audit gratuit pour mon entreprise : [nom de l'entreprise, ville]"),
    'it': dict(aria='Analisi gratuita', eyebrow='/ Analisi gratuita', h='Analisi gratuita della tua presenza online.',
               p='Mandami il nome della tua attività. Entro 48 ore ricevi un breve riepilogo: come ti vedono oggi su Google e sul web, e 3 cose concrete da migliorare. Gratis e senza impegno.',
               btn="Richiedi l'analisi su WhatsApp →", small='Rispondo entro 24 ore. Nessun obbligo, nessun gergo tecnico.',
               wa="Ciao, vorrei l'analisi gratuita per la mia attività: [nome attività, città]"),
}
CTA = {
    'en': dict(aria='Get in touch', go='Start a project →', quote='Request a quote →', wa='Chat on WhatsApp'),
    'fr': dict(aria='Nous contacter', go='Démarrer un projet →', quote='Demander un devis →', wa='Discuter sur WhatsApp'),
    'it': dict(aria='Contattami', go="Richiedi l'analisi gratuita →", quote='Richiedi un preventivo →', wa='Scrivimi su WhatsApp'),
}
SHOWROOM_ARIA = {'en': 'Concept site viewer', 'fr': 'Visionneuse des sites concept', 'it': 'Visualizzatore dei siti concept'}
