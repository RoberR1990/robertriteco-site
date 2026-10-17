"""Alle teksten van robertriteco.nl, per taal. Een project toevoegen = één blok in PROJECTS.

Statussen: live | proto | exp   (vol, open, streep in de opmaak)
Contactgegevens: vul CONTACT in; zolang ze leeg zijn toont de site een gele 'nog invullen'-regel.
"""

CONTACT = {
    "email": "",      # bijv. "robert@robertriteco.nl"
    "linkedin": "https://www.linkedin.com/in/rriteco/",   # volledige URL van je LinkedIn-profiel
}

SITE = {
    "domain": "https://robertriteco.nl",
    "github": "https://github.com/RoberR1990",
}

# ---------------------------------------------------------------- projecten

PROJECTS = [
    {
        "slug": "raadzoeker",
        "featured": True,
        "status": "live",
        "url": "https://raadzoeker.nl",
        "shot": "raadzoeker.jpg", "shot_w": 1440, "shot_h": 810,
        "code": "https://github.com/RoberR1990/raadzoeker",
        "nl": {
            "name": "Raadzoeker",
            "shot_alt": "Startpagina van Raadzoeker met een citaat uit de laatste raadsvergadering en zoekbalk",
            "tagline": "Wat de Rotterdamse raad zegt, besluit en belooft, op één plek doorzoekbaar.",
            "card": "Zoek in alles wat de Rotterdamse gemeenteraad, de commissies en de wijkraden sinds 2018 zeiden en schreven.",
            "status_label": "Live",
            "facts": [
                ("Status", "Live, onofficieel hulpmiddel"),
                ("Domein", "Lokale democratie, open raadsinformatie"),
                ("Data", "iBabs, ondertiteling van de raadsvideo's, Gemeenteblad, CBS, PDOK, RDW, Rekenkamer en Ombudsman"),
                ("Licentie", "EUPL-1.2 (open source)"),
                ("Gebouwd met", "Python, statische site op Cloudflare Pages, AI voor samenvattingen"),
            ],
            "sections": [
                ("Doel", [
                    "Raadsinformatie is openbaar, maar verspreid over vergaderstukken, notulen, video's en losse systemen. Raadzoeker brengt dat samen zodat je kunt zoeken op een onderwerp en meteen ziet wat er gezegd, besloten en beloofd is.",
                    "Je vindt per vergadering een korte en een uitgebreide samenvatting met letterlijke citaten en het videomoment. Per onderwerp, domein en gebied is er een eigen pagina, met open moties en toezeggingen en de plekken in de stad waar het speelt.",
                ]),
                ("Waarom", [
                    "Wie wil weten wat een raadslid ooit over parkeren zei of of een toezegging is nagekomen, moet nu in meerdere systemen zoeken. Dat drempelt voor inwoners, journalisten, ambtenaren en raadsleden zelf. Ik wilde laten zien hoeveel je met open data en AI-hulp in korte tijd kunt bouwen.",
                ]),
                ("Data", [
                    "Alles komt uit openbare bronnen: de iBabs-omgevingen van de gemeenteraad en de wijkraden, de openbare video en ondertiteling van de vergaderingen, officielebekendmakingen.nl, CBS, PDOK, RDW Open Data, Rekenkamer Rotterdam en de Ombudsman Rotterdam-Rijnmond.",
                    "Er zijn geen accounts en geen cookies. Namen van insprekers en bewoners worden niet getoond.",
                ]),
                ("Wat kun je ermee", [
                    "Zoek in debatten en stukken, volg een onderwerp en krijg een melding bij nieuws, bekijk wat er per wijk speelt, controleer of beloftes zijn nagekomen, of maak een briefing over een onderwerp.",
                    "AI-samenvattingen zijn als zodanig gelabeld. Elk citaat wordt mechanisch gecontroleerd op een letterlijke vondst in de bron. Dat vangt verzonnen citaten, maar een te ruime samenvatting van een echt citaat vangt het niet.",
                ]),
                ("Voor andere organisaties", [
                    "De bouwstenen zijn open: ophalen, uitlijnen van ondertiteling op sprekers, citaatcontrole en de opbouw van de dossiers. Voor een andere gemeente is aanpassing nodig, maar het ontwerp is bedoeld om hergebruikt te worden.",
                    "Voor griffies, raadsleden en afdelingen die beleid maken is het ook een voorbeeld van hoe je bestaande openbare informatie toegankelijk maakt zonder nieuwe systemen.",
                ]),
                ("Status en hoe verder", [
                    "De site draait en wordt elke nacht bijgewerkt. Het is een onofficieel hulpmiddel van mij, geen product van de gemeente of de griffie.",
                    "Ideeën voor verder: dezelfde aanpak voor andere gemeenten via open raadsinformatie, landelijk debat uit de Tweede Kamer naast het lokale, en regionale besluiten van MRDH en Provinciale Staten.",
                ]),
            ],
            "stats": [("2018", "bestrijkt de periode vanaf"), ("3", "organen: raad, commissies, wijkraden"), ("0", "accounts of cookies nodig")],
        },
        "en": {
            "name": "Raadzoeker",
            "shot_alt": "Raadzoeker home page with a quote from the latest council meeting and a search bar",
            "tagline": "What the Rotterdam city council says, decides and promises, searchable in one place.",
            "card": "Search everything the Rotterdam city council, its committees and the district councils said and wrote since 2018.",
            "status_label": "Live",
            "facts": [
                ("Status", "Live, unofficial tool"),
                ("Field", "Local democracy, open council information"),
                ("Data", "iBabs, subtitles of the council videos, the municipal gazette, CBS, PDOK, RDW, the Court of Audit and the Ombudsman"),
                ("License", "EUPL-1.2 (open source)"),
                ("Built with", "Python, static site on Cloudflare Pages, AI for summaries"),
            ],
            "sections": [
                ("Purpose", [
                    "Council information is public, but spread over agendas, minutes, videos and separate systems. Raadzoeker brings it together so you can search a topic and see right away what was said, decided and promised.",
                    "Every meeting has a short and a long summary with verbatim quotes and the video moment. Each topic, domain and area has its own page, with open motions and commitments and the places in the city where it plays out.",
                ]),
                ("Why", [
                    "To find out what a council member once said about parking, or whether a commitment was kept, you currently search several systems. That is a barrier for residents, journalists, civil servants and council members alike. I also wanted to show how much you can build quickly with open data and AI assistance.",
                ]),
                ("Data", [
                    "Everything comes from public sources: the iBabs environments of the city council and the district councils, the public video and subtitles of the meetings, officielebekendmakingen.nl, CBS, PDOK, RDW Open Data, the Rotterdam Court of Audit and the Rotterdam-Rijnmond Ombudsman.",
                    "There are no accounts and no cookies. Names of residents who spoke in public are not shown.",
                ]),
                ("What you can do with it", [
                    "Search debates and documents, follow a topic and get notified, see what is going on per district, check whether promises were kept, or generate a briefing on a topic.",
                    "AI summaries are labelled as such. Every quote is mechanically checked for a verbatim match in the source. That catches invented quotes, but not an overly broad summary of a real quote.",
                ]),
                ("For other organisations", [
                    "The building blocks are open: fetching, aligning subtitles to speakers, quote checking and the build of the topic pages. Another municipality needs some adaptation, but the design is meant to be reused.",
                    "For clerks' offices, council members and policy teams it is also an example of making existing public information accessible without new systems.",
                ]),
                ("Status and next steps", [
                    "The site is running and updated every night. It is my own unofficial tool, not a product of the municipality or the council clerk.",
                    "Ideas for next: the same approach for other municipalities through open council information, national debate from the House of Representatives next to the local one, and regional decisions of MRDH and the provincial council.",
                ]),
            ],
            "stats": [("2018", "covers the period since"), ("3", "bodies: council, committees, district councils"), ("0", "accounts or cookies needed")],
        },
    },
    {
        "slug": "doorzicht",
        "featured": False,
        "status": "exp",
        "url": "https://roberr1990.github.io/doorzicht/",
        "shot": "doorzicht.jpg", "shot_w": 820, "shot_h": 640,
        "code": "https://github.com/RoberR1990/doorzicht",
        "nl": {
            "name": "Doorzicht",
            "shot_alt": "3D-model van een fictieve parkeergarage met lagen, auto’s en meldingen",
            "tagline": "Zie wat verstopt zit: versnipperde informatie over een parkeergarage op één visuele plek, in 3D.",
            "card": "Een 3D-model van een fictieve parkeergarage waar droge, verspreide informatie samenkomt en bespreekbaar wordt.",
            "status_label": "Experiment",
            "facts": [
                ("Status", "Experiment met fictieve en open data"),
                ("Domein", "Assetbeheer, datagedreven werken"),
                ("Data", "Fictieve data en open data. De garage ‘Toppert’ en alle cijfers zijn verzonnen"),
                ("Gebouwd met", "Three.js, één statische pagina"),
            ],
            "sections": [
                ("Doel", [
                    "Informatie over een parkeergarage zit in tabellen, rapporten en systemen van verschillende afdelingen. Doorzicht zet die samen in een 3D-model, zodat je kunt rondkijken en een gesprek kunt voeren over wat je ziet in plaats van over losse cijfers.",
                ]),
                ("Waarom", [
                    "Veel waardevolle vragen vallen tussen de systemen: wat zegt de bezetting, wat zegt het onderhoud, wat zeggen de klachten, en hoe hangt dat samen? Een gezamenlijk beeld maakt het gesprek tussen rollen makkelijker. Het is een manier om te ontdekken welke vragen echt de moeite waard zijn voordat je iets groots bouwt.",
                ]),
                ("Data", [
                    "Alles is fictief of open data. Er is geen echte garage en er zijn geen echte gegevens van burgers of bedrijven gebruikt.",
                ]),
                ("Wat kun je ermee", [
                    "Je kunt een rondleiding volgen per rol en zien welke informatie voor jouw functie telt. De demo is bedoeld voor sessies waarin collega’s samen kijken en zeggen wat ze missen of juist niet nodig hebben.",
                ]),
                ("Voor andere organisaties", [
                    "Elke organisatie met verspreide informatie over een fysieke plek, zoals een gebouw, een kade of een wijk, kan hetzelfde idee gebruiken. De roadmap beschrijft hoe je van een experiment naar een gewogen besluit komt.",
                ]),
                ("Status en hoe verder", [
                    "Dit is een experiment, geen product. De roadmap beschrijft een trechter in plaats van een rechte lijn: eerst een demo, dan use cases ophalen en scoren, per use case een databron-check en een korte privacy- en beveiligingsscreening, en pas daarna een architectuurtoets, een businesscase en een go/no-go.",
                    "De volgende stap is het ophalen van echte use cases bij collega’s en het toetsen of de data ervoor bestaat.",
                ]),
            ],
            "stats": [],
        },
        "en": {
            "name": "Doorzicht",
            "shot_alt": "3D model of a fictional parking garage with levels, cars and alerts",
            "tagline": "See what is hidden: scattered information about a parking garage in one visual place, in 3D.",
            "card": "A 3D model of a fictional parking garage where dry, scattered information comes together and becomes something to talk about.",
            "status_label": "Experiment",
            "facts": [
                ("Status", "Experiment with fictional and open data"),
                ("Field", "Asset management, data-driven work"),
                ("Data", "Fictional and open data. The garage ‘Toppert’ and all figures are made up"),
                ("Built with", "Three.js, a single static page"),
            ],
            "sections": [
                ("Purpose", [
                    "Information about a parking garage sits in tables, reports and systems of different departments. Doorzicht puts it together in a 3D model, so you can look around and talk about what you see instead of about separate numbers.",
                ]),
                ("Why", [
                    "Many valuable questions fall between systems: what does occupancy say, what does maintenance say, what do complaints say, and how do they connect? A shared picture makes the conversation between roles easier. It is a way to discover which questions are worth pursuing before building anything big.",
                ]),
                ("Data", [
                    "Everything is fictional or open data. There is no real garage and no real data on citizens or companies was used.",
                ]),
                ("What you can do with it", [
                    "You can follow a tour per role and see which information matters for your job. The demo is meant for sessions where colleagues look together and say what they miss or do not need.",
                ]),
                ("For other organisations", [
                    "Any organisation with scattered information about a physical place, such as a building, a quay or a district, can use the same idea. The roadmap describes how to get from an experiment to a considered decision.",
                ]),
                ("Status and next steps", [
                    "This is an experiment, not a product. The roadmap describes a funnel rather than a straight line: first a demo, then collecting and scoring use cases, a data source check and a short privacy and security screening per use case, and only then an architecture review, a business case and a go/no-go.",
                    "The next step is collecting real use cases from colleagues and testing whether the data for them exists.",
                ]),
            ],
            "stats": [],
        },
    },
    {
        "slug": "bordenschouw",
        "featured": False,
        "status": "proto",
        "url": "https://roberr1990.github.io/bordenschouw/",
        "shot": "bordenschouw.jpg", "shot_w": 1440, "shot_h": 810,
        "code": "https://github.com/RoberR1990/bordenschouw",
        "nl": {
            "name": "Bordenschouw",
            "shot_alt": "Kaart van Rotterdam met voorbeeldborden als gekleurde punten",
            "tagline": "Alle verkeersborden in kaart: foto maken, AI laat het bord lezen, jij controleert.",
            "card": "Een prototype om verkeersborden vast te leggen vanaf een foto of tijdens een wandeling, met kaart, dashboard en export.",
            "status_label": "Prototype",
            "facts": [
                ("Status", "Prototype, alleen met testfoto’s"),
                ("Domein", "Beheer openbare ruimte, verkeersborden"),
                ("Data", "172 RVV-bordtekeningen als referentie. De 70 borden in de demo zijn voorbeelden"),
                ("Gebouwd met", "Eén statische pagina, Google Gemini met eigen sleutel voor herkenning"),
            ],
            "sections": [
                ("Doel", [
                    "Een bord schouwen betekent: welk bord staat waar, in welke staat en met welke tekst. Bordenschouw maakt dat vastleggen snel. Je maakt een foto, snijdt het bord uit, de AI stelt bordsoort, staat, tekst, tarief en tijden voor, en jij bevestigt.",
                    "Plek en richting komen uit live GPS en kompas tijdens een ronde, of uit de foto zelf. Er is ook een loopmodus waarin de app zelf foto’s maakt terwijl je loopt.",
                ]),
                ("Waarom", [
                    "Een actueel overzicht van borden is lastig te krijgen en kost veel handwerk. Ik wilde onderzoeken hoever je komt met een telefoon, een foto en AI-herkenning, en waar een mens nog nodig blijft.",
                ]),
                ("Data", [
                    "De app kent 172 RVV-bordtekeningen als referentie. De borden op de kaart en het dashboard zijn voorbeelddata. Foto’s blijven op je toestel. Alleen de uitsnede van het bord gaat naar de AI, en de app waarschuwt als er mensen of kentekens in beeld lijken te staan.",
                ]),
                ("Wat kun je ermee", [
                    "Borden vastleggen, ze op een kaart zien, een dashboard met de staat per bordsoort en per gebied, en een export als CSV of GeoJSON. Signalen, zoals een bord dat beplakt of verbleekt is, vallen meteen op.",
                ]),
                ("Voor andere organisaties", [
                    "Dezelfde aanpak past bij elke organisatie die dingen in de openbare ruimte moet inventariseren of controleren, zoals borden, meubilair of markeringen. De export maakt het mogelijk om het resultaat in bestaande systemen te laden.",
                ]),
                ("Status en hoe verder", [
                    "Dit is een prototype. Gebruik het voorlopig alleen met testfoto’s. De gebieden op de kaart zijn schematisch, niet officieel.",
                    "Voor verder gebruik zijn nodig: een toets op privacy en beveiliging, een keuze voor een AI-dienst die past bij de afspraken van de organisatie, en een koppeling met de bestaande bordenregistratie.",
                ]),
            ],
            "stats": [],
        },
        "en": {
            "name": "Bordenschouw",
            "shot_alt": "Map of Rotterdam with example signs as coloured points",
            "tagline": "Map every traffic sign: take a photo, AI reads the sign, you check it.",
            "card": "A prototype for capturing traffic signs from a photo or during a walk, with map, dashboard and export.",
            "status_label": "Prototype",
            "facts": [
                ("Status", "Prototype, test photos only"),
                ("Field", "Public space management, traffic signs"),
                ("Data", "172 Dutch traffic sign drawings as reference. The 70 signs in the demo are examples"),
                ("Built with", "A single static page, Google Gemini with your own key for recognition"),
            ],
            "sections": [
                ("Purpose", [
                    "Inspecting a sign means recording which sign is where, in what condition and with what text. Bordenschouw makes that quick. You take a photo, crop the sign, the AI proposes the sign type, condition, text, rate and hours, and you confirm.",
                    "Location and direction come from live GPS and compass during a round, or from the photo itself. There is also a walking mode in which the app takes photos by itself while you walk.",
                ]),
                ("Why", [
                    "An up-to-date overview of signs is hard to get and takes a lot of manual work. I wanted to find out how far you get with a phone, a photo and AI recognition, and where a human is still needed.",
                ]),
                ("Data", [
                    "The app knows 172 Dutch traffic sign drawings as reference. The signs on the map and dashboard are example data. Photos stay on your device. Only the crop of the sign goes to the AI, and the app warns when people or number plates seem to be in view.",
                ]),
                ("What you can do with it", [
                    "Capture signs, see them on a map, view a dashboard with condition per sign type and per area, and export as CSV or GeoJSON. Signals, such as a sign that is plastered over or faded, stand out right away.",
                ]),
                ("For other organisations", [
                    "The same approach suits any organisation that has to inventory or inspect things in public space, such as signs, street furniture or markings. The export makes it possible to load the result into existing systems.",
                ]),
                ("Status and next steps", [
                    "This is a prototype. For now use it only with test photos. The areas on the map are schematic, not official.",
                    "Further use needs a privacy and security review, a choice of AI service that fits the organisation’s rules, and a link with the existing sign register.",
                ]),
            ],
            "stats": [],
        },
    },
]

