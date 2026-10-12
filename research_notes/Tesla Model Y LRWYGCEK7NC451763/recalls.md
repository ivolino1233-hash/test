# Recalls and service campaigns for a 2022 Shanghai Model Y

Method note: researched 2026-10-12. WebFetch and curl could not reach any site from this environment (DNS failure on every host, including tesla.com, NHTSA, autoDNA and carVertical), so **every fact below comes from search-engine results and snippets, not from pages I opened**. Second research pass; the first pass ran out of shared search budget, so this pass re-checked or replaced its claims. Searches used: 30.

## Takeaway

I used 30 of 30 searches. KBA 14692R (TPMS, SB-24-00-018) is the only EU recall I could confirm covers this car's build date. auto motor und sport gives its Model Y window as 20 Jan 2020 to 23 Nov 2024, which includes the estimated ~Aug 2022 build. The fault breaks UN ECE R141. Tesla's de_lu support page says firmware 2024.38.7, 2024.38.10, 2024.40 or later fixes it (2024.44 and 2024.44.1 excluded), with no workshop visit needed. KBA 13972R (seat-occupancy detection / seat-belt warning, SB-24-00-008) covers 183,450 cars of all four models worldwide (6,725 in Germany) with a software fix, and is probably in scope. KBA 011824 (eCall, SB-22-00-010, 59,129 cars, published 29 Jun 2022, software fix) is uncertain: it covers '2022 production', but it was published about 6 weeks before this car was built. The CPU-cooling recall (KBA 011850 / SB-22-00-009) is probably NOT in scope, which reverses round 1. The OTA started 3 May 2022. China's version (107,293 cars) covered Shanghai builds only from 19 Oct 2021 to 26 Apr 2022, fixed by firmware 2022.12.3.3. KBA 14811R (power steering, builds Feb-Oct 2023, fixed by firmware 2023.38.4 or later) is not in scope. SB-24-32-001 (steering feels notchy in the cold, Australia REC-005875: 2022-23 Model 3/Y, no safety hazard, firmware 2023.38 or later) may include 2022 builds; it is fixed on any current firmware. The only possible workshop item I found is a single-source Spanish report of a German Safety Gate notice SB-24-13-003. It covers Model Y built 22 Jun 2022 to 25 Mar 2024 whose seat-back frames may be missing welds. The window covers this car, but the factory and remedy are unconfirmed, so ask Tesla specifically. Shanghai 2022 China-market recalls with windows covering this car: Dec 2022 rear position lamps (292,855 Model Y built 1 Jan 2021-11 Nov 2022, OTA), May 2023 regen choice / accelerator warning (built 12 Jan 2019-24 Apr 2023, OTA), Jan 2024 Autosteer (built up to 20 Dec 2023, OTA), and Aug 2026 door releases (1,956,713 Model Y, labels plus window-drop OTA, starting 25 Sep 2026). None of these is a confirmed EU recall. For the door releases, electrive (27 Aug 2026) reports no EU recall yet: the RDW, which holds Tesla's EU type approval and alone can order an EU recall, is monitoring, and the KBA has had an investigation open since April 2026. Recent US recalls 26V283 (HW3 rear-camera delay on 2026.8.6, OTA) and 26V507 (US-supplier headlamp too bright) are US/FMVSS filings, and I found no EU equivalent. To check this VIN in Europe, ask Tesla Service for a VIN-level recall/SB printout. In Romania, RAR issues registration documents (CIV) only after important safety recalls are done, and recalls can be done free at an authorised workshop even on cars bought abroad.

## Cited findings

### 1. KBA 14692R / SB-24-00-018 - TPMS warning not kept between drive cycles (EU) (high confidence, sourced in this pass)

KBA 14692R, Tesla SB-24-00-018, covers Model 3 and Model Y: 76,023 cars in Germany and 387,642 worldwide (car-recalls.eu). The TPMS warning does not stay on between drive cycles, which breaks UN ECE R141. Production windows (auto motor und sport, sparneuwagen): Model Y 20.01.2020-23.11.2024, Model 3 24.07.2017-20.11.2024. car-recalls.eu gives one window, 9 Jan 2018-21 Nov 2024. Remedy is OTA only. Tesla's support page says firmware 2024.38.7, 2024.38.10, 2024.40 or later fixes it (2024.44 and 2024.44.1 excluded), with no service visit needed. One search summary gave a KBA publication date of 21 Jul 2025; I treat that date as snippet-only.

