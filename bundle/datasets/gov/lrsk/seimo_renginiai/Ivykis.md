---
type: Table
title: "Ivykis — Duomenys apie Seime vykusius renginius"
description: "Rinkinyje pateikiami duomenys apie Seime organizuotus renginius nuo 2015m. Pateikiama informacija: renginio pavadinimas, kalba, pradžios ir pabaigos laikas, renginio vieta ir vietų skaičius."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/seimo_renginiai/Ivykis"
tags: [gov, lrsk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lrsk/seimo_renginiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/seimo_renginiai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Ivykis — Duomenys apie Seime vykusius renginius

Rinkinyje pateikiami duomenys apie Seime organizuotus renginius nuo 2015m. Pateikiama informacija: renginio pavadinimas, kalba, pradžios ir pabaigos laikas, renginio vieta ir vietų skaičius.

- **Model:** `datasets/gov/lrsk/seimo_renginiai/Ivykis`[^manifest]
- **Dataset:** [Duomenys apie Seime vykusius renginius](../seimo_renginiai.md) (`datasets/gov/lrsk/seimo_renginiai`)
- **Manifest CSV:** [datasets/gov/lrsk/seimo_renginiai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/seimo_renginiai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/seimo_renginiai/Ivykis`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo unikalus identifikatorius | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Renginio pavadinimas | — |
| `kalba` | `string` | — | `4` | `open` | — | Renginio kalba | — |
| `pradzia` | `date` | `D` | `4` | `open` | — | Renginio pradžios data | — |
| `pabaiga` | `date` | `D` | `4` | `open` | — | Renginio pabaigos data | — |
| `vieta` | `string` | — | `4` | `open` | — | Renginio vieta | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/seimo_renginiai.csv