# ---------------------------------------------------------------- pagina's

UI = {
    "nl": {
        "lang": "nl",
        "title_home": "Robert Riteco",
        "desc_home": "Robert Riteco bouwt met AI tools voor de publieke zaak, deelt wat werkt en zoekt mensen om mee samen te werken.",
        "nav": {"projects": "Projecten", "collab": "Samenwerken", "thoughts": "Gedachten"},
        "paths": {"projects": "/projecten/", "collab": "/samenwerken/", "thoughts": "/gedachten/", "home": "/"},
        "other_lang": "EN",
        "hero_h1": "Data en AI, samengebracht in slimme tools die werken.",
        "hero_lead": "Ik ben Robert Riteco en werk op de kruising van data en AI. Ik bouw tools die echt bruikbaar zijn, zoals Raadzoeker, en deel wat ik daarvan leer. Wil je iets uitproberen, hergebruiken of samen bouwen? Laat het me weten.",
        "hero_btn1": "Bekijk de projecten",
        "hero_btn2": "Samenwerken",
        "vibe_note": "Ik bouw met AI-hulp (vibecoding): software maken door in gewone taal samen te werken met een AI.",
        "venn_alt": "Twee elkaar overlappende cirkels: data en AI. Waar ze overlappen staan tools.",
        "venn_data": "Data", "venn_ai": "AI", "venn_tools": "Tools",
        "featured": "Uitgelicht",
        "view_project": "Bekijk het project",
        "open_live": "Open Raadzoeker",
        "more_projects": "Meer projecten",
        "all_projects": "Alle projecten",
        "about_h": "Over mij",
        "about": [
            "Ik ben productmanager data bij de gemeente Rotterdam. Mijn werk en mijn eigen projecten draaien om dezelfde vraag: hoe maak je data en AI praktisch bruikbaar? Ik bouw zelf, probeer uit met echte open data en deel wat wel en niet werkt.",
            "Wat ik hier deel is mijn eigen werk en mijn eigen kijk. Niets hiervan is een standpunt of product van mijn werkgever, tenzij dat er uitdrukkelijk bij staat.",
        ],
        "collab_h": "Samenwerken",
        "collab_teaser": "Ik zoek geen opdrachten maar mensen om mee te bouwen, te leren en te delen. Een idee uitproberen, een project van mij hergebruiken of gewoon ervaringen uitwisselen over AI in het werk.",
        "collab_link": "Hoe ik graag samenwerk",
        "thoughts_h": "Gedachten",
        "thoughts_teaser": "Korte stukken over hoe AI werk en samenleving verandert, vanuit wat ik zelf bouw en meemaak.",
        "thoughts_link": "Lees verder",
        "projects_h": "Projecten",
        "projects_intro": "Elk project heeft dezelfde opbouw: doel, waarom, data, wat je ermee kunt, wat het voor andere organisaties kan betekenen en wat de status is.",
        "status": "Status",
        "live": "Live", "proto": "Prototype", "exp": "Experiment",
        "open_site": "Open het project",
        "open_code": "Bekijk de code",
        "back": "Alle projecten",
        "facts_h": "In het kort",
        "collab_page_h": "Samenwerken",
        "collab_page_lead": "Ik ben op zoek naar mensen om dingen mee te bouwen, uit te proberen en van te leren. Het hoeft niet betaald te zijn en het hoeft niet groot.",
        "collab_list_h": "Waar ik zin in heb",
        "collab_items": [
            ("Een idee samen uitproberen.", "Heb je een probleem of een idee in je werk waar open data of AI mogelijk iets mee kan? Dan bouwen we in een paar dagen een eerste versie en kijken we wat er echt in zit."),
            ("Een project van mij hergebruiken.", "Raadzoeker is open source. Wil je dezelfde aanpak voor een andere gemeente, griffie of organisatie proberen? Ik denk graag mee en help je op weg."),
            ("Ervaringen uitwisselen.", "Werk je met AI in een gemeente of andere overheidsorganisatie en loop je tegen vragen aan over privacy, inkoop of beheer? Ik leer graag van jouw ervaring en deel de mijne."),
            ("Feedback op mijn werk.", "Zie je iets wat niet klopt of beter kan in een van mijn projecten? Dat helpt me meer dan een compliment."),
        ],
        "collab_how_h": "Hoe neem je contact op",
        "collab_how": "Stuur een kort bericht met drie zinnen: wie je bent, waar je mee bezig bent en wat je denkt dat we samen kunnen doen. Ik reageer meestal binnen een paar dagen.",
        "contact_email": "E-mail",
        "contact_linkedin": "LinkedIn",
        "contact_todo": "Contactgegevens nog invullen in content.py",
        "thoughts_page_h": "Gedachten",
        "thoughts_page_lead": "Hier komen korte stukken over hoe AI het werk en de samenleving verandert, vanuit wat ik zelf bouw en meemaak.",
        "thoughts_empty": "Het eerste stuk is in de maak. Wil je een melding als het er staat? Volg me op LinkedIn.",
        "thoughts_topics_h": "Waar ik over wil schrijven",
        "thoughts_topics": [
            "Wat vibecoding betekent voor wie nooit programmeur was",
            "Wat overheden kunnen leren van wat één persoon in een paar weken bouwt",
            "Waar AI in publiek werk wel en niet te vertrouwen is, en hoe je dat controleert",
            "Hoe je open data echt bruikbaar maakt",
        ],
        "footer_made": "Gemaakt door Robert Riteco, met hulp van AI.",
        "footer_unofficial": "Eigen werk en eigen mening, geen standpunt van mijn werkgever.",
        "footer_code": "Broncode van deze site",
        "skip": "Naar de inhoud",
    },
    "en": {
        "lang": "en",
        "title_home": "Robert Riteco",
        "desc_home": "Robert Riteco builds tools for the public good with AI, shares what works and looks for people to collaborate with.",
        "nav": {"projects": "Projects", "collab": "Collaborate", "thoughts": "Thoughts"},
        "paths": {"projects": "/en/projects/", "collab": "/en/collaborate/", "thoughts": "/en/thoughts/", "home": "/en/"},
        "other_lang": "NL",
        "hero_h1": "Data and AI, brought together in smart tools that work.",
        "hero_lead": "I am Robert Riteco and I work at the crossing of data and AI. I build tools that are genuinely useful, like Raadzoeker, and share what I learn. Want to try something out, reuse it or build it together? Get in touch.",
        "hero_btn1": "See the projects",
        "hero_btn2": "Collaborate",
        "vibe_note": "I build with AI assistance (vibe coding): making software by working with an AI in plain language.",
        "venn_alt": "Two overlapping circles: data and AI. Where they overlap are tools.",
        "venn_data": "Data", "venn_ai": "AI", "venn_tools": "Tools",
        "featured": "Featured",
        "view_project": "View the project",
        "open_live": "Open Raadzoeker",
        "more_projects": "More projects",
        "all_projects": "All projects",
        "about_h": "About me",
        "about": [
            "I am a data product manager at the city of Rotterdam. My work and my own projects revolve around the same question: how do you make data and AI practically useful? I build myself, try things out with real open data and share what does and does not work.",
            "What I share here is my own work and my own view. None of it is a position or product of my employer unless it explicitly says so.",
        ],
        "collab_h": "Collaborate",
        "collab_teaser": "I am not looking for assignments but for people to build, learn and share with. Trying out an idea, reusing one of my projects or just exchanging experiences with AI at work.",
        "collab_link": "How I like to collaborate",
        "thoughts_h": "Thoughts",
        "thoughts_teaser": "Short pieces on how AI changes work and society, based on what I build and experience myself.",
        "thoughts_link": "Read more",
        "projects_h": "Projects",
        "projects_intro": "Every project has the same structure: purpose, why, data, what you can do with it, what it can mean for other organisations and its status.",
        "status": "Status",
        "live": "Live", "proto": "Prototype", "exp": "Experiment",
        "open_site": "Open the project",
        "open_code": "View the code",
        "back": "All projects",
        "facts_h": "At a glance",
        "collab_page_h": "Collaborate",
        "collab_page_lead": "I am looking for people to build things with, try things with and learn from. It does not have to be paid and it does not have to be big.",
        "collab_list_h": "What I would enjoy",
        "collab_items": [
            ("Trying out an idea together.", "Do you have a problem or an idea at work where open data or AI might help? We build a first version in a few days and see what is really in it."),
            ("Reusing one of my projects.", "Raadzoeker is open source. Want to try the same approach for another municipality, clerk's office or organisation? I am happy to think along and help you get started."),
            ("Exchanging experiences.", "Do you work with AI in a municipality or another public organisation and run into questions about privacy, procurement or maintenance? I like to learn from your experience and share mine."),
            ("Feedback on my work.", "Do you see something wrong or something that could be better in one of my projects? That helps me more than a compliment."),
        ],
        "collab_how_h": "How to get in touch",
        "collab_how": "Send a short message of three sentences: who you are, what you are working on and what you think we could do together. I usually reply within a few days.",
        "contact_email": "Email",
        "contact_linkedin": "LinkedIn",
        "contact_todo": "Fill in contact details in content.py",
        "thoughts_page_h": "Thoughts",
        "thoughts_page_lead": "Short pieces on how AI changes work and society, based on what I build and experience myself.",
        "thoughts_empty": "The first piece is in the making. Want a heads-up when it is out? Follow me on LinkedIn.",
        "thoughts_topics_h": "What I want to write about",
        "thoughts_topics": [
            "What vibe coding means for people who were never programmers",
            "What governments can learn from what one person builds in a few weeks",
            "Where AI can and cannot be trusted in public work, and how you check",
            "How to make open data truly usable",
        ],
        "footer_made": "Made by Robert Riteco, with the help of AI.",
        "footer_unofficial": "My own work and opinion, not a position of my employer.",
        "footer_code": "Source code of this site",
        "skip": "Skip to content",
    },
}
