---
type: Table
title: "RinkimuTuras — Rinkimų turai"
description: "Vykdomų rinkimų lentelė."
resource: "https://get.data.gov.lt/datasets/gov/vrk/rinkeju_demografiniai_duomenys/RinkimuTuras"
tags: [gov, vrk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L24"
    last_modified: "2026-11-11T14:39:20Z"
---

# RinkimuTuras — Rinkimų turai

Vykdomų rinkimų lentelė. Vienas įrašas atitinka vykdomų rinkimų ir jų turų kombinaciją. Lentelė sudaryta iš vykdomų rinkimų identifikatoriaus ir pavadinimo, rinkimų turo identifikatoriaus, numerio, dienos ir požymio, ar turas yra einamasis.

- **Model:** `datasets/gov/vrk/rinkeju_demografiniai_duomenys/RinkimuTuras`[^manifest]
- **Dataset:** [Rinkėjų demografiniai duomenys](../rinkeju_demografiniai_duomenys.md) (`datasets/gov/vrk/rinkeju_demografiniai_duomenys`)
- **Manifest CSV:** [datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L24](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L24)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vrk/rinkeju_demografiniai_duomenys/RinkimuTuras`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `rinkimu_id` | `string` | — | `4` | `open` | — | Vykdomų rinkimų identifikatorius | — |
| `rinkimu_pav` | `string` | — | `4` | `open` | — | Vykdomų rinkimų pavadinimas | — |
| `rinkimu_turo_id` | `string` | — | `4` | `open` | — | Vykdomų rinkimų turo identifikatorius | — |
| `rinkimu_turo_nr` | `integer` | — | `4` | `open` | — | Vykdomų rinkimų turo numeris | — |
| `ar_rinkimu_turas_einamasis` | `string` | — | `4` | `open` | — | Ar vykdomų rinkimų turas yra einamasis | — |
| `rinkimu_turo_diena` | `date` | `D` | `4` | `open` | — | Vykdomų rinkimų turo diena | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv
