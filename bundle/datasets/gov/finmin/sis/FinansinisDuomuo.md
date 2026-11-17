---
type: Table
title: "FinansinisDuomuo — Lentelėje pateikti valstybės strategijų, programų finansiniai duomenys iš Lietuvos Respublikos finansų ministerijos Stebėsenos informacinė sistema (SIS)."
description: "Spinta table datasets/gov/finmin/sis/FinansinisDuomuo (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sis/FinansinisDuomuo"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sis/finmin.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sis/finmin.csv#L48"
    last_modified: "2026-11-11T14:39:20Z"
---

# FinansinisDuomuo — Lentelėje pateikti valstybės strategijų, programų finansiniai duomenys iš Lietuvos Respublikos finansų ministerijos Stebėsenos informacinė sistema (SIS).

- **Model:** `datasets/gov/finmin/sis/FinansinisDuomuo`[^manifest]
- **Dataset:** [datasets/gov/finmin/sis](../sis.md) (`datasets/gov/finmin/sis`)
- **Manifest CSV:** [datasets/gov/finmin/sis/finmin.csv#L48](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sis/finmin.csv#L48)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sis/FinansinisDuomuo`
- **Primary Key (`ref`):** `fnv_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fnv_id` | `string` | — | `4` | `open` | — | Įrašo identifikacinis numeris. Generuojamas seka FNV_SEQ. | — |
| `doc_id` | `string` | — | `4` | `open` | — | Dokumento kodas, atvaizduojamas ataskaitose. | — |
| `obj_id` | `string` | — | `4` | `open` | — | Žemesnio lygmens objektas (objektas-vaikas). Nuoroda į OBJECTS. OBJ_ID. | — |
| `pradz_data` | `date` | `D` | `4` | `open` | — | Finansavimo pradžios data | — |
| `pabaig_data` | `date` | `D` | `4` | `open` | — | Finansavimo pabaigos data | — |
| `verte_eur` | `number` | — | `4` | `open` | — | Planinė arba faktinė objekto finansinio rodiklio reikšmė (EUR). | — |
| `pozymis_1` | `string` | — | `4` | `open` | — | Požymis, ar planas, faktas, poreikis. | — |
| `islaidu_tipas` | `string` | — | `4` | `open` | — | Išlaidų tipas. | — |
| `finansavimo_saltinis` | `string` | — | `4` | `open` | — | Finansavimo šaltinio pavadinimas. | — |
| `pozymis_2` | `string` | — | `4` | `open` | — | Lėšų tipas. | — |
| `valst_funkcijos_pav` | `string` | — | `4` | `open` | — | Valstybės funkcijos pavadinimas. | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sis/finmin.csv
