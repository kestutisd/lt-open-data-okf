---
type: Table
title: "Rodiklis — Lentelėje pateikti valstybės strategijų, programų rodiklių duomenys iš Lietuvos Respublikos finansų ministerijos Stebėsenos informacinė sistema (SIS)."
description: "Spinta table datasets/gov/finmin/sis/Rodiklis (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sis/Rodiklis"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sis/finmin.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sis/finmin.csv#L36"
    last_modified: "2026-11-11T14:39:20Z"
---

# Rodiklis — Lentelėje pateikti valstybės strategijų, programų rodiklių duomenys iš Lietuvos Respublikos finansų ministerijos Stebėsenos informacinė sistema (SIS).

- **Model:** `datasets/gov/finmin/sis/Rodiklis`[^manifest]
- **Dataset:** [datasets/gov/finmin/sis](../sis.md) (`datasets/gov/finmin/sis`)
- **Manifest CSV:** [datasets/gov/finmin/sis/finmin.csv#L36](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sis/finmin.csv#L36)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sis/Rodiklis`
- **Primary Key (`ref`):** `id_planas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id_planas` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `id_faktas` | `string` | — | `4` | `open` | — | Fakto unikalus identifikatorius | — |
| `doc_id` | `string` | — | `4` | `open` | — | Dokumento kodas, atvaizduojamas ataskaitose. | — |
| `obj_id` | `string` | — | `4` | `open` | — | Žemesnio lygmens objektas (objektas-vaikas). Nuoroda į OBJECTS. OBJ_ID. | — |
| `data_nuo` | `date` | `D` | `4` | `open` | — | Laikotarpio pradžios diena. | — |
| `data_iki` | `date` | `D` | `4` | `open` | — | Laikotarpio pabaigos diena. | — |
| `plano_reiksme_kiekybine` | `number` | — | `4` | `open` | — | Rodiklio plano kiekybinė reikšmė | — |
| `plano_reiksme_kokybine` | `string` | — | `4` | `open` | — | Rodiklio plano kokybinė reikšmė | — |
| `fakto_reiksme_kiekybine` | `number` | — | `4` | `open` | — | Faktinė rodiklio reikšmė. | — |
| `fakto_reiksme_kokybine` | `string` | — | `4` | `open` | — | Faktinė rodiklio reikšmė (simbolinio tipo). | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sis/finmin.csv
