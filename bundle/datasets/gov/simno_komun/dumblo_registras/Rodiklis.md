---
type: Table
title: "Rodiklis — Dumblo susidarymas valymo įrenginiuose"
description: "SĮ \"Simno komunalininkas\" fiksuojamas dumblo susidarymas valymo įrenginiuose"
resource: "https://get.data.gov.lt/datasets/gov/simno_komun/dumblo_registras/Rodiklis"
tags: [gov, simno_komun, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/simno_komun/dumblo_registras.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/dumblo_registras.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Rodiklis — Dumblo susidarymas valymo įrenginiuose

SĮ "Simno komunalininkas" fiksuojamas dumblo susidarymas valymo įrenginiuose

- **Model:** `datasets/gov/simno_komun/dumblo_registras/Rodiklis`[^manifest]
- **Dataset:** [Dumblo susidarymas valymo įrenginiuose](../dumblo_registras.md) (`datasets/gov/simno_komun/dumblo_registras`)
- **Manifest CSV:** [datasets/gov/simno_komun/dumblo_registras.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/dumblo_registras.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/simno_komun/dumblo_registras/Rodiklis`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA sukurtas šifruotas eilutės unikalus numeris | — |
| `atskaitos_menuo` | `date` | `M` | `4` | `open` | — | Atskaitos mėnuo | — |
| `vietove` | `string` | — | `4` | `open` | — | Valymo įrenginių vietovė | — |
| `rodikliai` | `string` | — | `4` | `open` | — | Rodiklių pavadinimai | — |
| `reiksmes` | `number` | — | `4` | `open` | — | Rodiklių reikšmės | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vietove` | — | `"Daugai"` | — | — | — |
| `vietove` | — | `"Simnas"` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/simno_komun/dumblo_registras.csv
