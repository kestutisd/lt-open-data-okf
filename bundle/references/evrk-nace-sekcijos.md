---
type: Reference
title: "EVRK 2 / NACE Rev. 2 ekonominės veiklos rūšių klasifikatorius (ir EVRK 2.1 pereigos taisyklės)"
description: "EVRK 2 / NACE Rev. 2 21 sekcija (A–U), 88 skyriai (01–99) ir 272 grupės pagal Reglamentą (EB) Nr. 1893/2006 bei 2025-01-01 EVRK 2.1 (NACE Rev. 2.1) sekcijų ir 45 skyriaus pokyčių įspėjimas."
resource: "https://publications.europa.eu/resource/celex/32006R1893"
tags: [standards, evrk, evrk-2-1, nace, economic-activity, klasifikatorius, reference]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: std-evrk
    resource: "https://publications.europa.eu/resource/celex/32006R1893"
    title: "Regulation (EC) No 1893/2006 establishing the statistical classification of economic activities NACE Revision 2 (EVRK 2)"
    author: "team:eu-publications-office"
    last_modified: "2006-12-30T00:00:00Z"
  - id: std-evrk21
    resource: "https://publications.europa.eu/resource/celex/32023R0137"
    title: "Commission Delegated Regulation (EU) 2023/137 amending Regulation (EC) No 1893/2006 as regards NACE Rev. 2.1 (EVRK 2.1 effective 2025-01-01)"
    author: "team:eu-publications-office"
    last_modified: "2023-01-20T00:00:00Z"
---

# Ekonominės veiklos rūšių klasifikatorius (EVRK 2 / NACE Rev. 2 ir EVRK 2.1 pereiga)

Lietuvos **EVRK 2 red.** (*Ekonominės veiklos rūšių klasifikatorius*) tiesiogiai atitinka Europos Sąjungos **NACE Rev. 2** statistinį ekonominės veiklos klasifikatorių, patvirtintą Europos Parlamento ir Tarybos reglamentu (EB) Nr. 1893/2006 (`CELEX:32006R1893`).[^std-evrk]

## Kritinis 2025-01-01 EVRK 2 -> EVRK 2.1 (NACE Rev. 2.1) sekcijų ir 2 skaitmenų skyrių pokytis

> **Įspėjimas tyrėjams ir analitikams (jungimas per 2024–2026 m. ribą):** Nuo **2025-01-01** įsigaliojus Komisijos deleguotajam reglamentui (ES) 2023/137 (**NACE Rev. 2.1** / Lietuvos **EVRK 2.1 red.**), pasikeitė **tiek 1 raidės sekcijos, tiek 2 skaitmenų skyriai** (bei dalis grupių ir klasių):[^std-evrk21]
> 1. **1 raidės sekcijų poslinkis (`A`–`U` -> `A`–`V`):** Ankstesnė EVRK 2 sekcija **`J`** (*Informacija ir ryšiai*, skyriai `58`–`63`) padalinta į **`J`** (*Leidyba, transliavimas ir turinio kūrimas bei platinimas*, skyriai `58`–`60`) ir **`K`** (*Telekomunikacijos, kompiuterių programavimas, konsultavimas, skaičiavimo infrastruktūra ir kita informacinių paslaugų veikla*, skyriai `61`–`63`), todėl buvusios sekcijos **`K`–`U`** pasislinko **+1 raide** į **`L`–`V`** (`K` -> `L`, `L` -> `M`, `M` -> `N`, `N` -> `O`, `O` -> `P`, `P` -> `Q`, `Q` -> `R`, `R` -> `S`, `S` -> `T`, `T` -> `U`, `U` -> `V`).[^std-evrk21]
> 2. **2 skaitmenų skyriaus `45` panaikinimas ir kitų skyrių restruktūrizavimas:** Ankstesnis EVRK 2 skyrius **`45`** (*Variklinių transporto priemonių ir motociklų didmeninė ir mažmeninė prekyba bei remontas* / *Wholesale and retail trade and repair of motor vehicles and motorcycles*) **panaikintas (išformuotas)** — jo veiklos išskaidytos į skyrių **`46`** (*Didmeninė prekyba*), skyrių **`47`** (*Mažmeninė prekyba*) ir skyrių **`95`** (*Kompiuterių, asmeninių ir namų ūkio reikmenų bei variklinių transporto priemonių ir motociklų remontas ir techninė priežiūra*), kartu pergrupuojant skaitmeninio tarpininkavimo, energetikos ir informacinių paslaugų skyrius bei grupes.[^std-evrk21]
> 3. **Daugiamečių duomenų jungimo taisyklė:** Jungiant daugiamečius VDA, VMI, Sodros ar JAR rinkinius per `2025-01-01` ribą, **negalima tiesiogiai (naiviai) jungti nei pagal 1 raidės sekciją, nei pagal 2 skaitmenų skyriaus kodą** nepatikrinus klasifikatoriaus redakcijos (`EVRK 2` vs `EVRK 2.1`). Būtina naudoti oficialias VDA / Eurostat *EVRK 2 red. ir EVRK 2.1 red. ryšių lenteles* (correspondence tables) bei Spinta klasifikatorių lenteles [datasets/gov/lsd/cl/evrk/EkonominesVeiklosRusis](../datasets/gov/lsd/cl/evrk/EkonominesVeiklosRusis.md) ir [datasets/gov/lsd/cl/evrk2_1/EkonominesVeiklosRusis](../datasets/gov/lsd/cl/evrk2_1/EkonominesVeiklosRusis.md).[^std-evrk][^std-evrk21]

## EVRK 2 / NACE Rev. 2 hierarchinė struktūra

1. **Sekcija (Section):** 1 raidės kodas nuo `A` iki `U` (**21 sekcija** EVRK 2; `A`–`V` EVRK 2.1).[^std-evrk][^std-evrk21]
2. **Skyrius (Division):** 2 skaitmenų kodas nuo `01` iki `99` (**88 skyriai** EVRK 2; EVRK 2.1 skyrius `45` išformuotas).[^std-evrk][^std-evrk21]
3. **Grupė (Group):** 3 skaitmenų kodas `XX.X` (**272 grupės** EVRK 2).[^std-evrk]
4. **Klasė (Class):** 4 skaitmenų kodas `XX.XX` (nacionaliniame EVRK pridedamas 5–6 skaitmenų poklasis `XX.XX.XX`).[^std-evrk]

## 1. EVRK 2 / NACE Rev. 2 sekcijos (21 sekcija, `A`–`U`)

