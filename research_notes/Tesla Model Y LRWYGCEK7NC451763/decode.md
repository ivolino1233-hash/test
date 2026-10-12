# VIN decode: LRWYGCEK7NC451763

Method note: researched 2026-10-12. WebFetch and curl could not reach any site from this environment (DNS failure on every host, including tesla.com, NHTSA, autoDNA and carVertical), so **every fact below comes from search-engine results and snippets, not from pages I opened**. First research pass (about 58 searches for this lens).

## Takeaway

LRWYGCEK7NC451763 is a valid VIN. I recomputed the ISO 3779 check digit (weighted sum 414, mod 11 = 7) and it matches position 9. Decoded, it is a left-hand-drive, 5-seat Tesla Model Y Long Range dual-motor AWD with a nickel-based (NCM, not LFP) battery, built at Giga Shanghai in calendar year 2022. LRW = Tesla Shanghai and C = the Shanghai plant, both per Tesla's own service manual. For Shanghai and Berlin cars, Tesla's manual says position 10 is the calendar year of build, not a model year. So "N" means the car was built in 2022 and cannot be a late-2021 car.

Position 8 "K" is a dual-motor (non-Performance) code; several decoders describe it as dual motor with hairpin-wound motors. In real cars it is always Long Range AWD: every LRWYGCEK car found in Chinese databases and European Tesla used-car listings is LR AWD. Shanghai Performance cars use "L" (LRWYGCEL). Shanghai rear-wheel-drive cars use pos7 "F" (LFP battery) with pos8 "S" in 2022–23 (LRWYGCFS) and "J" in 2024 (LRWYGCFJ). "K" is not China-only, because Berlin LR AWD cars are XP7YGCEK. It is also not a battery-supplier code: chemistry is in position 7 and the supplier is not encoded anywhere in the VIN.

Shanghai Model Y serials run on their own counter, separate from Model 3. Model 3 serial 478258 left the factory on 4 Jan 2022 while Model Y serial 222058 left on 5 Jan 2022, and Model 3 serial 615127 left on 14 Aug 2022 while Model Y serial 455876 left on 13 Aug 2022. The Model Y counter is shared by left- and right-hand-drive, RWD and AWD, and China-domestic and export cars.

Tesla's "factory gate" dates (the date a car leaves the factory) for nearby serials bracket this car: 424830 = 28 Jul 2022, 455876 = 13 Aug 2022, 461600 = 17 Aug 2022. That puts serial 451763 at about 10–11 Aug 2022 (likely window 8–13 Aug). This was the record month after Shanghai's line upgrades: 56,721 Model Y built in August 2022, about 1,800–1,950 serials per day. Neighbouring European cars were first registered in September 2022: 452426 and 460654 in Finland in 9/2022, 455876 in Germany on 9 Sep 2022, and 461600 in Germany on 26 Sep 2022.

The VIN cannot show whether the car was built for China or for export. China-domestic cars use the same LRWYGC prefix; for example LRWYGCFS6NC424830 was delivered in Guangzhou. Only the right-hand-drive code "H" marks some Asia-Pacific and UK cars. Whether the car is EU-spec has to be confirmed from the EU certificate of conformity (CoC) and first-registration papers, or physically from the charge port: a European CCS2 port versus China's GB/T port.

No public record of this exact VIN was found.

## Cited findings

### 1. Check digit (pos 9) (high confidence)

I recomputed the check digit with the ISO 3779 / 49 CFR 565 method: the transliterated, weighted sum is 414, and 414 mod 11 = 7. That matches the '7' in position 9, so the VIN is internally valid with no typo detectable this way. China's VIN standard also uses a position-9 check digit; that is my background knowledge, not something sourced in this search.

- **This car:** The VIN is valid. A single mistyped character would almost always fail this check.
- **Sources:** (local computation, no web source)

### 2. WMI pos 1-3 'LRW' (high confidence)

LRW is Tesla's WMI (manufacturer code) for Giga Shanghai. Tesla's own Model Y service manual VIN pages list the codes 7SA = Austin/Fremont, LRW = Shanghai and XP7 = Berlin.

