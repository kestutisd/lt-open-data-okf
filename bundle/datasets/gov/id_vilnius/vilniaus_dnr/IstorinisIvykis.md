---
type: Table
title: "IstorinisIvykis — Vilniaus miesto istoriniai įvykiai"
description: "Duomenys iš „ID Vilnius“ apie svarbiausius Vilniaus miesto istorinius įvykius."
resource: "https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr/IstorinisIvykis"
tags: [gov, id_vilnius, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L111"
    last_modified: "2026-11-11T14:39:20Z"
---

# IstorinisIvykis — Vilniaus miesto istoriniai įvykiai

Duomenys iš „ID Vilnius“ apie svarbiausius Vilniaus miesto istorinius įvykius. Viena lentelės eilutė yra vienas unikalus įvykis. Eilutės informaciją sudaro įvykio identifikacinis numeris, įvykio pavadinimas, istorinis įvykių juostos laikotarpis, data, vieta, nuotrauka ir jos aprašymas.

- **Model:** `datasets/gov/id_vilnius/vilniaus_dnr/IstorinisIvykis`[^manifest]
- **Dataset:** [Vilniaus miesto istoriniai duomenys - Vilniaus DNR](../vilniaus_dnr.md) (`datasets/gov/id_vilnius/vilniaus_dnr`)
- **Manifest CSV:** [datasets/gov/id_vilnius/vilniaus_dnr.csv#L111](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L111)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr/IstorinisIvykis`
- **Primary Key (`ref`):** `ivykio_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ivykio_id` | `string` | — | `4` | `open` | — | Įvykio identifikacinis numeris (pirminis raktas) | — |
| `ivykis` | `string` | — | `4` | `open` | — | Įvykio pavadinimas | — |
| `vilniaus_laikotarpis` | `string` | — | `4` | `open` | — | Vilniaus istorinis laikotarpis | Vilniaus istorinių įvykių juostos laikotarpis, kuriam priklauso įvykis |
| `data` | `date` | `D` | `4` | `open` | — | Įvykio data | — |
| `vieta` | `string` | — | `4` | `open` | — | Įvykio vieta | — |
| `nuotrauka` | `string` | — | `4` | `open` | — | Nuotrauka susijusi su įvykiu | — |
| `nuotraukos_aprasymas` | `string` | — | `4` | `open` | — | Nuotraukos aprašymas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv
