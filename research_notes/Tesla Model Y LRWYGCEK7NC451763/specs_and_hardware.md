# Specification and hardware: 2022 Shanghai Model Y Long Range AWD

Method note: researched 2026-10-12. WebFetch and curl could not reach any site from this environment (DNS failure on every host, including tesla.com, NHTSA, autoDNA and carVertical), so **every fact below comes from search-engine results and snippets, not from pages I opened**. First research pass (about 58 searches for this lens). A second pass filled the gaps (appended below).

## Takeaway

Strongest evidence says VIN LRWYGCEK7NC451763 is a Giga Shanghai-built 2022 Tesla Model Y Long Range AWD (dual motor). This is not RWD and not Performance. Two other cars with the same LRWYGCEK…N prefix are listed by tesla-info.com as 2022 Model Y Long Range AWD sold in Europe. One of them, LRWYGCEK7NC455876, has a serial only ~4,100 above this car, is listed as built in China and was first registered in September 2022. 17vin decodes LRWYGCEK as a China-built Long Range AWD. The 2022 China RWD uses a different prefix, LRWYGCFS. I recomputed the check digit and got 7, so the VIN is valid. From the neighbouring serial, this car was most likely built around July–September 2022. That is an inference, not a confirmed build date. For that build window the car should have: the LG Energy Solution 2170 NMC "5L" pack (78.1 kWh nominal / 75.0 kWh usable, 4,416 cells; Shanghai switched from the 5C pack, 75/72 kWh, in Jan–Feb 2022), a front 3D3 induction motor and a rear permanent-magnet motor (EU total 378 kW / 514 PS, 493 Nm), 0–100 km/h in 5.0 s, 217 km/h top speed, 250 kW peak DC charging, and 1,600 kg braked towing. After the 5L update, European WLTP range was 565 km on 19" and 533 km on 20" wheels. Tesla-info shows 533 km for the sibling cars. Hardware: HW3 (Shanghai Model Y did not get HW4 until about Oct 2023 to early 2024), AMD Ryzen MCU3 (Shanghai from Nov 2021, phased into all China/US Model 3/Y by Q2 2022), and a lithium-ion low-voltage battery (15.5 V "16 V", 6.9 Ah). It should have no front radar: Europe-bound Model 3/Y were delivered without radar from April 2022. It should still have the 12 ultrasonic parking sensors, which Tesla removed only from early October 2022 for Europe; Shanghai exports without them appear in late 2022 to early 2023. For comparison: the 2022 Performance had the same 5L pack, 393 kW, 514 km WLTP on 21", 250 km/h and 3.7–4.0 s 0–100. The Shanghai RWD had a CATL LFP pack of 60 kWh nominal / 57 usable, 455 km WLTP, 170 kW DC and 6.9 s, with European deliveries starting only around Nov–Dec 2022. The WebSearch budget (200 calls shared across all agents) ran out partway through. So these were NOT verified in this session: AC on-board charger rating, boot/frunk volumes, heat pump/Octovalve, castings, mirrors, tow-hitch option, and the 2022 colour/interior list. The car's own build date, wheels and options should be confirmed with the seller or Tesla (Tesla app, build sheet, or the sticker on the B-pillar).

## Cited findings

### 1. VIN decode / trim (high confidence)

The prefix LRWYGCEK is used on Shanghai-built Model Y Long Range AWD cars sold in Europe. tesla-info.com lists LRWYGCEK2NC235190 as a 'New 2022 Model Y Long Range AWD' (France, Pearl White, WLTP 533 km) and LRWYGCEK7NC455876 as a 'CPO 2022 Model Y Long Range AWD' (Munich area, Midnight Silver, black interior, built in China). 17vin.com decodes LRWYGCEK as a Tesla China Model Y Long Range AWD (2021, 2022 and 2023 entries; 2022 entry gives 0–100 in 5 s and 217 km/h).