| Sekcija (EVRK 2) | Pavadinimas (LT) | Title (EN) |
| --- | --- | --- |
| `A` | ŽEMĖS ŪKIS, MIŠKININKYSTĖ IR ŽUVININKYSTĖ | AGRICULTURE, FORESTRY AND FISHING |
| `B` | KASYBA IR KARJERŲ EKSPLOATAVIMAS | MINING AND QUARRYING |
| `C` | APDIRBAMOJI GAMYBA | MANUFACTURING |
| `D` | ELEKTROS, DUJŲ, GARO TIEKIMAS IR ORO KONDICIONAVIMAS | ELECTRICITY, GAS, STEAM AND AIR CONDITIONING SUPPLY |
| `E` | VANDENS TIEKIMAS; NUOTEKŲ VALYMAS, ATLIEKŲ TVARKYMAS IR REGENERAVIMAS | WATER SUPPLY; SEWERAGE, WASTE MANAGEMENT AND REMEDIATION ACTIVITIES |
| `F` | STATYBA | CONSTRUCTION |
| `G` | DIDMENINĖ IR MAŽMENINĖ PREKYBA; VARIKLINIŲ TRANSPORTO PRIEMONIŲ IR MOTOCIKLŲ REMONTAS | WHOLESALE AND RETAIL TRADE; REPAIR OF MOTOR VEHICLES AND MOTORCYCLES |
| `H` | TRANSPORTAS IR SAUGOJIMAS | TRANSPORTATION AND STORAGE |
| `I` | APGYVENDINIMO IR MAITINIMO PASLAUGŲ VEIKLA | ACCOMMODATION AND FOOD SERVICE ACTIVITIES |
| `J` | INFORMACIJA IR RYŠIAI | INFORMATION AND COMMUNICATION |
| `K` | FINANSINĖ IR DRAUDIMO VEIKLA | FINANCIAL AND INSURANCE ACTIVITIES |
| `L` | NEKILNOJAMOJO TURTO OPERACIJOS | REAL ESTATE ACTIVITIES |
| `M` | PROFESINĖ, MOKSLINĖ IR TECHNINĖ VEIKLA | PROFESSIONAL, SCIENTIFIC AND TECHNICAL ACTIVITIES |
| `N` | ADMINISTRACINĖ IR APTARNAVIMO VEIKLA | ADMINISTRATIVE AND SUPPORT SERVICE ACTIVITIES |
| `O` | VIEŠASIS VALDYMAS IR GYNYBA; PRIVALOMASIS SOCIALINIS DRAUDIMAS | PUBLIC ADMINISTRATION AND DEFENCE; COMPULSORY SOCIAL SECURITY |
| `P` | ŠVIETIMAS | EDUCATION |
| `Q` | ŽMONIŲ SVEIKATOS PRIEŽIŪRA IR SOCIALINIS DARBAS | HUMAN HEALTH AND SOCIAL WORK ACTIVITIES |
| `R` | MENINĖ, PRAMOGINĖ IR POILSIO ORGANIZAVIMO VEIKLA | ARTS, ENTERTAINMENT AND RECREATION |
| `S` | KITA APTARNAVIMO VEIKLA | OTHER SERVICE ACTIVITIES |
| `T` | NAMŲ ŪKIŲ, SAMDANČIŲ DARBININKUS, VEIKLA; NAMŲ ŪKIŲ VEIKLA, SUSIJUSI SU SAVOMS REIKMĖMS TENKINTI SKIRTŲ NEDIFERENCIJUOJAMŲ GAMINIŲ GAMYBA IR PASLAUGŲ TEIKIMU | ACTIVITIES OF HOUSEHOLDS AS EMPLOYERS; UNDIFFERENTIATED GOODS- AND SERVICES-PRODUCING ACTIVITIES OF HOUSEHOLDS FOR OWN USE |
| `U` | EKSTRATERITORINIŲ ORGANIZACIJŲ IR ĮSTAIGŲ VEIKLA | ACTIVITIES OF EXTRATERRITORIAL ORGANISATIONS AND BODIES |

## 2. EVRK 2 / NACE Rev. 2 2 skaitmenų skyriai (88 skyriai, `01`–`99`)

