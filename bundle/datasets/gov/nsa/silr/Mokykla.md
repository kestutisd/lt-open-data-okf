---
type: Table
title: "Mokykla — Mokinių lankomumo duomenų mokyklos"
description: "Spinta table datasets/gov/nsa/silr/Mokykla (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/silr/Mokykla"
tags: [gov, nsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nsa/silr/silr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/silr/silr.csv#L21"
    last_modified: "2026-11-11T14:39:20Z"
---

# Mokykla — Mokinių lankomumo duomenų mokyklos

- **Model:** `datasets/gov/nsa/silr/Mokykla`[^manifest]
- **Dataset:** [Švietimo įstaigų lankomumo rodikliai](../silr.md) (`datasets/gov/nsa/silr`)
- **Manifest CSV:** [datasets/gov/nsa/silr/silr.csv#L21](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/silr/silr.csv#L21)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/silr/Mokykla`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `ins_kodas` | `string` | — | `4` | `open` | — | Švietimo įstaigos (mokyklos) kodas Juridinių asmenų registre | — |
| `pad_kodas` | `string` | — | `4` | `open` | — | Švietimo ir mokslo institucijų registro institucijos padalinio kodas | — |
| `ins_pav` | `string` | — | `4` | `open` | — | Švietimo įstaigos (mokyklos) pavadinimas Juridinių asmenų registre | — |
| `pad_pav` | `string` | — | `4` | `open` | — | Švietimo ir mokslo institucijų registro institucijos padalinio pavadinimas | — |
| `sav_kodas` | `string` | — | `4` | `open` | — | Savivaldybės kodas | — |
| `sav_pav` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/silr/silr.csv
