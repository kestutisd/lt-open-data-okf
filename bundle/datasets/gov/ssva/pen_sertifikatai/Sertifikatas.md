---
type: Table
title: "Sertifikatas — Pastatų energinio naudingumo sertifikatai"
description: "Pastatų energinio naudingumo sertifikatai"
resource: "https://get.data.gov.lt/datasets/gov/ssva/pen_sertifikatai/Sertifikatas"
tags: [gov, ssva, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ssva/pens_ekspertu_atestatai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pens_ekspertu_atestatai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sertifikatas — Pastatų energinio naudingumo sertifikatai

Pastatų energinio naudingumo sertifikatai

- **Model:** `datasets/gov/ssva/pen_sertifikatai/Sertifikatas`[^manifest]
- **Dataset:** [Duomenys apie pastatų energinio naudingumo sertifikatus](../pen_sertifikatai.md) (`datasets/gov/ssva/pen_sertifikatai`)
- **Manifest CSV:** [datasets/gov/ssva/pens_ekspertu_atestatai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pens_ekspertu_atestatai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/pen_sertifikatai/Sertifikatas`
- **Primary Key (`ref`):** `id`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `paskirtis` | `ref` | [Paskirtis](Paskirtis.md) | `4` | `open` | — | Pastatų paskirtis | — |
| `nr` | `string` | — | `4` | `open` | — | Sertifikato numeris | — |
| `versija` | `integer` | — | `3` | `open` | — | Sertifikato pateikimo versija | — |
| `pozymis` | `integer` | — | `4` | `open` | — | Tipinio buto sertifikato požymis | — |
| `adresas` | `string` | — | `2` | `open` | — | Adresas | — |
| `klase` | `string` | — | `4` | `open` | — | Pastato energinio naudingumo klasė | — |
| `plotas` | `number` | `m^2` | `4` | `open` | — | Pastato (jo dalies) šildomas plotas | — |
| `sanaudos` | `number` | — | `3` | `open` | — | Energijos sąnaudos | Skaičiuojamosios suminės energijos sąnaudos - pagal pirmosios 2005-12-20 AM įsakymu Nr. D1-624 patvirtintos STR 2.01.09:2005 redakcijos 21.5 punktą (naujesnėse STR'o versijose nebeskaičiuojamas). |
| `sildymas` | `number` | — | `3` | `open` | — | Energijos sąnaudos pastato šildymui | Energijos sąnaudos pastato šildymui - įvestos nuo 2012-02-01, įsigaliojus 2011-06-07 AM įsakymu Nr.D1-462 patvirtintiems STR 2.01.09:2005 pakeitimams, kurie panaikino aukščiau minėtų energijos sąnaudų skaičiavimą. |
| `saltiniai` | `string` | — | `3` | `open` | — | Šilumos šaltiniai | — |
| `isdavimas` | `date` | `D` | `4` | `open` | — | Sertifikato išdavimo data | — |
| `galiojimas` | `date` | `D` | `4` | `open` | — | Sertifikato galiojimo data | — |
| `atestatas` | `integer` | — | `4` | `open` | — | Eksperto atestato Nr. | — |
| `gavejas` | `string` | — | `4` | `public` | — | Eksperto vardas | — |
| `co2` | `number` | — | `3` | `open` | — | CO2 kiekis | — |
| `finansavimas` | `integer` | — | `4` | `open` | — | Finansavimo požymis | Pastato projektavimas ir (ar) statyba ir (ar) modernizavimas finansuojama Lietuvos Respublikos ir (ar) Europos Sąjungos biudžeto lėšomis: taip / taip dalinai / ne (informacija į registrą įtraukiama nuo 2022-08-01) |
| `pastaba` | `string` | — | `3` | `open` | — | Registro pastaba | — |
| `koord` | `geometry(point,3346)` | — | `3` | `open` | — | Pastato koordinatės | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pozymis` | `0` | — | — | Pastato (pastato dalies) sertifikatas | — |
| `pozymis` | `1` | — | — | Tipinis buto sertifikatas | — |
| `klase` | `"A++"` | — | — | A++ energinė klasė | A++ energinė klasė (C1 < 0,25 ir C2 £ 0,70). Toks pastatas priskiriamas pasyviam, nes beveik nenaudoja šiluminės energijos. Jei pastatui buvo suteikta A++ energinė klasė, vadinasi, pastatas išsiskiria labai mažu konstrukcijų šilumos laidumo koeficientu, jo atskiros konstrukcijos yra itin sandariai sujungtos, šalčio tilteliai visiškai sumažinti, o pasirinktas apšiltinimo būdas yra labai efektyvus. Taip pat toks statinys reikalingą energijos kiekį gauna iš atsinaujinančių energijos šaltinių: vėjo, saulės, aeroterminių / hidroterminių / geoterminių resursų ar biodujų, turi mechaninę vėdinimo sistemą – ši savybė itin vertinama ir mėgstama šiuolaikinių pirkėjų. |
| `klase` | `"A+"` | — | — | A+ energinė klasė | A+ (0,25 £ C1 < 0,375 ir C2 £ 0,80) energinės klasės. Tokiepastatai pasižymi puikiomis konstrukcijų šiluminėmis savybėmis, geru sandarumu, turi įmontuotus kokybiškus ir šilumai nepralaidžius langus, kruopščiai užsandarintus šalčio tiltelius, įdiegtą patikimą mechaninę vėdinimo sistemą. Tokios energinės klasės užtikrina pastato efektyumą ir ekonomiškumą. |
| `klase` | `"A"` | — | — | A energinė klasė | A (0,375 £ C1 < 0,5 ir C2 £ 0,85) energinės klasės. Tokiepastatai pasižymi puikiomis konstrukcijų šiluminėmis savybėmis, geru sandarumu, turi įmontuotus kokybiškus ir šilumai nepralaidžius langus, kruopščiai užsandarintus šalčio tiltelius, įdiegtą patikimą mechaninę vėdinimo sistemą. Tokios energinės klasės užtikrina pastato efektyumą ir ekonomiškumą. |
| `klase` | `"B"` | — | — | B energinė klasė | B (0,5 £ C1 < 1 ir C2 £ 0,99) energinės klasės. Tai nėra pirkėjams labai patrauklūs pastatai, nes jiems netaikomi griežti reikalavimai, nėra numatytų sąlygų vėdinimo sistemai, elektros energijos suvartojimui, pastato sandarumui. Jeigu pastato energinė klasė yra B arba C, tai tokį pastatą reiktų geriau apšiltinti, įmontuoti sandaresnius langus ir įvykdyti kitas specialistų pateiktas rekomendacijas, kad pastato efektyvumas padidėtų. |
| `klase` | `"C"` | — | — | C energinė klasė | C (1 £ C1< 1,5) energinės klasės. Tai nėra pirkėjams labai patrauklūs pastatai, nes jiems netaikomi griežti reikalavimai, nėra numatytų sąlygų vėdinimo sistemai, elektros energijos suvartojimui, pastato sandarumui. Jeigu pastato energinė klasė yra B arba C, tai tokį pastatą reiktų geriau apšiltinti, įmontuoti sandaresnius langus ir įvykdyti kitas specialistų pateiktas rekomendacijas, kad pastato efektyvumas padidėtų. |
| `klase` | `"D"` | — | — | D energinė klasė | D (1,5 £ C1< 2) energinės klasės. Tokie pastatai sunaudoja labai daug energijos, tačiau vienas didžiausių tokių statinių trūkumų – šiluma gali pasišalinti per išorines atitvaras (duris ir langus), sienas, stogus ar grindis. Tad toks pastatas nėra patrauklus ne tik finansiškai, bet ir komforto atžvilgiu. |
| `klase` | `"E"` | — | — | E energinė klasė | E (2 £ C1< 2,5) energinės klasės. Tokie pastatai sunaudoja labai daug energijos, tačiau vienas didžiausių tokių statinių trūkumų – šiluma gali pasišalinti per išorines atitvaras (duris ir langus), sienas, stogus ar grindis. Tad toks pastatas nėra patrauklus ne tik finansiškai, bet ir komforto atžvilgiu. |
| `klase` | `"F"` | — | — | F energinė klasė | F (2,5 £ C1< 3) energinės klasės. Tokie pastatai yra energiškai neefektyvūs, sunaudoja labai didelį energijos kiekį ir yra labai neekonomiški. |
| `klase` | `"G"` | — | — | G energinė klasė | G (C1 ³ 3) energinės klasės. Tokie pastatai yra energiškai neefektyvūs, sunaudoja labai didelį energijos kiekį ir yra labai neekonomiški. |
| `finansavimas` | `0` | — | — | Ne | — |
| `finansavimas` | `1` | — | — | Dalinai | — |
| `finansavimas` | `2` | — | — | Taip | — |
| `finansavimas` | `-1` | — | — | Neaišku | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/pens_ekspertu_atestatai.csv
