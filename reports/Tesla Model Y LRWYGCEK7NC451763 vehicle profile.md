# LRWYGCEK7NC451763 is an August 2022 Shanghai-built Model Y Long Range with no public history

The VIN is valid: the check digit recomputes to the **7** in position 9. It decodes to a **Tesla Model Y Long Range AWD**: dual motor, nickel-based (NCM, not LFP) battery, left-hand drive, five seats, built at **Giga Shanghai in calendar year 2022**. Neighbouring serial numbers put its factory-gate date at about **10–11 August 2022** (likely window 8–13 August). If it was sold new in the EU, it was probably first registered in September or early October 2022. For that build date it should have the HW3 Autopilot computer, the AMD Ryzen touchscreen computer, no front radar, all 12 ultrasonic parking sensors, and the LG Energy Solution "5L" pack of about 78 kWh nominal / 75 kWh usable. **No listing, auction lot, damage record or history page for this exact VIN is indexed anywhere I could search.** That covers more than 55 searches in nine languages across classifieds, salvage auctions and VIN-history sites. It says little, because most of those sites hide VINs from search engines.

For a buyer on 12 October 2026, three points matter most:

- **Built for Europe or for China?** The VIN cannot tell. A GB/T charge port or a missing EU certificate of conformity (CoC) means a grey import without Tesla's EU warranty.
- **Warranty.** The 4-year / 80,000 km basic warranty has very probably **just expired**. It runs from Tesla's delivery date, probably Sep–Oct 2022. The battery and drive unit stay covered to about **Sep–Oct 2030 or 192,000 km**.
- **Condition.** The Model Y came **last of 110 models** in the 2–3-year class of TÜV Report 2026 (17.3% with significant defects), mainly for suspension, brake discs and lights.

Clean EU-spec 2022 Long Range AWDs ask about **€30–36k** in Romania, Bulgaria and Germany in October 2026, depending on mileage. Bought from a private seller in Romania, the car carries **no VAT** in either country. Bulgaria then adds a product fee of about €92–96, possibly a municipal acquisition tax, and transport. **Every fact here comes from search-engine snippets.** WebFetch could not reach any site from this environment, including Tesla, NHTSA and the VIN-history services. The detailed, cited notes are in [research_notes/Tesla Model Y LRWYGCEK7NC451763](../research_notes/Tesla%20Model%20Y%20LRWYGCEK7NC451763/).

## The VIN decodes cleanly to a Shanghai Long Range AWD

| Position | Value | Meaning | Basis |
|---|---|---|---|
| 1–3 | LRW | Tesla, Giga Shanghai | Tesla service manual |
| 4 | Y | Model Y | Tesla service manual |
| 5 | G | 5-door SUV, left-hand drive (right-hand-drive cars read H) | Real VINs: AU/NZ/HK/UK cars read LRWYH… |
| 6 | C | Restraint system, 5-seat, non-North-American package | Third-party decoders; Tesla's exact wording not found |
| 7 | E | Electric, non-LFP lithium-ion (NCM) | LFP RWD cars read F |
| 8 | K | Dual motor, non-Performance = **Long Range AWD** | Third-party decoders; every LRWYGCEK car found is LR AWD |
| 9 | 7 | Check digit | Recomputed: weighted sum 414, mod 11 = 7 |
| 10 | N | **Built in calendar 2022** (Shanghai/Berlin rule, not model year) | Tesla service manual |
| 11 | C | Giga Shanghai plant | Tesla service manual |
| 12–17 | 451763 | Production serial (Model Y counter, separate from Model 3) | Model 3 / Model Y date pairs |

Tesla's Model Y service manual lists **LRW** for Shanghai, **C** for the Shanghai plant, and **D, E, F, J, K, L, R, S** as digit-8 codes. It also says that for Shanghai and Berlin cars, digit 10 is the **calendar year the car was built**, so "N" cannot be a late-2021 car ([Tesla service manual](https://service.tesla.com/docs/ModelY/ServiceManual/en-us/GUID-0C797294-574D-4EE4-8017-C339A7D58411.html)). The search extracts never paired "K" with its official label. The meaning comes from third-party decoders, which describe K as "two standard motors, hairpin windings" ([shop4tesla](https://www.shop4tesla.com/en/pages/tesla-ratgeber-tesla-vin-decoder); [FindMyElectric](https://www.findmyelectric.com/tesla-vin-decoder/)). Every real car with this prefix agrees: 17vin decodes LRWYGCEK as the China-built Long Range AWD for 2021–2024 ([17vin](https://en.17vin.com/model/xpviy.html)), and tesla-info lists siblings such as LRWYGCEK7NC455876 as a 2022 Long Range AWD ([tesla-info](https://tesla-info.com/car/DE-LRWYGCEK7NC455876)). The other trims use different codes. Shanghai Performance cars read **LRWYGCEL**, and Shanghai RWD cars read **LRWYGCFS** (LFP battery). An old decoder note calling "K" China-only is out of date, because Berlin-built Long Range cars read **XP7YGCEK** ([tesla-info](https://tesla-info.com/car/DE-XP7YGCEK1PB129059)).

## It left the factory around 10–11 August 2022

Shanghai Model Y serials run on one counter shared by China-domestic and export cars, RWD and AWD, and both left- and right-hand drive. Model 3 has its own counter. Published factory-gate dates for nearby serials bracket this car closely:

