---
type: Table
title: "Pazymejimas — Išduoti pažymėjimai energetikos darbuotojams"
description: "Energetikos darbuotojų atestavimo kontrolė yra viena iš Valstybinės energetikos reguliavimo tarybos (VERT) funkcijų."
resource: "https://get.data.gov.lt/datasets/gov/vert/isduoti/Pazymejimas"
tags: [gov, vert, pazymejimas, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vert/sertifikatai.csv#L9"
    title: "atviriduomenys/manifest — datasets/gov/vert/sertifikatai.csv#L9"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2891/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vert/isduoti"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pazymejimas — Išduoti pažymėjimai energetikos darbuotojams

Energetikos darbuotojų atestavimo kontrolė yra viena iš Valstybinės energetikos reguliavimo tarybos (VERT) funkcijų. Lietuvos Respublikos energetikos įstatymas numato, jog energetikos objektus, įrenginius įrengiantys ir eksploatuojantys darbuotojai privalo būti atitinkamos kvalifikacijos ir pasirengę įgyvendinti reikiamus uždavinius. Teisės aktų nustatyta tvarka atestuoti energetikos darbuotojai užtikrina saugų, efektyvų ir kokybišką energetikos įrenginių įrengimą ir/ar eksploatavimą. Tai leidžia užtikrinti darnų energetikos sektoriaus veikimą. Šiame rinkinyje pateikiami Energetikos darbuotojų atestavimo informacinės sistemos (EDAIS) duomenys nuo 2024m. iki dabar apie išduotus pažymėjimus energetikos darbuotojams Lietuvoje. Nurodoma informacija apie išduotą pažymėjimą (suteiktą įgaliojimą, veiklos sritį ir sektorių, galiojimo laikotarpį) ir sertifikavimo įstaigos vykdytą atestavimą (įstaigos pavadinimas, egzamino data ir vieta). Duomenų teikėjas - Valstybinė energetikos reguliavimo taryba. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt[^manifest]

- **Model:** `datasets/gov/vert/isduoti/Pazymejimas`[^manifest]
- **Dataset:** [Išduoti pažymėjimai energetikos darbuotojams](../isduoti.md) (`datasets/gov/vert/isduoti`)[^manifest]
- **Manifest CSV:** [datasets/gov/vert/sertifikatai.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vert/sertifikatai.csv#L9)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vert/isduoti/Pazymejimas` (`deployed`)[^manifest]
- **Provider:** `vert` — Valstybinė energetikos reguliavimo tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `pazymejimo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pazymejimo_id` | `string` | — | `4` | `open` | — | Išduoto pažymėjimo identifikatorius | — |
| `asmuo` | `string` | — | `4` | `open` | — | Energetikos darbuotojo, kuriam buvo išduotas pažymėjimas, identifikatorius | — |
| `igaliojimas` | `string` | — | `4` | `open` | — | Suteikto įgaliojimo pavadinimas | — |
| `sritis` | `string` | — | `4` | `open` | — | Veiklos sritis | — |
| `sektorius` | `string` | — | `4` | `open` | — | Veiklos sektoriaus pavadinimas | — |
| `galiojimo_pradzia` | `date` | `D` | `4` | `open` | — | Pažymėjimo galiojimo pradžios data | — |
| `galiojimo_pabaiga` | `date` | `D` | `4` | `open` | — | Pažymėjimo galiojimo pabaigos data | — |
| `egzamino_id` | `string` | — | `4` | `open` | — | Egzamino identifikacinis numeris | — |
| `egzamino_data` | `date` | `D` | `4` | `open` | — | Egzamino vykdymo data | — |
| `egzamino_miestas` | `string` | — | `4` | `open` | — | Miestas, kuriame buvo laikytas egzaminas | — |
| `atest_istaiga` | `string` | — | `4` | `open` | — | Atestavimą vykdžiusi įstaiga | — |
| `istaigos_jar` | `string` | — | `4` | `open` | — | Atestavimo įstaigos JAR kodas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `sektorius` | `"elektra"` | — | — | — | — |
| `sektorius` | `"dujos"` | — | — | — | — |
| `sektorius` | `"šiluma"` | — | — | — | — |
| `sektorius` | `"nafta"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vert/sertifikatai.csv#L9 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vert/sertifikatai.csv#L9)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vert/isduoti (https://data.gov.lt/datasets/2891/)