- **This car:** This VIN shares the exact 8-character prefix and model-year code N, so it is almost certainly a 2022 Shanghai-built Model Y Long Range AWD, not RWD or Performance. The Performance-specific and RWD-specific specs below are for comparison only.
- **Sources:** [tesla-info.com](https://tesla-info.com/car/FR-LRWYGCEK2NC235190), [tesla-info.com](https://tesla-info.com/car/DE-LRWYGCEK7NC455876), [en.17vin.com](https://en.17vin.com/model/xpviy.html), [en.17vin.com](https://en.17vin.com/model/mbkl9.html), [en.17vin.com](https://en.17vin.com/model/fzzgb.html)

### 2. VIN decode / position 8 'K' and RWD prefix (medium confidence)

17vin decodes the different prefix LRWYGCFS as the '2022 modified Tesla MODEL Y Two Wheel Drive Rear Wheel Drive Edition' (launched 2022-08-09). So the China RWD uses different position 7–8 characters (F-S) than this car (E-K). One third-party blog lists position-8 'K' as 'two standard motors of the type Hairpin Windings (Y#DB, 3#DB)'. NHTSA's US decoders list only D/E/F for Model Y and do not include K, because K is a non-US code.

- **This car:** Supports K = dual motor (Long Range) for this VIN and argues against RWD. The 'hairpin windings' meaning of K comes only from one blog snippet and is unconfirmed.
- **Sources:** [en.17vin.com](https://en.17vin.com/model/mbn89.html), [yeslak.com](https://www.yeslak.com/blogs/tesla-guide/tesla-vin-decoder-all-check-digits-explained), [driveteslacanada.ca](https://driveteslacanada.ca/tesla-vin-decoder/), [insideevs.com](https://insideevs.com/news/561819/identify-tesla-origin-vin-decoder/)

### 3. VIN check digit (high confidence)

I recomputed the ISO 3779 check digit for LRWYGCEK7NC451763 locally: weighted sum 414, mod 11 = 7. This matches position 9.

- **This car:** The VIN is internally valid, so there is no sign of a typo or altered VIN.
- **Sources:** none (reasoning or local calculation)

### 4. Estimated build date (medium confidence)

Sibling car LRWYGCEK7NC455876 shows first registration in September 2022 and a battery warranty to October 2030 / 192,000 km on tesla-info.com. This car's serial (451763) is about 4,100 lower, so it was most likely built around July–September 2022. This is an inference: Shanghai serial-to-date mapping is not published, and the serial may be shared with Model 3.

- **This car:** I tie running changes to a mid/late-Q3-2022 build below. Confirm the actual production month from the build sticker on the B-pillar or door jamb, the Tesla app, or the seller's documents.
- **Sources:** [tesla-info.com](https://tesla-info.com/car/DE-LRWYGCEK7NC455876)

### 5. Battery pack (Long Range / Performance) (high confidence)

The 2022 Shanghai Long Range AWD and Performance use the LG Energy Solution 2170 NMC 'LG 5L' pack: 78.1 kWh nominal, 75.0 kWh usable, 4,416 cells (EV Database entry 1619, Feb 2022–Feb 2025). It replaced the 'LG 5C' pack, 75.0 kWh nominal / 72.0 kWh usable (EV Database entry 1182, Aug 2021–Jan 2022). Akku-brief dates the switch to the 5L/M50 cells to 02/2022 in Shanghai (earlier cells M48). fiches-auto lists the 5L as LG 2170L NMC at about 79 kWh gross. Teslamag says the larger battery was reportedly an LG pack internally called 5L. Panasonic cells (cited by some US-oriented spec sites) do not apply to Shanghai cars.

- **This car:** A Q3-2022 Shanghai Long Range build should have the LG 5L NMC pack (about 78–79 kWh gross, 75 kWh usable). This is useful for judging state of health: about 75 kWh usable is the new-car reference.
- **Sources:** [ev-database.org](https://ev-database.org/car/1619/Tesla-Model-Y-Long-Range-AWD), [ev-database.org](https://ev-database.org/car/1182/Tesla-Model-Y-Long-Range-AWD), [akku-brief.de](https://akku-brief.de/en/models/tesla-model-y), [fiches-auto.fr](https://www.fiches-auto.fr/articles-auto/tesla/s-4155-quelles-versions-de-batteries-equipent-les-tesla-model-3-et-y-.php), [teslamag.de](https://teslamag.de/news/mehr-reichweite-tesla-model-y-europa-performance-maerz-aus-deutschland-44770)

### 6. Later battery changes (not applicable) (medium confidence)

Later Shanghai/Berlin Long Range packs were certified at 84.85 kWh (up from 81.65 kWh) using LGES 5,300 mAh cells instead of 5,000 mAh cells. These are 2024–2025 changes.

- **This car:** Does not apply to a 2022 build. Avoid listings or sellers that quote 80+ kWh for this car.
- **Sources:** [autoevolution.com](https://www.autoevolution.com/news/long-range-tesla-model-3-and-model-y-built-at-giga-shanghai-get-a-nice-battery-boost-253783.html), [thelec.net](https://www.thelec.net/news/articleView.html?idxno=5134), [x.com](https://x.com/TeslaNewswire/status/1887376649487864255)

### 7. WLTP range by wheel (medium confidence)

In early 2022 (Jan/Feb), when the 5L pack arrived, Tesla Europe's configurator raised Model Y Long Range AWD WLTP from 537 to 565 km on the standard 19" wheels and from 507 to 533 km on the optional 20" wheels. Performance (21") went from 480 to 514 km. Several other sources (InsideEVs, Teslarati, tesla-info listings) quote 533 km as the Long Range AWD figure. EV Database 1619 shows 533 km under one rating and 542 km under another. Some sources disagree on which wheel size the 533 km applies to: Drive Tesla says 19", Electrive says 20".

- **This car:** Expect 565 km WLTP on 19" Gemini or 533 km on 20" Induction. The Überturbine 21" wheels are Performance-only. Wheel names come from general knowledge; the searches did not explicitly confirm the Gemini/Induction names. EV Database's real-world estimate is about 445 km (169 Wh/km).
- **Sources:** [teslamag.de](https://teslamag.de/news/mehr-reichweite-tesla-model-y-europa-performance-maerz-aus-deutschland-44770), [teslamag.de](https://teslamag.de/news/neu-tesla-konfigurator-mehr-reichweite-model-3-model-y-standard-raeder-42891), [teslawissen.ch](https://teslawissen.ch/tesla-model-y-aenderungen-die-modellpflege-timeline/), [tesla-info.com](https://tesla-info.com/car/DE-LRWYGCEK7NC455876), [ev-database.org](https://ev-database.org/car/1619/Tesla-Model-Y-Long-Range-AWD), [electrive.com](https://www.electrive.com/2024/04/11/tesla-launches-model-y-with-large-battery-and-rear-wheel-drive/), [insideevs.com](https://insideevs.com/news/606692/tesla-model-y-standard-range-rwd-launches-europe/amp)

### 8. Motors and power (medium confidence)

EU-market Long Range AWD: total 378 kW (514 PS) and 493 Nm (EV Database). One spec site (EU 2022) splits this as rear 220 kW / 440 Nm and front 158 kW / 240 Nm. EVKX says the front motor is an induction motor and the rear a permanent-magnet synchronous motor. Chinese MIIT-based reporting gives the Shanghai Long Range (TSL6480BEVBA0) as front 3D3 at 137 kW and rear 3D5 at 180 kW. The later TSL6480BEVBA1 used a locally made rear 3D7 at about 194 kW (+14 kW). A 2026 report refers to the 'older 3D3 front motor'. 220 kW is associated with the 3D6 rear motor of the Model 3/Y Performance. One evspecifications page instead lists 180 kW + 137 kW and calls the front motor a PMSM-reluctance unit, which conflicts with the induction description.

- **This car:** Front 3D3 AC induction plus rear PMSM (3D5 or 3D7; which one this 2022 car has is not confirmed). Use 378 kW / 514 PS for the EU registration document comparison. The COC (certificate of conformity) for this exact VIN will show the homologated per-motor power.
- **Sources:** [ev-database.org](https://ev-database.org/car/1182/Tesla-Model-Y-Long-Range-AWD), [evspecifications.com](https://www.evspecifications.com/en/model/328d3af), [evspecifications.com](https://www.evspecifications.com/en/model/b5be112), [evkx.net](https://evkx.net/models/tesla/model_y/model_y_long_range/), [42how.com](https://www.42how.com/en/article/3048), [zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/452769333), [teslanorth.com](https://teslanorth.com/2026/07/10/tesla-is-quietly-upgrading-its-china-cars-the-model-y-performance-is-coming-back/)

### 9. Performance figures (Long Range) (high confidence)

Model Y Long Range AWD: 0–100 km/h in 5.0 s and top speed 217 km/h (EV Database; 17vin China decode).

- **This car:** Applies directly to this car.
- **Sources:** [ev-database.org](https://ev-database.org/car/1619/Tesla-Model-Y-Long-Range-AWD), [en.17vin.com](https://en.17vin.com/model/xpviy.html)

### 10. DC/AC charging (medium confidence)

Long Range AWD (5L pack): peak DC 250 kW, average 10–80% about 124 kW (EV Database 1619). I could not find a source in this session for the AC on-board charger. It is generally understood to be 11 kW (3-phase, 16 A) on European Model Y, but that is unverified here.

- **This car:** 250 kW DC applies. Confirm the 11 kW AC on-board charger (and Type 2/CCS2 sockets for EU cars) on the car or its COC.
- **Sources:** [ev-database.org](https://ev-database.org/car/1619/Tesla-Model-Y-Long-Range-AWD)

### 11. Weight, towing, dimensions (medium confidence)

Long Range AWD: EU unladen weight 2,054 kg (EV Database, EU definition includes driver), curb weight 1,979 kg (evspecifications), towing 1,600 kg braked / 750 kg unbraked (EV Database). Dimensions: length 4,751 mm, width 1,921 mm without mirrors, height 1,624 mm, wheelbase 2,890 mm (evspecifications). Boot and frunk volumes were not verified in this session.

- **This car:** The 1,600 kg braked towing applies only if a tow hitch is fitted. Check whether this car has the factory tow hitch and the trailer power adapter (see the low-voltage battery entry). Weight figures differ by definition (EU unladen vs curb).
- **Sources:** [ev-database.org](https://ev-database.org/car/1619/Tesla-Model-Y-Long-Range-AWD), [evspecifications.com](https://www.evspecifications.com/en/model/328d3af)

### 12. Comparison: 2022 Performance (medium confidence)

Model Y Performance (2022–2025, EV Database 1183): same 75.0 kWh usable / 78.1 kWh nominal pack, total 393 kW (534 PS), top speed 250 km/h, EU unladen 2,072 kg, 0–100 listed as 4.0 s (evspecifications lists 3.7 s). WLTP rose from 480 to 514 km on 21" with the 5L pack in early 2022. EU Performance deliveries from Grünheide started in March 2022, though China import was also possible. The first China Performance deliveries were on 25 Nov 2021.

- **This car:** For comparison only. This VIN decodes as Long Range AWD, not Performance. If a seller claims 'Performance', check for 21" Überturbine wheels, red calipers, carbon spoiler and lowered suspension, and confirm in the Tesla app.
- **Sources:** [ev-database.org](https://ev-database.org/car/1183/Tesla-Model-Y-Performance), [evspecifications.com](https://www.evspecifications.com/en/model/c06b113), [teslamag.de](https://teslamag.de/news/mehr-reichweite-tesla-model-y-europa-performance-maerz-aus-deutschland-44770), [electrive.net](https://www.electrive.net/2022/01/24/tesla-bestaetigt-auslieferung-von-model-y-aus-gruenheide-im-maerz/), [electrek.co](https://electrek.co/2021/11/26/tesla-moves-amd-chip-new-model-y-china/)

### 13. Comparison: Shanghai RWD (LFP) (medium confidence)

Model Y RWD with CATL LFP (EV Database 1743, 'CATL 6L'/LFP60): 60.0 kWh nominal / 57.0 kWh usable, WLTP 455 km, peak DC 170 kW (10–80% average 108 kW), 0–100 in 6.9 s, period Nov 2022–Jan 2025. European RWD orders opened in 2022 with the earliest delivery windows in Dec 2022 (Drive Tesla) or Dec 2022–Feb 2023 (ArenaEV). The China-market RWD with CATL LFP launched in July 2021. A later BYD-cell version allows 175 kW DC.

- **This car:** Does not apply. A 2022 EU-delivered Shanghai Model Y built in Q3 2022 would not normally be an RWD, and the RWD prefix seen is LRWYGCFS, not LRWYGCEK.
- **Sources:** [ev-database.org](https://ev-database.org/car/1743/Tesla-Model-Y-RWD), [ev-database.org](https://ev-database.org/car/1974/Tesla-Model-Y-RWD), [driveteslacanada.ca](https://driveteslacanada.ca/model-y/tesla-launches-model-y-rwd-orders-in-europe/), [arenaev.com](https://www.arenaev.com/tesla_model_y_standard_range_new_entry_trim_lands_in_europe-news-629.php), [libattery.ofweek.com](https://libattery.ofweek.com/2021-07/ART-36001-8500-30508898.html), [en.17vin.com](https://en.17vin.com/model/mbn89.html)

### 14. Autopilot computer (HW3 vs HW4) (high confidence)

Shanghai-built Model Y stayed on Hardware 3 through 2022. HW4 came to Fremont Model Y around early to May 2023. For Shanghai Model Y, Drive Tesla reported HW4 with the Oct 2023 refresh, while Teslarati (15 Oct 2023) said the base China Model Y was still HW3. Tesla China's Weibo later (about March 2024) said all new Model Ys were built with HW4.

- **This car:** A 2022 build is HW3 (FSD Computer 3). Under Controls > Software > Additional Vehicle Information it should show 'Autopilot Computer: Full self-driving computer'.
- **Sources:** [driveteslacanada.ca](https://driveteslacanada.ca/news/tesla-adds-hw4-and-quicksilver-to-model-y-from-giga-shanghai/), [teslarati.com](https://www.teslarati.com/tesla-delivery-shanghai-model-y/), [insideevs.com](https://insideevs.com/news/655934/tesla-hardware-4-vehicles-deliveries/), [driveteslacanada.ca](https://driveteslacanada.ca/news/tesla-releases-updated-model-y-in-china/)

### 15. Infotainment (MCU3 AMD Ryzen) (high confidence)

The AMD Ryzen MCU (MCU3, replacing Intel Atom) first appeared on Shanghai-built Model Y Performance delivered in China from 25 Nov 2021. Leaked documents (Dec 2021) said Tesla would phase Ryzen and the Li-ion LV battery into all Model 3/Y made in California and China by Q2 2022, with no retrofits. Tesla's European parts catalog listed 'MCU-Z' (Ryzen), and early-2022 photos from Germany showed Model 3 and Model Y with the Ryzen MCU and Li-ion LV battery.

- **This car:** A Q3-2022 Shanghai Model Y should have the AMD Ryzen MCU3. Verify on screen (Additional Vehicle Information: 'Infotainment Processor: AMD Ryzen').
- **Sources:** [electrek.co](https://electrek.co/2021/11/26/tesla-moves-amd-chip-new-model-y-china/), [engadget.com](https://www.engadget.com/tesla-model-y-amd-ryzen-china-174802550.html), [electrek.co](https://electrek.co/2021/12/28/tesla-launches-amd-chip-12v-li-ion-battery-2022-model-3-y/), [driveteslacanada.ca](https://driveteslacanada.ca/model-3/tesla-parts-catalog-hints-giga-shanghai-amd-ryzen/), [driveteslacanada.ca](https://driveteslacanada.ca/model-3/latest-tesla-model-3-y-updates-arrive-in-europe/), [insideevs.com](https://insideevs.com/news/559570/report-amd-ryzen-retrofits-tesla/)

### 16. Low-voltage battery (medium confidence)

Tesla's service manual lists the 2022 Model Y low-voltage battery as lithium-ion, 6.9 Ah, '16V' (15.5 V nominal), replacing the 12 V 45 Ah lead-acid unit of the 2020 car. A small Li-ion LV battery was found on Shanghai-built Model Y Performance in China around Nov–Dec 2021, and it was phased into 2022 Model 3/Y. The 15.5 V battery needs a power conversion adapter for 12 V trailer power. Later (2025) Tesla moved to a 12.8 V LFP LV battery, partly because of trailer compatibility problems with the 16 V NMC unit.

- **This car:** A 2022 build very likely has the 15.5/16 V Li-ion LV battery. If towing, check that the tow-hitch wiring includes Tesla's trailer power adapter. Early reports disagreed on whether the Shanghai unit was '12V' or '16V'.
- **Sources:** [service.tesla.com](https://service.tesla.com/docs/ModelY/ServiceManual/en-us/GUID-8CBDB47F-0D3A-4827-AB98-982A92234D79.html), [ithome.com](https://www.ithome.com/0/589/569.htm), [gizchina.com](https://www.gizchina.com/tech/tesla-model-y-high-performance-version-manufactured-in-china-offers-longer-battery-life), [electrek.co](https://electrek.co/2021/12/28/tesla-launches-amd-chip-12v-li-ion-battery-2022-model-3-y/), [autoevolution.com](https://www.autoevolution.com/news/tesla-installed-a-new-lfp-128-volt-low-voltage-battery-in-its-latest-models-249724.html)

### 17. Radar (medium confidence)

Tesla said that from deliveries in April 2022, Model 3 and Model Y built for Europe and the Middle East would no longer have radar (Tesla Vision), with temporary Autosteer limits of 80 mph max and longer minimum following distance. A Twitter report (Tesla_Adri) said Shanghai approval V22 of 21 Feb 2022 removed radar from Shanghai exports from Q2 2022 (unofficial). A March 2023 MIIT filing marked four China Model Y variants 'no radar', but a CnEVPost reader suggested it meant the ultrasonic sensors.

- **This car:** A Q3-2022 Europe-bound Shanghai build should have NO front radar (camera-only Tesla Vision). Only a build from before about Feb–Mar 2022 would have radar.
- **Sources:** [autoevolution.com](https://www.autoevolution.com/news/tesla-removes-radar-vision-from-autopilot-and-fsd-for-model-3-and-model-y-in-europe-185830.html), [tesmanian.com](https://www.tesmanian.com/blogs/tesmanian-blog/tesla-model-3-and-y-without-radar-will-start-delivering-to-europe-from-q2-2022), [screenrant.com](https://screenrant.com/tesla-vision-model-3-y-europe-middle-east/), [cnevpost.com](https://cnevpost.com/2023/03/09/regulatory-filing-tesla-removing-radars-china-made-model-y/)

### 18. Ultrasonic parking sensors (USS) (high confidence)

Tesla's support page says that from early October 2022, Model 3 and Model Y built for Europe (and North America, Middle East, Taiwan, Korea and others) are built without the 12 front/rear ultrasonic sensors. Park Assist, Autopark, Summon and Smart Summon were disabled at first. Forum reports put Shanghai-built UK/EU cars without USS in late 2022 to early 2023, with a VIN-assignment acceptance notice. Shanghai was described as the last factory to drop USS for China-market cars (MIIT filing, March 2023).

- **This car:** A build before Oct 2022 should still have the 12 USS: look for the round sensor discs in the front and rear bumpers, and the distance readouts in cm on the screen when parking. If they are missing, the car was built Oct 2022 or later, which contradicts the estimated build date.
- **Sources:** [tesla.com](https://www.tesla.com/en_eu/support/transitioning-tesla-vision), [tesla.com](https://www.tesla.com/en_au/support/transitioning-tesla-vision), [iotworldtoday.com](https://www.iotworldtoday.com/2022/10/06/tesla-removing-ultrasonic-sensors-from-autopilot/), [teslamotorsclub.com](https://teslamotorsclub.com/tmc/threads/2023-model-y-updates-and-production.284379/), [teslanorth.com](https://teslanorth.com/2023/03/09/tesla-model-y-in-china-gets-pure-vision-autopilot-ultrasonic-sensors-removed/), [arenaev.com](https://www.arenaev.com/tesla_begins_removing_ultrasonic_sensors_from_model_y_in_china-news-1527.php)

### 19. Heated steering wheel and double glazing (low confidence)

Forum reports say Shanghai-built Model Y have had a heated steering wheel since around the end of 2021, although it was not listed in the EU configurator. Shanghai Model Y have double-pane front side windows. Drive Tesla reported that the China-built Model Y Performance gained double-pane rear side windows, unlike other China variants that had only front double-pane glass. Berlin owners report single-pane rear glass.

- **This car:** Likely has a heated steering wheel (check Climate > Seat heater menu for the steering-wheel icon) and double-pane front windows. Rear double glazing on a Long Range export car is uncertain; check the glass edge.
- **Sources:** [teslamotorsclub.com](https://teslamotorsclub.com/tmc/threads/does-model-y-come-with-heated-steering-wheel-now.280561/), [driveteslacanada.ca](https://driveteslacanada.ca/model-y/tesla-model-y-performance-in-china-gains-double-pane-rear-windows/), [teslamotorsclub.com](https://teslamotorsclub.com/tmc/threads/2024-model-y-lr-will-sound-deadening-material-make-a-difference.339046/page-2)

### 20. Shanghai Model Y export history (high confidence)

Shanghai-made Model Y was first shipped overseas in July 2021 (8,210 units to Europe). European orders for China-built Model Y opened 9 July 2021 with September delivery. China domestic deliveries started January 2021. Berlin (Grünheide) Model Y deliveries started March 2022.

- **This car:** Puts this car in the 2nd year of Shanghai exports to Europe. In 2022 a Long Range AWD in Europe could come from Shanghai (this VIN, LRW) or Berlin (XP7 WMI).
- **Sources:** [scmp.com](https://www.scmp.com/business/money/article/3145199/electric-vehicles-tesla-ships-shanghai-made-model-y-overseas-first), [electrek.co](https://electrek.co/2021/07/09/tesla-opens-orders-across-europe-for-made-in-china-model-y-with-sept-delivery/), [electrive.net](https://www.electrive.net/2022/01/24/tesla-bestaetigt-auslieferung-von-model-y-aus-gruenheide-im-maerz/), [en.wikipedia.org](https://en.wikipedia.org/wiki/Tesla_Model_Y)

### 21. Running changes on Shanghai Model Y relevant to a 2022 build (chronological) (medium confidence)

Nov 2021: China Model Y Performance launches with AMD Ryzen MCU3, Li-ion LV battery and double-pane rear windows. Dec 2021: Tesla documents set the 2022 Model 3/Y changes for Europe (Ryzen, 15.5 V Li-ion, trailer adapter), phased in by Q2 2022. Jan–Feb 2022: LG 5L pack replaces 5C in Long Range/Performance; EU WLTP becomes 565 km (19") / 533 km (20") for Long Range and 514 km for Performance. 21 Feb 2022: approval reportedly removes radar from Shanghai exports. Apr 2022: Europe deliveries without radar. Mar 2022: Berlin Model Y deliveries begin. Early Oct 2022: Europe-bound Model 3/Y begin dropping USS; Shanghai EU exports follow by late 2022 to early 2023. Nov–Dec 2022: EU Model Y RWD (CATL LFP) deliveries begin. Mar 2023: MIIT filing removes USS (labelled 'radar') on China-market Model Y. Oct 2023: China Model Y refresh (ambient lighting, new 19" wheels); HW4 reported for Shanghai Model Y from about Oct 2023 to early 2024. I did not find month-by-month Shanghai changes for May–Sept 2022 beyond these.

- **This car:** For a build around Jul–Sep 2022, expect: LG 5L pack, Ryzen MCU3, Li-ion LV battery, HW3, no radar, 12 USS present, pre-refresh interior (no ambient light strip). If the car shows radar or an Intel Atom MCU, it was built earlier; if it has no USS, it was built later.
- **Sources:** [electrek.co](https://electrek.co/2021/11/26/tesla-moves-amd-chip-new-model-y-china/), [electrek.co](https://electrek.co/2021/12/28/tesla-launches-amd-chip-12v-li-ion-battery-2022-model-3-y/), [teslamag.de](https://teslamag.de/news/mehr-reichweite-tesla-model-y-europa-performance-maerz-aus-deutschland-44770), [teslawissen.ch](https://teslawissen.ch/tesla-model-y-aenderungen-die-modellpflege-timeline/), [akku-brief.de](https://akku-brief.de/en/models/tesla-model-y), [tesmanian.com](https://www.tesmanian.com/blogs/tesmanian-blog/tesla-model-3-and-y-without-radar-will-start-delivering-to-europe-from-q2-2022), [tesla.com](https://www.tesla.com/en_eu/support/transitioning-tesla-vision), [ev-database.org](https://ev-database.org/car/1743/Tesla-Model-Y-RWD), [cnevpost.com](https://cnevpost.com/2023/03/09/regulatory-filing-tesla-removing-radars-china-made-model-y/), [driveteslacanada.ca](https://driveteslacanada.ca/news/tesla-adds-hw4-and-quicksilver-to-model-y-from-giga-shanghai/), [notateslaapp.com](https://www.notateslaapp.com/news/1635/tesla-updates-model-y-with-ambient-lighting-new-wheels-and-improved-performance-in-china)

### 22. Items NOT verified in this session (low confidence)

The shared web-search budget ran out before these could be checked: (a) AC on-board charger rating (believed 11 kW 3-phase); (b) boot and frunk volumes; (c) heat pump and Octovalve (believed standard on all Model Y since 2020); (d) structural castings (Shanghai Model Y believed to use a single-piece rear underbody casting with a conventional, non-structural 2170 pack); (e) power-folding/heated mirrors; (f) factory tow-hitch option and price in 2022; (g) 2022 EU colour and interior list (believed Pearl White Multi-Coat, Solid Black, Midnight Silver Metallic, Deep Blue Metallic, Red Multi-Coat; interiors All Black or Black and White). Sibling VINs on tesla-info show Pearl White and Midnight Silver with a black interior.

- **This car:** Treat these as unverified general knowledge. Check them physically on the car or against its COC, or run a follow-up search session.
- **Sources:** [tesla-info.com](https://tesla-info.com/car/FR-LRWYGCEK2NC235190), [tesla-info.com](https://tesla-info.com/car/DE-LRWYGCEK7NC455876)

## Second pass: spec gaps and decode cross-check

Nothing I found contradicts the round-1 decode. Tesla's own service manuals (2020-2024 and 2025 Model Y) confirm that for Giga Shanghai and Giga Berlin cars, digit 10 is the calendar year the car was built, so 'N' means built in 2022. The manual lists K among the valid digit-8 codes (D E F J K L R S), but the search extracts never showed which letter pairs with which label, so Tesla's official wording for 'K' is still unconfirmed. The only explicit meaning comes from a third party (shop4tesla): 'two standard motors, Hairpin Windings (Y#DB, 3#DB)', i.e. dual motor, non-Performance. I re-checked two of the three date anchors on tesla-info.com (search snippets only, not the full pages): 455876 left the factory on 13 Aug 2022 (first registered 9 Sep 2022, Munich) and 461600 on 17 Aug 2022 (first registered 26 Sep 2022, Potsdam). The third anchor, 424830, was not re-checked. That sibling 461600 is on 19-inch Gemini wheels but is listed at 533 km WLTP, which contradicts round 1's '565 km on 19 inch'. The WLTP-by-wheel figure stays open; this car's CoC will settle it. Specs now sourced: AC on-board charger 11 kW (3-phase 16 A; a 22 kW wallbox gives no gain; about 7h45-8h15 for 0-100%). Boot 854 L (measured to the roof), frunk 117 L, 2,158 L with seats folded per EV Database (other outlets give 2,041 L). Heat pump is standard. A factory tow hitch was orderable in Europe for €1,350 (Germany, May 2022), rated 1,600 kg braked / 750 kg unbraked. 2022 EU paints were Pearl White (free) plus Solid Black, Midnight Silver, Deep Blue and Red Multi-Coat; their prices moved several times in 2022 (Midnight Silver about €1,200-1,600, Red about €2,000-2,200). Quicksilver and Midnight Cherry Red (from Oct 2022) were Berlin-only, so original paint in either colour on this Shanghai car would be a red flag. China-market Model Ys use a GB/T charge port (Tesla China owner's manual); EU cars have CCS2. Tesla's EU type approvals come from the Dutch RDW, so the number starts 'e4*', not 'e1*'. A Model Y EC CoC shows Type 003 with variant code Y6LR, but I did not find the full approval number for type 003. Ukraine and most other post-Soviet countries do not require EU homologation, and China-spec (GB/T) EVs and CCS2-to-GB/T adapters are traded there. I found no source showing China-market Model Ys being grey-imported into Romania or Bulgaria. Not found: 2022 prices for 20-inch Induction wheels and the black-and-white interior, heated mirrors, how a China-market car behaves with the Tesla app or account region, and Tesla-specific EU wording for the build-date label. I used all 25 of my searches.

### 1. Decode check: pos 10 'N' = calendar year of build (Shanghai) (high confidence, sourced in this pass)

Tesla's 2020-2024 Model Y service manual VIN page says digit 10 is the 'Calendar year in which the vehicle was built for Giga Shanghai and Giga Berlin built vehicles', and lists codes H through S for 2017-2025. The 2025 manual says the same and gives S, T and V for 2025, 2026 and 2027. Fremont and Texas cars use model year instead. I could not refute this.

- **This car:** 'N' means the car was built in calendar 2022 at Shanghai. It cannot be a late-2021 build sold as a 2022 model.
- **Sources:** [service.tesla.com](https://service.tesla.com/docs/ModelY/ServiceManual/en-us/GUID-0C797294-574D-4EE4-8017-C339A7D58411.html), [service.tesla.com](https://service.tesla.com/docs/ModelY/ServiceManual/2025/en-us/GUID-BB4CE449-3F8E-4905-AF4A-96DFA87535B5.html)

### 2. Decode check: pos 8 'K' (medium confidence, sourced in this pass)

Tesla's Model Y service manual (2020-2024 and 2025) lists D, E, F, J, K, L, R and S as digit-8 codes, with labels including Single Motor, Dual Motor Standard and Dual Motor Performance. The search extracts do not show which letter pairs with which label, so Tesla's official wording for K is still unconfirmed. The shop4tesla decoder defines K as 'two standard motors of the type Hairpin Windings (Y#DB, 3#DB)' and J as a single standard/performance hairpin motor. US NHTSA decoders for 2020-2022 list only D, E and F for Model Y (E = Dual Motor Standard, F = Dual Motor Performance), so K never appears in US data. No source I found contradicts K = dual motor, non-Performance.

- **This car:** Supports dual-motor non-Performance = Long Range AWD. The only explicit definition is third-party; the manual table could not be read in full.
- **Sources:** [service.tesla.com](https://service.tesla.com/docs/ModelY/ServiceManual/en-us/GUID-0C797294-574D-4EE4-8017-C339A7D58411.html), [shop4tesla.com](https://shop4tesla.com/en/pages/tesla-ratgeber-tesla-vin-decoder), [insideevs.com](https://insideevs.com/news/561819/identify-tesla-origin-vin-decoder/), [vpic.nhtsa.dot.gov](https://vpic.nhtsa.dot.gov/mid/home/displayfile/54414e8c-d20d-4011-8158-48838c122a87)

### 3. Decode check: date anchor serial 455876 (medium confidence, sourced in this pass)

tesla-info.com lists LRWYGCEK7NC455876 as a CPO 2022 Model Y Long Range AWD (München Haag): factory-gate date 13 Aug 2022, first registered 9 Sep 2022. This is an aggregator, not a Tesla source.

- **This car:** Confirms the upper anchor of the date bracket. Serial 451763 is about 4,100 lower, so it was probably built a few days before 13 Aug 2022. Search snippet only; I could not open the page.
- **Sources:** [tesla-info.com](https://tesla-info.com/car/DE-LRWYGCEK7NC455876)

### 4. Decode check: date anchor serial 461600 (and a WLTP conflict) (medium confidence, sourced in this pass)

tesla-info.com lists LRWYGCEK7NC461600 as a CPO 2022 Model Y Long Range AWD (Potsdam-Mittelmark): factory date 17 Aug 2022, first registered 26 Sep 2022, Midnight Silver, black interior, 19-inch Gemini wheels, Enhanced Autopilot, 5 seats, 533 km WLTP, 94,826 km, status 'Previous Accidents'. Battery and drive-unit warranty run to 29 Sep 2030 / 192,000 km.

- **This car:** Confirms the 17 Aug 2022 anchor, and confirms that the battery warranty counts 8 years from first registration. Note the conflict: a neighbouring car on 19-inch Gemini wheels is listed at 533 km WLTP, not the 565 km round 1 gave for 19 inch. Search snippet only.
- **Sources:** [tesla-info.com](https://tesla-info.com/car/DE-LRWYGCEK7NC461600)

### 5. AC on-board charger (high confidence, sourced in this pass)

For the 2022-2025 Model Y Long Range AWD, EV Database's European charging table lists 3-phase 16 A (11 kW) at about 8h15m for 0-100% (7h45m for the earlier LG M48-cell version). A 3-phase 32 A / 22 kW supply is 'limited by on-board charger, vehicle cannot charge faster'. Green Cars Compare also says AC is capped at 11 kW and that the 2022 Europe car has a CCS Type 2 port.

- **This car:** Applies. Home or public AC charging maxes out at 11 kW (3-phase 16 A). A 22 kW wallbox is not needed. On single-phase 230 V the car charges at about 3.7 kW (that figure is general knowledge, not sourced here).
- **Sources:** [ev-database.org](https://ev-database.org/car/1619/Tesla-Model-Y-Long-Range-AWD), [ev-database.org](https://ev-database.org/car/1182/Tesla-Model-Y-Long-Range-AWD), [greencarscompare.com](https://greencarscompare.com/global/cars/tesla-model-y-long-range-awd/)

### 6. Boot and frunk volume (high confidence, sourced in this pass)

EV Database lists 854 L of cargo with seats up, 2,158 L with the rear seats folded, and a 117 L frunk. UK reviews also give 854 L and 117 L and note that 854 L is measured to the roof. Folded figures vary between sources (2,041 L, 1,869 L, 2,138 L including the frunk). The rear seat splits 40/20/40 and does not fold fully flat.

- **This car:** Applies (5-seat car). The 854 L figure is to the roof, so it overstates usable space against rivals measured to the window line.
- **Sources:** [ev-database.org](https://ev-database.org/car/1619/Tesla-Model-Y-Long-Range-AWD), [carbuyer.co.uk](https://www.carbuyer.co.uk/tesla/model-y/practicality), [drivingelectric.com](https://www.drivingelectric.com/tesla/model-y/practicality)

### 7. Heat pump (high confidence, sourced in this pass)

EV Database lists 'Heat pump: Yes; HP standard equipment: Yes' for both the 2021-2022 and 2022-2025 Model Y Long Range AWD. 2020 reporting describes the Model Y as Tesla's first car with a heat pump, integrated with the Octovalve.

- **This car:** The car should have the heat pump. Weak cabin heat in winter can point to known heat-pump or Octovalve faults; ask for service history.
- **Sources:** [ev-database.org](https://ev-database.org/car/1619/Tesla-Model-Y-Long-Range-AWD), [ev-database.org](https://ev-database.org/car/1182/Tesla-Model-Y-Long-Range-AWD), [cleantechnica.com](https://cleantechnica.com/2020/04/14/teslas-octovalve-enabled-a-staggering-10-increase-in-range-for-the-model-y/), [testops.teslarati.com](https://testops.teslarati.com/?p=135166)

### 8. Tow hitch option and rating (high confidence, sourced in this pass)

From May 2022 the factory tow hitch could be added in the European configurator for Model Y Long Range and Performance, priced at €1,350 in Germany, with a 1,600 kg towing rating. EV Database: tow hitch possible, 1,600 kg braked, 750 kg unbraked.

- **This car:** An August 2022 build could have the factory hitch. Check whether one is fitted and whether the registration document lists the trailer masses. If a hitch was retrofitted, it must be entered in the papers.
- **Sources:** [shop4tesla.com](https://www.shop4tesla.com/en/blogs/news/anhangerkupplung-fur-das-model-y-jetzt-konfigurierbar-zinssatz-erhoht), [ev-database.org](https://ev-database.org/car/1619/Tesla-Model-Y-Long-Range-AWD)

### 9. 2022 EU paint options and prices (medium confidence, sourced in this pass)

Pearl White Multi-Coat was the free colour in Europe. The paid colours were Solid Black (about €1,200), Midnight Silver Metallic and Deep Blue Metallic (reported at €1,200, then €1,600, and €2,200 in one Drive Tesla report for Germany), and Red Multi-Coat (reported €2,200, then €2,000). In October 2022 the Berlin-only colours Quicksilver (€3,000) and Midnight Cherry Red (€3,200) replaced Midnight Silver (€1,600) and Red Multi-Coat (€2,000) for Berlin-built LR and Performance cars. Prices changed several times during 2022, and the sources disagree on the exact dates.

- **This car:** An August 2022 Shanghai car should be one of Pearl White, Solid Black, Midnight Silver, Deep Blue or Red Multi-Coat. Quicksilver or Midnight Cherry Red on this car would suggest a respray or wrap; check the paint code and door shuts.
- **Sources:** [carscoops.com](https://www.carscoops.com/2022/10/tesla-model-y-gains-two-new-multi-layer-paint-options-in-europe-and-middle-east/), [insideevs.com](https://insideevs.com/news/692047/tesla-midnight-cherry-red-price-cut/), [shop4tesla.com](https://www.shop4tesla.com/es/blogs/news/neue-farben-fur-das-tesla-model-y-aus-grunheide-anpassung-bei-den-preisen-fur-zusatzliche-farben-beim-model-3), [driveteslacanada.ca](https://driveteslacanada.ca/?p=42983), [insideevs.com](https://insideevs.com/news/675057/tesla-changes-free-color-option-model-3-y-north-america/)

### 10. Wheels, interior and Enhanced Autopilot prices (2022) (low confidence, NOT re-verified)

19-inch Gemini was the standard LR wheel; the sibling LRWYGCEK7NC461600 is listed on 19-inch Gemini. 2022 German used LR AWD listings mention 20-inch Induction wheels. I did not find 2022 EU option prices for 20-inch Induction wheels or the black-and-white interior. Enhanced Autopilot cost €3,800 in Austria, from an undated configurator article that is probably from 2021.

- **This car:** The wheel names are confirmed in listing data, but the 2022 option prices for wheels and interior were not found. Check what is installed under Controls > Software (Autopilot/EAP/FSD); this did not come from a source in this run.
- **Sources:** [tesla-info.com](https://tesla-info.com/car/DE-LRWYGCEK7NC461600), [firstev.de](https://firstev.de/marktplatz/tesla-model-y-lr-awd-2/), [futurezone.at](https://futurezone.at/produkte/tesla-model-y-konfigurator-oesterreich-preis-verfuegbarkeit-extras/401441659)

### 11. Heated steering wheel and heated rear seats (medium confidence, sourced in this pass)

Tesla's China owner's manual confirmed a heated steering wheel on Model 3/Y in late 2020 to early 2021. InsideEVs reported the Model Y heated wheel heading to the US and Europe, and US Standard Range and Long Range cars were delivered with it active. Drive Tesla notes that whether a car has it depends on when and where it was built; it is a hardware item. A UK dealer spec template for 2022 Model Y LR AWD lists heated front and rear seats and a heated steering wheel (weak source).

- **This car:** An August 2022 Shanghai LR very likely has a heated steering wheel and heated rear seats. Confirm on the climate screen (steering-wheel and rear-seat heater icons). This corrects round 1's 'since end of 2021': it was 2020-2021.
- **Sources:** [insideevs.com](https://insideevs.com/news/466855/tesla-model-y-model-3-heated-steering/), [driveteslacanada.ca](https://driveteslacanada.ca/?p=19146), [driveteslacanada.ca](https://driveteslacanada.ca/?p=18446), [selectcarleasing.co.uk](https://www.selectcarleasing.co.uk/used-car-leasing/tesla-model-y-long-range-awd-5dr-auto-aj22fxc)

### 12. Mirrors (power folding; heated not confirmed) (medium confidence, sourced in this pass)

Tesla's Model Y owner's manual: mirrors can be power-folded via Controls > Fold/Unfold Mirrors or the left scroll button, and auto-fold on lock if Mirror Auto Fold is on. Manually folded mirrors unfold at 50 km/h and cannot be folded above 50 km/h. The manual warns that 'depending on trim, configuration, and date of manufacture, your vehicle may not be equipped with folding mirrors'. I found no source on heated mirrors in this run.

- **This car:** Test Fold/Unfold Mirrors on the touchscreen during the inspection. Heated mirrors are unconfirmed.
- **Sources:** [tesla.com](https://www.tesla.com/ownersmanual/modely/en_us/GUID-3EFBA9D5-76B6-468D-BBD0-9090C0E05F22.html), [tesla.com](https://www.tesla.com/ownersmanual/2020_2024_modely/en_us/Owners_Manual.pdf)

### 13. EU vs China-market car: charge port (high confidence, sourced in this pass)

Tesla's China-region Model Y owner's manual (en_cn) describes the GB/T charge port and Tesla's 'GB/T to Type A/I outlet adapter'. Green Cars Compare gives the 2022 Europe Model Y port as CCS Type 2. In Ukraine, CCS2-to-GB/T adapters are sold 'for cars from China' and are flashed for each car model.

- **This car:** Quickest physical check: an EU-market car has a CCS2 port (Type 2 AC plus two DC pins below). A GB/T port means a China-market car; it cannot use EU Superchargers without an adapter and is a strong reason to walk away.
- **Sources:** [tesla.com](https://www.tesla.com/OWNERSMANUAL/modely/en_cn/GUID-2AFEEA7F-3FF1-4544-B23B-488EAD0E199F.html), [greencarscompare.com](https://greencarscompare.com/global/cars/tesla-model-y-long-range-awd/), [olx.ua](https://www.olx.ua/d/uk/obyavlenie/perehdnik-adapter-ccs2-gbt-300a-olink-dlya-avto-z-kitayu-240kvt-shvidka-zaryadka-ostannya-versya-perehodnika-ID10hbzb.html)

### 14. EU type approval / CoC number format (medium confidence, sourced in this pass)

Tesla's EU whole-vehicle type approvals are issued by the Netherlands RDW, so they start 'e4'. Tesla's EU type numbers are 001 Roadster, 002 Model S/X, 003 Model 3 and Model Y (same approval set), plus 004 and 005 with approvals e4*18/858*00086*00 and e4*18/858*00135*00. Type 005 is the Berlin BYD-battery Model Y RWD (variant Y7CR), approved by RDW on 1 Jul 2022. A Model Y EC CoC dated 26 Nov 2023 (copy held by a Croatian agency) shows Type 003, variant Y6LR, commercial name Model Y. I did not find the full approval number for type 003.

- **This car:** An EU-market car should come with a Tesla EC CoC showing an 'e4*...' approval number, Type 003, and a Model Y variant code. Expect 'e4', not 'e1'. A missing CoC, or registration based only on individual approval, suggests a non-EU-market car.
- **Sources:** [blog.kenteken.tv](https://blog.kenteken.tv/2022/07/17/two-new-european-type-approval-numbers-for-tesla-models/), [static-pin.fzoeu.hr](https://static-pin.fzoeu.hr/zexport/katalog_821e13636ae8434e86ac407458ea0ccf_f99aa9d37735475d9ccedbe197c4448f_202402261019480958.pdf), [cnevpost.com](https://cnevpost.com/2022/08/12/tesla-model-y-with-byd-batteries-has-received-eu-approval/), [insideevs.com](https://insideevs.com/news/604025/byd-tesla-modely-eu-approval/)

### 15. Grey imports of China-market cars (Ukraine/RO/BG) (low confidence, sourced in this pass)

An ABRP feature-request post says China-spec EVs imported directly from China are much cheaper than EU/CCS2-spec cars, and that Ukraine and most post-Soviet countries do not require EU homologation. That is why GB/T cars and adapters circulate there. A 2025 Romanian article says China-only Tesla variants (Model Y+) can be bought only through parallel import from China via specialised firms, with extra bureaucracy and cost. I found no source documenting China-market 2022 Model Ys grey-imported into Romania or Bulgaria.

- **This car:** China-spec Teslas do flow through Ukraine and other non-EU neighbours, so a car arriving via Ukraine or Moldova, or with a non-EU first registration, deserves extra checks (charge port, CoC, Tesla service history). No RO/BG-specific evidence was found.
- **Sources:** [abrp.upvoty.com](https://abrp.upvoty.com/b/request-a-feature/support-gbt-port), [playtech.ro](https://playtech.ro/2025/tesla-model-y-cu-autonomie-de-invidiat-mai-greu-de-gasit-decat-ar-trebui-unde-gasesti-modelul-cu-821-de-kilometri-departe-de-priza/)

### 16. Grey-import warranty/software caveats (low confidence, sourced in this pass)

Reporting from 2016 on grey-market Teslas says warranties were voided and Tesla service would repair them only at the owner's cost (citing Forbes). It also notes market-specific software, e.g. the China fleet used NavInfo maps. I found no source on Tesla app or account region locks for China-market cars moved abroad.

- **This car:** This is old and about other models, but it supports asking Tesla Romania or Tesla Europe to confirm in writing that this VIN is covered by the EU battery and drive-unit warranty and can be moved to the buyer's Tesla account.
- **Sources:** [electrek.co](https://electrek.co/2016/08/05/tesla-model-x-popular-grey-market-china-premium/), [autoblog.com](https://www.autoblog.com/2016/08/06/grey-market-tesla-model-x-240000-china/)

### 17. Where the build date is shown (low confidence, sourced in this pass)

Generic vehicle-ID guidance: the driver's door certification label gives the month and year of manufacture. Coverage of a Tesla Model Y recall says the driver-door label carries tyre data, maximum loaded weight and the manufacture date (US context). An accessory guide places Tesla's white VIN/build sticker on the driver-side B-pillar. I found no Tesla-specific EU wording ('Date of manufacture').

- **This car:** Open the driver door and read the B-pillar labels for a build month and year. Expect 08/2022. Also check that the VIN on the label matches the windscreen/dash VIN and the registration documents.
- **Sources:** [autoupkeep.com](https://www.autoupkeep.com/diy-learning/introduction-and-how-cars-work/vehicle-identification/year), [rss.boorghani.com](https://rss.boorghani.com/tesla-recalls-thousands-of-model-ys-at-risk-of-missing-a-sticker), [basenor.com](https://www.basenor.com/blogs/tesla-guides/tesla-vin-build-month-fitment-guide)

### 18. On-screen hardware/options check (medium confidence, sourced in this pass)

Controls > Software > Additional Vehicle Information shows the Autopilot computer. HW3 reads 'Full self-driving computer' (older units 'AP2.5'); newer cars show HW4 or AP4.5. The current sources do not confirm the exact 'Infotainment Processor' line.

- **This car:** Expect 'Full self-driving computer' (HW3). If it shows HW4, that contradicts a 2022 Shanghai build. The same screen also shows the installed software package (Basic Autopilot / EAP / FSD).
- **Sources:** [abstractocean.com](https://www.abstractocean.com/pages/faq-how-to-know-if-your-tesla-has-hw4), [teslamotorsclub.com](https://teslamotorsclub.com/tmc/threads/what-does-fsd-get-us.199611/latest), [electrek.co](https://electrek.co/2026/01/26/tesla-quietly-starts-shipping-model-y-with-new-ai4-5-computer/)

### Corrections from the second pass

- Task premise 'EU CoC/type-approval number e1*2018/858*...' is very likely wrong for Tesla: Tesla's EU approvals are issued by the Dutch RDW ('e4'). Model Y sits under Tesla EU type 003 (shared with Model 3), and a Model Y CoC shows Type 003, variant Y6LR (kenteken.tv; Croatian-agency CoC copy).
- specs.md WLTP claim '565 km on 19-inch / 533 km on 20-inch' is not supported in this run. Sibling LRWYGCEK7NC461600 (factory gate 17 Aug 2022) is listed on 19-inch Gemini wheels with 533 km WLTP. EV Database lists 533/542 km, and evkx says up to 542 km, falling to 533 km depending on wheel size. Treat 565 km as unverified and use the figure on this car's CoC.
- decode.md says the K wording was 'read in one extract as Dual Motor Standard' from Tesla's manual. In this run the manual table again listed only the code set (D E F J K L R S) without a readable letter-to-label pairing, so Tesla's official meaning of K is still unconfirmed. The explicit 'two standard hairpin motors' definition is third-party (shop4tesla). The conclusion (LR AWD) still stands.
- specs.md listed AC on-board charger, boot/frunk, heat pump and tow hitch as unverified. Now sourced: 11 kW 3-phase AC on-board charger (22 kW gives no gain); 854 L boot / 117 L frunk / 2,158 L folded (EV Database; some outlets give 2,041 L); heat pump standard; factory tow hitch €1,350 (Germany, May 2022) with 1,600 kg braked / 750 kg unbraked.
- specs.md said 'Shanghai Model Y have had a heated steering wheel since around the end of 2021'. Sources point to late 2020 to early 2021 (China owner's manual, then US/Europe-bound cars).
- Colour list in specs.md (Pearl White, Solid Black, Midnight Silver, Deep Blue, Red Multi-Coat) is consistent with sources. Addition: Quicksilver and Midnight Cherry Red (Oct 2022, €3,000/€3,200) were Berlin-only and should not be original paint on a 2022 Shanghai car.
- The decode date anchors 455876 = 13 Aug 2022 and 461600 = 17 Aug 2022 were re-confirmed from tesla-info snippets, along with first registrations of 9 Sep and 26 Sep 2022. The 424830 = 28 Jul 2022 anchor was not re-checked in this run.

### Second-pass open questions

- What is Tesla's exact official wording for digit-8 'K' in the 2020-2024 Model Y service manual? Search extracts could not pair the letters with their labels; reading the page directly would settle it.
- What is the full EU type-approval number (e4*...) for Tesla type 003 / Model Y, and which variant code (e.g. Y6LR?) appears on a 2022 Shanghai LR AWD CoC?
- Was the WLTP figure for a 2022 Shanghai LR AWD 565 km or 533 km on 19-inch Gemini wheels? This car's CoC shows the homologated value.
- What were the 2022 EU option prices for 20-inch Induction wheels and the black-and-white interior? Not found.
- Are heated exterior mirrors standard on the 2022 Model Y? Not confirmed by any source in this run.
- How does a China-market Model Y behave outside China (Tesla account or app transfer, Supercharger access, map region, EU warranty)? No source found; ask Tesla Romania or Tesla Europe to confirm warranty coverage and account transfer for this VIN in writing.
- Have China-market Model Ys been grey-imported into Romania or Bulgaria specifically? Only Ukraine/post-Soviet and general Romanian parallel-import evidence was found.
- Exact build date of LRWYGCEK7NC451763: still interpolated (about 10-11 Aug 2022). Confirm from the B-pillar label, the CoC, or Tesla.
- The sibling 461600 is flagged 'Previous Accidents' on tesla-info. This says nothing about this car, but it shows that cars from this batch are on the CPO and used market with accident histories, so a paid history check is worthwhile.

## Open questions

- Exact production month of LRWYGCEK7NC451763. The July–September 2022 estimate comes from a neighbouring VIN; confirm via the build sticker on the B-pillar or door jamb, the Tesla app, or the COC/registration documents.
- Which rear motor this car has (3D5 at about 180 kW or the locally made 3D7 at about 194 kW per MIIT), and the homologated per-motor kW in its EU COC.
- Wheel option fitted (19" Gemini, 565 km WLTP, vs 20" Induction, 533 km WLTP), and whether the original wheels are still on the car.
- Whether this car has USS (expected yes for a pre-Oct-2022 build) and no radar (expected). Inspect the bumpers and the screen.
- AC on-board charger rating, boot/frunk volume, heat pump/Octovalve, castings, power-folding mirrors, tow hitch and 2022 colour/interior list were not verified because the shared WebSearch budget (200 calls) ran out. The user can send a follow-up to continue searching.
- Whether a Shanghai-built 2022 Long Range export car has double-pane rear side windows (reported for China Performance only).
