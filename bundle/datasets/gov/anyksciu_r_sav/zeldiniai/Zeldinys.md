---
type: Table
title: "Zeldinys — Anykščių miesto želdiniai"
description: "Informacija apie Anykščių miesto želdinius"
resource: "https://get.data.gov.lt/datasets/gov/anyksciu_r_sav/zeldiniai/Zeldinys"
tags: [gov, anyksciu_r_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/anyksciu_r_sav/zeldiniai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anyksciu_r_sav/zeldiniai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Zeldinys — Anykščių miesto želdiniai

Informacija apie Anykščių miesto želdinius

- **Model:** `datasets/gov/anyksciu_r_sav/zeldiniai/Zeldinys`[^manifest]
- **Dataset:** [Anykščių miesto želdiniai ir želdynai](../zeldiniai.md) (`datasets/gov/anyksciu_r_sav/zeldiniai`)
- **Manifest CSV:** [datasets/gov/anyksciu_r_sav/zeldiniai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anyksciu_r_sav/zeldiniai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/anyksciu_r_sav/zeldiniai/Zeldinys`
- **Primary Key (`ref`):** `objekto_id`
- **Level:** `4`

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

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `zona` | `"miesto"` | — | — | Miesto zona | — |
| `zona` | `"gatves"` | — | — | Gatvės zona | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/anyksciu_r_sav/zeldiniai.csv