- **This car:** IN SCOPE: the estimated ~Aug 2022 build is inside the Model Y window (Jan 2020-Nov 2024). The fix is OTA, so the recall is closed if the car runs firmware 2024.40 or later (or 2024.38.7/.10), but not 2024.44/2024.44.1. Check under Controls > Software.
- **Sources:** [tesla.com](https://www.tesla.com/de_lu/support/recall-vehicle-firmware-correct-tpms-malfunction), [auto-motor-und-sport.de](https://www.auto-motor-und-sport.de/verkehr/tesla-rueckruf-softwareproblem-reifendruckwarnsystem/), [sparneuwagen.de](https://www.sparneuwagen.de/news/noch-ein-rueckruf-teslas-haben-ein-problem-mit-der-reifendruckmessung/), [car-recalls.eu](https://car-recalls.eu/fr/tesla-model-y-model-3-tyre-pressure-monitoring-system-malfunction-kba/)

### 2. KBA 13972R / SB-24-00-008 - seat-occupancy detection and seat-belt warning (EU) (medium confidence, sourced in this pass)

KBA 13972R, Tesla SB-24-00-008. Faulty seat-occupancy detection means the seat-belt warning may not activate. Covers 183,450 Model 3/S/X/Y worldwide (Autohaus headline 'about 180,000'), 6,725 in Germany (auto motor und sport). It extends the 2022 US recall of 817,143 cars. Remedy is a software update. In the US version, the software drops the occupancy-sensor dependency and warns based on buckle and ignition status. Whether the EU fix is identical is not stated. An aggregator gives the KBA publication date as 29.07.2024. Round 1 gave the production range as 2012-2024, and I did not re-confirm it.

- **This car:** PROBABLY IN SCOPE. The population is broad and covers all four models. The fix is software, so it is likely already installed if the car is on firmware from mid/late 2024 or later. Confirm SB-24-00-008 status by VIN with Tesla.
- **Sources:** [autohaus.de](https://www.autohaus.de/nachrichten/autohersteller/passagiererkennung-und-gurtwarnung-defekt-tesla-ruft-180-000-modelle-zurueck-3544566), [auto-motor-und-sport.de](https://www.auto-motor-und-sport.de/verkehr/rueckruf-tesla-anschnallwarner-problem/), [car-recalls.eu](https://car-recalls.eu/it/seat-occupancy-detection-failure-tesla-kba/)

### 3. KBA 011824 / SB-22-00-010 - eCall failure (EU) (medium confidence, sourced in this pass)

The KBA published recall 011824 (Tesla SB-22-00-010) on 29 Jun 2022 for Model 3 and Model Y of the 2022 production year. Some outlets say 2022 model year instead. It covers 59,129 vehicles worldwide; the German number was not stated. Cause is a software fault that can make the eCall emergency-call system fail. Remedy is a software update (apparently OTA) or a Tesla / authorised workshop visit. No accidents were known as of July 2022.

- **This car:** UNCERTAIN, not 'likely' as round 1 said. The recall was published on 29 Jun 2022, about 6 weeks before this car's estimated factory-gate date (~10-11 Aug 2022). It may have left the factory with corrected software. The exact production/VIN range is not public. The fix is software either way, so it is resolved on any current firmware. Confirm SB-22-00-010 status with Tesla.
- **Sources:** [insideevs.de](https://insideevs.de/news/596180/tesla-model-y-3-ruckruf/), [winfuture.de](https://winfuture.de/news,130549.html), [auto-motor-und-sport.de](https://www.auto-motor-und-sport.de/verkehr/rueckruf-tesla-model-3-y-ausfall-des-e-call-systems/), [ecomento.de](https://ecomento.de/2022/07/04/tesla-rueckruf-fuer-model-3-und-model-y-automatischer-notruf-kann-ausfallen/)

### 4. KBA 011850 / SB-22-00-009 - infotainment CPU overheating (EU) and the China equivalent (medium confidence, sourced in this pass)

EU: Model S/3/X/Y built in 2021-2022, 14,807 in Germany (another source says 14,804) of 209,211 worldwide. The infotainment CPU can overheat before or during Supercharging, so the centre screen lags, reboots or goes blank. The rear camera, defrost and gear indicators may then be lost. Tesla began the OTA fix on 3 May 2022. China equivalent (SAMR, May 2022): 107,293 Shanghai-built Model 3/Y built 19 Oct 2021-26 Apr 2022, OTA to firmware 2022.12.3.3 or later, campaign starting 23 May 2022. Note: this run's search did not show the KBA/SB numbers in the same snippet; that link comes from round 1 (autoservicepraxis).

- **This car:** PROBABLY NOT IN SCOPE, which corrects round 1's 'possibly'. The OTA fix started in May 2022, and the Shanghai population in the China recall ended on 26 Apr 2022. A car built ~Aug 2022 would have left the factory on newer firmware. It is resolved on current firmware in any case.
- **Sources:** [pcgameshardware.de](https://www.pcgameshardware.de/Automotive-Thema-261936/News/Tesla-Rueckruf-Software-Update-CPU-ueberhitzt-1402656/), [shop4tesla.com](https://www.shop4tesla.com/blogs/news/kba-tesla-ruckrufaktion-wegen-unzureichender-kuhlung-der-prozessoren), [auto-motor-und-sport.de](https://www.auto-motor-und-sport.de/verkehr/rueckruf-tesla-model-s-3-x-y-heisse-prozessoren/), [autonews.gasgoo.com](https://autonews.gasgoo.com/articles/news/tesla-recalls-107293-locally-made-model-3s-model-ys-in-china-70020351), [asiafinancial.com](https://www.asiafinancial.com/china-says-tesla-recalling-107293-model-3-y-cars), [investinglive.com](https://investinglive.com/news/tesla-to-recall-over-100000-vehicles-in-china-20220517/)

### 5. Safety Gate / German notice SB-24-13-003 - Model Y seat-back frame missing welds (possible workshop item) (low confidence, sourced in this pass)

Autofacil (Spain) reports a Safety Gate notice issued by German authorities under Tesla code SB-24-13-003. It covers Model Y built 22 Jun 2022-25 Mar 2024 whose seat-backrest frames may be missing certain welds, which could reduce seat stiffness in a crash and raise injury risk. I found no second source. The factory, alert number, publication date and remedy were not in the snippet. Do not confuse it with two US recalls. The first covered 27 Giga Texas Model Y built 28-30 Oct 2024 (recliner weld penetration, seat replaced). The second covered 3,470 US Model Y built 23 May 2022-5 Feb 2023 (loose second-row seat-back bolts).

- **This car:** POSSIBLY IN SCOPE. ~Aug 2022 falls inside the 22 Jun 2022-25 Mar 2024 window, but it may apply only to Berlin-built cars or a small VIN subset. It is probably a hardware/workshop remedy, so it would NOT be fixed by OTA. Ask Tesla explicitly whether SB-24-13-003 applies to LRWYGCEK7NC451763 and whether it is closed.
- **Sources:** [autofacil.es](https://www.autofacil.es/tesla-model-y-revision/), [driveteslacanada.ca](https://driveteslacanada.ca/model-y/tesla-recalls-27-model-y-vehicles-over-seat-weld-defect/), [notateslaapp.com](https://www.notateslaapp.com/news/1247/un)

### 6. KBA 14811R / SB-25-00-004 - loss of power-steering assist (EU), Australia REC-006300 (high confidence, sourced in this pass)

KBA 14811R, Tesla SB-25-00-004: possible loss of EPAS assist on Model 3/Y built Feb-Oct 2023, 39,200 in Germany (over 550,000 worldwide). It extends a Feb 2025 US recall. Remedy is software 2023.38.4 or later, delivered OTA (auto motor und sport, autoservicepraxis); expert-zoom claims a workshop visit is needed. The Australian equivalent, REC-006300 (Mar 2025), covers 297 'MY2022-2023' Model 3/Y and is fixed by OTA.

- **This car:** NOT IN SCOPE (Feb-Oct 2023 builds). Even if it were, firmware 2023.38.4 or later fixes it.
- **Sources:** [autoservicepraxis.de](https://www.autoservicepraxis.de/rueckrufe/artikel/tesla-rueckruf-fuer-model-y-und-3-ausfall-der-servolenkung-3665255), [auto-motor-und-sport.de](https://www.auto-motor-und-sport.de/verkehr/rueckruf-tesla-model-3-model-y-servolenkung-software/), [expert-zoom.com](https://expert-zoom.com/de/nachrichten/tesla-ruckruf-2026-deutschland-servolenkung-rechte-fahrzeughalter), [vehiclerecalls.gov.au](https://www.vehiclerecalls.gov.au/recalls/rec-006300), [thecourier.com.au](https://www.thecourier.com.au/story/8907375/tesla-model-y-model-3-recalled/)

### 7. SB-24-32-001 - steering wheel feels notchy in cold temperatures (Australia REC-005875; round 1's KBA '12321') (medium confidence, sourced in this pass)

Australian recall REC-005875 under Tesla campaign SB-24-32-001 covers 4,383 Model 3 and Model Y of 2022-2023 model years. A software issue can make the steering feel notchy in the cold, which may break an Australian Design Rule. The regulator says there is no safety hazard and performance is unaffected. Remedy is software 2023.38 or later. teslamag reported 'two new Tesla recalls in the KBA database' including a steering item (title only). I could not verify the KBA reference '12321' or the 'summer 2023 builds' window from round 1. The auto motor und sport 'Servolenkung zickt' article may actually describe 14811R.

- **This car:** POSSIBLY IN SCOPE (Australian MY2022 Shanghai cars were included), but it is not safety-critical and is fixed on any firmware 2023.38 or later. It has no practical effect if the car is on current software.
- **Sources:** [vehiclerecalls.gov.au](https://www.vehiclerecalls.gov.au/recalls/rec-005875), [australiancar.reviews](https://australiancar.reviews/recalls-faults-tesla-model-y-2022/), [teslamag.de](https://teslamag.de/news/zwei-deutsche-tesla-rueckrufe-autopilot-lenkung-59397)

### 8. Safety Gate A12/00503/22 - Model Y steering knuckles (EU), and China Dec 2021 recall (medium confidence, sourced in this pass)

Safety Gate alert A12/00503/22 was reported by Germany and published 01/04/2022. It covers about 23,437 Model Y built June 2020-November 2021: the knuckles may break or deform, so suspension arms could detach. The remedy is a workshop visit. The China Dec 2021 recall (21,599 Shanghai Model Y built 4 Feb-30 Oct 2021) is the same issue: front/rear steering knuckle (转向节) strength not meeting requirements. That corrects round 1's vague 'suspension'.

- **This car:** NOT IN SCOPE (window ends Nov 2021; this car was built ~Aug 2022).
- **Sources:** [car-recalls.eu](https://car-recalls.eu/es/recall/tesla-model-y-2021-steering-knuckles/), [car-recalls.eu](https://car-recalls.eu/fr/recall/tesla-model-y-2021-steering-knuckles/), [m.thepaper.cn](https://m.thepaper.cn/newsDetail_forward_15674828)

### 9. China SAMR Dec 2022 - rear position lamps software (Shanghai Model 3/Y) (high confidence, sourced in this pass)

Announced 1 Dec 2022. Covers 142,277 China-made Model 3 and 292,855 China-made Model Y built 1 Jan 2021-11 Nov 2022 (Gasgoo; Yicai says Dec 2020-Nov 2022), 435,132 in total. Software may mis-initialise parameters at start-up, so one or both rear position lamps may not light. Remedy is a free OTA. The US (about 321,000 cars, Nov 2022) and Australia (Nov 2022, 2022 Model Y tail lamps, Shanghai-built) recalled for the same issue. I found no KBA/EU entry.

- **This car:** The build window covers this car if it was China-market. For an EU-market car I found no formal EU recall, but the same Shanghai hardware and software is very likely affected and was fixed by a late-2022 OTA. It is resolved on current firmware.
- **Sources:** [autonews.gasgoo.com](https://autonews.gasgoo.com/articles/ev/tesla-recalls-435132-shanghai-made-model-3s-model-ys-in-china-70021799), [bnnbloomberg.ca](https://www.bnnbloomberg.ca/tesla-to-fix-rear-lighting-issue-on-over-435-000-china-made-cars-1.1853436), [yicaiglobal.com](https://yicaiglobal.com/news/tesla-recalls-over-400000-vehicles-in-china-due-to-headlight-safety-issue), [australiancar.reviews](https://australiancar.reviews/recalls-faults-tesla-model-y-2022/), [t3n.de](https://t3n.de/news/tesla-19-rueckruf-321-000-autos-1514826/)

### 10. China SAMR May 2023 - regenerative-braking choice and hard-acceleration warning (high confidence, sourced in this pass)

SAMR announced on 12 May 2023 a recall of 1,104,622 vehicles from 29 May 2023: imported S/X/3 and China-made Model 3/Y built 12 Jan 2019-24 Apr 2023. The cars did not let the driver choose regen-braking strength, and warnings for prolonged deep accelerator press may be insufficient, together raising the risk of pedal misapplication. Remedy is OTA: a regen-strength option, a changed default regen setting, and a warning on prolonged deep accelerator press. It followed a SAMR defect investigation.

- **This car:** China-market recall. The window covers 2022 Shanghai builds. I found no EU equivalent, so for an EU car it is not formally applicable.
- **Sources:** [autohome.com.cn](https://www.autohome.com.cn/news/202305/1284457.html), [cs.com.cn](https://cs.com.cn/cj2020/202305/t20230512_6343852.html), [huxiu.com](https://www.huxiu.com/article/1529783.html)

### 11. China SAMR Jan 2024 - Autosteer misuse (OTA) (high confidence, sourced in this pass)

SAMR disclosed on 5 Jan 2024 that Tesla Shanghai and Beijing would recall 1,610,105 vehicles: imported Model S/X/3 and China-made Model 3/Y built 26 Aug 2014-20 Dec 2023. With Autosteer engaged, the driver could misuse the Level-2 assistance and raise collision risk. Remedy is a phased OTA adding extra Autosteer controls and alerts; cars unable to take the OTA are updated free by service centres. The same filing included a separate S/X door-latch issue (7,538 cars).

- **This car:** China-market recall (mirrors the US Dec 2023 Autosteer recall). The window covers 2022 Shanghai builds. I found no KBA/RDW equivalent, so it is not formally applicable to an EU car.
- **Sources:** [m.thepaper.cn](https://m.thepaper.cn/newsDetail_forward_25910723), [news.china.com](https://news.china.com/domestic/945/20240105/46046469.html), [cls.cn](https://www.cls.cn/detail/1562979)

### 12. China SAMR Feb 2022 - heat-pump expansion valve (out of scope) (high confidence, sourced in this pass)

Recall of 12,003 Model 3 and 14,044 Model Y (China-made) built 28 Dec 2020-15 Jan 2022: the heat-pump electronic expansion valve may fail, affecting defrost and heating. Remedy is OTA.

- **This car:** NOT IN SCOPE (window ends 15 Jan 2022).
- **Sources:** [autohome.com.cn](https://www.autohome.com.cn/news/202202/1239195.html)

### 13. China Aug 2026 emergency door-release recall - EU status (high confidence, sourced in this pass)

Covers 2,975,910 Tesla vehicles in China, including 973,156 China-made Model 3 and 1,956,713 China-made Model Y. It starts 25 Sep 2026. The mechanical emergency releases match the interior trim colour and are hard to find. Remedy is warning labels plus an OTA that lowers the windows after a detected crash; there is no hardware change to the door mechanism. Europe: per electrive (27 Aug 2026) the RDW told Reuters there is currently no EU recall and it is monitoring. The KBA has had an investigation open since April 2026, after a crash in Schwerte with three occupants killed. The KBA cannot order an EU recall; the RDW, as type-approval authority, can.

- **This car:** No EU recall as of late Aug 2026. Not formally applicable to an EU-registered car, but the hard-to-find release applies physically to this car. The buyer should learn where the front and rear mechanical releases are and watch for an RDW/KBA decision. An EU recall could follow.
- **Sources:** [electrive.com](https://electrive.com/2026/08/27/huge-tesla-recalls-in-china-while-european-authorities-remain-cautious), [driveteslacanada.ca](https://driveteslacanada.ca/news/tesla-china-recall-emergency-door-release/), [notateslaapp.com](https://www.notateslaapp.com/news/4601/tesla-recalls-nearly-3m-cars-in-china-for-door-handles), [netzwelt.de](https://www.netzwelt.de/news/257970-298-millionen-teslas-ueckgerufen-riesen-rueckruf-fuer-fahrer-deutschland-bedeutet.html)

### 14. US 26V283 - rear-camera image delay on HW3 cars (2026) (medium confidence, sourced in this pass)

NHTSA 26V283 covers 218,868 HW3 vehicles (Model 3 2017/2021-23, Model Y 2020-23, S, X) built 29 Nov 2017-3 Jan 2024 and running firmware 2026.8.6. The rear-camera image may be delayed when reverse is selected (FMVSS 111). Remedy is a free OTA; a secondary source says 99.92% were fixed before NHTSA posted the recall on 6 May 2026. The Tesla recall number is inconsistent across sources (SB-26-00-016 per NHTSA letter).

- **This car:** US filing only, and I found no EU recall. This car is HW3, so the software bug in 2026.8.6 could affect it physically. It is resolved if the car runs any firmware after the fix. Check that the car is not stuck on 2026.8.6.
- **Sources:** [static.nhtsa.gov](https://static.nhtsa.gov/odi/rcl/2026/RCAK-26V283-8069.pdf), [static.nhtsa.gov](https://static.nhtsa.gov/odi/rcl/2026/RCLRPT-26V283-7135.pdf), [bizzycar.com](https://www.bizzycar.com/blog/may-2026-tesla-recall-for-rearview-camera-image-delay-affecting-218868-vehicles)

### 15. US 26V507 - headlamp low beam too bright (2026) (medium confidence, sourced in this pass)

NHTSA 26V507 (Tesla SB-24-17-003) covers 18,735 Model Y 2020-2023 and 1,614 Model 3 2017-2023 built or serviced with a headlamp whose supplier manufacture date is 2 Jun 2023 or later. Low-beam output exceeds the FMVSS 108 maximum. A secondary source names Marelli in Mexico as the supplier. As of the report, the remedy was not finalised.

- **This car:** Very unlikely: this is a US FMVSS filing for US-supplied headlamps. It would matter only if a US-spec replacement headlamp were fitted. I found no EU equivalent.
- **Sources:** [static.nhtsa.gov](https://static.nhtsa.gov/odi/rcl/2026/RCLRPT-26V507-7698.pdf), [notateslaapp.com](https://www.notateslaapp.com/news/4567/tesla-issues-physical-recall-for-20349-model-3-and-model-y-vehicles-over-headlights)

### 16. Model Y inoperable reverse lamp recall (2025 builds, out of scope) (high confidence, sourced in this pass)

Covers Model Y built 6 Feb 2025-26 Jul 2025 (new-generation Model Y) with reverse lamps that may not work. The UK page cites UN ECE R48. Berlin found the fault during an end-of-line check.

- **This car:** NOT IN SCOPE (2025 builds).
- **Sources:** [tesla.com](https://www.tesla.com/en_gb/support/recall-inoperable-reverse-lamp), [static.nhtsa.gov](https://static.nhtsa.gov/odi/rcl/2025/RCLRPT-25V658-2725.pdf)

### 17. How to check open recalls for this VIN in Europe / Romania (medium confidence, sourced in this pass)

(1) Tesla publishes per-recall EU support pages on tesla.com with firmware fix versions (for example the TPMS page). Only Tesla Service can give a VIN-level open/closed list. (2) The RDW is the EU type-approval authority for Tesla and is the body that can order EU-wide recalls (electrive). (3) Romania: RAR has a 'Campanii de rechemare' section on rarom.ro that routes users to each brand's official recall check or an authorised workshop. Recall work can be done free in Romania's authorised network even for cars bought in another state. RAR advises a visit to an authorised workshop after registering an import so the manufacturer's database is updated. Vehicles presented to RAR for a CIV that have an important safety, health or environmental recall get registration documents only after the corrective action is done. (4) car-recalls.eu offers a third-party Tesla VIN recall check (not official). (5) I could not confirm whether the KBA database supports VIN search; one article claims it does, but I have not verified this.

- **This car:** Actionable. Before buying, ask the seller or Tesla Romania (Voluntari) for a VIN-level recall/SB printout for LRWYGCEK7NC451763. Name SB-24-00-018, SB-24-00-008, SB-22-00-010, SB-24-13-003 and SB-24-32-001, and confirm the current firmware version. The RAR snippets do not identify which article states the CIV rule. I did not check Bulgarian registration rules.
- **Sources:** [tesla.com](https://www.tesla.com/de_lu/support/recall-vehicle-firmware-correct-tpms-malfunction), [electrive.com](https://electrive.com/2026/08/27/huge-tesla-recalls-in-china-while-european-authorities-remain-cautious), [antena3.ro](https://www.antena3.ro/actualitate/rar-a-creat-pe-site-sectiunea-campanii-de-rechemare-pentru-ca-soferii-sa-verifice-daca-si-masina-lor-e-vizata-cum-functioneaza-792367.html), [capital.ro](https://www.capital.ro/decizie-pentru-soferii-din-romania-anuntul-facut-de-rar-trebuie-sa-verificati-este-gratuit.html), [avocatnet.ro](https://www.avocatnet.ro/articol_70007/Rechem%C4%83rile-auto-in-service-Care-sunt-drepturile-%C8%99oferilor-conform-directorului-RAR.html), [car-recalls.eu](https://car-recalls.eu/ro/vin-check-recalls/Tesla/)

### 18. Unidentified KBA recall: 142,781 Model 3/S/X/Y built 2016-2022 (low confidence, NOT re-verified)

car-recalls.eu lists a KBA recall of 142,781 Tesla Model 3, S, X and Y built between 2016 and 2022. The defect, reference number and remedy were cut off in the snippets.

- **This car:** UNKNOWN. The window includes 2022, so this needs a check in the KBA database or with Tesla.
- **Sources:** [car-recalls.eu](https://car-recalls.eu/ro/recall-news/kba-recalls/Tesla/model-y/), [car-recalls.eu](https://car-recalls.eu/es/recall-news/kba-recalls/Tesla/model-y/)

## Corrections to the first pass

- KBA 011850 / SB-22-00-009 (CPU cooling): round 1 said 'POSSIBLY IN SCOPE'. The OTA fix began 3 May 2022, and China's equivalent covered Shanghai builds only up to 26 Apr 2022 (firmware 2022.12.3.3). A ~Aug 2022 build is probably NOT in scope. Round 1's open question about the Ryzen MCU does not affect this.
- KBA 011824 / SB-22-00-010 (eCall): round 1 said 'LIKELY IN SCOPE'. It was published 29 Jun 2022 and covers 59,129 cars worldwide, about 6 weeks before this car's build. Scope is UNCERTAIN; the fix is software either way.
- KBA 14692R (TPMS): round 1 said 'probably in scope, range unknown'. The Model Y window is 20 Jan 2020-23 Nov 2024 (387,642 cars worldwide), so it is IN SCOPE. The fix is UN R141-compliance firmware 2024.38.7/.10 or 2024.40 or later (not 2024.44/2024.44.1), OTA.
- KBA 13972R (seat-belt warning): round 1 said 'about 180,000'. The exact figures are 183,450 worldwide and 6,725 in Germany; KBA publication 29 Jul 2024 (aggregator). It extends the 2022 US recall of 817,143 cars. Remedy is software.
- China Dec 2021 recall (21,599 Model Y): round 1 called it 'suspension, part not given'. It was the front/rear steering knuckles (转向节) not meeting strength requirements. The EU counterpart is Safety Gate A12/00503/22 (Model Y built Jun 2020-Nov 2021, reported by Germany, published 1 Apr 2022).
- China May 2023 and Jan 2024 recalls, marked 'background knowledge' in round 1, are now verified. May 2023: 1,104,622 cars built 12 Jan 2019-24 Apr 2023, regen choice and hard-acceleration warning, OTA from 29 May 2023. Jan 2024: 1,610,105 cars built 26 Aug 2014-20 Dec 2023, Autosteer misuse, OTA.
- Round 1 missed the China Dec 2022 rear-position-lamp software recall: 292,855 Shanghai Model Y built 1 Jan 2021-11 Nov 2022, OTA. Its window covers this car. The US and Australia ran parallel Nov 2022 recalls.
- Round 1 missed the China May 2022 CPU recall (107,293 Shanghai Model 3/Y built 19 Oct 2021-26 Apr 2022).
- Round 1 missed a possible EU seat-back weld notice (SB-24-13-003, Model Y built 22 Jun 2022-25 Mar 2024, reported via Safety Gate by Germany per Autofacil). Its window covers this car and it is likely a workshop remedy. It is single-source, so ask Tesla.
- Round 1 said 'No EU Safety Gate entry for Model Y'. At least one exists (A12/00503/22, steering knuckles), and the Autofacil report cites a second (SB-24-13-003).
- KBA '12321' / SB-24-32-001: Australia REC-005875 shows SB-24-32-001 is a notchy steering feel in the cold (4,383 MY2022-23 Model 3/Y, no safety hazard, fix firmware 2023.38 or later). The 'summer 2023 builds' window and the '12321' reference are unverified. The auto motor und sport 'Servolenkung zickt' article appears to describe 14811R instead.
- KBA 14811R: remedy confirmed as firmware 2023.38.4 or later via OTA (one source says workshop). Australian counterpart REC-006300 (297 cars, Mar 2025).
- Aug 2026 China door recall: Model Y count is 1,956,713; campaign starts 25 Sep 2026. The EU status is now sourced: no EU recall yet, the RDW (Tesla's EU type-approval authority) is monitoring, and the KBA has had an investigation open since April 2026 after the Schwerte fatal crash.
- Romania RAR: round 1 said 'background knowledge, RAR checks campaigns'. Snippets now say RAR issues a CIV only after important safety recalls are completed. RAR's 'Campanii de rechemare' section routes users to brand checks, and recall work is free in the Romanian authorised network even for cars bought abroad.

## Open questions

- Is SB-24-13-003 (Model Y seat-back frame welds, built 22 Jun 2022-25 Mar 2024) real, which factory does it cover, and is it open on this VIN? There is only one secondary source (Autofacil), and no Safety Gate alert number was found.
- What is the defect and KBA reference of the car-recalls.eu-listed KBA recall of 142,781 Model 3/S/X/Y built 2016-2022?
- What is the exact production/VIN range of KBA 011824 (eCall)? Does it include Aug 2022 Shanghai builds?
- Has Tesla filed an EU (RDW) recall for HW3 rear-camera delay (US 26V283) or for the China-style door-release labels and window-drop OTA after Aug 2026?
- Was there an EU/KBA counterpart to the China Dec 2022 and US Nov 2022 rear-light software recall? None was found.
- Is the car EU-market or China-domestic? This decides whether the SAMR recalls (Dec 2022 lamps, May 2023 regen, Jan 2024 Autosteer, Aug 2026 doors) legally apply.
- What is the actual build date from the B-pillar label, to confirm ~Aug 2022 against the window boundaries (eCall 2022, seat welds from 22 Jun 2022)?
- Not checked: UK DVSA entries (no results), Norway, NZ, Korea, Japan, RDW recall list (no results), and Bulgarian rules (whether ИААА/КАТ require completed recalls at registration of an import).
- Does the KBA Rückrufdatenbank support VIN lookup? One article implies it does; this is unverified.

## Follow-up check (main session, 2026-10-12)

- I searched for "SB-24-13-003" plus seat-weld and Safety Gate wording and found no record of it. The only matching Tesla seat-weld recall is **SB-24-13-004** (NHTSA 24V886000): 27 Model Y built 28–30 Oct 2024 at Giga Texas, where the weld attaching the seat recliner to the front seat back can fail and the seat is replaced. A separate SB-25-13-003 (seat-back fasteners) covers 2026 model-year cars. The Autofacil "SB-24-13-003, built 22 Jun 2022–25 Mar 2024" item is therefore **unconfirmed and may be a mix-up**. It is still worth naming when asking Tesla for this VIN's campaign list. — [carcomplaints.com](https://www.carcomplaints.com/news/2024/tesla-model-y-vehicles-recalled-seat-welds.shtml), [driveteslacanada.ca](https://driveteslacanada.ca/model-y/tesla-recalls-27-model-y-vehicles-over-seat-weld-defect/), [auto-recalls.justia.com](https://auto-recalls.justia.com/tesla/model-y/2024/24v886000)