- **This car:** The car was built by Tesla at Gigafactory Shanghai, China.
- **Sources:** [service.tesla.com](https://service.tesla.com/docs/ModelY/ServiceManual/2025/en-us/GUID-BB4CE449-3F8E-4905-AF4A-96DFA87535B5.html), [service.tesla.com](https://service.tesla.com/docs/ModelY/ServiceManual/en-us/GUID-0C797294-574D-4EE4-8017-C339A7D58411.html), [shop4tesla.com](https://www.shop4tesla.com/en/pages/tesla-ratgeber-tesla-vin-decoder)

### 3. pos 4 'Y' (high confidence)

Position 4 is the line/series code, and Y = Model Y, per Tesla's service manual VIN table.

- **This car:** Model Y.
- **Sources:** [service.tesla.com](https://service.tesla.com/docs/ModelY/ServiceManual/2025/en-us/GUID-BB4CE449-3F8E-4905-AF4A-96DFA87535B5.html)

### 4. pos 5 'G' (body type / drive side) (high confidence)

G = 5-door small MPV/SUV, left-hand drive; H = the right-hand-drive version. Real VINs confirm it: right-hand-drive Shanghai Model Ys sold in Australia, New Zealand, Hong Kong and the UK read LRWYH… (LRWYHCFS2NC415958 AU, LRWYHCFS8NC400431 NZ, LRWYHCEK8NC248491 HK, LRWYHCEK6PC542894 UK). Left-hand-drive cars in China and the EU read LRWYG…. Electrek reported that G first appeared with the Model Y in NHTSA VIN data in 2020.

- **This car:** Left-hand drive, 5-door Model Y body. This is correct for Bulgaria and for EU, China, Korea or Middle East origin.
- **Sources:** [findmyelectric.com](https://www.findmyelectric.com/tesla-vin-decoder/), [yeslak.com](https://www.yeslak.com/blogs/tesla-guide/tesla-vin-decoder-all-check-digits-explained), [electrek.co](https://electrek.co/2020/01/15/tesla-model-y-vins-appear-in-nhtsa-database-ahead-of-deliveries/), [ev-inventory.com](https://ev-inventory.com/car/AU-LRWYHCFS2NC415958), [ev-inventory.com](https://ev-inventory.com/car/NZ-LRWYHCFS8NC400431), [tesla-info.com](https://tesla-info.com/car/HK-LRWYHCEK8NC248491), [ev-inventory.com](https://ev-inventory.com/car/GB-LRWYHCEK6PC542894)

### 5. pos 6 'C' (restraint system) (medium confidence)

Position 6 is the restraint-system code. Every 5-seat Shanghai- and Berlin-built Model Y seen reads 'C' (LRWYGC…, LRWYHC…, XP7YGC…). US Fremont/Austin cars read 'D' (7SAYGDE…), and a 2023 Shanghai-built Canada-market car reads LRWYGDEE… with 'D'. The JOWUA decoder defines C (Model X/Y) as Type 2 manual seatbelts with front airbags, PODS (passenger occupant detection) and side inflatable restraints. A developer's GitHub pull request claims C/D = 5-seat. NHTSA's US filings list only A/B/D for Model Y, so C appears to be a non-North-American variant code. Its exact official wording was not found.

- **This car:** The standard restraint package for a 5-seat Shanghai/EU-style Model Y. It is not a 7-seater and not a North-America-coded car. The exact airbag list behind 'C' is unconfirmed from an official Tesla text.
- **Sources:** [jowua-life.com](https://www.jowua-life.com/pages/tesla-vin-decoder-cybertruck-s3xy), [github.com](https://github.com/songsterq/tesla-inventory-helper/pull/18), [cdn.motor1.com](https://cdn.motor1.com/pdf-files/tesla-my2023-vin-decoder.pdf), [tesla-info.com](https://tesla-info.com/car/CA-LRWYGDEE5PC005890), [tesla-info.com](https://tesla-info.com/car/DE-XP7YGCEL9NB011511)

### 6. pos 7 'E' (fuel / battery type) (medium confidence)

E = electric with a lithium-ion battery that is not LFP. F = LFP (lithium iron phosphate). One guide says that on Shanghai cars E specifically means an NMC/NCA pack. In 2022, Shanghai Long Range Model Ys used LG Energy Solution NCM cells, while Shanghai Standard Range/RWD cars used CATL LFP (hence LRWYGCFS). China MIIT filings from Aug 2021 listed two LR AWD variants: one with a made-in-China motor and a 78.4 kWh pack, and one with an imported motor and a 76.8 kWh pack. The VIN does not show which of the two a car has.

- **This car:** The battery is nickel-based (very likely LG Energy Solution NCM from China), not LFP. Pack capacity and supplier have to be confirmed on the car's screen (Controls > Software > Additional Vehicle Information) or by Tesla.
- **Sources:** [teslano1.com](https://teslano1.com/tesla-vin-decoder/), [shop4tesla.com](https://www.shop4tesla.com/en/pages/tesla-ratgeber-tesla-vin-decoder), [autoevolution.com](https://www.autoevolution.com/news/long-range-tesla-model-3-and-model-y-built-at-giga-shanghai-get-a-nice-battery-boost-253783.html), [teslamotorsclub.com](https://teslamotorsclub.com/tmc/threads/anyone-knows-the-y-awd-lr-coming-from-china-uses-ncm-or-lfp-battery.303751/), [insideevs.com](https://insideevs.com/news/525975/tesla-modely-china-new-variants/), [driveteslacanada.ca](https://driveteslacanada.ca/?p=29156)

### 7. pos 8 'K' (motor / drive unit) (high confidence)

K is a dual-motor, non-Performance drive-unit code. FindMyElectric, shop4tesla, tparts and teslabs all describe it as dual (2x standard) motors with hairpin windings (Y#DB/3#DB), and the Taiwanese decoder teslano1 groups Model Y codes as E/K = dual motor and F/L = Performance dual motor. Tesla's Model Y service manual (2020-2024, en-us and zh-cn) lists D, E, F, J, K, L, R and S for digit 8. The search extracts of that table were garbled, so the exact official wording of K could not be read; one extract read K as 'Dual Motor Standard'. In real cars, every LRWYGCEK car found is a Long Range AWD: 17vin's Chinese spec pages for 2021, 2022, 2023 and 2024, plus many tesla-info listings. teslatap added K after a 2021 China-built LR AWD owner reported the code, and said it was 'believed China only'. That belief is outdated: Berlin LR AWD cars are XP7YGCEK… (2023-24). US NHTSA filings for Model Y list only D/E/F, so K never appears in US data. K is not tied to battery supplier.

- **This car:** Dual-motor AWD, non-Performance, i.e. Model Y Long Range AWD. In 2022 Shanghai built no other dual-motor non-Performance Model Y. It is NOT a Performance (that would be 'L') and NOT RWD (that would be 'F' + 'S' or 'J').
- **Sources:** [findmyelectric.com](https://www.findmyelectric.com/tesla-vin-decoder/), [shop4tesla.com](https://www.shop4tesla.com/en/pages/tesla-ratgeber-tesla-vin-decoder), [tparts.com](https://www.tparts.com/blogs/tesla-knowledge-blogs/tesla-vin-decoder-explained), [teslabs.de](https://teslabs.de/en/blogs/tesla-must-know/tesla-vin-decoder-en), [teslano1.com](https://teslano1.com/tesla-vin-decoder/), [teslatap.com](https://teslatap.com/vin-decoder/), [service.tesla.cn](https://service.tesla.cn/docs/ModelY/ServiceManual/zh-cn/GUID-0C797294-574D-4EE4-8017-C339A7D58411.html), [service.tesla.com](https://service.tesla.com/docs/ModelY/ServiceManual/en-us/GUID-0C797294-574D-4EE4-8017-C339A7D58411.html), [en.17vin.com](https://en.17vin.com/model/xpviy.html), [en.17vin.com](https://en.17vin.com/model/fzzgb.html), [en.17vin.com](https://en.17vin.com/model/mbkl9.html), [17vin.com](https://www.17vin.com/model/pxdlf.html), [tesla-info.com](https://tesla-info.com/car/DE-XP7YGCEK1PB129059), [vpic.nhtsa.dot.gov](https://vpic.nhtsa.dot.gov/mid/home/displayfile/fbec7f77-5e2b-4d06-b46c-267e7327c2ff)

### 8. Sibling codes: Shanghai Performance and RWD (high confidence)

Shanghai Performance = LRWYGCEL (17vin lists 2021, 2022, 2023 and 2024 Performance AWD under it; the 2022 Performance spec page says 0-100 km/h in 3.7 s). Shanghai RWD = LRWYGCFS in 2022-2023 (e.g. China-domestic LRWYGCFS6NC424830; EU 2023 cars LRWYGCFS2PC712458 and LRWYGCFS1PC739425) and LRWYGCFJ for 2024 (LRWYGCFJ2RC442030, Beijing). Right-hand-drive RWD = LRWYHCFS (AU/NZ). Berlin uses the same scheme: XP7YGCEK = LR AWD, XP7YGCEL = Performance. US Fremont/Austin LR = 7SAYGDEE, US Performance = 7SAYGDEF.

- **This car:** Comparing against these codes confirms that 'EK' in positions 7-8 = NCM-battery Long Range AWD.
- **Sources:** [en.17vin.com](https://en.17vin.com/model/hhwvq.html), [17vin.com](https://www.17vin.com/model/unrrc.html), [17vin.com](https://www.17vin.com/model/il5bk.html), [en.17vin.com](https://en.17vin.com/model/mbn89.html), [tesla-info.com](https://tesla-info.com/car/CN-LRWYGCFS6NC424830), [tesla-info.com](https://tesla-info.com/car/DE-LRWYGCFS2PC712458), [tesla-info.com](https://tesla-info.com/car/CN-LRWYGCFJ2RC442030), [tesla-info.com](https://tesla-info.com/car/DE-XP7YGCEL9NB011511), [tesla-info.com](https://tesla-info.com/car/US-7SAYGDEF5NF538997)

### 9. Engine/motor codes in Chinese databases (low confidence)

17vin lists the engine (motor) number codes for the LRWYGCEK Long Range AWD as '3D3/3D7', with a 137 kW front motor. Its '2022 modified' (2022改款) LR AWD entry gives a market launch date of 2022-08-09 and a CLTC range of 660 km. A Sohu article calls 3D7 Tesla's newest third-generation, flat-wire (hairpin) motor.

- **This car:** The car was built around 10 Aug 2022, so it probably falls within the '2022改款' spec period, and its motor stampings may read 3D3 (front) and 3D7 (rear). Unverified for this car; check the stampings or ask Tesla.
- **Sources:** [17vin.com](https://www.17vin.com/model/xpviy.html), [en.17vin.com](https://en.17vin.com/model/xpviy.html), [sohu.com](https://www.sohu.com/a/754584401_121124485)

### 10. pos 10 'N' (year): calendar year, not model year (high confidence)

Tesla's Model 3 and Model Y service manuals say digit 10 is the model year for Fremont and Giga Texas cars, but for Giga Shanghai and Giga Berlin cars it is the calendar year the vehicle was built (N = 2022). Drive Tesla Canada's decoder says the same. The manual also says the sequence number does not restart at 000001 each year, so digit 10 differs between cars with the same serial. The data agrees: the earliest NC Model Y found (222058) left the factory on 5 Jan 2022, while 2021 cars carry 'M' (e.g. LRWYGCEK1MC058369, LRWYGCEK7MC140381).

- **This car:** 'N' means built in calendar 2022. The North American pattern of late-2021 builds carrying a 2022 model year does NOT apply to this Shanghai car.
- **Sources:** [service.tesla.com](https://service.tesla.com/docs/Model3/ServiceManual/en-us/GUID-0C797294-574D-4EE4-8017-C339A7D58411.html), [service.tesla.com](https://service.tesla.com/docs/ModelY/ServiceManual/en-us/GUID-0C797294-574D-4EE4-8017-C339A7D58411.html), [driveteslacanada.ca](https://driveteslacanada.ca/tesla-vin-decoder/), [tesla-info.com](https://tesla-info.com/car/NL-LRWYGCEK3NC222058), [tesla-info.com](https://tesla-info.com/car/NL-LRWYGCEK1MC058369)

### 11. pos 11 'C' (plant) (high confidence)

C = Giga Shanghai, per Tesla's service manual plant table and Drive Tesla Canada (B = Berlin, F = Fremont, A = Austin).

- **This car:** Shanghai, consistent with the LRW manufacturer code.
- **Sources:** [service.tesla.com](https://service.tesla.com/docs/Model3/ServiceManual/2024/en-us/GUID-B7B9507C-C984-41F2-89EE-D23CA4E682ED.html), [driveteslacanada.ca](https://driveteslacanada.ca/tesla-vin-decoder/)

### 12. Serial counter: Model Y separate from Model 3 (high confidence)

Shanghai serials are NOT shared between Model 3 and Model Y. Model 3 LRW3F7FS4NC478258 left the factory on 4 Jan 2022 while Model Y LRWYGCEK3NC222058 left on 5 Jan 2022. Model 3 LRW3F7EL4NC615127 left on 14 Aug 2022 while Model Y LRWYGCEK7NC455876 left on 13 Aug 2022. The Model Y counter is shared across left- and right-hand drive, RWD/AWD/Performance, and China-domestic and export cars: China RWD 424830 (28 Jul), AU right-hand-drive RWD 415958 (31 Jul) and DE LR 455876 (13 Aug) sit in one sequence. A 2023 Shanghai-built Canada car has serial 005890 (LRWYGDEE5PC005890), which hints at a separate counter for North-America-coded cars (not verified).

- **This car:** Serial 451763 should be read only against other Shanghai Model Y serials, never against Model 3 serials.
- **Sources:** [tesla-info.com](https://tesla-info.com/car/IE-LRW3F7FS4NC478258), [tesla-info.com](https://tesla-info.com/car/GB-LRW3F7EL4NC615127), [tesla-info.com](https://tesla-info.com/car/NL-LRWYGCEK3NC222058), [tesla-info.com](https://tesla-info.com/car/DE-LRWYGCEK7NC455876), [tesla-info.com](https://tesla-info.com/car/CN-LRWYGCFS6NC424830), [ev-inventory.com](https://ev-inventory.com/car/AU-LRWYHCFS2NC415958), [tesla-info.com](https://tesla-info.com/car/CA-LRWYGDEE5PC005890)

### 13. Build-date bracket for serial 451763 (medium confidence)

Factory-gate dates for nearby Shanghai Model Y serials, from tesla-info / ev-inventory (some only from search snippets): 222058 = 5 Jan 2022; 234845 = 14 Jan; 235355 and 236116 = 15 Jan; 255801 = 29 Jan; 257895 = 3 Feb; 346683 = 14 May; 400431 (NZ RWD) = 29 Jun; 424830 (China RWD) = 28 Jul, delivered 3 Aug; 415958 (AU RWD) = 31 Jul; 455876 (DE LR) = 13 Aug 2022, first registered 9 Sep 2022; 461600 (DE LR) = 17 Aug 2022, first registered 26 Sep 2022; 557340 (NZ RWD) = 8 Oct 2022. Finnish listings show 452426 and 460654 first registered 9/2022. Between 424830 and 455876 the rate is about 1,940 serials/day, and between 455876 and 461600 about 1,430/day. Serial 451763 is 4,113 below 455876, which puts its factory-gate date at about 10–11 Aug 2022 (likely window 8–13 Aug). End-of-line build was probably a day or two earlier. Gate dates for export and domestic cars can differ by ±3 days: 415958 has a later gate date than 424830.

- **This car:** Most likely built in early-to-mid August 2022, factory gate around 10–11 Aug 2022. If it was sold new in Europe, expect first registration around September (possibly October) 2022. Registration papers showing a very different first-registration date, or a first registration outside the EU, deserve questions.
- **Sources:** [tesla-info.com](https://tesla-info.com/car/DE-LRWYGCEK7NC455876), [tesla-info.com](https://tesla-info.com/car/DE-LRWYGCEK7NC461600), [tesla-info.com](https://tesla-info.com/car/CN-LRWYGCFS6NC424830), [ev-inventory.com](https://ev-inventory.com/car/AU-LRWYHCFS2NC415958), [ev-inventory.com](https://ev-inventory.com/car/NZ-LRWYHCFS8NC400431), [tesla-info.com](https://tesla-info.com/car/NZ-LRWYHCFS0NC557340), [tesla-info.com](https://tesla-info.com/car/FR-LRWYGCEKXNC346683), [tesla-info.com](https://tesla-info.com/car/DE-LRWYGCEK7NC257895), [ev-inventory.com](https://ev-inventory.com/car/FI-LRWYGCEK6NC255801), [tesla-info.com](https://tesla-info.com/car/DK-LRWYGCEK6NC236116), [tesla-info.com](https://tesla-info.com/car/FR-LRWYGCEK8NC235355), [tesla-info.com](https://tesla-info.com/car/FR-LRWYGCEK9NC234845), [tesla-info.com](https://tesla-info.com/car/NL-LRWYGCEK3NC222058), [nettiauto.com](https://www.nettiauto.com/en/tesla/model-y/15734109), [nettiauto.com](https://www.nettiauto.com/yritys/2308090/vaihtoautot/15863549)

### 14. Production context, August 2022 (high confidence)

Shanghai's Model Y line finished its upgrade on 16 July 2022 and the Model 3 line on about 7-8 Aug 2022. CPCA data shows August 2022 was a record month for Giga Shanghai: 76,605 cars built, of which 56,721 were Model Y. 42,463 cars were exported that month.

- **This car:** The car comes from the high-volume, export-heavy August 2022 run after the line upgrades. The roughly 1,800–1,950 Model Y serials per day seen in the data match the 56,721 August total.
- **Sources:** [driveteslacanada.ca](https://driveteslacanada.ca/?p=57536), [cnevpost.com](https://cnevpost.com/2022/06/23/teslas-shanghai-plant-will-reportedly-finish-upgrades-around-august-7-with-significant-capacity-increases), [insideevs.com](https://insideevs.com/news/600789/tesla-giga-shanghai-3000-cars-day-after-upgrades/)

### 15. Export vs China-domestic: what the VIN can and cannot show (high confidence)

The LRWYGC… pattern (left-hand drive, 'C' restraint) is used for China-domestic cars as well as left-hand-drive exports. Example: LRWYGCFS6NC424830 was delivered new in Guangzhou on 3 Aug 2022, and its serial is very close to this car's. Chinese VIN databases (17vin) list LRWYGCEK…NC… cars, including NC389819 and NC493269. Only pos5 'H' (right-hand drive) separates AU/NZ/HK/UK/JP-type markets. Physical difference: China-market cars use the GB/T charging standard, while European cars use Type 2/CCS2; the Chinese and European Type 2 plugs look alike but are incompatible.

- **This car:** The VIN alone cannot show whether this car was built for Europe or for China. Check: (1) an EU CoC with an EU type-approval number, (2) the first-registration country and date in the papers, and (3) the charge port, which should be CCS2 on an EU-spec car. Its serial sits among cars that were registered in Germany and Finland in Sep 2022, which fits, but does not prove, a European-market car.
- **Sources:** [tesla-info.com](https://tesla-info.com/car/CN-LRWYGCFS6NC424830), [en.17vin.com](https://en.17vin.com/model/xpviy.html), [teslamotorsclub.com](https://www.teslamotorsclub.com/tmc/threads/tesla-charge-ports-plugs-from-china-north-america-and-europe-compared-for-models-s-x-3-y.246571/), [akyga.com](https://www.akyga.com/news-list/93-how-to-charge-chinese-electric-cars-in-europe-gb-t-adapters-for-type-2-and-ccs2.html)

### 16. This exact VIN online (high confidence)

Exact-match searches for 'LRWYGCEK7NC451763' and 'NC451763' found no listing, auction, salvage record or registry page. The nearest public siblings are LRWYGCEK5NC452426 (Finnish used listing, LR, first registered 9/2022), LRWYGCEK1NC455064 (Finnish listing), LRWYGCEK7NC455876 (DE, factory gate 13 Aug 2022), LRWYGCEK3NC460654 (Finland, Tesla CPO, first registered 9/2022), LRWYGCEK7NC461600 (DE), LRWYGCEK8NC462240, LRWYGCEKXNC464197 and LRWYGCEK2NC472424 (EU auction lots).

- **This car:** No public history for this car was found online, including no auction or salvage record. That does not mean it has no history; a paid history check and Tesla service records are still needed.
- **Sources:** [nettiauto.com](https://www.nettiauto.com/en/tesla/model-y/15734109), [nettiauto.com](https://www.nettiauto.com/en/tesla/model-y/15632583), [nettiauto.com](https://www.nettiauto.com/yritys/2308090/vaihtoautot/15863549), [carsbat.com](https://carsbat.com/de/detail/lrwygcek8nc462240-ipx7nu/), [carsbat.com](https://carsbat.com/de/detail/lrwygcekxnc464197-2vhdlz/), [carsbat.com](https://carsbat.com/de/detail/lrwygcek2nc472424-derjll/)

### 17. Battery-reliability context (not encoded in VIN) (medium confidence)

In Dec 2025 the Croatian repair shop EV Clinic reported high failure rates and poor repairability for LG NCM811 packs made in Nanjing and fitted to China-built Model 3/Y Long Range and Performance cars. This is one shop's data; New Mobility News questioned how representative it is, and no Tesla or LG response was found.

- **This car:** The 'E' (NCM) plus Shanghai LR combination puts this car in the group EV Clinic is talking about. The claim itself is disputed. Ask for a battery health / state-of-health report, and check how much of Tesla's 8-year / 192,000 km battery warranty remains (from the first-registration date, about Sep 2022 → about Sep 2030).
- **Sources:** [electrek.co](https://electrek.co/2025/12/01/tesla-model-3-y-chinese-lg-batteries-showing-catastrophic-failure-rates-repair-shop/), [insideevs.com](https://insideevs.com/news/780568/tesla-lg-battery-pack-defects-china/), [newmobility.news](https://newmobility.news/2025/12/02/how-credible-is-ev-clinics-warning-on-teslas-china-built-nmc-batteries/)

### 18. FINAL DECODE TABLE (high confidence)

L-R-W = Tesla Shanghai (WMI) | Y = Model Y | G = 5-door SUV/MPV, left-hand drive | C = restraint system, 5-seat non-North-American package (exact official wording not found) | E = electric, non-LFP lithium-ion (NCM) | K = dual-motor non-Performance (hairpin) drive unit = Long Range AWD | 7 = check digit (verified) | N = calendar year of build 2022 (Shanghai rule) | C = Giga Shanghai plant | 451763 = Shanghai Model Y-only production serial, estimated factory gate about 10–11 Aug 2022 (window about 8–13 Aug 2022).

- **This car:** The whole table is for LRWYGCEK7NC451763. The trim (LR AWD), plant, year and drive side are high confidence. The build date is medium confidence, interpolated from nearby serials. The exact meaning of 'C' in position 6 is medium confidence.
- **Sources:** [service.tesla.com](https://service.tesla.com/docs/ModelY/ServiceManual/en-us/GUID-0C797294-574D-4EE4-8017-C339A7D58411.html), [service.tesla.com](https://service.tesla.com/docs/Model3/ServiceManual/en-us/GUID-0C797294-574D-4EE4-8017-C339A7D58411.html), [findmyelectric.com](https://www.findmyelectric.com/tesla-vin-decoder/), [teslano1.com](https://teslano1.com/tesla-vin-decoder/), [en.17vin.com](https://en.17vin.com/model/xpviy.html), [tesla-info.com](https://tesla-info.com/car/DE-LRWYGCEK7NC455876)

## Open questions

- The exact official wording of position 6 'C' (restraint system) and position 8 'K' in Tesla's own 2020-2024 Model Y service manual table. Search-engine extracts of the table were garbled; reading the page directly (service.tesla.com …GUID-0C797294…) would settle it.
- The actual factory-gate and first-registration dates of THIS car. They are only estimated here (gate about 10–11 Aug 2022) from neighbouring serials. Get them from the seller's registration papers or EU CoC, from Tesla (the build date is also on the driver door-pillar sticker), or from a tesla-info VIN lookup run outside this environment.
- Whether this car was first delivered in the EU or in China (and later exported). The VIN cannot tell. Check the CoC / type approval, the first-registration country, and the charge port (CCS2 vs GB/T).
- Which of the two Shanghai LR AWD battery/motor variants in the MIIT filings it has (78.4 kWh with made-in-China motor vs 76.8 kWh with imported motor), the exact pack part number, and the current battery health. The VIN does not encode any of these.
- Whether the 2023 Shanghai-built Canada-market car with serial 005890 (LRWYGDEE…) means a separate serial counter for North-America-coded Shanghai cars. This does not affect this EU-pattern VIN.
- The exact first-registration date of the closest sibling LRWYGCEK5NC452426 (only '9/2022' seen in a snippet) and the date of LRWYGCEK1NC455064. Both would tighten the bracket further.
