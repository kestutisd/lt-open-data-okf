---
type: Table
title: "Zeldinys — Anykščių miesto želdiniai"
description: "Informacija apie Anykščių miesto želdinius"
resource: "https://get.data.gov.lt/datasets/gov/anyksciu_r_sav/zeldiniai/Zeldinys"
tags: [gov, anyksciu_r_sav, zeldinys, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anyksciu_r_sav/zeldiniai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/anyksciu_r_sav/zeldiniai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2900/"
    title: "data.gov.lt DCAT-AP — datasets/gov/anyksciu_r_sav/zeldiniai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Zeldinys — Anykščių miesto želdiniai

Informacija apie Anykščių miesto želdinius[^manifest]

- **Model:** `datasets/gov/anyksciu_r_sav/zeldiniai/Zeldinys`[^manifest]
- **Dataset:** [Anykščių miesto želdiniai ir želdynai](../zeldiniai.md) (`datasets/gov/anyksciu_r_sav/zeldiniai`)[^manifest]
- **Manifest CSV:** [datasets/gov/anyksciu_r_sav/zeldiniai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anyksciu_r_sav/zeldiniai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/anyksciu_r_sav/zeldiniai/Zeldinys` (`deployed`)[^manifest]
- **Provider:** `anyksciu_r_sav` — Anykščių rajono savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `objekto_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `objekto_id` | `string` | — | `4` | `open` | — | Želdinio identifikatorius | — |
| `zona` | `string` | — | `4` | `open` | — | Zona nurodanti ar želdinys yra gatvės ar miesto teritorijoje | — |
| `kvartalas_gatve` | `string` | — | `4` | `open` | — | Kvartalo numeris arba gatvės pavadinimas kurioje auga želdinys | — |
| `sklypo_numeris` | `string` | — | `4` | `open` | — | Sklypo numeris, kuriame auga želdinys | — |
| `kvartalas_gatve_sklypas` | `string` | — | `4` | `open` | — | Kvartalo ir sklypo numeriai arba gatvės pavadinimas ir sklypo numeris | — |
| `rusis_bendra` | `string` | — | `4` | `open` | — | Želdinio bendroji rūšis (gentis) | — |
| `rusis` | `string` | — | `4` | `open` | — | Želdinio rūšis | — |
| `zeldinio_aukstis` | `integer` | — | `4` | `open` | — | Želdinio aukštis metrais | — |
| `zeldinio_skersmuo` | `integer` | — | `4` | `open` | — | Želdinio skersmuo centimetrais | — |
| `urbanistikos_kontroles_priemones` | `string` | — | `4` | `open` | — | Taikomos urbanistikos kontrolės priemonės | — |
| `pastabos` | `string` | — | `4` | `open` | — | Pastabos apie želdinį | — |
| `zeldinio_vieta` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Želdinio vieta nurodyta LKS koordinačių sistemoje | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `zona` | `"miesto"` | — | — | Miesto zona | — |
| `zona` | `"gatves"` | — | — | Gatvės zona | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/anyksciu_r_sav/zeldiniai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anyksciu_r_sav/zeldiniai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/anyksciu_r_sav/zeldiniai (https://data.gov.lt/datasets/2900/)