| Serial | Car | Factory gate | First registration |
|---|---|---|---|
| 424830 | LRWYGCFS6NC424830 (China RWD) | 28 Jul 2022 | Delivered in Guangzhou, 3 Aug 2022 ([tesla-info](https://tesla-info.com/car/CN-LRWYGCFS6NC424830)) |
| **451763** | **this car** | **≈10–11 Aug 2022 (interpolated)** | **≈Sep–Oct 2022 if EU** |
| 452426 | LRWYGCEK5NC452426 | — | Finland, 9/2022 (Finnish listings, snippet only: [Nettiauto](https://www.nettiauto.com/en/tesla/model-y/15734109), [Nettiauto](https://www.nettiauto.com/yritys/2308090/vaihtoautot/15863549)) |
| 455876 | LRWYGCEK7NC455876 | 13 Aug 2022 | Germany, 9 Sep 2022 ([tesla-info](https://tesla-info.com/car/DE-LRWYGCEK7NC455876)) |
| 461600 | LRWYGCEK7NC461600 | 17 Aug 2022 | Germany, 26 Sep 2022 ([tesla-info](https://tesla-info.com/car/DE-LRWYGCEK7NC461600)) |

Between 28 July and 13 August the counter advanced about 1,940 serials a day. That fits August 2022, a record month in which Shanghai built 56,721 Model Ys after its line upgrades ([CnEVPost](https://cnevpost.com/2022/06/23/teslas-shanghai-plant-will-reportedly-finish-upgrades-around-august-7-with-significant-capacity-increases); [Drive Tesla](https://driveteslacanada.ca/?p=57536)). German forum members reported "NC45xxxx" cars delivered around 24 September 2022 ([TFF Forum](https://tff-forum.de/t/model-y-vin-vergabe-2022/210397)). This is an interpolation, not a record of this car. **The build month is printed on the label on the driver-side B-pillar and should read 08/2022.**

The VIN cannot show whether the car was built for Europe or China. China-domestic cars use the same LRWYGC prefix, and serial 424830, a few thousand below this car, was delivered in Guangzhou. The neighbours registered in Germany and Finland make an EU car likely, but not certain.

## What it should have, and how the car itself confirms it

| Item | Expected for an Aug-2022 Shanghai LR AWD | Source |
|---|---|---|
| Battery | LG Energy Solution 2170 NCM "5L": 78.1 kWh nominal / 75.0 kWh usable, 4,416 cells (other sources give 78.4 / 76.8 / 81.65 kWh) | [EV Database](https://ev-database.org/car/1619/Tesla-Model-Y-Long-Range-AWD), [akku-brief](https://akku-brief.de/en/models/tesla-model-y) |
| Motors | Front 3D3 induction + rear permanent-magnet (3D5 or 3D7); EU figure about 378 kW / 514 PS, 493 Nm, but sources conflict, so read the CoC | [EV Database](https://ev-database.org/car/1182/Tesla-Model-Y-Long-Range-AWD), [42how](https://www.42how.com/en/article/3048) |
| Performance | 0–100 km/h 5.0 s, 217 km/h | [EV Database](https://ev-database.org/car/1619/Tesla-Model-Y-Long-Range-AWD) |
| WLTP range | 533 km listed for sibling 461600 on 19" Gemini; 565 km on 19" also reported after the 5L pack. Unresolved: the CoC shows the homologated figure | [tesla-info](https://tesla-info.com/car/DE-LRWYGCEK7NC461600), [teslamag](https://teslamag.de/news/mehr-reichweite-tesla-model-y-europa-performance-maerz-aus-deutschland-44770) |
| Charging | DC peak 250 kW; AC 11 kW three-phase (a 22 kW wallbox gives nothing extra) | [EV Database](https://ev-database.org/car/1619/Tesla-Model-Y-Long-Range-AWD) |
| Space, towing | Boot 854 L (measured to the roof), frunk 117 L; 1,600 kg braked towing if hitched (factory hitch €1,350 in Germany from May 2022) | [EV Database](https://ev-database.org/car/1619/Tesla-Model-Y-Long-Range-AWD), [shop4tesla](https://www.shop4tesla.com/en/blogs/news/anhangerkupplung-fur-das-model-y-jetzt-konfigurierbar-zinssatz-erhoht) |
| Computers | HW3 ("Full self-driving computer"); AMD Ryzen touchscreen computer; HW4 reached Shanghai Model Y only from late 2023 | [Drive Tesla](https://driveteslacanada.ca/news/tesla-adds-hw4-and-quicksilver-to-model-y-from-giga-shanghai/), [Electrek](https://electrek.co/2021/12/28/tesla-launches-amd-chip-12v-li-ion-battery-2022-model-3-y/) |
| Sensors | No radar (Europe-bound cars from April 2022); 12 ultrasonic sensors (removed only from October 2022) | [Tesla EU](https://www.tesla.com/en_eu/support/transitioning-tesla-vision), [Tesmanian](https://www.tesmanian.com/blogs/tesmanian-blog/tesla-model-3-and-y-without-radar-will-start-delivering-to-europe-from-q2-2022) |
| Other | Heat pump standard; 15.5 V lithium-ion low-voltage battery; heated steering wheel and rear seats likely | [EV Database](https://ev-database.org/car/1619/Tesla-Model-Y-Long-Range-AWD), [Tesla service manual](https://service.tesla.com/docs/ModelY/ServiceManual/en-us/GUID-8CBDB47F-0D3A-4827-AB98-982A92234D79.html) |
| Paint | Pearl White, Solid Black, Midnight Silver, Deep Blue or Red Multi-Coat. Quicksilver and Midnight Cherry Red were Berlin-only from October 2022 | [Carscoops](https://www.carscoops.com/2022/10/tesla-model-y-gains-two-new-multi-layer-paint-options-in-europe-and-middle-east/) |

These quick checks confirm the build date and the market:

| Check | Expected | If not |
|---|---|---|
| Charge port | **CCS2** (Type 2 plus two DC pins) | **GB/T means a China-market car**: no EU warranty, and it needs adapters. Walk away ([Tesla China manual](https://www.tesla.com/OWNERSMANUAL/modely/en_cn/GUID-2AFEEA7F-3FF1-4544-B23B-488EAD0E199F.html)) |
| CoC and papers | Tesla EC CoC with an **e4\*** type approval (Tesla's EU approvals come from the Dutch RDW), Type 003; first registration in an EU state | A missing CoC or individual approval points to a non-EU car ([kenteken.tv](https://blog.kenteken.tv/2022/07/17/two-new-european-type-approval-numbers-for-tesla-models/)) |
| B-pillar label | Built 08/2022; VIN matches the windscreen plate and the papers | Any mismatch is an identity question |
| Bumpers | 12 round ultrasonic sensor discs | None means built October 2022 or later, which contradicts the VIN |
| Controls > Software > Additional Vehicle Information | Full self-driving computer (HW3), AMD Ryzen | HW4 or Intel Atom contradicts a mid-2022 Shanghai build |
| Paint code | One of the five 2022 Shanghai colours | Quicksilver or Midnight Cherry Red means a respray or wrap |

## Nothing about this exact car is public

The search covered more than 55 queries. They used the full VIN, lower-case and partial forms (NC451763, LRWYGCEK7NC45…), and pairings with Romanian, Bulgarian, German, Polish, Nordic, Dutch, French, Czech, Ukrainian and Korean classifieds, EU salvage-auction archives, VIN-history aggregators and Tesla inventory trackers. **No indexed page contains this VIN.** Two pages surfaced for VIN queries, but both belong to other cars: AUTO.RIA 37048811 is LRWYGCEK7NC259159, and Nettiauto 15732595 is LRWYGCEK9NC219844. Similar cars from this batch do appear on [carsbat.com](https://carsbat.com/de/detail/lrwygcek8nc462240-ipx7nu/) (EU Copart/OPENLANE archive) and in Tesla's used inventory, and one neighbour, 461600, is listed with "Previous Accidents" ([tesla-info](https://tesla-info.com/car/DE-LRWYGCEK7NC461600)). The empty result is not a clean history. Search carsbat.com, ev-inventory.com and autobaza.pl by hand in a browser, and buy a paid report (below).

One lead to keep apart: the Varna dealer Тесла БГ listed a **damaged** 2022 Long Range 4x4, production August 2022, about 129,000 km, at €11,900 excluding VAT (listing dated 14 Aug 2026) ([tesla.mobile.bg](https://tesla.mobile.bg/obiava-11718521894513606-tesla-model-y-long-range-4x4)). No VIN is visible. A bazar.bg ad with the same 129,000 km describes a car coming from Canada, which would make it North American and not this car ([bazar.bg](https://bazar.bg/obiava-54721702/tesla-model-y-long-range-4x4-2022)).

## The basic warranty has probably just run out; the battery is covered to about 2030

Tesla's EU terms give **4 years / 80,000 km basic cover** and **8 years / 192,000 km with at least 70% capacity** for the Long Range battery and drive unit ([Tesla EU warranty](https://www.tesla.com/en_EU/support/vehicle-warranty)). Cover starts on the day **Tesla delivers the car to its first buyer**, or the day it first goes into service, whichever is earlier. The registration date does not set it ([Tesla EU NVLW PDF](https://digitalassets.tesla.com/tesla-contents/image/upload/tesla-new-vehicle-limited-warranty-en-eu.pdf)). The siblings show delivery can follow registration by weeks: 461600 was registered on 26 Sep 2022 with battery cover to 29 Sep 2030, and 455876 was registered on 9 Sep 2022 with battery cover to October 2030. So this car's basic warranty most likely ended between mid-September and October 2026. **If it was delivered on or after 12 Oct 2022 and is under 80,000 km, a few days or weeks may remain.** In that case, get any fault logged with Tesla now. Cover follows the car to a new owner, but only in the **warranty region where Tesla first sold it**. A China-market car brought into the EU should not expect EU cover.

If the car comes from Tesla's own used stock, Tesla adds a **Used Vehicle Limited Warranty** of 1 year / 20,000 km ([Tesla UVLW PDF](https://digitalassets.tesla.com/tesla-contents/image/upload/tesla-used-vehicle-limited-warranty-en-gb.pdf)). I found no Tesla Extended Service Agreement on sale in Europe, and the 2025 US launch excluded used purchases ([Not a Tesla App](https://www.notateslaapp.com/news/2844/tesla)).

Software and service access:

- **FSD and other purchased software.** Purchased FSD stays with the car on a private sale ([Tesla EU](https://www.tesla.com/en_eu/support/fsd-transfer)). But Tesla's free FSD transfer offer (new cars delivered from 18 Jul 2025, extended into Q4 2025) reset donor cars to basic Autopilot, so check the package on the car itself.
- **FSD (Supervised) in Europe.** It is approved in 8 EU states as of 29 Sep 2026, not including Bulgaria or Romania. It runs only on HW4, and the HW3 "v14 Lite" build is US and Canada only ([fsd-eu-tracker](https://fsd-eu-tracker.de/en/); [Electrek](https://electrek.co/2026/04/28/tesla-promises-fsd-v14-lite-hw3-international-markets/)).
- **Service in Bulgaria.** Tesla BGR EOOD was registered in Sofia on 18 Feb 2026 and is hiring service staff, but **no Sofia service centre is confirmed open**. Warranty work means Tesla Center Bucharest-Voluntari (Mon–Fri 08:00–16:30) or Thessaloniki ([Tesla Find Us](https://www.tesla.com/findus/location/service/TeslaCenterBucharestPipera); [Drive Tesla](https://driveteslacanada.ca/news/tesla-bulgaria-expansion/)).
- **Superchargers in Bulgaria.** There are two in Sofia (Paradise Center, Bulgaria Mall) and one in Plovdiv ([Tesla](https://www.tesla.com/en_EU/findus/list/superchargers/Bulgaria)).

## Recalls: all confirmed items are software fixes, one seat item is unconfirmed

| Campaign | Issue | Remedy | This car |
|---|---|---|---|
| KBA 14692R / SB-24-00-018 | TPMS warning not kept between drive cycles (UN R141); Model Y built 20 Jan 2020–23 Nov 2024 | Over the air: firmware 2024.38.7/.10 or 2024.40+ (not 2024.44/.44.1) | **In scope**; closed on current firmware ([Tesla](https://www.tesla.com/de_lu/support/recall-vehicle-firmware-correct-tpms-malfunction); [ams](https://www.auto-motor-und-sport.de/verkehr/tesla-rueckruf-softwareproblem-reifendruckwarnsystem/)) |
| KBA 13972R / SB-24-00-008 | Seat-occupancy detection / seat-belt warning; 183,450 cars | Software | Probably in scope ([Autohaus](https://www.autohaus.de/nachrichten/autohersteller/passagiererkennung-und-gurtwarnung-defekt-tesla-ruft-180-000-modelle-zurueck-3544566)) |
| KBA 011824 / SB-22-00-010 | eCall may fail, "2022 production"; published 29 Jun 2022 | Software | Uncertain: published before this build ([ams](https://www.auto-motor-und-sport.de/verkehr/rueckruf-tesla-model-3-y-ausfall-des-e-call-systems/)) |
| KBA 011850 / SB-22-00-009 | Touchscreen CPU overheating | Over the air from May 2022; China scope ended at builds of 26 Apr 2022 | Probably not ([Gasgoo](https://autonews.gasgoo.com/articles/news/tesla-recalls-107293-locally-made-model-3s-model-ys-in-china-70020351)) |
| SB-24-32-001 (AU REC-005875) | Steering feels notchy in the cold; 2022–23 cars; no safety hazard | Firmware 2023.38+ | Possibly; closed on current firmware ([vehiclerecalls.gov.au](https://www.vehiclerecalls.gov.au/recalls/rec-005875)) |
| "SB-24-13-003" (Autofacil) | Seat-back frame missing welds, Model Y built 22 Jun 2022–25 Mar 2024 | Probably workshop | **Unconfirmed.** I found only the US SB-24-13-004 (27 Texas cars, Oct 2024), so this may be a mix-up. Ask Tesla anyway ([Autofacil](https://www.autofacil.es/tesla-model-y-revision/); [Drive Tesla](https://driveteslacanada.ca/model-y/tesla-recalls-27-model-y-vehicles-over-seat-weld-defect/)) |
| KBA 14811R; Safety Gate A12/00503/22 | Power-steering loss (2023 builds); steering knuckles (builds to Nov 2021) | — | Not in scope |

If the car turns out to be **China-market**, four Chinese SAMR recalls cover its build date, all fixed by software or labels. They are rear position lamps (Dec 2022), regenerative-braking choice and accelerator warning (May 2023), Autosteer (Jan 2024), and **hard-to-find emergency door releases** (Aug 2026: labels plus an over-the-air update that drops the windows after a crash). There is no EU door-release recall yet. The RDW is monitoring, and the KBA has had an investigation open since April 2026 ([electrive](https://electrive.com/2026/08/27/huge-tesla-recalls-in-china-while-european-authorities-remain-cautious)). Either way, learn where the mechanical door releases are. The US recall 26V283 (HW3 rear-camera delay on firmware 2026.8.6) is a US filing, so just make sure the car is not stuck on that version. Only Tesla Service can print the open and closed campaigns for this VIN. In Romania, RAR issues registration documents only after important safety recalls are done ([Antena 3](https://www.antena3.ro/actualitate/rar-a-creat-pe-site-sectiunea-campanii-de-rechemare-pentru-ca-soferii-sa-verifice-daca-si-masina-lor-e-vizata-cum-functioneaza-792367.html)).

## Condition: TÜV ranks this model last, so check suspension, brakes and lights first

In TÜV Report 2026 the Model Y came **last of 110 models** in the 2–3-year class at **17.3%**. That is the worst figure in that class in ten years, driven by axle suspension, brake discs and lighting ([mobiflip](https://www.mobiflip.de/tuev-report-2026-tesla-stuerzt-auf-letzten-platz/); [ecomento](https://ecomento.de/2025/11/20/tuev-report-2026-tesla-modelle-auf-letztem-und-drittletztem-platz-bei-juengeren-fahrzeugen/)). There is no 4–5-year Model Y figure yet. The closely related Model 3 scored 21.0% at 4–5 years (about 86,000 km), third-worst in that class. Breakdowns are a different story: ADAC rates the Model 3 at 0.7 per 1,000 cars, and flat low-voltage batteries cause 45.4% of all ADAC call-outs ([auto motor und sport](https://www.auto-motor-und-sport.de/verkehr/adac-pannenstatistik-2026-warum-ausgerechnet-toyota-schlecht-abschneidet/)).

Battery benchmarks:

- **Typical health.** Aviloo's Model Y median state of health (SoH) is **94.5% at 50,000 km and 90.3% at 150,000 km** ([transportandenergy.com](https://transportandenergy.com/?p=35198)). Geotab measures **2.3% a year** on average, 1.5% with little fast charging and 3.0% with heavy >100 kW use ([Electric Autonomy](https://electricautonomy.ca/ev-supply-chain/batteries/2026-01-13/latest-geotab-study-finds-ev-batteries-lose-just-2-3-life-per-year/)). Expect about **90–94%**. I treat **below about 88%** at moderate mileage as a red flag; that threshold is mine, not a published one.
- **The LG pack dispute.** In November 2025 the Croatian repair shop EV Clinic claimed that Nanjing-made LG NCM811 packs, the type this car most likely has, reach end of life around 240–250k km and are mostly unrepairable at cell level. That is one shop's view of failed cars, and New Mobility News and fleet data dispute how far it generalises ([InsideEVs](https://insideevs.com/news/780568/tesla-lg-battery-pack-defects-china/); [New Mobility News](https://newmobility.news/2025/12/02/how-credible-is-ev-clinics-warning-on-teslas-china-built-nmc-batteries/)). It matters if you plan to keep the car past 2030 or 192,000 km.
- **One measured LG car.** A 2022 LG-pack Model Y LR measured 11.5% down at about 155,000 km ([InsideEVs](https://insideevs.com/features/754691/tesla-model-y-degradation-test/)).

Inspection checklist for this car:

1. **Papers.** Registration certificate field B (first registration), Tesla invoice or delivery date, EU CoC, all ITP/TÜV reports, Tesla service invoices. Look for yearly brake-caliper cleaning and lubrication on salted roads, and the 4-year brake-fluid check, which is due about now ([Tesla maintenance](https://www.tesla.com/ownersmanual/modely/en_sg/GUID-E95DAAD9-646E-4249-9930-B109ED7B1D91.html)).
2. **Battery Health test**, run by the seller. Go to Controls > Service > Battery Health Test. It needs AC of at least 5 kW, a start below 20%, no alerts and no pending update, and takes up to 24 h ([Tesla manual](https://www.tesla.com/ownersmanual/modely/en_il/GUID-B9807218-7291-4F68-9AFF-7C525CF498F3.html)). Ask for a photo of the result with the odometer visible, or pay for an Aviloo test.
3. **Service Mode.** Controls > Software, hold "MODEL", type "service". Read the active alerts and camera status; do not drive in this mode ([Not a Tesla App](https://www.notateslaapp.com/news/2046/tesla-service-mode-how-to-access-it-and-what-it-does)).
4. **Wheels, brakes and suspension.** Brake discs inside and out, rear especially (rust band or lip). Front upper control-arm ball joints and bushings: creaks or knocks over bumps below 30 km/h, and play on a lift. All lights and their aim.
5. **Heat pump.** Full heat, defrost and A/C. Cold-air-only faults are reported from Nordic winters.
6. **Cameras and body.** Every camera view after a drive (B-pillar cameras can fog). Windscreen and roof glass. Paint thickness on each panel. Underbody pack and jacking points. Water in the sub-trunk. Tyre wear and alignment.
7. **Identity.** The physical checks in the table above: CCS2 port, B-pillar date, ultrasonic sensors, HW3/Ryzen, paint code.

## Price: about €29–34k for a clean car, depending on mileage

October 2026 market averages for 2022 Model Ys in Germany, all variants:

| Source | Figure |
|---|---|
| AutoUncle.de | Average ask **€34,877** (5th–95th percentile €29,188–39,992), median 62,200 km, **−€3,180 over 12 months** ([AutoUncle](https://www.autouncle.de/de/gebrauchtwagen/Tesla/Model%20Y/y-2022)) |
| mobile.de | €32,692–35,982 ([mobile.de](https://suchen.mobile.de/auto/tesla-model-y-2022.html)) |
| AutoScout24.de | Average **€34,575** ([AutoScout24](https://www.autoscout24.de/auto/tesla/tesla-model-y/)) |

About 30 individual asks for 2022 Long Range AWDs in Romania, Bulgaria, Germany and other EU markets give these bands:

| Mileage | Asks seen (VAT-inclusive or margin scheme) | Fair negotiated price (my estimate) |
|---|---|---|
| under 60,000 km | €32–36k (e.g. Bulgaria 54,000 km €33,500; Otopeni dealer 55,286 km €35,900) | €31–34k |
| 60–100,000 km | €30–35k (e.g. Netherlands 98,126 km, 92% SoH, €30,800; Germany 85,884 km €34,990) | €29–32.5k |
| 100–150,000 km | €27–34k (e.g. Romania 129,000 km €31,000; Germany 143,134 km €26,980) | €26–30k |
| over 150,000 km | Thin: €25k at 260,000 km | ≈€22–27k |

Bulgarian dealers already holding registered EU cars ask **€33.5–37k** ([mobile.bg](https://www.mobile.bg/obiavi/avtomobili-dzhipove/tesla/model-y)). Romanian dealer ads marked **"NET + TVA" need 21% added** for a private buyer ([autovit.ro](https://www.autovit.ro/autoturisme/anunt/tesla-t-model-y-ver-long-range-dual-motor-awd-ID7HQz7X.html)). Damaged or North-American imports at €12–24k are not comparable. New cars cap what this one is worth: a new **Model Y Standard costs €39,990 in Germany** and a **Standard Long Range RWD €46,990 in Romania**, both with fresh warranties ([web.de](https://web.de/magazine/auto/tesla-model-y-standard-test-y-basis-konkurrenz-vergleich-42719868); [playtech.ro](https://playtech.ro/2026/tesla-aduce-in-romania-model-y-standard-long-range-cu-tractiune-spate-657-km-autonomie-si-o-pozitionare-interesanta-la-46-990-euro/)). Values are still falling by about €250–300 a month. Take €1–3k off for SoH below about 90%, an expired basic warranty, worn tyres or discs, or missing service records.

## Run these history checks before paying

| Check | Cost | Input | What it shows |
|---|---|---|---|
| RAR "Istoric vehicul" (Romania) | Free | VIN + email | RAR-recorded odometer readings, ITP validity, technical data, but only if RAR has ever seen the car ([alba24](https://alba24.ro/istoric-vehicul-rar-a-lansat-aplicatia-online-prin-care-se-poate-verifica-numarul-de-kilometri-al-masinilor-702900.html)) |
| RAR Auto-Pass (Romania) | 42 lei, valid 60 days | VIN | Odometer history, accidents, serious brake/steering damage, repairs, recalls; free "no record" certificate if RAR has none ([economica.net](https://www.economica.net/registrul-auto-roman-va-emite-de-la-1-decembrie-2024-certificatul-rar-auto-pass_723849.html)) |
| AIDA RCA check (Romania) | Free | Plate or VIN | Current insurer and policy dates, which show whether it is on Romanian plates now ([playtech.ro](https://playtech.ro/2026/verificarea-rca-online-in-2026-cum-afli-rapid-daca-o-masina-are-polita-valabila/)) |
| Vincario stolen check | Free | VIN | Police databases of RO, CZ, HU, SK, SI, IT (not BG or DE) ([vincario.com](https://vincario.com/stolen-vehicle-check/)) |
| RNPM (formerly AEGRM, Romania) | Fee not found | Via notary or operator | Pledges, leasing notices, seizures ([infocontact.ro](https://www.infocontact.ro/cumparare-auto-sh-sechestru-gaj/)) |
| autoDNA | €24.99 (free preview) | VIN | Earlier registrations by country and date, odometer, damage, stolen flags ([review](https://www.carcheckervin.com/autodna-review)) |
| carVertical | Single price not found (≈$35 inferred from bundles) | VIN | Cross-check for autoDNA ([carVertical](https://www.carvertical.com/pricing)) |
| Tesla Service | Free | VIN (may answer only the owner) | Delivery date, warranty region and dates, open recalls, salvage or warranty-void flags |

No free source gives first-registration date and country from a VIN alone. Field B of the registration certificate, RAR or a paid report are the routes. Bulgaria has no public online pre-purchase stolen-vehicle check that I could find; KAT checks at registration.

## Buying it in Romania and registering it in Bulgaria

The used-car route differs from the new-car route in the earlier reports in five ways:

- **VAT.** A car is "used" for VAT once it is more than 6 months past first entry into service **and** has done more than 6,000 km. From a private seller there is then **no VAT in either country** ([Your Europe](https://europa.eu/youreurope/citizens/vehicles/cars/vat-on-cars-bought-abroad/index_en.htm)). From a dealer, the margin scheme means VAT is included and not shown; normal invoicing adds **21% Romanian VAT**, which is a final cost with no refund.
- **Getting it across the border.** Romanian red provisional plates are **valid only in Romania**, whoever holds them ([Romanian Border Police](https://www.politiadefrontiera.ro/ro/main/i-este-posibila-trecerea-frontierei-cu-un-vehicul-care-circula-cu-numere-de-inmatriculare-provizorii-7527.html)). Use a carrier, or Bulgarian "T" transit plates (€40.90 for a month, from KAT, MTPL required; it is unconfirmed whether KAT issues them while the car is still in Romania). Carrier options are in [Tesla Bucharest to Bulgaria car transport](Tesla%20Bucharest%20to%20Bulgaria%20car%20transport.md).
- **Romanian deregistration.** The seller deregisters (radiere) with a tax certificate and proof of export: the sale contract with a certified translation, or your Bulgarian registration. Put the agreed order of steps into the contract.
- **KAT registration.** Present the car in person **within 1 month**. Bring the Romanian registration certificate and CIV, the contract or invoice, a declaration of acquisition, proof the product fee was paid and MTPL. Foreign documents need a **legalised translation**. If the car has no valid EU roadworthiness certificate, the technical check is done at the traffic police point ([MVR](https://mvr.bg/upload/21666/62a323c3-dokumenti_za_reg_mps2pdf.pdf)).
- **Costs.**
  - **Product fee:** about €92–96 for a used EV up to 5 years old, charged since 1 Jul 2025. A repeal passed only first reading, and on 30 Sep 2026 the governing parties proposed to drop it, so assume you will pay ([Capital](https://www.capital.bg/politika_i_ikonomika/bulgaria/2026/09/30/4960892_upravliavashtite_s_novi_popravki_v_zakona_za/)).
  - **Annual vehicle tax:** €0 for an EV in the large municipalities.
  - **Acquisition tax:** municipal, possibly **0.1–3% of value**; ask your municipality ([minfin.bg](https://www.minfin.bg/bg/784)).
  - **Total:** I estimate **€400–700** on top of the price, plus MTPL and any acquisition tax, over **1–3 weeks**.

## What is still unknown, and how to settle it

| Unknown | How to settle it |
|---|---|
| EU-market or China-market car | Charge port (CCS2), EU CoC with an e4\* approval, EU first-registration document |
| Exact first-delivery date, so whether any basic warranty is left | Tesla invoice or delivery document; ask Tesla Voluntari by VIN |
| Mileage, accidents, salvage, fleet use | RAR Auto-Pass, autoDNA/carVertical, ITP/TÜV reports, Tesla service history shown live in the seller's app |
| Battery health | In-car Battery Health test or Aviloo |
| Options: wheels, hitch, colour, Autopilot/EAP/FSD | Controls > Software, the CoC, the car itself |
| Seller type and VAT; liens | Invoice wording (margin scheme vs +21%); RNPM search; owner field on the CIV |
| Tesla's own wording for "K" and the exact WLTP figure | Service manual page (not reachable here); this car's CoC |

Method: two multi-agent research passes on 2026-10-12. The first covered decode, footprint and specs; the second used per-agent search caps to redo warranty, recalls, reliability, prices, history checks and import, plus an adversarial re-check of the decode. I added three follow-up checks of my own. All web evidence came through search-engine snippets because WebFetch failed on every host. No private owner or seller details were collected.
