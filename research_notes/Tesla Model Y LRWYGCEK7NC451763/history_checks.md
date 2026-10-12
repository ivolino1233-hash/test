# History, lien and theft checks for this VIN

Method note: researched 2026-10-12. WebFetch and curl could not reach any site from this environment (DNS failure on every host, including tesla.com, NHTSA, autoDNA and carVertical), so **every fact below comes from search-engine results and snippets, not from pages I opened**. Second research pass; the first pass ran out of shared search budget, so this pass re-checked or replaced its claims. Searches used: 22.

## Takeaway

I used all 22 searches in my cap. Official pages could not be fetched, so every verified fact below comes from search-result snippets from news sites, vendors and secondary sites, not from the official portals. The most useful result for a buyer in Romania is RAR's own two services, both searchable by VIN. The first is the free 'Istoric vehicul' service at rarom.ro: you enter an email and the VIN and get back a code. It returns RAR activity, recorded odometer readings, ITP (Romanian roadworthiness inspection) validity, pollution class and some technical data, but only if the car has passed through RAR at least once. The second is the paid 'RAR Auto-Pass' certificate, issued online only since 1 Dec 2024. It costs 42 lei (earlier reports said about 50 lei) and is valid 60 days. It lists odometer values, the date and nature of accidents, serious damage to the braking or steering systems, maintenance, repair and software work, and recall campaigns. If RAR holds no record for the VIN, it issues a free 'no record' certificate. Romanian press reports that sellers of used cars must present the Auto-Pass. Round 1 was wrong on one major point: the AEGRM pledge archive was replaced by the RNPM (Registrul Național de Publicitate Mobiliară) after Law 297/2018. The RNPM is now the register to check for leasing, pledge and seizure entries on a Romanian car, but its search fee and whether the public can search it online by VIN were not found. Romania's RCA (compulsory motor liability insurance) check is free on the AIDA platform, which one source says BAAR runs. You can search by plate or VIN, and it shows the insurer, policy number, validity and expiry, but no claims history. The Romanian Police site has an 'Autovehicule furate' (stolen vehicles) section, but I could not confirm its URL. Vincario (vincario.com/stolen-vehicle-check) offers a free stolen check by VIN with no registration needed. It covers the national police databases of Romania, Czechia, Hungary, Slovakia, Slovenia and Italy, but not Bulgaria or Germany. Since a 2023 government decision, Romania will not register any vehicle reported stolen in Romania or abroad. For multi-country history, autoDNA charges €24.99 for a full report. Its free preview shows which kinds of data exist, and the full report can show the dates and countries of earlier registrations, stolen-database hits, odometer readings and damage. carVertical's single-report price was not found. Its 10-report business bundle is $15 per report, described as a 57% saving, which implies roughly $35 for one report (my inference). EUCARIS and SIS are open to authorities only. I found no source confirming a public Bulgarian online wanted-vehicle check by VIN at MVR, nor the operator, URL or fee for ЦРОЗ (the Bulgarian special pledges register). The Bulgarian Guarantee Fund's MTPL (third-party liability) check is free online according to a secondary document. No free source reliably gives the first-registration date and country from a VIN. Field B of the registration certificate, a RAR check for a car registered in Romania, or a paid autoDNA or carVertical report are the practical routes. I found no official Tesla procedure for a buyer to get a previous owner's service history, so seeing it live in the seller's Tesla app remains the practical approach, and that is unverified.

## Cited findings

### 1. Romania – RAR 'Istoric vehicul' (free) (medium confidence, sourced in this pass)

RAR runs a free online 'Istoric vehicul' service at rarom.ro. You enter an email address and the VIN (serie caroserie/șasiu), receive an access code by email, and the results arrive by email after validation. It covers RAR activity, recorded mileage, validity of the identity document, some technical data, the pollution level and ITP validity. It only works if the vehicle has passed through RAR at least once (for example an ITP, registration homologation or RAR inspection).

