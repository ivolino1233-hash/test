# Reliability, battery health and pre-purchase inspection

Method note: researched 2026-10-12. WebFetch and curl could not reach any site from this environment (DNS failure on every host, including tesla.com, NHTSA, autoDNA and carVertical), so **every fact below comes from search-engine results and snippets, not from pages I opened**. Second research pass; the first pass ran out of shared search budget, so this pass re-checked or replaced its claims. Searches used: 25.

## Takeaway

I verified most of the round-1 claims and corrected several, using 25 of my 25 searches. TÜV Report 2026 (published 20 Nov 2025, HU data Jul 2024-Jun 2025) puts the Model Y last of 110 models in the 2-3-year class at 17.3% significant or dangerous defects, the worst figure in that class in ten years. The main defect areas were axle suspension, brake discs and lighting. In the same report the Model 3 was third-to-last at 2-3 years (13.1%) and third-to-last at 4-5 years (21.0%, at an average of about 86,000 km). The 2026 report has no 4-5-year figure for the Model Y. Going by the German 3-then-5-year HU cycle, the first such figure more likely appears in TÜV Report 2028 (about Nov 2027) than in 2027; this is my inference. The Model Y is absent from TÜV 2024 and 2025. The Model 3 was last in the youngest class in both (14.7% and 14.2%), and last at 4-5 years in 2025 (19.7%, per AutoScout24). ADAC breakdown data look benign: Model 3 at 0.7 per 1,000 in 2026, and Model Y at 0.9 in an earlier edition per Auto Bild. 12 V batteries caused 45.4% of all breakdowns in the 2026 edition. On the battery, the Croatian repair shop EV Clinic (29 Nov 2025) claims that the Nanjing-made LG NCM811 packs Tesla uses in Europe for Long Range (LR) and Performance cars, the pack this car most likely has, wear out around 240-250k km. It also says over 90% of the LG packs it receives cannot be repaired at cell level. These are unverified figures from one repair shop, which mainly sees cars that have already failed (selection bias). Fleet-style data show LG packs at about 91-92% after more than 100,000 km, and Tesla says Model 3/Y LR packs lose about 15% at 200,000 miles. Benchmarks: Aviloo found a Model Y median state of health (SoH) of 94.5% at 50,000 km and 90.3% at 150,000 km, with the LR 78.8 kWh losing 5.5% at 50,000 km. Geotab's 2025 average is 2.3% a year: 1.5% with little DC fast charging, up to 3.0% with heavy charging above 100 kW. One 2022 LG-pack Model Y LR measured 11.5% loss at about 155,000 km (Bjørn Nyland). So about 90-94% SoH is a fair expectation at 4 years and normal mileage, and below about 88% is a red flag (my estimate). The in-car Battery Health test needs an AC charger of at least 5 kW, a start below 20%, no active battery/thermal alerts and no pending software update, and can take up to 24 h. The known issues are mostly forum- or vendor-sourced: front upper control arm ball-joint creak (SB-20-31-006 covered only 2018-2020 builds; the 2025-26 bulletins are for the refreshed Model Y only), heat-pump/Octovalve failures in Nordic winters, and B-pillar camera condensation (I found no 'vented camera' fix). The liftgate water-ingress bulletin SB-23-10-003 lists Fremont and Austin builds only, not Shanghai. The 2021 China knuckle recall covered Shanghai Model Y built Feb-Oct 2021, not this Aug-2022 car. Tesla's EU warranty is 8 years/192,000 km with at least 70% capacity for the LR, and the basic warranty is 4 years/80,000 km. With a first registration around Sep 2022 the basic warranty has very likely just ended, so suspension, HVAC and camera repairs would be paid by the buyer. Tesla's schedule calls for cleaning and lubricating the calipers every year or 20,000 km on salted roads and a brake-fluid check every 4 years; ask for proof of both.

## Cited findings

### 1. TÜV Report 2026: Model Y, 2-3-year class (high confidence, sourced in this pass)

In TÜV Report 2026 (TÜV-Verband with AutoBild; published 20 Nov 2025; based on HU inspections Jul 2024-Jun 2025), the Tesla Model Y came last of 110 models in the 2-3-year class at 17.3% of cars with significant or dangerous defects. t3n calls it the worst result in this age class in ten years. Main defect areas were axle suspension, brake discs and lighting. The class winner was the Mazda 2 at 2.9%. The overall defect rate across all ages was 21.5% (+0.9 points). I found no average for the 2-3-year class.