| Skyrius (2 sk.) | Sekcija (EVRK 2) | Pavadinimas (LT) | Title (EN) |
| --- | --- | --- | --- |
| `01` | `A` | Augalininkystė ir gyvulininkystė, medžioklė ir susijusių paslaugų veikla | Crop and animal production, hunting and related service activities |
| `02` | `A` | Miškininkystė ir medienos ruoša | Forestry and logging |
| `03` | `A` | Žvejyba ir akvakultūra | Fishing and aquaculture |
| `05` | `B` | Akmens anglių ir rusvųjų anglių kasyba | Mining of coal and lignite |
| `06` | `B` | Žalios naftos ir gamtinių dujų gavyba | Extraction of crude petroleum and natural gas |
| `07` | `B` | Metalų rūdų kasyba | Mining of metal ores |
| `08` | `B` | Kita kasyba ir karjerų eksploatavimas | Other mining and quarrying |
| `09` | `B` | Kasybai būdingų paslaugų veikla | Mining support service activities |
| `10` | `C` | Maisto produktų gamyba | Manufacture of food products |
| `11` | `C` | Gėrimų gamyba | Manufacture of beverages |
| `12` | `C` | Tabako gaminių gamyba | Manufacture of tobacco products |
| `13` | `C` | Tekstilės gaminių gamyba | Manufacture of textiles |
| `14` | `C` | Drabužių siuvimas (gamyba) | Manufacture of wearing apparel |
| `15` | `C` | Odos ir odos dirbinių gamyba | Manufacture of leather and related products |
| `16` | `C` | Medienos bei medienos ir kamštienos gaminių, išskyrus baldus, gamyba; gaminių iš šiaudų ir pynimo medžiagų gamyba | Manufacture of wood and of products of wood and cork, except furniture; manufacture of articles of straw and plaiting materials |
| `17` | `C` | Popieriaus ir popieriaus gaminių gamyba | Manufacture of paper and paper products |
| `18` | `C` | Spausdinimas ir įrašytų laikmenų tiražavimas | Printing and reproduction of recorded media |
| `19` | `C` | Kokso ir rafinuotų naftos produktų gamyba | Manufacture of coke and refined petroleum products |
| `20` | `C` | Chemikalų ir chemijos produktų gamyba | Manufacture of chemicals and chemical products |
| `21` | `C` | Pagrindinių vaistų pramonės gaminių ir farmacinių preparatų gamyba | Manufacture of basic pharmaceutical products and pharmaceutical preparations |
| `22` | `C` | Guminių ir plastikinių gaminių gamyba | Manufacture of rubber and plastic products |
| `23` | `C` | Kitų nemetalo mineralinių produktų gamyba | Manufacture of other non-metallic mineral products |
| `24` | `C` | Pagrindinių metalų gamyba | Manufacture of basic metals |
| `25` | `C` | Metalo gaminių, išskyrus mašinas ir įrenginius, gamyba | Manufacture of fabricated metal products, except machinery and equipment |
| `26` | `C` | Kompiuterinių, elektroninių ir optinių gaminių gamyba | Manufacture of computer, electronic and optical products |
| `27` | `C` | Elektros įrangos gamyba | Manufacture of electrical equipment |
| `28` | `C` | Niekur kitur nepriskirtų mašinų ir įrangos gamyba | Manufacture of machinery and equipment n.e.c. |
| `29` | `C` | Variklinių transporto priemonių, priekabų ir puspriekabių gamyba | Manufacture of motor vehicles, trailers and semi-trailers |
| `30` | `C` | Kitų transporto priemonių ir įrangos gamyba | Manufacture of other transport equipment |
| `31` | `C` | Baldų gamyba | Manufacture of furniture |
| `32` | `C` | Kita gamyba | Other manufacturing |
| `33` | `C` | Mašinų ir įrangos remontas ir įrengimas | Repair and installation of machinery and equipment |
| `35` | `D` | Elektros, dujų, garo tiekimas ir oro kondicionavimas | Electricity, gas, steam and air conditioning supply |
| `36` | `E` | Vandens rinkimas, valymas ir tiekimas | Water collection, treatment and supply |
| `37` | `E` | Nuotekų valymas | Sewerage |
| `38` | `E` | Atliekų rinkimas, tvarkymas ir šalinimas; medžiagų panaudojimas | Waste collection, treatment and disposal activities; materials recovery |
| `39` | `E` | Regeneravimas ir kita atliekų tvarkyba | Remediation activities and other waste management services |
| `41` | `F` | Pastatų statyba | Construction of buildings |
| `42` | `F` | Inžinerinių statinių statyba | Civil engineering |
| `43` | `F` | Specializuota statybos veikla | Specialised construction activities |
| `45` | `G` | Variklinių transporto priemonių ir motociklų didmeninė ir mažmeninė prekyba bei remontas | Wholesale and retail trade and repair of motor vehicles and motorcycles |
| `46` | `G` | Didmeninė prekyba, išskyrus prekybą variklinėmis transporto priemonėmis ir motociklais | Wholesale trade, except of motor vehicles and motorcycles |
| `47` | `G` | Mažmeninė prekyba, išskyrus variklinių transporto priemonių ir motociklų prekybą | Retail trade, except of motor vehicles and motorcycles |
| `49` | `H` | Sausumos transportas ir transportavimas vamzdynais | Land transport and transport via pipelines |
| `50` | `H` | Vandens transportas | Water transport |
| `51` | `H` | Oro transportas | Air transport |
| `52` | `H` | Sandėliavimas ir transportui būdingų paslaugų veikla | Warehousing and support activities for transportation |
| `53` | `H` | Pašto ir pasiuntinių (kurjerių) veikla | Postal and courier activities |
| `55` | `I` | Apgyvendinimo veikla | Accommodation |
| `56` | `I` | Maitinimo ir gėrimų teikimo veikla | Food and beverage service activities |
| `58` | `J` | Leidybinė veikla | Publishing activities |
| `59` | `J` | Kino filmų, vaizdo filmų ir televizijos programų gamyba, garso įrašymo ir muzikos įrašų leidybos veikla | Motion picture, video and television programme production, sound recording and music publishing activities |
| `60` | `J` | Programų rengimas ir transliavimas | Programming and broadcasting activities |
| `61` | `J` | Telekomunikacijos | Telecommunications |
| `62` | `J` | Kompiuterių programavimo, konsultacinė ir susijusi veikla | Computer programming, consultancy and related activities |
| `63` | `J` | Informacinių paslaugų veikla | Information service activities |
| `64` | `K` | Finansinių paslaugų veikla, išskyrus draudimą ir pensijų lėšų kaupimą | Financial service activities, except insurance and pension funding |
| `65` | `K` | Draudimo, perdraudimo ir pensijų lėšų kaupimo, išskyrus privalomąjį socialinį draudimą, veikla | Insurance, reinsurance and pension funding, except compulsory social security |
| `66` | `K` | Pagalbinė finansinių paslaugų ir draudimo veikla | Activities auxiliary to financial services and insurance activities |
| `68` | `L` | Nekilnojamojo turto operacijos | Real estate activities |
| `69` | `M` | Teisinė ir apskaitos veikla | Legal and accounting activities |
| `70` | `M` | Pagrindinių buveinių veikla; konsultacinė valdymo veikla | Activities of head offices; management consultancy activities |
| `71` | `M` | Architektūrinė ir inžinerijos veikla; techninis tikrinimas ir analizė | Architectural and engineering activities; technical testing and analysis |
| `72` | `M` | Moksliniai tyrimai ir taikomoji veikla | Scientific research and development |
| `73` | `M` | Reklama ir rinkos tyrimas | Advertising and market research |
| `74` | `M` | Kita profesinė, mokslinė ir techninė veikla | Other professional, scientific and technical activities |
| `75` | `M` | Veterinarinė veikla | Veterinary activities |
| `77` | `N` | Nuoma ir išperkamoji nuoma | Rental and leasing activities |
| `78` | `N` | Įdarbinimo veikla | Employment activities |
| `79` | `N` | Kelionių agentūrų, ekskursijų organizatorių, išankstinio užsakymo paslaugų ir susijusi veikla | Travel agency, tour operator reservation service and related activities |
| `80` | `N` | Apsaugos ir tyrimo veikla | Security and investigation activities |
| `81` | `N` | Pastatų aptarnavimas ir kraštovaizdžio tvarkymas | Services to buildings and landscape activities |
| `82` | `N` | Administracinė veikla, įstaigų ir kitų verslo įmonių aptarnavimo veikla | Office administrative, office support and other business support activities |
| `84` | `O` | Viešasis valdymas ir gynyba; privalomasis socialinis draudimas | Public administration and defence; compulsory social security |
| `85` | `P` | Švietimas | Education |
| `86` | `Q` | Žmonių sveikatos priežiūros veikla | Human health activities |
| `87` | `Q` | Kita stacionarinė globos veikla | Residential care activities |
| `88` | `Q` | Nesusijusio su apgyvendinimu socialinio darbo veikla | Social work activities without accommodation |
| `90` | `R` | Kūrybinė, meninė ir pramogų organizavimo veikla | Creative, arts and entertainment activities |
| `91` | `R` | Bibliotekų, archyvų, muziejų ir kita kultūrinė veikla | Libraries, archives, museums and other cultural activities |
| `92` | `R` | Azartinių žaidimų ir lažybų organizavimo veikla | Gambling and betting activities |
| `93` | `R` | Sportinė veikla, pramogų ir poilsio organizavimo veikla | Sports activities and amusement and recreation activities |
| `94` | `S` | Narystės organizacijų veikla | Activities of membership organisations |
| `95` | `S` | Kompiuterių ir asmeninių bei namų ūkio reikmenų taisymas | Repair of computers and personal and household goods |
| `96` | `S` | Kita asmenų aptarnavimo veikla | Other personal service activities |
| `97` | `T` | Namų ūkių, samdančių namų ūkio personalą, veikla | Activities of households as employers of domestic personnel |
| `98` | `T` | Privačių namų ūkių veikla, susijusi su savoms reikmėms tenkinti skirtų nediferencijuojamų gaminių gamyba ir paslaugų teikimu | Undifferentiated goods- and services-producing activities of private households for own use |
| `99` | `U` | Ekstrateritorinių organizacijų ir įstaigų veikla | Activities of extraterritorial organisations and bodies |

