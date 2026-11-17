---
type: Table
title: "SkaidrumoDeklaracija — Pateiktų lobistų skaidrumo deklaracijų skaičius"
description: "Pateikiama per mėnesį registruotų lobistų skaidrumo deklaracijų statistika."
resource: "https://get.data.gov.lt/datasets/gov/vtek/ataskaita/SkaidrumoDeklaracija"
tags: [gov, vtek, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vtek/ataskaitos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/ataskaitos.csv#L16"
    last_modified: "2026-11-11T14:39:20Z"
---

# SkaidrumoDeklaracija — Pateiktų lobistų skaidrumo deklaracijų skaičius

Pateikiama per mėnesį registruotų lobistų skaidrumo deklaracijų statistika.

- **Model:** `datasets/gov/vtek/ataskaita/SkaidrumoDeklaracija`[^manifest]
- **Dataset:** [Lobistinės veiklos statistiniai duomenys](../ataskaita.md) (`datasets/gov/vtek/ataskaita`)
- **Manifest CSV:** [datasets/gov/vtek/ataskaitos.csv#L16](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/ataskaitos.csv#L16)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vtek/ataskaita/SkaidrumoDeklaracija`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `data` | `date` | `D` | `4` | `open` | — | Ataskaitinė data | — |
| `paskelbta` | `integer` | — | `4` | `open` | — | Paskelbtų daklaracijų skaičius per mėnesį | — |
| `viso_paskelbta` | `integer` | — | `4` | `open` | — | Bendras paskelbtų deklaracijų skaičius nuo stebėjimų pradžios | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vtek/ataskaitos.csv
