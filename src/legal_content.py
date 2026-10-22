# -*- coding: utf-8 -*-
"""Privacy notice + cookie page copy (DRAFT) in EN / FR / IT, used by build.py."""
T = lambda s: f'<span class="todo">{s}</span>'

# file -> public URL
PAGES = {
  ('privacy', 'en'): ('privacy.html', '/privacy'),
  ('privacy', 'fr'): ('fr/confidentialite.html', '/fr/confidentialite'),
  ('privacy', 'it'): ('it/privacy.html', '/it/privacy'),
  ('cookie', 'en'): ('cookies.html', '/cookies'),
  ('cookie', 'fr'): ('fr/cookies.html', '/fr/cookies'),
  ('cookie', 'it'): ('it/cookie.html', '/it/cookie'),
}
HOME = {'en': '/', 'fr': '/fr/', 'it': '/it/'}

C = {}
# ───────────────────────── ITALIANO ─────────────────────────
C['it'] = dict(
  back='← Home', updated='Ultimo aggiornamento: 17 ottobre 2026 (bozza)',
  draft_h='Bozza da revisionare',
  draft='Questo testo è una bozza preparata per essere verificata dal titolare (ed eventualmente da un consulente legale) prima della pubblicazione definitiva. Le parti evidenziate tra parentesi quadre sono da completare o confermare.',
  rights_footer='© 2026 Upmarkpro. Tutti i diritti riservati.', foot_priv='Privacy', foot_cookie='Cookie',
  privacy=dict(
    title='Informativa sulla privacy', meta='Come Upmarkpro tratta i dati personali di chi visita il sito o scrive tramite il modulo, WhatsApp o email.',
    sections=[
      ('Titolare del trattamento', [
        f'Il titolare del trattamento è <strong>Adem — Upmarkpro</strong>, contattabile all\'indirizzo <a href="mailto:hello@upmarkpro.com">hello@upmarkpro.com</a>. {T("[Indirizzo e P. IVA: da aggiungere dopo la registrazione dell\'attività]")}']),
      ('Quali dati raccogliamo e come', [
        '<strong>Modulo di contatto.</strong> Il modulo non invia i dati a un server di Upmarkpro. Quando premi «Invia su WhatsApp», il sito prepara un messaggio con le informazioni che hai inserito (nome, email, nome dell\'attività, servizio di interesse e messaggio) e apre WhatsApp: i dati ci arrivano solo se tocchi Invia nell\'app.',
        '<strong>Messaggi diretti.</strong> Se ci scrivi o ci chiami su WhatsApp, per email o per telefono, trattiamo il tuo numero o indirizzo e il contenuto della conversazione.',
        '<strong>Strumento «Quanto ti costano le chiamate perse?».</strong> I valori che inserisci restano nel tuo browser. Se scegli di inviare l\'audit su WhatsApp, vale come un messaggio diretto.',
        '<strong>Dati di navigazione.</strong> Il fornitore di hosting del sito (Cloudflare) può registrare dati tecnici come indirizzo IP, data e ora e pagina richiesta, per far funzionare il servizio e proteggerlo da abusi.',
        'Il sito non usa cookie di profilazione né strumenti di analisi: vedi la pagina <a href="/it/cookie/">Cookie</a>.']),
      ('Perché li utilizziamo e su quale base', [
        '<ul><li>Rispondere alle tue richieste e preparare un\'eventuale proposta: misure precontrattuali richieste da te (art. 6.1.b GDPR).</li>'
        '<li>Ricontattarti dopo la tua richiesta: il tuo consenso, che dai con la casella nel modulo (art. 6.1.a GDPR) e che puoi revocare quando vuoi.</li>'
        '<li>Sicurezza e funzionamento tecnico del sito: legittimo interesse (art. 6.1.f GDPR).</li>'
        '<li>Adempiere a obblighi di legge se nasce un rapporto di lavoro, per esempio la fatturazione (art. 6.1.c GDPR).</li></ul>',
        'Fornire i dati è facoltativo, ma senza i dati essenziali non possiamo rispondere alla tua richiesta. Non facciamo profilazione né decisioni automatizzate.']),
      ('A chi comunico i dati', [
        'Ai fornitori tecnici necessari al servizio: Cloudflare (hosting del sito), Meta Platforms / WhatsApp (messaggistica, con una propria informativa) e '
        + T('[fornitore della posta elettronica: da confermare]') + '. Non vendiamo né cediamo i tuoi dati a terzi per scopi di marketing.']),
      ('Trasferimenti fuori dallo Spazio economico europeo', [
        'Alcuni fornitori possono trattare dati anche fuori dallo SEE. In questo caso si appoggiano alle garanzie previste dal GDPR, come le clausole contrattuali standard o le decisioni di adeguatezza (per esempio l\'EU-US Data Privacy Framework). '
        + T('[da verificare con i fornitori scelti]')]),
      ('Per quanto tempo li conserviamo', [
        'I dati delle richieste restano per il tempo necessario a rispondere e, se non nasce un rapporto, non oltre ' + T('[12 mesi: periodo da confermare]') + '. '
        'Se nasce un rapporto di lavoro, li conserviamo per la sua durata e per i termini previsti dalla legge (per esempio per i documenti contabili). I log tecnici seguono le politiche del fornitore di hosting.']),
      ('I tuoi diritti', [
        'Puoi chiedere in qualsiasi momento l\'accesso ai tuoi dati, la rettifica, la cancellazione, la limitazione del trattamento, la portabilità e opporti al trattamento. Puoi anche revocare il consenso, senza che questo pregiudichi il trattamento già avvenuto.',
        'Per esercitare i tuoi diritti scrivici a <a href="mailto:hello@upmarkpro.com">hello@upmarkpro.com</a>. Se ritieni che il trattamento violi la normativa, puoi presentare reclamo al <a href="https://www.garanteprivacy.it" rel="noopener">Garante per la protezione dei dati personali</a>.']),
      ('Cookie', ['Il sito non imposta cookie. Maggiori dettagli nella pagina <a href="/it/cookie/">Cookie</a>.']),
    ]),
  cookie=dict(
    title='Cookie', meta='Il sito di Upmarkpro non usa cookie né strumenti di tracciamento.',
    sections=[
      ('In breve', ['Questo sito <strong>non imposta cookie</strong>, né propri né di terze parti, e non usa strumenti di analisi, pixel pubblicitari o altri sistemi di tracciamento. Per questo non mostra un banner dei cookie.']),
      ('Cosa succede quando navighi', [
        '<ul><li>Nessun cookie e nessun dato salvato nel browser (né cookie, né localStorage o sessionStorage).</li>'
        '<li>I caratteri e gli script del sito sono ospitati sullo stesso sito: per caricarli non viene contattato nessun servizio esterno.</li>'
        '<li>Nessuna mappa, video o altro contenuto incorporato da terzi.</li></ul>']),
      ('Link verso altri servizi', [
        'Il sito contiene link verso servizi esterni, come WhatsApp, Facebook, Instagram e i siti dimostrativi ospitati su Vercel. Quando li apri lasci questo sito: quei servizi hanno le proprie politiche sulla privacy e sui cookie.']),
      ('Se cambia qualcosa', [
        'Se in futuro useremo strumenti di analisi o altri servizi che richiedono cookie, aggiorneremo questa pagina e chiederemo il tuo consenso prima di attivarli. Per domande: <a href="mailto:hello@upmarkpro.com">hello@upmarkpro.com</a>. Vedi anche l\'<a href="/it/privacy/">informativa sulla privacy</a>.']),
    ]),
)
# ───────────────────────── ENGLISH ─────────────────────────
C['en'] = dict(
  back='← Home', updated='Last updated: 17 October 2026 (draft)',
  draft_h='Draft to review',
  draft='This text is a draft prepared for the controller (and, if needed, a legal adviser) to check before final publication. The highlighted parts in square brackets still need to be completed or confirmed.',
  rights_footer='© 2026 Upmarkpro. All rights reserved.', foot_priv='Privacy', foot_cookie='Cookies',
  privacy=dict(
    title='Privacy notice', meta='How Upmarkpro handles the personal data of people who visit the site or write through the form, WhatsApp or email.',
    sections=[
      ('Data controller', [
        f'The data controller is <strong>Adem — Upmarkpro</strong>, reachable at <a href="mailto:hello@upmarkpro.com">hello@upmarkpro.com</a>. {T("[Address and VAT number: to be added once the business is registered]")}']),
      ('What data we collect and how', [
        '<strong>Contact form.</strong> The form does not send data to an Upmarkpro server. When you press “Send via WhatsApp”, the site prepares a message with what you entered (name, email, business name, service of interest and message) and opens WhatsApp: the data reaches us only if you tap Send in the app.',
        '<strong>Direct messages.</strong> If you write to or call us on WhatsApp, by email or by phone, we process your number or address and the content of the conversation.',
        '<strong>The “missed calls” calculator.</strong> The values you enter stay in your browser. If you choose to send the audit on WhatsApp, it counts as a direct message.',
        '<strong>Browsing data.</strong> The site’s hosting provider (Cloudflare) may log technical data such as IP address, date and time and the page requested, to run the service and protect it from abuse.',
        'The site uses no profiling cookies or analytics tools: see the <a href="/cookies/">Cookies</a> page.']),
      ('Why we use it and on what basis', [
        '<ul><li>To answer your requests and prepare a proposal if you want one: pre-contractual steps you asked for (Art. 6(1)(b) GDPR).</li>'
        '<li>To get back to you after your request: your consent, given with the checkbox on the form (Art. 6(1)(a) GDPR), which you can withdraw at any time.</li>'
        '<li>Security and technical operation of the site: legitimate interest (Art. 6(1)(f) GDPR).</li>'
        '<li>Legal obligations if we end up working together, such as invoicing (Art. 6(1)(c) GDPR).</li></ul>',
        'Providing your data is optional, but without the essential details we cannot answer your request. We do no profiling and no automated decision-making.']),
      ('Who receives the data', [
        'The technical providers needed to run the service: Cloudflare (website hosting), Meta Platforms / WhatsApp (messaging, which has its own privacy notice) and '
        + T('[email provider: to be confirmed]') + '. We do not sell or pass your data to third parties for marketing.']),
      ('Transfers outside the European Economic Area', [
        'Some providers may process data outside the EEA. In that case they rely on the safeguards provided by the GDPR, such as standard contractual clauses or adequacy decisions (for example the EU-US Data Privacy Framework). '
        + T('[to be verified with the chosen providers]')]),
      ('How long we keep it', [
        'Request data is kept for as long as needed to answer and, if no working relationship follows, no longer than ' + T('[12 months: period to be confirmed]') + '. '
        'If we work together, we keep it for the duration of the relationship and for the periods required by law (for example accounting records). Technical logs follow the hosting provider’s policies.']),
      ('Your rights', [
        'You can ask at any time for access to your data, correction, erasure, restriction of processing and portability, and you can object to the processing. You can also withdraw your consent, without affecting processing already carried out.',
        'To exercise your rights write to <a href="mailto:hello@upmarkpro.com">hello@upmarkpro.com</a>. If you believe the processing breaches the rules, you can complain to the Italian <a href="https://www.garanteprivacy.it" rel="noopener">Garante per la protezione dei dati personali</a> or to the supervisory authority of your country.']),
      ('Cookies', ['The site sets no cookies. More details on the <a href="/cookies/">Cookies</a> page.']),
    ]),
  cookie=dict(
    title='Cookies', meta='The Upmarkpro website uses no cookies or tracking tools.',
    sections=[
      ('In short', ['This site <strong>sets no cookies</strong>, neither its own nor third-party, and uses no analytics, advertising pixels or other tracking. That is why it shows no cookie banner.']),
      ('What happens when you browse', [
        '<ul><li>No cookies and nothing stored in your browser (no cookies, localStorage or sessionStorage).</li>'
        '<li>The site’s fonts and scripts are hosted on the site itself: no external service is contacted to load them.</li>'
        '<li>No maps, videos or other content embedded from third parties.</li></ul>']),
      ('Links to other services', [
        'The site links to external services such as WhatsApp, Facebook, Instagram and the concept sites hosted on Vercel. When you open them you leave this site: those services have their own privacy and cookie policies.']),
      ('If anything changes', [
        'If we later use analytics or other services that need cookies, we will update this page and ask for your consent before switching them on. Questions: <a href="mailto:hello@upmarkpro.com">hello@upmarkpro.com</a>. See also the <a href="/privacy/">privacy notice</a>.']),
    ]),
)
# ───────────────────────── FRANÇAIS ─────────────────────────
C['fr'] = dict(
  back='← Accueil', updated='Dernière mise à jour : 17 octobre 2026 (brouillon)',
  draft_h='Brouillon à relire',
  draft='Ce texte est un brouillon préparé pour être vérifié par le responsable du traitement (et, si besoin, un conseil juridique) avant la publication définitive. Les passages surlignés entre crochets restent à compléter ou à confirmer.',
  rights_footer='© 2026 Upmarkpro. Tous droits réservés.', foot_priv='Confidentialité', foot_cookie='Cookies',
  privacy=dict(
    title='Politique de confidentialité', meta='Comment Upmarkpro traite les données personnelles des personnes qui visitent le site ou écrivent via le formulaire, WhatsApp ou email.',
    sections=[
      ('Responsable du traitement', [
        f'Le responsable du traitement est <strong>Adem — Upmarkpro</strong>, joignable à <a href="mailto:hello@upmarkpro.com">hello@upmarkpro.com</a>. {T("[Adresse et numéro de TVA : à ajouter après l’enregistrement de l’activité]")}']),
      ('Quelles données nous collectons et comment', [
        '<strong>Formulaire de contact.</strong> Le formulaire n’envoie aucune donnée à un serveur d’Upmarkpro. Quand vous appuyez sur « Envoyer via WhatsApp », le site prépare un message avec ce que vous avez saisi (nom, email, nom de l’entreprise, service souhaité et message) et ouvre WhatsApp : les données ne nous parviennent que si vous touchez Envoyer dans l’application.',
        '<strong>Messages directs.</strong> Si vous nous écrivez ou nous appelez sur WhatsApp, par email ou par téléphone, nous traitons votre numéro ou adresse et le contenu de l’échange.',
        '<strong>Outil « appels manqués ».</strong> Les valeurs saisies restent dans votre navigateur. Si vous choisissez d’envoyer l’audit sur WhatsApp, cela équivaut à un message direct.',
        '<strong>Données de navigation.</strong> L’hébergeur du site (Cloudflare) peut enregistrer des données techniques comme l’adresse IP, la date et l’heure et la page demandée, pour faire fonctionner le service et le protéger contre les abus.',
        'Le site n’utilise ni cookies de profilage ni outils d’analyse : voir la page <a href="/fr/cookies/">Cookies</a>.']),
      ('Pourquoi nous les utilisons et sur quelle base', [
        '<ul><li>Répondre à vos demandes et préparer une proposition si vous le souhaitez : mesures précontractuelles prises à votre demande (art. 6.1.b RGPD).</li>'
        '<li>Vous recontacter après votre demande : votre consentement, donné avec la case du formulaire (art. 6.1.a RGPD), que vous pouvez retirer à tout moment.</li>'
        '<li>Sécurité et fonctionnement technique du site : intérêt légitime (art. 6.1.f RGPD).</li>'
        '<li>Obligations légales si nous travaillons ensemble, par exemple la facturation (art. 6.1.c RGPD).</li></ul>',
        'Fournir vos données est facultatif, mais sans les informations essentielles nous ne pouvons pas répondre à votre demande. Nous ne faisons ni profilage ni décision automatisée.']),
      ('Qui reçoit les données', [
        'Les prestataires techniques nécessaires au service : Cloudflare (hébergement du site), Meta Platforms / WhatsApp (messagerie, avec sa propre politique de confidentialité) et '
        + T('[fournisseur de messagerie email : à confirmer]') + '. Nous ne vendons pas vos données et nous ne les transmettons pas à des tiers à des fins de marketing.']),
      ('Transferts hors de l’Espace économique européen', [
        'Certains prestataires peuvent traiter des données hors de l’EEE. Ils s’appuient alors sur les garanties prévues par le RGPD, comme les clauses contractuelles types ou les décisions d’adéquation (par exemple le EU-US Data Privacy Framework). '
        + T('[à vérifier avec les prestataires choisis]')]),
      ('Combien de temps nous les conservons', [
        'Les données des demandes sont conservées le temps nécessaire pour répondre et, si aucune collaboration ne suit, pas plus de ' + T('[12 mois : durée à confirmer]') + '. '
        'Si nous travaillons ensemble, nous les conservons pendant la collaboration et pour les durées légales (par exemple pour les pièces comptables). Les journaux techniques suivent les politiques de l’hébergeur.']),
      ('Vos droits', [
        'Vous pouvez demander à tout moment l’accès à vos données, leur rectification, leur effacement, la limitation du traitement et leur portabilité, et vous opposer au traitement. Vous pouvez aussi retirer votre consentement, sans effet sur le traitement déjà effectué.',
        'Pour exercer vos droits, écrivez-nous à <a href="mailto:hello@upmarkpro.com">hello@upmarkpro.com</a>. Si vous estimez que le traitement enfreint les règles, vous pouvez introduire une réclamation auprès du <a href="https://www.garanteprivacy.it" rel="noopener">Garante per la protezione dei dati personali</a> (Italie) ou de l’autorité de contrôle de votre pays.']),
      ('Cookies', ['Le site ne dépose aucun cookie. Plus de détails sur la page <a href="/fr/cookies/">Cookies</a>.']),
    ]),
  cookie=dict(
    title='Cookies et traceurs', meta='Le site d’Upmarkpro n’utilise ni cookies ni outils de suivi.',
    sections=[
      ('En bref', ['Ce site <strong>ne dépose aucun cookie</strong>, ni les siens ni ceux de tiers, et n’utilise ni outils d’analyse, ni pixels publicitaires, ni autre système de suivi. C’est pourquoi il n’affiche pas de bandeau de cookies.']),
      ('Ce qui se passe quand vous naviguez', [
        '<ul><li>Aucun cookie et rien d’enregistré dans votre navigateur (ni cookies, ni localStorage ou sessionStorage).</li>'
        '<li>Les polices et scripts du site sont hébergés sur le site lui-même : aucun service externe n’est contacté pour les charger.</li>'
        '<li>Aucune carte, vidéo ou autre contenu intégré depuis des tiers.</li></ul>']),
      ('Liens vers d’autres services', [
        'Le site contient des liens vers des services externes comme WhatsApp, Facebook, Instagram et les sites de démonstration hébergés sur Vercel. En les ouvrant, vous quittez ce site : ces services ont leurs propres politiques de confidentialité et de cookies.']),
      ('Si quelque chose change', [
        'Si nous utilisons plus tard des outils d’analyse ou d’autres services qui nécessitent des cookies, nous mettrons cette page à jour et nous demanderons votre consentement avant de les activer. Questions : <a href="mailto:hello@upmarkpro.com">hello@upmarkpro.com</a>. Voir aussi la <a href="/fr/confidentialite/">politique de confidentialité</a>.']),
    ]),
)

