---
type: Dataset
title: "datasets/gov/migracija/lt_pilietybe"
description: "Duomenys apie asmenis, kuriems Lietuvos Respublikos pilietybė buvo atkurta, suteikta natūralizacijos, supaprastinta ar išimties tvarka, kurie grąžino Lietuvos Respublikos pilietybę, taip pat vaikus, kuriems buvo konstatuotas Lietuvos..."
resource: "https://get.data.gov.lt/datasets/gov/migracija/lt_pilietybe"
tags: [gov, migracija, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/migracija/lt_pilietybe.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/lt_pilietybe.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/migracija/lt_pilietybe

Duomenys apie asmenis, kuriems Lietuvos Respublikos pilietybė buvo atkurta, suteikta natūralizacijos, supaprastinta ar išimties tvarka, kurie grąžino Lietuvos Respublikos pilietybę, taip pat vaikus, kuriems buvo konstatuotas Lietuvos Respublikos pilietybės turėjimo faktas, kurie Lietuvos Respublikos pilietybę įgijo juos įvaikinus arba pasikeitus tėvų pilietybei, neatsižvelgiant į jų gyvenamąją vietą.

- **Namespace:** `datasets/gov/migracija/lt_pilietybe`[^manifest]
- **Manifest CSV:** [datasets/gov/migracija/lt_pilietybe.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/lt_pilietybe.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/migracija/lt_pilietybe`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Prasymas](lt_pilietybe/Prasymas.md) | Prašymai dėl Lietuvos Respublikos pilietybės | `4` | `id` | `open` | 7 | — |
| [Sprendimas](lt_pilietybe/Sprendimas.md) | Sprendimai dėl Lietuvos Respublikos pilietybės suteikimo | `4` | `id` | `open` | 7 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/migracija/lt_pilietybe.csv
