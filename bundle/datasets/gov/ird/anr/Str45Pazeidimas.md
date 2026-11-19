---
type: Table
title: "Str45Pazeidimas — ANK 45 str. pažeidimai ir pažeidėjai"
description: "Administracinių nusižengimų registro (ANR) bylos, kuriose minimas Administracinių nusižengimų kodekso (ANK) 45 straipsnis (\"Visuomenės sveikatos srities Europos Sąjungos reglamentų ar sprendimų, higienos norminių aktų ar kitų visuomenės sveikatos srities teisės aktų, Lietuvos..."
resource: "https://get.data.gov.lt/datasets/gov/ird/anr/Str45Pazeidimas"
tags: [gov, ird, str45pazeidimas, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/anr.csv#L40"
    title: "atviriduomenys/manifest — datasets/gov/ird/anr.csv#L40"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2558/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ird/anr"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Str45Pazeidimas — ANK 45 str. pažeidimai ir pažeidėjai

Administracinių nusižengimų registro (ANR) bylos, kuriose minimas Administracinių nusižengimų kodekso (ANK) 45 straipsnis ("Visuomenės sveikatos srities Europos Sąjungos reglamentų ar sprendimų, higienos norminių aktų ar kitų visuomenės sveikatos srities teisės aktų, Lietuvos Respublikos žmonių užkrečiamųjų ligų profilaktikos ir kontrolės įstatymo pažeidimas"). Pateikiama neagreguota lentelė (mikroduomenys). Viena eilutė yra vieno administracinio nusižengimo vieno straipsnio vienos dalies vienas pažeidėjas. Detalizuojama demografinė informacija apie pažeidėją bei pažeidimo vietos aplinkybes. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/ird/anr/Str45Pazeidimas`[^manifest]
- **Dataset:** [Administracinių nusižengimų registras](../anr.md) (`datasets/gov/ird/anr`)[^manifest]
- **Manifest CSV:** [datasets/gov/ird/anr.csv#L40](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/anr.csv#L40)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/anr/Str45Pazeidimas` (`deployed`)[^manifest]
- **Provider:** `ird` — Informatikos ir ryšių departamentas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus įrašo (eilutės) identifikatorius | Techninė paskirtis, analitikai nenaudingas |
| `anr_id` | `string` | — | `4` | `open` | — | Šifruotas unikalus individualaus pažeidimo identifikatorius (iš ANR) | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Šifruotas asmens kodas | — |
| `anr_uzregistruota` | `date` | `D` | `4` | `open` | — | Administracinio nusižengimo registravimo registre data | — |
| `amzius` | `integer` | — | `4` | `open` | — | Pažeidėjo amžius nusižengimo registravimo registre datą | — |
| `lytis` | `string` | — | `4` | `open` | — | Pažeidėjo lytis (gali būti nežinoma) | — |
| `ank_straipsnis` | `string` | — | `4` | `open` | — | Administracinių nusižengimų kodekso straipsnis | — |
| `ank_straipsnio_dalis` | `string` | — | `4` | `open` | — | Administracinių nusižengimų kodekso straipsnio dalis | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Nusižengimo padarymo vietos savivaldybės pavadinimas | — |
| `vietos_objektas_lygis_1_lt` | `string` | — | `4` | `open` | — | Nusižengimo padarymo vietos objektas (aukštesnis lygis) | — |
| `vietos_objektas_lygis_2_lt` | `string` | — | `4` | `open` | — | Nusižengimo padarymo vietos objektas (žemesnis lygis) | — |
| `koordinate` | `geometry(point,3346)` | `m` | `4` | `open` | — | Nusižengimo padarymo vietos koordinatė (LKS sistemoje), pritaikius triukšminimo metodą | Triukšminimo metodas taikomas dėl konfidencialumo ir asmens duomenų apsaugos: įvykio koordinatės yra paslenkamos atsitiktine kryptimi taikant normalųjį triukšmo skirstinį su standartiniu nuokrypiu nuo 100 iki 1000 metrų, priklausomai nuo gyventojų tankio: mažesnis gyventojų tankis – didesnis nuokrypis. |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ank_straipsnio_dalis` | `"1 d."` | — | — | 45 str. 1 dalis | — |
| `ank_straipsnio_dalis` | `"2 d."` | — | — | 45 str. 2 dalis | — |
| `ank_straipsnio_dalis` | `"3 d."` | — | — | 45 str. 3 dalis | — |
| `ank_straipsnio_dalis` | `"4 d."` | — | — | 45 str. 4 dalis | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vietos_objektas_lygis_1_lt` | `update(property: "vietos_objektas_lygis_1_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `vietos_objektas_lygis_2_lt` | `update(property: "vietos_objektas_lygis_2_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/anr.csv#L40 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/anr.csv#L40)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ird/anr (https://data.gov.lt/datasets/2558/)