## 3. EVRK 2 / NACE Rev. 2 3 skaitmenų grupės (272 grupės)

| Grupė (3 sk.) | Sekcija (EVRK 2) | Pavadinimas (LT) | Title (EN) |
| --- | --- | --- | --- |
| `01.1` | `A` | Vienmečių augalų auginimas | Growing of non-perennial crops |
| `01.2` | `A` | Daugiamečių augalų auginimas | Growing of perennial crops |
| `01.3` | `A` | Augalų dauginimas | Plant propagation |
| `01.4` | `A` | Gyvulininkystė | Animal production |
| `01.5` | `A` | Mišrusis žemės ūkis | Mixed farming |
| `01.6` | `A` | Žemės ūkiui būdingų paslaugų ir derliaus apdorojimo veikla | Support activities to agriculture and post-harvest crop activities |
| `01.7` | `A` | Medžioklė, gaudymas spąstais ir susijusių paslaugų veikla | Hunting, trapping and related service activities |
| `02.1` | `A` | Miško medžių auginimas ir kita miškininkystės veikla | Silviculture and other forestry activities |
| `02.2` | `A` | Medienos ruoša | Logging |
| `02.3` | `A` | Laukinių ne medžių produktų rinkimas | Gathering of wild growing non-wood products |
| `02.4` | `A` | Miškininkystei būdingų paslaugų veikla | Support services to forestry |
| `03.1` | `A` | Žvejyba | Fishing |
| `03.2` | `A` | Akvakultūra | Aquaculture |
| `05.1` | `B` | Juodųjų akmens anglių (antracito) kasyba | Mining of hard coal |
| `05.2` | `B` | Rusvųjų anglių kasyba | Mining of lignite |
| `06.1` | `B` | Žalios naftos gavyba | Extraction of crude petroleum |
| `06.2` | `B` | Gamtinių dujų gavyba | Extraction of natural gas |
| `07.1` | `B` | Geležies rūdų kasyba | Mining of iron ores |
| `07.2` | `B` | Spalvotųjų metalų rūdų kasyba | Mining of non-ferrous metal ores |
| `08.1` | `B` | Akmens, smėlio ir molio karjerų eksploatavimas | Quarrying of stone, sand and clay |
| `08.9` | `B` | Niekur kitur nepriskirta kasyba ir karjerų eksploatavimas | Mining and quarrying n.e.c. |
| `09.1` | `B` | Naftos ir gamtinių dujų gavybai būdingų paslaugų veikla | Support activities for petroleum and natural gas extraction |
| `09.9` | `B` | Kitai kasybai ir karjerų eksploatavimui būdingų paslaugų veikla | Support activities for other mining and quarrying |
| `10.1` | `C` | Mėsos perdirbimas ir konservavimas ir mėsos produktų gamyba | Processing and preserving of meat and production of meat products |
| `10.2` | `C` | Žuvų, vėžiagyvių ir moliuskų perdirbimas ir konservavimas | Processing and preserving of fish, crustaceans and molluscs |
| `10.3` | `C` | Vaisių ir daržovių perdirbimas ir konservavimas | Processing and preserving of fruit and vegetables |
| `10.4` | `C` | Gyvūninių ir augalinių riebalų bei aliejaus gamyba | Manufacture of vegetable and animal oils and fats |
| `10.5` | `C` | Pieno produktų gamyba | Manufacture of dairy products |
| `10.6` | `C` | Grūdų malimo produktų, krakmolo ir krakmolo produktų gamyba | Manufacture of grain mill products, starches and starch products |
| `10.7` | `C` | Kepyklos ir miltinių produktų gamyba | Manufacture of bakery and farinaceous products |
| `10.8` | `C` | Kitų maisto produktų gamyba | Manufacture of other food products |
| `10.9` | `C` | Paruoštų pašarų gyvuliams gamyba | Manufacture of prepared animal feeds |
| `11.0` | `C` | Gėrimų gamyba | Manufacture of beverages |
| `12.0` | `C` | Tabako gaminių gamyba | Manufacture of tobacco products |
| `13.1` | `C` | Tekstilės pluoštų paruošimas ir verpimas | Preparation and spinning of textile fibres |
| `13.2` | `C` | Tekstilės audimas | Weaving of textiles |
| `13.3` | `C` | Tekstilės apdaila | Finishing of textiles |
| `13.9` | `C` | Kitų tekstilės gaminių ir dirbinių gamyba | Manufacture of other textiles |
| `14.1` | `C` | Drabužių, išskyrus kailinius drabužius, siuvimas (gamyba) | Manufacture of wearing apparel, except fur apparel |
| `14.2` | `C` | Kailinių dirbinių ir gaminių gamyba | Manufacture of articles of fur |
| `14.3` | `C` | Megztų (trikotažinių) ir nertų drabužių gamyba | Manufacture of knitted and crocheted apparel |
| `15.1` | `C` | Odų rauginimas ir išdirbimas; lagaminų, rankinių, balno reikmenų ir pakinktų gamyba; kailių išdirbimas ir dažymas | Tanning and dressing of leather; manufacture of luggage, handbags, saddlery and harness; dressing and dyeing of fur |
| `15.2` | `C` | Avalynės gamyba | Manufacture of footwear |
| `16.1` | `C` | Medienos pjaustymas ir obliavimas | Sawmilling and planing of wood |
| `16.2` | `C` | Gaminių ir dirbinių iš medienos, kamštienos, šiaudų ir pynimo medžiagų gamyba | Manufacture of products of wood, cork, straw and plaiting materials |
| `17.1` | `C` | Plaušienos, popieriaus ir kartono gamyba | Manufacture of pulp, paper and paperboard |
| `17.2` | `C` | Popieriaus ir kartoninių gaminių gamyba | Manufacture of articles of paper and paperboard |
| `18.1` | `C` | Spausdinimas ir su spausdinimu susijusios paslaugos | Printing and service activities related to printing |
| `18.2` | `C` | Įrašytų laikmenų tiražavimas | Reproduction of recorded media |
| `19.1` | `C` | Koksavimo krosnių produktų gamyba | Manufacture of coke oven products |
| `19.2` | `C` | Rafinuotų naftos produktų gamyba | Manufacture of refined petroleum products |
| `20.1` | `C` | Pagrindinių chemikalų, trąšų ir azoto junginių, pirminių plastikų ir pirminio sintetinio kaučiuko gamyba | Manufacture of basic chemicals, fertilisers and nitrogen compounds, plastics and synthetic rubber in primary forms |
| `20.2` | `C` | Pesticidų ir kitų agrocheminių medžiagų gamyba | Manufacture of pesticides and other agrochemical products |
| `20.3` | `C` | Dažų, lakų ir panašių dangų medžiagų, spaustuvinių dažų ir mastikų gamyba | Manufacture of paints, varnishes and similar coatings, printing ink and mastics |
| `20.4` | `C` | Muilo ir ploviklių, valiklių ir blizgiklių, kvepalų ir tualeto priemonių gamyba | Manufacture of soap and detergents, cleaning and polishing preparations, perfumes and toilet preparations |
| `20.5` | `C` | Kitų cheminių medžiagų gamyba | Manufacture of other chemical products |
| `20.6` | `C` | Cheminių pluoštų gamyba | Manufacture of man-made fibres |
| `21.1` | `C` | Pagrindinių vaistų pramonės gaminių gamyba | Manufacture of basic pharmaceutical products |
| `21.2` | `C` | Farmacinių preparatų gamyba | Manufacture of pharmaceutical preparations |
| `22.1` | `C` | Guminių gaminių gamyba | Manufacture of rubber products |
| `22.2` | `C` | Plastikinių gaminių gamyba | Manufacture of plastics products |
| `23.1` | `C` | Stiklo ir stiklo gaminių bei dirbinių gamyba | Manufacture of glass and glass products |
| `23.2` | `C` | Ugniai atsparių gaminių gamyba | Manufacture of refractory products |
| `23.3` | `C` | Statybinių medžiagų iš molio gamyba | Manufacture of clay building materials |
| `23.4` | `C` | Kitų porcelianinių ir keraminių gaminių bei dirbinių gamyba | Manufacture of other porcelain and ceramic products |
| `23.5` | `C` | Cemento, kalkių ir gipso gamyba | Manufacture of cement, lime and plaster |
| `23.6` | `C` | Betono, cemento ir gipso gaminių bei dirbinių gamyba | Manufacture of articles of concrete, cement and plaster |
| `23.7` | `C` | Akmens pjaustymas, tašymas ir apdailinimas | Cutting, shaping and finishing of stone |
| `23.9` | `C` | Abrazyvinių gaminių ir niekur kitur nepriskirtų nemetalo mineralinių produktų gamyba | Manufacture of abrasive products and non-metallic mineral products n.e.c. |
| `24.1` | `C` | Tomo ketaus ir plieno bei ferolydinių gamyba | Manufacture of basic iron and steel and of ferro-alloys |
| `24.2` | `C` | Plieninių vamzdžių, vamzdelių, tuščiavidurių profilių ir susijusių jungiamųjų detalių gamyba | Manufacture of tubes, pipes, hollow profiles and related fittings, of steel |
| `24.3` | `C` | Kitų plieno pirminio apdirbimo gaminių gamyba | Manufacture of other products of first processing of steel |
| `24.4` | `C` | Pagrindinių tauriųjų ir kitų spalvotųjų metalų gamyba | Manufacture of basic precious and other non-ferrous metals |
| `24.5` | `C` | Metalų liejinių gamyba | Casting of metals |
| `25.1` | `C` | Konstrukcinių metalo gaminių gamyba | Manufacture of structural metal products |
| `25.2` | `C` | Metalinių cisternų, rezervuarų ir talpyklų gamyba | Manufacture of tanks, reservoirs and containers of metal |
| `25.3` | `C` | Garo generatorių, išskyrus centrinio šildymo karšto vandens katilus, gamyba | Manufacture of steam generators, except central heating hot water boilers |
| `25.4` | `C` | Ginklų ir šaudmenų gamyba | Manufacture of weapons and ammunition |
| `25.5` | `C` | Metalo kalimas, presavimas, štampavimas ir profiliavimas; miltelių metalurgija | Forging, pressing, stamping and roll-forming of metal; powder metallurgy |
| `25.6` | `C` | Metalų apdorojimas ir dengimas; mechaninis apdirbimas | Treatment and coating of metals; machining |
| `25.7` | `C` | Valgomųjų įrankių, kitų įrankių ir bendrųjų metalo dirbinių gamyba | Manufacture of cutlery, tools and general hardware |
| `25.9` | `C` | Kitų metalo gaminių gamyba | Manufacture of other fabricated metal products |
| `26.1` | `C` | Elektroninių komponentų ir plokščių gamyba | Manufacture of electronic components and boards |
| `26.2` | `C` | Kompiuterių ir išorinės įrangos gamyba | Manufacture of computers and peripheral equipment |
| `26.3` | `C` | Ryšių įrangos gamyba | Manufacture of communication equipment |
| `26.4` | `C` | Vartotojiškos elektroninės įrangos gamyba | Manufacture of consumer electronics |
| `26.5` | `C` | Matavimo, bandymo, navigacinės ir kontrolės įrangos gamyba; įvairių tipų laikrodžių gamyba | Manufacture of instruments and appliances for measuring, testing and navigation; watches and clocks |
| `26.6` | `C` | Švitinimo, elektromedicininės ir elektroterapinės įrangos gamyba | Manufacture of irradiation, electromedical and electrotherapeutic equipment |
| `26.7` | `C` | Optinių prietaisų ir fotografijos įrangos gamyba | Manufacture of optical instruments and photographic equipment |
| `26.8` | `C` | Magnetinių ir optinių laikmenų gamyba | Manufacture of magnetic and optical media |
| `27.1` | `C` | Elektros variklių, generatorių, transformatorių bei elektros skirstomosios ir valdymo įrangos gamyba | Manufacture of electric motors, generators, transformers and electricity distribution and control apparatus |
| `27.2` | `C` | Baterijų ir akumuliatorių gamyba | Manufacture of batteries and accumulators |
| `27.3` | `C` | Laidų ir instaliacijos įtaisų gamyba | Manufacture of wiring and wiring devices |
| `27.4` | `C` | Elektros apšvietimo įrangos gamyba | Manufacture of electric lighting equipment |
| `27.5` | `C` | Buitinių aparatų ir prietaisų gamyba | Manufacture of domestic appliances |
| `27.9` | `C` | Kitos elektros įrangos gamyba | Manufacture of other electrical equipment |
| `28.1` | `C` | Bendrosios paskirties mašinų gamyba | Manufacture of general — purpose machinery |
| `28.2` | `C` | Kitų bendrosios paskirties mašinų ir įrangos gamyba | Manufacture of other general-purpose machinery |
| `28.3` | `C` | Žemės ir miškų ūkio mašinų gamyba | Manufacture of agricultural and forestry machinery |
| `28.4` | `C` | Metalo formavimo įrangos ir staklių gamyba | Manufacture of metal forming machinery and machine tools |
| `28.9` | `C` | Kitų specialiosios paskirties mašinų gamyba | Manufacture of other special-purpose machinery |
| `29.1` | `C` | Variklinių transporto priemonių gamyba | Manufacture of motor vehicles |
| `29.2` | `C` | Variklinių transporto priemonių kėbulų gamyba; priekabų ir puspriekabių gamyba | Manufacture of bodies (coachwork) for motor vehicles; manufacture of trailers and semi-trailers |
| `29.3` | `C` | Variklinių transporto priemonių ir jų dalių bei pagalbinių reikmenų gamyba | Manufacture of parts and accessories for motor vehicles |
| `30.1` | `C` | Įvairių tipų laivų statyba | Building of ships and boats |
| `30.2` | `C` | Geležinkelio lokomotyvų bei riedmenų gamyba | Manufacture of railway locomotives and rolling stock |
| `30.3` | `C` | Orlaivių ir erdvėlaivių bei susijusios įrangos gamyba | Manufacture of air and spacecraft and related machinery |
| `30.4` | `C` | Karinių kovinių transporto priemonių gamyba | Manufacture of military fighting vehicles |
| `30.9` | `C` | Niekur kitur nepriskirtų transporto priemonių gamyba | Manufacture of transport equipment n.e.c. |
| `31.0` | `C` | Baldų gamyba | Manufacture of furniture |
| `32.1` | `C` | Papuošalų, juvelyrinių, bižuterijos ir panašių dirbinių gamyba | Manufacture of jewellery, bijouterie and related articles |
| `32.2` | `C` | Muzikos instrumentų gamyba | Manufacture of musical instruments |
| `32.3` | `C` | Sporto reikmenų gamyba | Manufacture of sports goods |
| `32.4` | `C` | Žaidimų ir žaislų gamyba | Manufacture of games and toys |
| `32.5` | `C` | Medicinos ir odontologijos prietaisų, instrumentų ir reikmenų gamyba | Manufacture of medical and dental instruments and supplies |
| `32.9` | `C` | Niekur kitur nepriskirta gamyba | Manufacturing n.e.c. |
| `33.1` | `C` | Metalo gaminių, mašinų ir įrangos remontas | Repair of fabricated metal products, machinery and equipment |
| `33.2` | `C` | Pramoninių mašinų ir įrangos įrengimas | Installation of industrial machinery and equipment |
| `35.1` | `D` | Elektros energijos gamyba, perdavimas ir paskirstymas | Electric power generation, transmission and distribution |
| `35.2` | `D` | Dujų gamyba; dujinio kuro paskirstymas dujotiekiais | Manufacture of gas; distribution of gaseous fuels through mains |
| `35.3` | `D` | Garo tiekimas ir oro kondicionavimas | Steam and air conditioning supply |
| `36.0` | `E` | Vandens rinkimas, valymas ir tiekimas | Water collection, treatment and supply |
| `37.0` | `E` | Nuotekų valymas | Sewerage |
| `38.1` | `E` | Atliekų rinkimas | Waste collection |
| `38.2` | `E` | Atliekų tvarkymas ir šalinimas | Waste treatment and disposal |
| `38.3` | `E` | Medžiagų atgavimas | Materials recovery |
| `39.0` | `E` | Regeneravimas ir kita atliekų tvarkyba | Remediation activities and other waste management services |
| `41.1` | `F` | Statybų plėtra | Development of building projects |
| `41.2` | `F` | Gyvenamųjų ir negyvenamųjų pastatų statyba | Construction of residential and non-residential buildings |
| `42.1` | `F` | Kelių ir geležinkelių tiesimas | Construction of roads and railways |
| `42.2` | `F` | Komunalinių statinių statyba | Construction of utility projects |
| `42.9` | `F` | Kitų inžinerinių statinių statyba | Construction of other civil engineering projects |
| `43.1` | `F` | Statinių nugriovimas ir statybvietės paruošimas | Demolition and site preparation |
| `43.2` | `F` | Elektros, vandentiekio ir kitos įrangos įrengimas | Electrical, plumbing and other construction installation activities |
| `43.3` | `F` | Statybos baigimas ir apdaila | Building completion and finishing |
| `43.9` | `F` | Kita specializuota statybos veikla | Other specialised construction activities |
| `45.1` | `G` | Variklinių transporto priemonių pardavimas | Sale of motor vehicles |
| `45.2` | `G` | Variklinių transporto priemonių techninė priežiūra ir remontas | Maintenance and repair of motor vehicles |
| `45.3` | `G` | Variklinių transporto priemonių atsarginių dalių ir pagalbinių reikmenų pardavimas | Sale of motor vehicle parts and accessories |
| `45.4` | `G` | Motociklų ir jų atsarginių dalių bei pagalbinių reikmenų pardavimas, techninė priežiūra ir remontas | Sale, maintenance and repair of motorcycles and related parts and accessories |
| `46.1` | `G` | Didmeninė prekyba už atlygį ar pagal sutartį | Wholesale on a fee or contract basis |
| `46.2` | `G` | Žemės ūkio žaliavų ir gyvų gyvulių didmeninė prekyba | Wholesale of agricultural raw materials and live animals |
| `46.3` | `G` | Maisto produktų, gėrimų, tabako ir jo gaminių didmeninė prekyba | Wholesale of food, beverages and tobacco |
| `46.4` | `G` | Namų ūkio reikmenų didmeninė prekyba | Wholesale of household goods |
| `46.5` | `G` | Informacijos ir ryšių technologijų (IRT) įrangos didmeninė prekyba | Wholesale of information and communication equipment |
| `46.6` | `G` | Kitų mašinų, įrangos ir reikmenų didmeninė prekyba | Wholesale of other machinery, equipment and supplies |
| `46.7` | `G` | Kita specializuota didmeninė prekyba | Other specialised wholesale |
| `46.9` | `G` | Nespecializuota didmeninė prekyba | Non-specialised wholesale trade |
| `47.1` | `G` | Mažmeninė prekyba nespecializuotose parduotuvėse | Retail sale in non-specialised stores |
| `47.2` | `G` | Maisto, gėrimų ir tabako mažmeninė prekyba specializuotose parduotuvėse | Retail sale of food, beverages and tobacco in specialised stores |
| `47.3` | `G` | Automobilių degalų mažmeninė prekyba specializuotose parduotuvėse | Retail sale of automotive fuel in specialised stores |
| `47.4` | `G` | Informacijos ir ryšių technologijų (IRT) įrangos mažmeninė prekyba specializuotose parduotuvėse | Retail sale of information and communication equipment in specialised stores |
| `47.5` | `G` | Kitos namų ūkio įrangos mažmeninė prekyba specializuotose parduotuvėse | Retail sale of other household equipment in specialised stores |
| `47.6` | `G` | Kultūros ir poilsio prekių mažmeninė prekyba specializuotose parduotuvėse | Retail sale of cultural and recreation goods in specialised stores |
| `47.7` | `G` | Kitų prekių mažmeninė prekyba specializuotose parduotuvėse | Retail sale of other goods in specialised stores |
| `47.8` | `G` | Mažmeninė prekyba kioskuose ir prekyvietėse | Retail sale via stalls and markets |
| `47.9` | `G` | Mažmeninė prekyba ne parduotuvėse, kioskuose ar prekyvietėse | Retail trade not in stores, stalls or markets |
| `49.1` | `H` | Tarpmiestinis keleivinis geležinkelio transportas | Passenger rail transport, interurban |
| `49.2` | `H` | Krovininis geležinkelio transportas | Freight rail transport |
| `49.3` | `H` | Kitas keleivinis sausumos transportas | Other passenger land transport |
| `49.4` | `H` | Krovininis kelių transportas ir perkraustymo veikla | Freight transport by road and removal services |
| `49.5` | `H` | Transportavimas vamzdynais | Transport via pipeline |
| `50.1` | `H` | Jūrų ir pakrančių keleivinis vandens transportas | Sea and coastal passenger water transport |
| `50.2` | `H` | Jūrų ir pakrančių krovininis vandens transportas | Sea and coastal freight water transport |
| `50.3` | `H` | Vidaus vandenų keleivinis transportas | Inland passenger water transport |
| `50.4` | `H` | Vidaus vandenų krovininis transportas | Inland freight water transport |
| `51.1` | `H` | Keleivinis oro transportas | Passenger air transport |
| `51.2` | `H` | Krovininis oro transportas ir kosminis transportas | Freight air transport and space transport |
| `52.1` | `H` | Sandėliavimas ir saugojimas | Warehousing and storage |
| `52.2` | `H` | Transportui būdingų paslaugų veikla | Support activities for transportation |
| `53.1` | `H` | Pašto pagal įpareigojimą teikti universaliąsias paslaugas atliekama veikla | Postal activities under universal service obligation |
| `53.2` | `H` | Kita pašto ir pasiuntinių (kurjerių) veikla | Other postal and courier activities |
| `55.1` | `I` | Viešbučių ir panašių laikinų buveinių veikla | Hotels and similar accommodation |
| `55.2` | `I` | Poilsiautojų ir kita trumpalaikio apgyvendinimo veikla | Holiday and other short-stay accommodation |
| `55.3` | `I` | Poilsinių transporto priemonių, priekabų aikštelių ir stovyklaviečių veikla | Camping grounds, recreational vehicle parks and trailer parks |
| `55.9` | `I` | Kita apgyvendinimo veikla | Other accommodation |
| `56.1` | `I` | Restoranų ir pagaminto valgio teikimo veikla | Restaurants and mobile food service activities |
| `56.2` | `I` | Pagaminto valgio tiekimas renginiams ir kitų maitinimo paslaugų veikla | Event catering and other food service activities |
| `56.3` | `I` | Gėrimų pardavimo vartoti vietoje veikla | Beverage serving activities |
| `58.1` | `J` | Knygų, periodinių leidinių leidyba ir kita leidybinė veikla | Publishing of books, periodicals and other publishing activities |
| `58.2` | `J` | Programinės įrangos leidyba | Software publishing |
| `59.1` | `J` | Kino filmų, vaizdo filmų ir televizijos programų rengėjų veikla | Motion picture, video and television programme activities |
| `59.2` | `J` | Garso įrašymas ir muzikos įrašų leidyba | Sound recording and music publishing activities |
| `60.1` | `J` | Radijo programų transliavimas | Radio broadcasting |
| `60.2` | `J` | Televizijos programų rengimas ir transliavimas | Television programming and broadcasting activities |
| `61.1` | `J` | Laidinio ryšio paslaugų veikla | Wired telecommunications activities |
| `61.2` | `J` | Bevielio ryšio pasaugų veikla | Wireless telecommunications activities |
| `61.3` | `J` | Palydovinio ryšio paslaugų veikla | Satellite telecommunications activities |
| `61.9` | `J` | Kitų ryšių paslaugų veikla | Other telecommunications activities |
| `62.0` | `J` | Kompiuterių programavimo, konsultacinė ir susijusi veikla | Computer programming, consultancy and related activities |
| `63.1` | `J` | Duomenų apdorojimo, interneto serverių paslaugų (prieglobos) ir susijusi veikla; interneto vartų paslaugų veikla | Data processing, hosting and related activities; web portals |
| `63.9` | `J` | Kita informacinių paslaugų veikla | Other information service activities |
| `64.1` | `K` | Piniginis tarpininkavimas | Monetary intermediation |
| `64.2` | `K` | Kontroliuojančiųjų bendrovių veikla | Activities of holding companies |
| `64.3` | `K` | Trestų, fondų ir panašių finansinių institucijų veikla | Trusts, funds and similar financial entities |
| `64.9` | `K` | Kita finansinių paslaugų veikla, išskyrus draudimą ir pensijų lėšų kaupimą | Other financial service activities, except insurance and pension funding |
| `65.1` | `K` | Draudimas | Insurance |
| `65.2` | `K` | Perdraudimas | Reinsurance |
| `65.3` | `K` | Pensijų lėšų kaupimas | Pension funding |
| `66.1` | `K` | Pagalbinė finansinių paslaugų, išskyrus draudimą ir pensijų lėšų kaupimą, veikla | Activities auxiliary to financial services, except insurance and pension funding |
| `66.2` | `K` | Pagalbinė draudimo ir pensijų lėšų kaupimo veikla | Activities auxiliary to insurance and pension funding |
| `66.3` | `K` | Fondų valdymo veikla | Fund management activities |
| `68.1` | `L` | Nuosavo nekilnojamojo turto pirkimas ir pardavimas | Buying and selling of own real estate |
| `68.2` | `L` | Nuosavo arba nuomojamo nekilnojamojo turto nuoma ir eksploatavimas | Renting and operating of own or leased real estate |
| `68.3` | `L` | Nekilnojamojo turto operacijos už atlygį arba pagal sutartį | Real estate activities on a fee or contract basis |
| `69.1` | `M` | Teisinė veikla | Legal activities |
| `69.2` | `M` | Apskaitos, buhalterijos ir audito veikla; konsultacijos mokesčių klausimais | Accounting, bookkeeping and auditing activities; tax consultancy |
| `70.1` | `M` | Pagrindinių buveinių veikla | Activities of head offices |
| `70.2` | `M` | Konsultacinė valdymo veikla | Management consultancy activities |
| `71.1` | `M` | Architektūros ir inžinerijos veikla bei su ja susijusios techninės konsultacijos | Architectural and engineering activities and related technical consultancy |
| `71.2` | `M` | Techninis tikrinimas ir analizė | Technical testing and analysis |
| `72.1` | `M` | Gamtos mokslų ir inžinerijos moksliniai tyrimai ir taikomoji veikla | Research and experimental development on natural sciences and engineering |
| `72.2` | `M` | Socialinių ir humanitarinių mokslų moksliniai tyrimai ir taikomoji veikla | Research and experimental development on social sciences and humanities |
| `73.1` | `M` | Reklama | Advertising |
| `73.2` | `M` | Rinkos tyrimas ir viešosios nuomonės apklausa | Market research and public opinion polling |
| `74.1` | `M` | Specializuota projektavimo veikla | Specialised design activities |
| `74.2` | `M` | Fotografavimo veikla | Photographic activities |
| `74.3` | `M` | Vertimo raštu ir žodžiu veikla | Translation and interpretation activities |
| `74.9` | `M` | Kita, niekur kitur nepriskirta, profesinė, mokslinė ir techninė veikla | Other professional, scientific and technical activities n.e.c. |
| `75.0` | `M` | Veterinarinė veikla | Veterinary activities |
| `77.1` | `N` | Variklinių transporto priemonių nuoma ir išperkamoji nuoma | Renting and leasing of motor vehicles |
| `77.2` | `N` | Asmeninių ir namų ūkio prekių nuoma ir išperkamoji nuoma | Renting and leasing of personal and household goods |
| `77.3` | `N` | Kitų mašinų, įrangos ir materialiųjų vertybių nuoma ir išperkamoji nuoma | Renting and leasing of other machinery, equipment and tangible goods |
| `77.4` | `N` | Intelektinės nuosavybės ir panašių produktų, išskyrus autorių teisių ginamus kūrinius, išperkamoji nuoma | Leasing of intellectual property and similar products, except copyrighted works |
| `78.1` | `N` | Įdarbinimo agentūrų veikla | Activities of employment placement agencies |
| `78.2` | `N` | Laikinojo įdarbinimo agentūrų veikla | Temporary employment agency activities |
| `78.3` | `N` | Kitas darbo jėgos teikimas | Other human resources provision |
| `79.1` | `N` | Kelionių agentūrų ir ekskursijų organizatorių veikla | Travel agency and tour operator activities |
| `79.9` | `N` | Kitų išankstinio užsakymo ir susijusių paslaugų veikla | Other reservation service and related activities |
| `80.1` | `N` | Privati apsauga | Private security activities |
| `80.2` | `N` | Apsaugos sistemų paslaugų veikla | Security systems service activities |
| `80.3` | `N` | Tyrimo veikla | Investigation activities |
| `81.1` | `N` | Kombinuota patalpų funkcionavimo užtikrinimo veikla | Combined facilities support activities |
| `81.2` | `N` | Valymo veikla | Cleaning activities |
| `81.3` | `N` | Kraštovaizdžio tvarkymas | Landscape service activities |
| `82.1` | `N` | Įstaigų administracinė ir aptarnavimo veikla | Office administrative and support activities |
| `82.2` | `N` | Užsakomųjų informacinių paslaugų centrų veikla | Activities of call centres |
| `82.3` | `N` | Posėdžių ir verslo renginių organizavimas | Organisation of conventions and trade shows |
| `82.9` | `N` | Niekur kitur nepriskirta verslui būdingų paslaugų veikla | Business support service activities n.e.c. |
| `84.1` | `O` | Valstybės valdymas ir bendroji ekonominė bei socialinė bendruomenės politika | Administration of the State and the economic and social policy of the community |
| `84.2` | `O` | Bendruomenei teikiamų paslaugų užtikrinimas | Provision of services to the community as a whole |
| `84.3` | `O` | Privalomojo (valstybinio) socialinio draudimo veikla | Compulsory social security activities |
| `85.1` | `P` | Ikimokyklinis ugdymas | Pre-primary education |
| `85.2` | `P` | Pradinis ugdymas | Primary education |
| `85.3` | `P` | Vidurinis ugdymas | Secondary education |
| `85.4` | `P` | Aukštasis mokslas | Higher education |
| `85.5` | `P` | Kitas mokymas | Other education |
| `85.6` | `P` | Švietimui būdingų paslaugų veikla | Educational support activities |
| `86.1` | `Q` | Ligoninių veikla | Hospital activities |
| `86.2` | `Q` | Medicininės ir odontologinės praktikos veikla | Medical and dental practice activities |
| `86.9` | `Q` | Kita žmonių sveikatos priežiūros veikla | Other human health activities |
| `87.1` | `Q` | Stacionarinė slaugos įstaigų veikla | Residential nursing care activities |
| `87.2` | `Q` | Stacionarinė protiškai atsilikusių, psichikos ligonių, sergančiųjų priklausomybės ligomis globos veikla | Residential care activities for mental retardation, mental health and substance abuse |
| `87.3` | `Q` | Stacionarinė pagyvenusių ir neįgaliųjų asmenų globos veikla | Residential care activities for the elderly and disabled |
| `87.9` | `Q` | Kita stacionarinė globos veikla | Other residential care activities |
| `88.1` | `Q` | Nesusijusio su apgyvendinimu socialinio darbo su pagyvenusiais ir neįgaliaisiais asmenimis veikla | Social work activities without accommodation for the elderly and disabled |
| `88.9` | `Q` | Kita, nesusijusi su apgyvendinimu, socialinio darbo veikla | Other social work activities without accommodation |
| `90.0` | `R` | Kūrybinė, meninė ir pramogų organizavimo veikla | Creative, arts and entertainment activities |
| `91.0` | `R` | Bibliotekų, archyvų, muziejų ir kita kultūrinė veikla | Libraries, archives, museums and other cultural activities |
| `92.0` | `R` | Azartinių žaidimų ir lažybų organizavimo veikla | Gambling and betting activities |
| `93.1` | `R` | Sportinė veikla | Sports activities |
| `93.2` | `R` | Pramogų ir poilsio organizavimo veikla | Amusement and recreation activities |
| `94.1` | `S` | Verslininkų, darbdavių ir profesinių narystės organizacijų veikla | Activities of business, employers and professional membership organisations |
| `94.2` | `S` | Profesinių sąjungų veikla | Activities of trade unions |
| `94.9` | `S` | Kitų narystės organizacijų veikla | Activities of other membership organisations |
| `95.1` | `S` | Kompiuterių ir ryšių įrangos remontas | Repair of computers and communication equipment |
| `95.2` | `S` | Asmeninių ir namų ūkio reikmenų taisymas | Repair of personal and household goods |
| `96.0` | `S` | Kita asmenų aptarnavimo veikla | Other personal service activities |
| `97.0` | `T` | Namų ūkių, samdančių namų ūkio personalą, veikla | Activities of households as employers of domestic personnel |
| `98.1` | `T` | Privačių namų ūkių veikla, susijusi su savoms reikmėms tenkinti skirtų nediferencijuojamų gaminių ar reikmenų gamyba | Undifferentiated goods-producing activities of private households for own use |
| `98.2` | `T` | Privačių namų ūkių veikla, susijusi su savoms reikmėms tenkinti skirtų nediferencijuojamų paslaugų teikimu | Undifferentiated service-producing activities of private households for own use |
| `99.0` | `U` | Ekstrateritorinių organizacijų ir įstaigų veikla | Activities of extraterritorial organisations and bodies |

[^std-evrk]: Regulation (EC) No 1893/2006 establishing the statistical classification of economic activities NACE Revision 2 (EVRK 2) (https://publications.europa.eu/resource/celex/32006R1893)
[^std-evrk21]: Commission Delegated Regulation (EU) 2023/137 amending Regulation (EC) No 1893/2006 as regards NACE Rev. 2.1 (EVRK 2.1 effective 2025-01-01) (https://publications.europa.eu/resource/celex/32023R0137)