- **This car:** Input is the VIN only, so run it straight away with LRWYGCEK7NC451763. An empty result is itself informative: the car has probably never been registered or inspected in Romania, which points to it being a recent import. This is snippet-level evidence; the official rarom.ro page was not retrieved.
- **Sources:** [alba24.ro](https://alba24.ro/istoric-vehicul-rar-a-lansat-aplicatia-online-prin-care-se-poate-verifica-numarul-de-kilometri-al-masinilor-702900.html), [economedia.ro](https://economedia.ro/?p=152498)

### 2. Romania – RAR Auto-Pass certificate (paid) (medium confidence, sourced in this pass)

RAR began issuing the 'RAR Auto-Pass' certificate on 1 December 2024. It is digital and can only be requested online, using the VIN and some applicant details, without bringing the car. Most sources give the fee as 42 lei; earlier 2024 coverage said about 50 lei. The certificate is valid 60 days. It lists odometer values, the VIN, the date and nature of road accidents, serious damage to braking or steering systems, work done (maintenance, repair, software updates) and manufacturer recall campaigns. If RAR holds no record for a VIN, it issues a free certificate saying so. A RAR representative warned that the certificate does not rule out later tampering.

- **This car:** This is the best value-for-money check if the car is or was registered in Romania: about 42 lei, by VIN. A 2022 car registered in Romania from new should have at least one ITP odometer reading on file. If the car is a fresh import from Germany or Finland, expect a free 'no record' certificate. Whether Tesla service centre work in Romania feeds into Auto-Pass was not confirmed.
- **Sources:** [economica.net](https://www.economica.net/registrul-auto-roman-va-emite-de-la-1-decembrie-2024-certificatul-rar-auto-pass_723849.html), [alba24.ro](https://alba24.ro/registrul-auto-roman-emite-online-certificatul-pentru-istoricul-masinilor-ce-date-contine-si-cat-costa-1058797.html), [digi24.ro](https://www.digi24.ro/stiri/actualitate/social/cum-verifici-istoricul-real-al-unei-masini-second-hand-cat-costa-documentul-care-poate-arata-daca-are-kilometrajul-modificat-3760193), [newsweek.ro](https://newsweek.ro/auto/veste-proasta-pentru-samsarii-de-masini-din-decembrie-rar-le-a-pragatit-o-surpriza-costa-50-lei)

### 3. Romania – seller obligation to present Auto-Pass (low confidence, sourced in this pass)

Romanian press (Digi24, StartupCafe) reports that people selling second-hand cars in Romania are required to present the RAR Auto-Pass certificate.

- **This car:** If the seller is in Romania, ask for a current (under 60 days old) Auto-Pass certificate for this VIN. The legal basis, its start date and the penalty for not providing it were not confirmed; the evidence is two press snippets.
- **Sources:** [digi24.ro](https://www.digi24.ro/stiri/actualitate/social/cum-verifici-istoricul-real-al-unei-masini-second-hand-cat-costa-documentul-care-poate-arata-daca-are-kilometrajul-modificat-3760193), [startupcafe.ro](https://startupcafe.ro/regula-romani-masini-sh-certificat-rar-auto-pass-obligatoriu-htm-29474)

### 4. Romania – Autovit RAR data check (medium confidence, sourced in this pass)

Autovit.ro added a free check against the RAR database to its listings. It verifies 9 fields: chassis serial, make, model, engine power, cylinder capacity, fuel type, year of manufacture, country of registration and ITP validity.

- **This car:** If this car is listed on autovit.ro, look for the RAR-verified badge or data on the listing. It may show the country of registration. This only works for cars listed on Autovit.
- **Sources:** [revistabiz.ro](https://www.revistabiz.ro/nu-se-mai-poate-da-kilometrajul-inapoi-autovit-a-implementat-verificarea-masinilor-la-rar/)

### 5. Romania – lien/pledge register: AEGRM replaced by RNPM (medium confidence, sourced in this pass)

The AEGRM (Arhiva Electronică de Garanții Reale Mobiliare) has been modernised and renamed the RNPM (Registrul Național de Publicitate Mobiliară). Law 297/2018 repealed OG 89/2000, which governed AEGRM registrations. The RNPM is a national public electronic register under Ministry of Justice supervision. It records chattel mortgages (ipoteci mobiliare), pledges, guarantee notices and seizures (sechestre) on movable goods, and cars are among the items most often registered. Entries take effect against third parties. The search fee and whether a public online search by VIN exists were NOT found.

- **This car:** If the car is registered in Romania, search the RNPM, not 'AEGRM', for pledges, leasing notices or seizures before paying. A notary or an RNPM operator can run the search. Also check the owner field on the CIV/talon, since a leasing company is listed as owner under leasing. The fee was not found.
- **Sources:** [infocontact.ro](https://www.infocontact.ro/cumparare-auto-sh-sechestru-gaj/), [legeaz.net](https://legeaz.net/noul-cod-civil/art-2413-arhiva-electronica-de-garantii-reale-mobiliare-ipoteca-mobiliara-ipoteca), [legeaz.net](https://legeaz.net/hg-802-1999-regulament-arhiva-electronica-aegrm/)

### 6. Romania – RCA (MTPL) validity check (medium confidence, sourced in this pass)

Romania has a free online RCA validity check on the AIDA database. You can search by plate number (entered without spaces, e.g. AB24CDE) or by VIN. Results show the validity period, insurer, policy number, expiry date and status, and you can choose a reference date. It shows no claims history. Very recent policies may take time to appear. One source says BAAR (the Romanian motor insurers' bureau) runs the platform; sources disagree on what the acronym stands for, and one calls the database CEDAM.

- **This car:** Run it with the VIN. A hit confirms the car is insured in Romania now and gives the policy dates, which hint at how long it has been on Romanian plates. It reveals no accidents. The exact official URL (aida.info.ro or similar) was not confirmed.
- **Sources:** [playtech.ro](https://playtech.ro/2026/verificarea-rca-online-in-2026-cum-afli-rapid-daca-o-masina-are-polita-valabila/), [alba24.ro](https://alba24.ro/verificare-rca-online-in-2026-cum-afli-rapid-daca-un-vehicul-are-asigurare-valabila-si-ce-informatii-sunt-necesare-1114712.html), [infocontact.ro](https://www.infocontact.ro/verificare-valabilitate-rca-baza-de-date-aida/)

### 7. Romania – police stolen-vehicle check (low confidence, sourced in this pass)

The Romanian Police website has an 'Autovehicule furate' (stolen vehicles) section, recommended as the first step before buying, followed by a check against European databases. The official page URL and its search fields were not retrieved.

- **This car:** Search the section on politiaromana.ro with the VIN. It covers Romanian theft reports only; theft reports from other countries live in SIS, which the public cannot search.
- **Sources:** [newsweek.ro](https://newsweek.ro/auto/foto-verificati-atent-masina-sh-inainte-de-achizitie-rar-a-descoperit-acte-si-serii-masluite)

### 8. Free multi-country stolen check – Vincario (medium confidence, sourced in this pass)

Vincario (Czech) runs a 'Free Vehicle Stolen Check' at vincario.com/stolen-vehicle-check. Input is the 17-character VIN, and Romanian press says no registration is needed. It checks the national police databases of Romania, Czechia, Hungary, Slovenia, Slovakia and Italy, plus Vincario's own stolen-vehicle database. Some integration pages also list Lithuania.

- **This car:** A free, quick check that covers Romania's police database. It does NOT cover Bulgaria, Germany or Finland (where neighbouring VINs were first registered), so a clean result is only partial assurance.
- **Sources:** [vincario.com](https://vincario.com/stolen-vehicle-check/), [economica.net](https://www.economica.net/?p=924973), [wall-street.ro](https://www.wall-street.ro/articol/auto/romania-unul-dintre-cei-mai-mari-importatori-de-vehicule-second-hand-din-ue.html), [newsweek.ro](https://newsweek.ro/economie/romania-ramane-unul-dintre-cei-mai-mari-importatori-masini-second-hand-ue)

### 9. Romania – stolen vehicles cannot be registered (2023 rule) (medium confidence, sourced in this pass)

A 2023 Romanian government decision provides that vehicles reported stolen in Romania or abroad, or wanted by Romanian or foreign authorities, are not registered. Previously the ban applied only when the car was flagged both in Romania and abroad. The registration authority checks through national, European and international channels.

- **This car:** If the car already carries Romanian plates, it passed a theft check at registration, which is some reassurance but not proof against a later report. The same kind of check will happen when you register it in Bulgaria.
- **Sources:** [playtech.ro](https://playtech.ro/2023/se-schimba-modalitatea-de-inmatriculare-a-masinilor-ce-trebuie-sa-stie-soferii-din-romania/)

### 10. autoDNA (medium confidence, sourced in this pass)

autoDNA's free VIN check shows which types of data exist for the VIN before you pay. A full report costs €24.99 according to a vendor review page and a Trustpilot reviewer. It draws on records from 26+ European countries plus the US and Canada. It can show stolen-database presence, earlier odometer readings, recorded damage, and the dates and countries of previous registrations. A 2021 Romanian article gave a report price from 36.50 lei; that figure is outdated.

- **This car:** Run the free preview first. If it shows registration records, the paid report may answer the key unknowns for this car: the first-registration date (which sets the warranty start) and the country (EU-built or China-built, and import route). The price came from secondary pages, so confirm it at checkout on autodna.ro or autodna.com.
- **Sources:** [carcheckervin.com](https://www.carcheckervin.com/autodna-review), [fi.trustpilot.com](https://fi.trustpilot.com/review/autodna.com), [wall-street.ro](https://www.wall-street.ro/articol/Social/219238/autodna-masini-second-hand-verificare-istoric-vin-razvan-pavel.html), [automoli.com](https://www.automoli.com/ro/blog/cumparati-informat-o-masina-de-ocazie-cereti-online-un-raport-vin-cu-istoricul-ei-complet)

### 11. carVertical (low confidence, NOT re-verified)

The single-report price for consumers was NOT found. carVertical's business page lists bundles: 10 reports at $15 each (described as 'save 57%'), 30 at $12 each and 100 at $11 each. The 57% saving implies a single-report list price of about $35; that figure is my inference, not a published price. carVertical says it collects data from over 1,000 databases worldwide. Its help page describes what a report may contain, but per-country data sources for RO/BG/DE were not retrieved. A 2026 transparency index reported in Romanian media ranks Romania 22nd of 25 countries for vehicle-history data transparency, because of a data gap on imported cars.

- **This car:** Input is the VIN. Use it as a cross-check with autoDNA. Romanian coverage may be thin, and a report with 'no records' is not proof of a clean history. The exact price must be read from carvertical.com/pricing at checkout.
- **Sources:** [carvertical.com](https://www.carvertical.com/us/business), [carvertical.com](https://www.carvertical.com/pricing), [carvertical.com](https://www.carvertical.com/en/help/pricing/what-information-may-appear-in-the-carvertical-report), [tvrinfo.ro](https://tvrinfo.ro/romania-ocupa-locul-22-din-25-de-tari-in-privinta-transparentei-datelor-legate-de-istoricul-autovehiculelor-second-hand-importate/)

### 12. EUCARIS (high confidence, sourced in this pass)

EUCARIS is a treaty-based exchange of vehicle and driving-licence data between national registration authorities and enforcement bodies. One of its stated uses is letting a registration office find out whether a vehicle is recorded as stolen abroad. It also has a 'Mileage' registration and exchange application. No source shows that private buyers can query it.

- **This car:** Not usable by the buyer directly. KAT in Bulgaria (or the Romanian registration office) will use it, and SIS and other channels, when registering the car.
- **Sources:** [en.wikipedia.org](https://en.wikipedia.org/wiki/EUCARIS), [eucaris.net](https://www.eucaris.net/general-information/legal-basis/), [m.likumi.lv](https://m.likumi.lv/ta/id/61514-treaty-concerning-a-european-vehicle-and-driving-licence-information-system-eucaris)

### 13. EU SIS / no single public European stolen register (medium confidence, sourced in this pass)

There is no single European register a private buyer can query to settle whether a car is stolen. Registration authorities check foreign theft status through official channels (EUCARIS, SIS).

- **This car:** Combine the national police checks, Vincario and autoDNA, and protect yourself contractually: pay by traceable bank transfer, and have the contract hold the seller liable if a theft flag or lien surfaces at KAT registration.
- **Sources:** [automoli.com](https://www.automoli.com/bg/blog/avtomobilni-saveti), [en.wikipedia.org](https://en.wikipedia.org/wiki/EUCARIS)

### 14. Bulgaria – Guarantee Fund MTPL check (low confidence, sourced in this pass)

The Bulgarian Guarantee Fund (Гаранционен фонд) offers a free online check of whether a vehicle has valid 'Гражданска отговорност' (MTPL) insurance. This comes from a secondary document; the official page, its URL and its search fields (plate or frame number) were not retrieved. An FSC draft regulation provides for data exchange between the Fund and MVR so that registrations can be restored once MTPL is taken out.

- **This car:** Only relevant if the car is or was registered in Bulgaria. It will show nothing for a car insured in Romania. Use it after registration to confirm your own policy appears.
- **Sources:** [calameo.com](https://www.calameo.com/books/008183684faf02a54add0), [fsc.bg](https://www.fsc.bg/wp-content/uploads/2026/07/spravka-obsthestveni-konsultaczii-nid-49-final.pdf)

### 15. Bulgaria – MVR/KAT wanted-vehicle check (low confidence, NOT re-verified)

No source found for a public online МВР/e-uslugi service that checks whether a vehicle is wanted or stolen by VIN or frame number. The only MVR document found concerns restoring a vehicle identification number through the regional directorate and the 'Пътна полиция' (traffic police) unit, which suggests such matters go through the police in person. Round-1's claim that e-uslugi offers a wanted-vehicle check by plate or VIN is UNSUPPORTED.

- **This car:** Do not count on a Bulgarian online stolen check. In practice KAT checks at first registration. Ask a Bulgarian notary or KAT whether a pre-purchase inquiry is possible.
- **Sources:** [mvr.bg](https://www.mvr.bg/upload/16387/454-recovery-of-vehicle-identification-number_fixed.doc)

### 16. Bulgaria – ЦРОЗ (Central Register of Special Pledges) (low confidence, NOT re-verified)

NOT FOUND. No search returned an official or secondary Bulgarian page giving ЦРОЗ's current operator (Ministry of Justice or Registry Agency), its URL, its search fee, or whether vehicle searches by frame number are possible.

- **This car:** Only relevant if the car was ever owned or financed in Bulgaria. For a car registered in Romania, the RNPM (Romania) is the relevant lien register.
- **Sources:** none (reasoning or local calculation)

### 17. Tesla service history (low confidence, NOT re-verified)

I found no official Tesla procedure for a prospective buyer to get a previous owner's service records. One secondary guide says service history is visible in the owner's Tesla app. A UK firm, VehicleScore, claims to pull Tesla service history by VIN for UK cars; these are unverified UK-only claims.

- **This car:** Practical route (not verified): ask the seller to show the service history, warranty and recall screens live in the Tesla app for this VIN. Then ask Tesla Service (Romania, or Bulgaria via Tesla BGR if it has started operating) to confirm warranty status, the delivery date and open recalls by VIN.
- **Sources:** [csp7.commcom.com.au](https://csp7.commcom.com.au/astro-station/used-tesla-2nd-hand-2025-guide-1770907013), [vehiclescore.co.uk](https://vehiclescore.co.uk/en-US/service-history-check/tesla/model-y)

### 18. First-registration date/country from VIN – free sources (medium confidence, sourced in this pass)

No free online source reliably gives the first-registration date and country from a VIN. Free national checks usually show only current status or basic inspection records. The first-registration date is printed in field B of the EU-format registration certificate. A paid autoDNA report can list the dates and countries of previous registrations. In Romania, the free RAR 'Istoric vehicul' service or Autovit's RAR check can show RAR data, including country of registration on Autovit, for cars RAR has seen.

- **This car:** Ask the seller for the registration certificate (CIV/talon or the foreign one) and read field B. That date starts the 4-year/80,000 km basic warranty and the 8-year battery warranty. Cross-check it with the autoDNA preview or report.
- **Sources:** [wheelstreet.lt](https://www.wheelstreet.lt/en/straipsniai/vin-patikra-gidas), [fiatforum.com](https://fiatforum.com/threads/vin-number-checker.512967/latest), [carcheckervin.com](https://www.carcheckervin.com/autodna-review), [revistabiz.ro](https://www.revistabiz.ro/nu-se-mai-poate-da-kilometrajul-inapoi-autovit-a-implementat-verificarea-masinilor-la-rar/)

## Corrections to the first pass

- AEGRM: round 1 said to search 'AEGRM (aegrm.ro)'. Correction: the AEGRM was modernised and renamed the RNPM (Registrul Național de Publicitate Mobiliară), and Law 297/2018 repealed OG 89/2000, which governed AEGRM registrations. Search the RNPM for pledges, leasing notices and seizures. The fee and whether it can be searched online by VIN were not found (infocontact.ro, legeaz.net).
- RAR Auto-Pass: round 1 said 'since about 2023' and called it an electronic file needing owner access. Correction: RAR has issued the 'RAR Auto-Pass' certificate since 1 Dec 2024. It is online only, requested by VIN with no owner account needed, costs 42 lei (early reports said about 50 lei), is valid 60 days, and is free when RAR has no record (economica.net, alba24.ro, digi24.ro).
- RAR free check: round 1 called it 'ITP validity and history' generically. Correction: the free service is 'Istoric vehicul' on rarom.ro. You give an email and the VIN, receive a code by email, and get results only if the car has passed through RAR at least once (alba24.ro).
- RCA check: round 1 named CEDAM/ASF with an unverified AIDA domain. Correction: sources describe a free check on the AIDA platform (one says BAAR runs it) by plate or VIN, showing insurer, policy number, validity and expiry. The official URL is still unconfirmed.
- Bulgaria MVR: round 1's claim that MVR e-uslugi offers a wanted or stolen vehicle check by plate or VIN is unsupported. No such public online service was found in this run.
- Bulgaria Guarantee Fund: round 1 gave guaranteefund.org and search by plate or VIN. A free online MTPL check is confirmed only by a secondary document; the domain and search fields remain unverified.
- ЦРОЗ: round 1 said it is run by the Ministry of Justice. This is unverified. No source found its current operator, URL or fee.
- carVertical: round 1 said roughly €20–35 per report. The single-report price was not found. Business bundles cost $11–15 per report, and the advertised 57% saving at $15 implies a list price of about $35 per report (inference only).
- autoDNA: round 1 said 'tens of euros'. More specifically, a full report is €24.99 (vendor review page and Trustpilot), and the free preview shows which kinds of data exist.
- Romanian stolen check: round 1 omitted that Vincario offers a free VIN stolen check covering Romanian police data (plus CZ, HU, SK, SI, IT), and that since 2023 Romania refuses to register vehicles reported stolen at home or abroad.

## Open questions

- What is carVertical's current single-report consumer price, and does it have Romanian and Bulgarian registry, ITP or insurance data for this VIN? Check the free preview at carvertical.com.
- What does an RNPM search cost, can a foreign private person search it online by VIN, and what is the exact URL (rnpm.ro)?
- What is the exact URL and search form of the Romanian Police 'Autovehicule furate' search, and does it accept the VIN?
- What is the official URL of the Romanian AIDA RCA check, and does BAAR or ASF operate it?
- Does Bulgaria's MVR offer any public pre-purchase wanted-vehicle check, or only checks at KAT registration?
- Who currently operates ЦРОЗ (Ministry of Justice or Registry Agency), and what are the URL and fee for a search by vehicle frame number?
- What is the Bulgarian Guarantee Fund's official MTPL check URL, and does it accept a VIN or only a plate?
- What is the legal basis and start date of the reported Romanian obligation for sellers to present RAR Auto-Pass?
- Does Tesla service work done in Romania (Voluntari service centre) feed into RAR Auto-Pass?
- Can a buyer get Tesla to confirm by VIN the delivery date, warranty start, open recalls and any salvage flag before purchase?
- Is this car currently registered in Romania? Running the free RAR 'Istoric vehicul' service and the AIDA RCA check by VIN would answer this at no cost.
