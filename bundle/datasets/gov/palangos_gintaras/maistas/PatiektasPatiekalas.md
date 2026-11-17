---
type: Table
title: "PatiektasPatiekalas — Vaikų reabilitacijos sanatorijos \"Palangos gintaras\" patiektų patiekalų sąrašas"
description: "Šiame rinkinyje pateikiamas vaikų reabilitacijos sanatorijos \"Palangos gintaras\" patiektų patiekalų sąrašas."
resource: "https://get.data.gov.lt/datasets/gov/palangos_gintaras/maistas/PatiektasPatiekalas"
tags: [gov, palangos_gintaras, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/palangos_gintaras/maistas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/palangos_gintaras/maistas.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# PatiektasPatiekalas — Vaikų reabilitacijos sanatorijos "Palangos gintaras" patiektų patiekalų sąrašas

Šiame rinkinyje pateikiamas vaikų reabilitacijos sanatorijos "Palangos gintaras" patiektų patiekalų sąrašas. Duomenys pateikiami už 2016-2023 metus. Pateiki duomenys nebebus atnaujinami.

- **Model:** `datasets/gov/palangos_gintaras/maistas/PatiektasPatiekalas`[^manifest]
- **Dataset:** [datasets/gov/palangos_gintaras/maistas](../maistas.md) (`datasets/gov/palangos_gintaras/maistas`)
- **Manifest CSV:** [datasets/gov/palangos_gintaras/maistas.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/palangos_gintaras/maistas.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/palangos_gintaras/maistas/PatiektasPatiekalas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Identifikacinis numeris | — |
| `meniu_id` | `string` | — | `4` | `open` | — | Meniu identifikacinis numeris | — |
| `data` | `date` | `D` | `4` | `open` | — | Data | — |
| `valgytoju_gr_id` | `string` | — | `4` | `open` | — | Valgytojų grupės identifikacinis numeris | — |
| `valgytoju_gr_pav` | `string` | — | `4` | `open` | — | Valgytojų grupės pavadinimas | — |
| `mait_laikas` | `string` | — | `3` | `open` | — | Maitinimo laikas | — |
| `patiekalas` | `string` | — | `4` | `open` | — | Patiekalas | — |
| `kodas` | `string` | — | `4` | `open` | — | Patiekalo kodas | — |
| `simbolis` | `string` | — | `3` | `open` | — | Simbolis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/palangos_gintaras/maistas.csv
