---
type: Table
title: "FinStrategija — Valstybės strategijų elementų finansiniai duomenys"
description: "Lentelėje pateikti valstybės strategijų objektų elementų, kurie turi priskirtas pinigines vertes (pvz., lėšų projekcijas), finansiniai duomenys iš Lietuvos Respublikos finansų ministerijos Strateginio valdymo informacinės sistemos (SVIS)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/strategiju_finansiniai_duomenys/FinStrategija"
tags: [gov, finmin, finstrategija, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/strategiju_finansiniai_duomenys.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/finmin/strategiju_finansiniai_duomenys.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2846/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/strategiju_finansiniai_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# FinStrategija — Valstybės strategijų elementų finansiniai duomenys

Lentelėje pateikti valstybės strategijų objektų elementų, kurie turi priskirtas pinigines vertes (pvz., lėšų projekcijas), finansiniai duomenys iš Lietuvos Respublikos finansų ministerijos Strateginio valdymo informacinės sistemos (SVIS). Informacija pateikiama nuo duomenų rinkimo pradžios (2023 metų) atnaujinant kas ketvirtį. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/finmin/strategiju_finansiniai_duomenys/FinStrategija`[^manifest]
- **Dataset:** [Valstybės strategijų elementų finansiniai duomenys](../strategiju_finansiniai_duomenys.md) (`datasets/gov/finmin/strategiju_finansiniai_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/strategiju_finansiniai_duomenys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/strategiju_finansiniai_duomenys.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/strategiju_finansiniai_duomenys/FinStrategija` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `dok_kodas` | `string` | — | `4` | `open` | — | Dokumento kodas | — |
| `dok_pav` | `string` | — | `4` | `open` | — | Dokumento pavadinimas | — |
| `dok_versija` | `string` | — | `4` | `open` | — | Dokumento versijos numeris | — |
| `ar_paskutine_versija` | `boolean` | — | `4` | `open` | — | Požymis, nusakantis, ar dokumento versija yra paskutinė: "true" - paskutinė, "false" - priešingu atveju. | — |
| `dok_tipas` | `string` | — | `4` | `open` | — | Dokumento tipas | — |
| `dokumentas_galioja_nuo` | `date` | `D` | `4` | `open` | — | Dokumento galiojimo pradžios data (kai dirbama ne pagal darbo sekas). | — |
| `dokumentas_galioja_iki` | `date` | `D` | `4` | `open` | — | Dokumento planuojama parengimo data (kai dirbama ne pagal darbo sekas). | — |
| `strat_obj_kodas` | `string` | — | `4` | `open` | — | Strategijos objekto (elemento) identifikatorius | — |
| `strat_obj_pav_lt` | `string` | — | `4` | `open` | — | Strategijos objekto (elemento) vystomos versijos pavadinimas | — |
| `verte_eur` | `number` | — | `4` | `open` | — | Strategijos objekto (elemento) finansinio rodiklio reikšmė (EUR) | — |
| `pozymis` | `string` | — | `4` | `open` | — | Strategijos objekto (elemento) finansinio rodiklio reikšmės požymis (pvz.: Pažangos uždavinio finansinės projekcijos) | — |
| `finansavimo_saltinis` | `string` | — | `4` | `open` | — | Finansavimo šaltinio pavadinimas | — |
| `iraso_mod_data` | `datetime` | `S` | `4` | `open` | — | Duomenų įrašo modifikavimo data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `strat_obj_pav_lt` | `update(property: "strat_obj_pav@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `verte_eur` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/strategiju_finansiniai_duomenys.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/strategiju_finansiniai_duomenys.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/strategiju_finansiniai_duomenys (https://data.gov.lt/datasets/2846/)
