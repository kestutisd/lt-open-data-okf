---
type: Table
title: "Prasymas — Duomenys apie trečiųjų šalių piliečių prašymus išduoti ar pakeisti leidimą laikinai gyventi Lietuvos Respublikoje"
description: "Spinta table datasets/gov/migracija/teise_gyventi_lr/Prasymas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/migracija/teise_gyventi_lr/Prasymas"
tags: [gov, migracija, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/migracija/teise_gyventi_lr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/teise_gyventi_lr.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Prasymas — Duomenys apie trečiųjų šalių piliečių prašymus išduoti ar pakeisti leidimą laikinai gyventi Lietuvos Respublikoje

- **Model:** `datasets/gov/migracija/teise_gyventi_lr/Prasymas`[^manifest]
- **Dataset:** [datasets/gov/migracija/teise_gyventi_lr](../teise_gyventi_lr.md) (`datasets/gov/migracija/teise_gyventi_lr`)
- **Manifest CSV:** [datasets/gov/migracija/teise_gyventi_lr.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/teise_gyventi_lr.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/migracija/teise_gyventi_lr/Prasymas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `pateikimas` | `date` | `D` | `4` | `open` | — | Prašymo pateikimo data | — |
| `prasymo_registracija` | `date` | `D` | `4` | `open` | — | Prašymo registracijos data | — |
| `pagrindas` | `string` | — | `3` | `open` | — | Prašymo pagrindas | — |
| `pilietybe` | `string` | — | `2` | `open` | — | Asmens pilietybė | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Asmens amžiaus grupė pagal gimimo datą | — |
| `lytis` | `string` | — | `4` | `open` (inherited) | — | Lytis byloje | — |
| `skubus_prasymas` | `boolean` | — | `4` | `open` | — | Prašymo nagrinėjimo tvarka | — |
| `skyrius` | `string` | — | `4` | `open` | — | Prašymo būsenos sukūrimo vieta | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"M"` | — | `open` | Moteris | — |
| `lytis` | `"V"` | — | — | Vyras | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pilietybe` | `"update(property: ""pilietybe[]"", type: ""array"", source: ""Pilietybe"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/migracija/teise_gyventi_lr.csv