- **This car:** Directly relevant to this model and cohort. TÜV does not split results by factory, so the cohort mixes Shanghai and Berlin builds. Suspension, brake discs and lighting should be the top inspection priorities.
- **Sources:** [mobiflip.de](https://www.mobiflip.de/tuev-report-2026-tesla-stuerzt-auf-letzten-platz/), [ecomento.de](https://ecomento.de/2025/11/20/tuev-report-2026-tesla-modelle-auf-letztem-und-drittletztem-platz-bei-juengeren-fahrzeugen/), [t3n.de](https://t3n.de/news/?p=1718129), [elektroauto-news.net](https://www.elektroauto-news.net/news/tuev-mehr-maengel-tesla-enttaeuscht), [telematik-markt.de](https://telematik-markt.de/sites/default/files/news/attachments/2025_TUEV-Verband_TUV-Report_2026_Praesentation.pdf), [tuv.com](https://www.tuv.com/content-media-files/master-content/press/images/2025_11/20251120_t%C3%BCv-rheinland_t%C3%BCv-report-2026_pressemitteilung_de-(1).pdf)

### 2. TÜV Report 2026: Model 3 figures, and no 4-5-year figure for Model Y (high confidence, sourced in this pass)

TÜV Report 2026 has no Model Y entry in the 4-5-year class. The sister Model 3 was third-to-last in both younger classes: 13.1% at 2-3 years, and 21.0% at 4-5 years (average about 86,000 km, between the BMW 2 Series Active Tourer at 20.6% and the BMW 5/6 Series at 21.5%). The TÜV-Verband press material says the Model 3 is among the worst three in both age classes.

- **This car:** This car is about 4 years old and falls in the 4-5-year bracket. The Model 3's 21.0% at about 86,000 km is the closest proxy for what a second inspection of this platform finds.
- **Sources:** [telematik-markt.de](https://telematik-markt.de/sites/default/files/news/attachments/2025_TUEV-Verband_TUV-Report_2026_Praesentation.pdf), [ecomento.de](https://ecomento.de/2025/11/20/tuev-report-2026-tesla-modelle-auf-letztem-und-drittletztem-platz-bei-juengeren-fahrzeugen/), [leadersnet.at](https://www.leadersnet.at/news/95079,diese-autos-haben-die-meisten-wenigsten-maengel.html)

### 3. When the first Model Y 4-5-year TÜV data will appear (inference) (medium confidence, NOT re-verified)

The TÜV 4-5-year class is the second HU at about 60 months. TÜV Report 2026 used data from Jul 2024 to Jun 2025, so each edition uses a July-June window. The earliest EU Model Ys (registered Aug 2021) only reach their 5-year HU from Aug 2026, which falls in the window for TÜV Report 2028 (Jul 2026-Jun 2027, published about Nov 2027). The 2027 edition (about Nov 2026) therefore probably still has no Model Y 4-5-year figure. This is my inference from the data window and the HU cycle, not a TÜV statement.

- **This car:** The buyer should not expect official 4-5-year Model Y defect data before deciding. Use the Model 3's 4-5-year figure (21.0%) as the proxy.
- **Sources:** [mobiflip.de](https://www.mobiflip.de/tuev-report-2026-tesla-stuerzt-auf-letzten-platz/)

### 4. TÜV Report 2025 (Model Y absent; Model 3 last) (medium confidence, sourced in this pass)

TÜV Report 2025 (published Nov 2024) does not list the Model Y. The Model 3 came last of 111 models in the 2-3-year class at 14.2%, and was reported last in the 4-5-year class too. AutoScout24 gives 19.7% as the worst Model 3 figure, but its age class is not clearly stated. TÜV-Verband head Joachim Bühler cited defects in brakes and axles plus particularly many lighting defects, and said this points to deficits in service and maintenance.

- **This car:** Indirect evidence from a model that shares most of its brake, suspension and lighting hardware. The 14.2% is firm; the 19.7% 4-5-year attribution is from snippets only.
- **Sources:** [t3n.de](https://t3n.de/news/tuev-report-tesla-faellt-oft-durch-die-gruende-1659766/), [autoscout24.de](https://www.autoscout24.de/informieren/news/tuev-report-2025-die-sieger-und-verlierer/), [blick.ch](https://www.blick.ch/auto/news_n_trends/trauriger-titelverteidiger-erneut-floppt-ein-tesla-im-deutschen-tuev-report-id20359913.html), [elektroauto-news.net](https://www.elektroauto-news.net/news/tuev-vw-e-golf-tesla-model-3)

### 5. TÜV Report 2024 (Model 3 last in its first appearance) (high confidence, sourced in this pass)

TÜV Report 2024 (about 10.2 million HUs, 221 models, six age classes for the first time) put the Model 3 last in the youngest class ('bis 3 Jahre') at 14.7%, replacing the Dacia Logan (11.4%) in last place. Main defects were axle suspension and brakes, plus lighting.

- **This car:** Indirect, but it shows the same platform defect pattern (brakes, suspension, lights) across three TÜV editions.
- **Sources:** [mobiflip.de](https://www.mobiflip.de/shortnews/tesla-versagt-im-tuev-report/), [giga.de](https://www.giga.de/news/dacia-schlagt-tesla-e-auto-hersteller-kassiert-herbe-tuev-niederlage/), [herthundbuss.com](https://herthundbuss.com/en/industry-more/the-tuev-report-2024/)

### 6. ADAC Pannenstatistik (medium confidence, sourced in this pass)

In ADAC Pannenstatistik 2026, 45.4% of all breakdowns came from a flat or faulty 12 V battery, and ADAC notes EVs are affected too. The Model 3 scored 0.7 breakdowns per 1,000 vehicles, second best behind the BMW i3 at 0.4. In the 2025 statistic the Model 3 was the best EV among 2-year-old cars (2021 registrations) at 0.5. Auto Bild reports a Model Y figure of 0.9; the edition and registration year are unclear. I found no Model Y figure for the 2022 registration year.

- **This car:** Breakdown risk looks low, which contrasts with the poor TÜV defect rates: the faults are wear items found at inspection, not breakdowns. The low-voltage battery is still the most likely no-start cause, so check for LV-battery alerts. The point that ADAC may undercount Tesla breakdowns because Tesla runs its own roadside assistance was not verified in this run.
- **Sources:** [auto-motor-und-sport.de](https://www.auto-motor-und-sport.de/verkehr/adac-pannenstatistik-2026-warum-ausgerechnet-toyota-schlecht-abschneidet/), [heidelberg24.de](https://www.heidelberg24.de/verbraucher/adac-pannenstatistik-2026-traditionsmarke-enttaeuscht-auf-ganzer-linie-zr-94275408.html), [utopia.de](https://utopia.de/ratgeber/neue-adac-pannenstatistik-2026-sind-e-autos-zuverlaessiger-als-verbrenner_932572/), [autobild.de](https://www.autobild.de/artikel/elektroautos-adac-pannenstatistik-21223871.html), [web.de](https://web.de/magazine/auto/adac-pannenstatistik-2025-zeigt-autos-zuverlaessigsten-40865544)

### 7. EV Clinic claims (Nov/Dec 2025) on LG NCM811 Nanjing packs (medium confidence, sourced in this pass)

EV Clinic, a Croatian independent repair shop, posted on X on 29 Nov 2025, with wide coverage in early December. Its claims: LG Energy Solution NCM811 packs made in Nanjing are used in Long Range and Performance Model 3/Y sold mainly in Europe and parts of Asia. Cell-level repair is impossible in over 90% of the LG cases it receives, and failures cascade. LG packs approach end of life at about 240-250k km (about 150k miles), against about 400k km for Panasonic NCA packs. New LG cells measure about 28 milliohms of internal resistance, against about 10 for Panasonic. EV Clinic now charges a 'repair viability assessment fee' for LG packs. I found no Tesla or LG response.

- **This car:** Probably in scope: round 1 places this car's pack as the LG 5L NCM pack from a Shanghai LR AWD build for Europe. The claimed failures are a high-mileage, end-of-life matter (240k km and up), mostly beyond typical 4-year mileage and the 192,000 km warranty. They matter more for someone keeping the car past about 2030 or 200k km.
- **Sources:** [insideevs.com](https://insideevs.com/news/780568/tesla-lg-battery-pack-defects-china/), [m.arenaev.com](https://m.arenaev.com/tesla_model_3_and_model_y_batteries_from_china_show_catastrophic_failure_risk-amp-5375.php), [notebookcheck.net](https://www.notebookcheck.net/Tesla-drivers-unsettled-LG-batteries-from-China-with-surprisingly-high-failure-rates.1176510.0.html), [electrive.com](https://www.electrive.com/2025/12/08/teslas-panasonic-batteries-reportedly-last-significantly-longer-than-lgs), [hdmotori.it](https://www.hdmotori.it/tesla-batterie-lg-panasonic-confronto-durata/), [clubalfa.it](https://www.clubalfa.it/en/tesla-faces-serious-reliability-problems-with-some-model-3-and-model-y-versions-29870)

### 8. Rebuttals and fleet data contradicting EV Clinic (medium confidence, sourced in this pass)

New Mobility News questions how representative EV Clinic's data are and points to the shop's opacity: a repair shop sees only failed packs, so its 90% is a share of its repair cases, not of the fleet. YouTuber 'Tesla Geek' does not dispute the individual failures but questions how far they generalise, citing owners' results from the in-car battery test. A fleet-style dataset reported by Drive Tesla Canada puts the Model Y LG Chem 78.8 kWh NMC pack at 92.18% average health past 62,000 miles. The same dataset gives the Model 3 LG Chem 91.5% against Panasonic 89.8%/88.2%. Another analysis reportedly found 6% loss for China-built LG packs against 11% for Fremont Panasonic packs. The datasets behind these comparisons are not well identified.

- **This car:** For a 4-year-old LG-pack Model Y, measured SoH matters more than the debate. Fleet data suggest LG packs age normally in capacity terms, but the EV Clinic claims about late, hard-to-repair failures are not disproved. Most of the fleet figures come from snippets only.
- **Sources:** [newmobility.news](https://newmobility.news/2025/12/02/how-credible-is-ev-clinics-warning-on-teslas-china-built-nmc-batteries/), [fiches-auto.fr](https://www.fiches-auto.fr/articles-auto/nouveautes-automobiles/s-3956-battery-gate-de-tesla-ev-clinic-vs-tesla-geek.php), [driveteslacanada.ca](https://driveteslacanada.ca/news/new-study-reveals-which-tesla-battery-holds-up-best-over-time/), [hibridosyelectricos.com](https://www.hibridosyelectricos.com/coches/este-experto-analiza-baterias-lg-panasonic-tesla-pone-fin-interesante-debate_83905_102.html)

### 9. Degradation benchmarks: Aviloo (high confidence, sourced in this pass)

Aviloo analysed over 500,000 SoH tests across 20 popular models. The Model Y median SoH is 94.5% at 50,000 km and 90.3% at 150,000 km, in the lower part of the field. The Model Y Long Range 78.8 kWh loses on average 5.5% at 50,000 km (about 379 km real-world range, about 20 km less than new). Individual cars vary by up to 11 SoH points, worth about 46 km of range.

- **This car:** This is the best mileage-based benchmark for this car. Interpolating, expect about 92-94% at about 80-100k km and about 90% at about 150k km. The data are not split by cell supplier.
- **Sources:** [transportandenergy.com](https://transportandenergy.com/?p=35198), [whichcar.com.au](https://www.whichcar.com.au/?p=705611), [auto-swiat.pl](https://www.auto-swiat.pl/porady/eksploatacja/jak-szybko-starzeja-sie-baterie-w-elektrykach-mamy-analize-500-tys-aut/zldtrvb)

### 10. Degradation benchmarks: Tesla Impact Report, Geotab, Nyland LG-pack Model Y (high confidence, sourced in this pass)

Tesla's 2023 Impact Report (published 2024) says Model 3/Y Long Range packs lose about 15% on average after 200,000 miles, against about 12% for S/X. Arenaev adds that about 68% of the fleet stays above 80% at that mileage. Geotab's 2025 study of more than 22,700 EVs across 21 models found 2.3% loss a year on average, up from about 1.8% in the 2023 update. The rate is 1.5% a year when DC fast charging is under 12% of sessions, 2.5% above that, and up to 3.0% when 40% or more of DC sessions are above 100 kW. Bjørn Nyland's test of a 2022 Model Y LR with an LG-made pack at about 155-160k km measured 11.5% degradation, against a typical 5-7% for Teslas of that age and mileage. The cause is unclear: only about a third of its charging was DC. InsideEVs notes the LG pack apparently struggles to accept the full 250 kW.

- **This car:** Geotab's average over about 4.1 years gives about 90-91%; with low DC fast-charging use, about 93-94%. Combined with Aviloo, a reasonable band is about 90-94% at normal mileage. Below about 88% at under 100k km is a red flag for heavy DC or fleet use or a weak pack (my threshold, not a published one). The Nyland car shows a 2022 LG-pack LR can sit about 11-12% down at about 155k km.
- **Sources:** [insideevs.com](https://insideevs.com/news/723734/tesla-model-3y-battery-capacity-degradation-200000miles/), [arenaev.com](https://www.arenaev.com/teslas_electric_cars_are_built_to_last_according_to_battery_degradation_data-news-3651.php), [electricautonomy.ca](https://electricautonomy.ca/ev-supply-chain/batteries/2026-01-13/latest-geotab-study-finds-ev-batteries-lose-just-2-3-life-per-year/), [geotab.com](https://www.geotab.com/blog/ev-battery-health/?mode=reply), [electricdrives.tv](https://electricdrives.tv/geotab-ev-battery-survey-shows-minimal-degradation-across-22700-evs/), [insideevs.com](https://insideevs.com/features/754691/tesla-model-y-degradation-test/), [rouleur-electrique.fr](https://rouleur-electrique.fr/degradation-de-la-batterie-tesla-model-y-apres-160-000-km-des-resultats-qui-remettent-en-question-la-durabilite/)

### 11. In-car Battery Health test: prerequisites and path (high confidence, sourced in this pass)

Tesla's Model Y owner's manual says the High Voltage Battery Health test needs an AC charger supplying at least 5 kW, the car in Park, no pending software update, no active battery or thermal alerts, and a battery level below 20%. It runs for up to 24 hours. The manual's path is Controls > Service > Battery Health Test. Tesla advises running it only if there is a concern about energy retention. Not a Tesla App says the test can also be run from Service Mode, with the result shown under High Voltage. It must be on AC, not a Supercharger. It estimates at least 12 h, and more than 48 h for a Long Range on low amperage. One TMC owner reported that a Service Mode run on a 10 kW charger took under 2 hours just to draw the charge down from 27%.

- **This car:** The seller has to run it, ideally overnight on a 3-phase 11 kW wallbox starting below 20%. Ask for a photo or video of the result screen with the VIN or odometer visible. If that is not possible, an Aviloo test is the independent alternative.
- **Sources:** [tesla.com](https://www.tesla.com/ownersmanual/modely/en_il/GUID-B9807218-7291-4F68-9AFF-7C525CF498F3.html), [notateslaapp.com](https://notateslaapp.com/news/2049/teslas-battery-health-test-see-your-battery-health-in-app-or-in-service-mode), [teslamotorsclub.com](https://teslamotorsclub.com/tmc/threads/battery-health-test-on-2023-my-lr.325993/)

### 12. Service Mode access and what to check (medium confidence, sourced in this pass)

To open Service Mode: Controls > Software, press and hold 'MODEL' under the car image for about 2 seconds, and type the access code 'service'. A red border and a red wrench app appear. Vehicle Info contains Service Alerts, Service Settings, Software Reinstall and a touchscreen check. Driver Assist > Cameras shows camera information including pitch. Many safety features are disabled in Service Mode, so do not drive in it. Exit with the red door icon (press and hold).

- **This car:** Use it at the viewing to read Service Alerts and camera status. Whether past (cleared) alerts are visible to the owner was not confirmed. The source is a single third-party site.
- **Sources:** [notateslaapp.com](https://www.notateslaapp.com/news/2046/tesla-service-mode-how-to-access-it-and-what-it-does)

### 13. Front upper control arms / ball joints (medium confidence, sourced in this pass)

Tesla bulletin SB-20-31-006 (Mobile Service campaign, all regions) resealed the front upper control arm ball joints on 2018-2020 Model 3/Y/X built before Tesla began sealing the part at the factory. The cause is moisture getting past the ball-joint seal, leading to corrosion and creaking. The arms have no grease fittings. Aftermarket vendor Dorman claims the front upper left arm on certain Model 3/Y can crack and separate from the steering knuckle (vendor marketing, unverified). The newer bulletins SB-25-31-005 (replace front upper control arm mounts, and dampers on Premium/Performance; confirm noise on a road test under 20 mph) and SB-26-31-003 (replace dampers if noise persists) apply to the refreshed 2025+ Model Y only. TÜV's 'axle suspension' defects (Achsaufhängung) are the official evidence of wear in this area.

- **This car:** Neither bulletin applies to an Aug-2022 Shanghai build: SB-20-31-006 covers pre-sealing builds, and the 2025/26 bulletins cover the refreshed model. The wear pattern is still relevant. Test for creaks and knocks over bumps below 30 km/h and check the ball joints for play on a lift. Out of basic warranty, the buyer pays.
- **Sources:** [driveteslacanada.ca](https://driveteslacanada.ca/?p=25923), [go-parts.com](https://www.go-parts.com/garage/suspension-control-arm-tesla-model-3-tesla-model-y-2017-2026), [service.tesla.com](https://service.tesla.com/docs/ServiceBulletins/External/SB/SB-25-31-005_Replace_Suspension_Components_R1.pdf), [notateslaapp.com](https://www.notateslaapp.com/news/4210/tesla-issues-service-bulletins-for-refreshed-model-y-suspension-creaks), [driveteslacanada.ca](https://driveteslacanada.ca/model-y/tesla-model-y-suspension-service-bulletin-2026/), [teslamotorsclub.com](https://teslamotorsclub.com/tmc/threads/creaky-front-end.343427/), [lordco.com](https://lordco.com/Product/Suspension-Control-Arm-And-Ball-Joint-Assembly-DOR527-513)

### 14. Heat pump / Octovalve (low confidence, sourced in this pass)

Owner reports from Finland, Sweden and Norway (TMC thread; motor.es on Sweden) describe Model Y heat pumps blowing only cold air in deep cold. Electrek reported a case where both the A/C compressor and the Octovalve supermanifold were replaced. Aggregator au7o says that on 2021-2022 Model Ys the electronic expansion valve in the supermanifold can stick when controller communication is interrupted, cutting heat and defrost below about -10 °C. It quotes repair costs of $0-5,000. Go-Parts estimates supermanifold labour at $1,600-2,400 and mentions a Quebec class action (not confirmed). I found no Tesla bulletin text or EU regulator action.

- **This car:** Relevant for Bulgarian and Romanian winters. Run full heat and full A/C, check defrost, and look for thermal or HVAC alerts. Sources are anecdotal or from aggregators; how often it happens on 2022 Shanghai builds is unknown.
- **Sources:** [teslamotorsclub.com](https://teslamotorsclub.com/tmc/threads/model-y-heat-pump-issues.250527/), [motor.es](https://www.motor.es/noticias/tesla-fallo-suecia-bomba-calor-202284062.html), [electrek.co](https://electrek.co/?p=219876), [au7o.io](https://au7o.io/known-issues/tesla-model-y?year=2022), [go-parts.com](https://www.go-parts.com/garage/hvac-heater-assembly-tesla-model-3-tesla-model-y-2019-2026)

### 15. B-pillar camera condensation (low confidence, sourced in this pass)

Tesla Motors Club threads report condensation inside the B-pillar cameras of Model 3/Y, sometimes within 20-25 minutes of highway driving. Some owners had cameras and covers replaced under warranty, with mixed results: fogging came back for some, while other owners were told it was normal. One post says the cameras are not sealed from the cabin. Preconditioning reportedly helps. I found no source for a revised 'vented' camera part.

- **This car:** Check the camera views after a drive or a wash. A fogged feed is mostly a cosmetic or Autopilot-availability problem, not a safety-inspection one. Forum evidence only.
- **Sources:** [teslamotorsclub.com](https://teslamotorsclub.com/tmc/threads/condensation-in-b-pillar-cameras.210074/), [teslamotorsclub.com](https://teslamotorsclub.com/tmc/threads/b-pillar-cameras-fogging-up.172226/page-2), [teslamotorsclub.com](https://teslamotorsclub.com/tmc/threads/pillar-camera-condensation.348285/)

### 16. Liftgate water ingress bulletin does not cover Shanghai builds (medium confidence, sourced in this pass)

Tesla's SB-23-10-003 (Apr 2023) covers liftgate water ingress on 2020-2023 Model Y. The fix is to reseal the liftgate assembly (about 1.8 h, with new sealant, and the parts list includes liftgate lamp gaskets). It lists only Fremont and Giga Austin as build locations. Drive Tesla Canada reported a free re-fix under warranty in Canada. I found no Shanghai-specific or Europe-specific water-leak bulletin.

- **This car:** Lower priority for this Shanghai car, but a 30-second sub-trunk check for water or tide marks is still worth doing.
- **Sources:** [static.nhtsa.gov](https://static.nhtsa.gov/odi/tsbs/2023/MC-10247838-9999.pdf), [driveteslacanada.ca](https://driveteslacanada.ca/?p=73660), [notebookcheck.net](https://www.notebookcheck.net/Tesla-takes-a-second-pass-at-Model-Y-trunk-water-leakage-fix-with-new-sealant.723233.0.html)

### 17. Recalls relevant or not relevant to this build (medium confidence, sourced in this pass)

China's market regulator SAMR recalled 21,599 China-built Model Y produced between 4 Feb and 30 Oct 2021 over front and rear steering-knuckle (Achsschenkel) defects. The German federal vehicle authority KBA required a software recall (reference 011824) for 2022-production Model 3/Y over an eCall fault, 59,129 cars worldwide, including Grünheide-built cars. Sources do not say whether Shanghai-built cars are included. car-recalls.eu lists KBA Model Y campaigns.

- **This car:** The knuckle recall does not cover an Aug-2022 build. The eCall recall may apply and was a software fix; ask Tesla Service to confirm this VIN has no open campaigns.
- **Sources:** [whichcar.com.au](https://whichcar.com.au/news/tesla-model-y-recalled-in-china), [autobild.de](https://www.autobild.de/artikel/rueckrufaktion-bei-tesla-in-china-25069969.html), [insideevs.de](https://insideevs.de/news/596180/tesla-model-y-3-ruckruf/), [auto-motor-und-sport.de](https://www.auto-motor-und-sport.de/verkehr/rueckruf-tesla-model-3-y-ausfall-des-e-call-systems/), [car-recalls.eu](https://car-recalls.eu/ro/recall-news/kba-recalls/Tesla/model-y/)

### 18. Tesla maintenance items relevant to brakes (high confidence, sourced in this pass)

Tesla's Model Y maintenance intervals: a brake-fluid health check every 4 years (replace if needed). Brake calipers should be cleaned and lubricated every 12 months or 20,000 km (12,500 miles) where roads are salted in winter. The Singapore manual says 'clean' only; the US service page says 'clean and lubricate'. Cabin and HEPA filter intervals vary by market. I could not verify the A/C desiccant-bag interval.

- **This car:** On salted RO/BG roads the caliper service should have been done every year. The 4-year brake-fluid check falls due around Aug-Sep 2026. Missing records combined with rusted discs means budgeting for discs and pads before the ГТП/ITP inspection.
- **Sources:** [tesla.com](https://www.tesla.com/ownersmanual/modely/en_sg/GUID-E95DAAD9-646E-4249-9930-B109ED7B1D91.html), [service.tesla.com](https://service.tesla.com/docs/Public/diy/modely/en_us/GUID-A84FDD77-7A8C-42F6-9385-E3F9CEE245A4.html), [tesla.cn](https://www.tesla.cn/ownersmanual/modely/en_cn/GUID-E95DAAD9-646E-4249-9930-B109ED7B1D91.html)

### 19. Warranty status (medium confidence, sourced in this pass)

Tesla's EU warranty page lists 8 years or 192,000 km, with at least 70% capacity retained, for the battery and drive unit on Model Y Long Range variants (now named 'Premium LR' RWD/AWD) and Performance. The standard Model Y RWD gets 160,000 km. The basic warranty of 4 years or 80,000 km is confirmed indirectly: Tesla's German/Austrian page says certified pre-owned cars carry the remaining term of the 4-year/80,000 km Basic Vehicle Limited Warranty.

- **This car:** Factory gate was about Aug 2022 and neighbouring cars were first registered in Sep 2022. The basic warranty probably ended around Sep 2026 (or at 80,000 km if reached earlier), so it is very likely expired as of 12 Oct 2026. Battery and drive-unit cover runs to about Sep 2030 or 192,000 km. The exact start date (delivery or first registration) has to come from the documents; that warranty starts on that date is model knowledge, not verified in this run.
- **Sources:** [tesla.com](https://www.tesla.com/en_EU/support/vehicle-warranty), [tesla.com](https://www.tesla.com/de_at/support/vehicle-warranty)

### 20. Periodic inspection (brake roller test) procedure (high confidence, sourced in this pass)

Tesla's Model Y service manual has a section '0006 - Periodic Roadworthiness Inspections' covering VIN locations, jacking points, free-wheeling settings and how to complete brake tests. Tesla's UK/IE MOT page describes Tow Mode for letting the wheels roll freely, and the Electronic Parking Brake (EPB) Dynamic Mode test on a rolling road: shift to Neutral, then press and hold Park until the rear wheels stop. I found no menu labelled 'Dyno mode'.

- **This car:** Useful for the Bulgarian ГТП or Romanian ITP: point the station to Tesla's inspection procedure and Tow Mode instead of a 'Dyno mode'.
- **Sources:** [service.tesla.com](https://service.tesla.com/docs/ModelY/ServiceManual/en-us/GUID-329BA50E-C294-41CD-942D-F3FAA05668D4.html), [tesla.com](https://www.tesla.com/en_gb/support/mot-testing)

### 21. Pre-purchase checklist: steps backed by sources in this run (medium confidence, sourced in this pass)

(1) Documents: Tesla service invoices, recall status for the VIN, and all HU/ITP/APK reports. Check for proof of yearly caliper cleaning and lubrication on salted roads and the 4-year brake-fluid check (due around Aug-Sep 2026). Confirm the first-registration date: it sets the basic warranty end (probably about Sep 2026) and the battery warranty end (about 2030/192,000 km). (2) Service Mode (Controls > Software, hold 'MODEL', type 'service'): read Service Alerts, the Driver Assist camera status and the High Voltage section. Do not drive in Service Mode. (3) Battery Health test, run by the seller: AC of at least 5 kW, start below 20%, no alerts or pending update, up to 24 h (longer at low amps). Benchmarks: about 92-95% is good at under about 100k km; about 90% is normal at about 150k km; under about 88% at moderate km is a red flag or price lever (my thresholds, from Aviloo and Geotab). Aviloo is the fallback. (4) TÜV's top three defect areas: brake discs (inner and outer faces, rear especially: rust band or lip), front and rear suspension joints and bushings (creak or knock below 30 km/h over bumps, play on a lift), and all lighting (function and aim). (5) Heat pump: full heat, defrost and A/C, and no thermal alerts. (6) Cameras: check every feed for fog after a drive. (7) Sub-trunk: quick look for water. (8) LV battery: no low-voltage alerts. 12 V/LV battery faults are 45.4% of all ADAC breakdowns.

- **This car:** Built for this car: a Shanghai Aug-2022 LR AWD with an LG pack, now about 4 years old, basic warranty probably just ended, used on Balkan salted roads.
- **Sources:** [tesla.com](https://www.tesla.com/ownersmanual/modely/en_il/GUID-B9807218-7291-4F68-9AFF-7C525CF498F3.html), [notateslaapp.com](https://www.notateslaapp.com/news/2046/tesla-service-mode-how-to-access-it-and-what-it-does), [tesla.com](https://www.tesla.com/ownersmanual/modely/en_sg/GUID-E95DAAD9-646E-4249-9930-B109ED7B1D91.html), [mobiflip.de](https://www.mobiflip.de/tuev-report-2026-tesla-stuerzt-auf-letzten-platz/), [transportandenergy.com](https://transportandenergy.com/?p=35198), [electricautonomy.ca](https://electricautonomy.ca/ev-supply-chain/batteries/2026-01-13/latest-geotab-study-finds-ev-batteries-lose-just-2-3-life-per-year/), [tesla.com](https://www.tesla.com/en_EU/support/vehicle-warranty)

### 22. Pre-purchase checklist: additional steps carried over from round 1 (not re-sourced) (medium confidence, NOT re-verified)

(a) Charge port must be CCS2 (Type 2 + DC), not GB/T. A GB/T port means a Chinese-domestic grey import. Test 3-phase AC at about 11 kW and one DC session, and check the port door and latch. (b) Check that the 12 ultrasonic sensors are present in the bumpers (round 1 says an Aug-2022 build should have them). (c) Check the build month/year on the label on the driver-side B-pillar; it should read about 08/2022 and match the VIN estimate. (d) Controls > Software > Additional Vehicle Information should show Autopilot computer HW3 and an AMD Ryzen infotainment processor. (e) Check the windscreen near the camera housing and both roof glass panels for chips or cracks. (f) Tyres: inner-edge wear, DOT dates, matching brands. (g) Underbody HV pack: dents, scrapes, damaged jack pads. (h) Paint-thickness gauge on every panel, and rear-casting area repairs. (i) RAR odometer history (if registered in Romania) and carVertical. (j) Signs of fleet/taxi use.

- **This car:** Standard checks for this car. Not re-verified in this run because the search cap was reached.
- **Sources:** none (reasoning or local calculation)

## Corrections to the first pass

- The TÜV Report 2026 Model Y figure of 17.3% (last of 110, 2-3 years) is confirmed. Round 1 left the Model 3 figures unconfirmed: it was third-to-last at 2-3 years (13.1%) and third-to-last at 4-5 years (21.0%, about 86,000 km).
- Round 1 said the first Model Y 4-5-year TÜV data would appear in TÜV Report 2027 (about Nov 2026). That is probably wrong: the 4-5-year class is the 5-year HU, and the earliest EU Model Ys (Aug 2021) only reach it from Aug 2026, inside the TÜV Report 2028 window (Jul 2026-Jun 2027). This is an inference.
- TÜV Report 2025: the Model 3 at 14.2% (last of 111, 2-3 years) is confirmed. Round 1 missed that the Model 3 was also reported last in the 4-5-year class, at 19.7% according to AutoScout24.
- TÜV Report 2024: the 14.7% is confirmed, but the class was 'bis 3 Jahre' (up to 3 years; the report used six age classes for the first time), and the Dacia Logan at 11.4% was the previous last-placed car.
- Round 1 used Geotab's average of about 1.8% a year. The 2025 Geotab update is 2.3% a year: 1.5% with less than 12% DC fast charging, 2.5% above that, and up to 3.0% with heavy charging above 100 kW.
- The Tesla Impact Report figure of about 15% loss at 200,000 miles for Model 3/Y (LR) is confirmed. It comes from the 2023 Impact Report, published 2024.
- Round 1's battery SoH estimate of 88-93% is somewhat pessimistic for moderate mileage. Aviloo's Model Y median is 94.5% at 50,000 km and 90.3% at 150,000 km, and the LR loses 5.5% at 50,000 km. A better band is about 90-94%, with 88% as the red-flag line.
- Water leaks: the liftgate water-ingress bulletin SB-23-10-003 lists Fremont and Austin builds only. I found no Shanghai bulletin, so this item should be downgraded for this car.
- B-pillar cameras: I found no source for Tesla replacing them with revised 'vented' units. Forum reports describe warranty replacements with mixed results.
- Front upper control arms: a bulletin does exist (SB-20-31-006, a ball-joint reseal), but it covers 2018-2020 builds made before factory sealing. The new bulletins SB-25-31-005 and SB-26-31-003 are for the refreshed 2025+ Model Y and do not apply to this car.
- 'Dyno mode': I found no Tesla menu by that name. Tesla documents Tow Mode/free-wheel settings, a 'Periodic Roadworthiness Inspections' service-manual section and an EPB Dynamic Mode rolling-road test.
- Battery Health test prerequisites are now confirmed from the owner's manual: AC of at least 5 kW, start below 20%, Park, no pending update, no battery or thermal alerts, up to 24 h. The path is Controls > Service > Battery Health Test, or Service Mode > High Voltage.
- ADAC: round 1 had no figures. The 2026 edition gives the Model 3 0.7 per 1,000, attributes 45.4% of all breakdowns to the 12 V battery, and Auto Bild cites a Model Y figure of 0.9 (edition unclear).
- Recalls: the China knuckle recall of Shanghai Model Y (21,599 cars built 4 Feb-30 Oct 2021) does not cover this Aug-2022 car. There is a KBA eCall software recall (011824) for 2022-production Model 3/Y; whether it includes Shanghai builds is unclear.
- Warranty: round 1 said the basic warranty 'probably ends during 2026'. With an Aug-2022 factory date and neighbours registered in Sep 2022, it has most likely already expired by 12 Oct 2026. The EU battery and drive-unit warranty of 8 years/192,000 km with at least 70% retention for LR is confirmed.
- Round 1 had no EV Clinic material. Added: EV Clinic's 29 Nov 2025 claims against Nanjing LG NCM811 packs, the rebuttals (New Mobility News, Tesla Geek, fleet data showing LG packs at about 91-92%), and the Nyland 2022 LG-pack Model Y LR at -11.5% at about 155k km.

## Open questions

- What is the average defect rate for the TÜV Report 2026 2-3-year class? Not found.
- Is there an ADAC Pannenkennziffer for the Model Y by registration year (2021/2022), and which edition does Auto Bild's 0.9 come from? Not found.
- Does the KBA eCall recall 011824 (2022 production) cover Shanghai-built EU Model Y, and does this VIN have any open campaign? Tesla Service must confirm.
- Did Aug-2022 Shanghai builds have factory-sealed front upper control arm ball joints? This is inferred, not confirmed.
- How big are EV Clinic's sample and the competing fleet datasets (Drive Tesla Canada / unnamed study, Tessie, TeslaFi, Recurrent)? I found no Model Y LG-pack degradation curve by mileage.
- Can Service Mode show the history of cleared alerts, or only active ones? Not confirmed.
- Is the A/C desiccant-bag replacement interval for Model Y 4 years or 6 years? Not verified.
- Does the warranty start at delivery or first registration, and what are this car's actual mileage and date? These decide whether the 4-year/80,000 km basic warranty has ended. The seller's documents are needed.
- Is it confirmed that Aug-2022 Shanghai builds keep the 12 ultrasonic sensors (removal began around Oct 2022)? Not re-verified in this run.
- Bulgarian ГТП periodicity, and recognition of a valid Romanian ITP when re-registering: outside this lens and not searched.
