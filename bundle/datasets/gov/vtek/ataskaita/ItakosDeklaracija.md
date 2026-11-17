---
type: Table
title: "ItakosDeklaracija — Asmenų, patyrusių lobistinę įtaką, pateiktų deklaracijų skaičius"
description: "Pateikiama mėnesinė patirtos lobistinės įtakos deklaracijų statistika."
resource: "https://get.data.gov.lt/datasets/gov/vtek/ataskaita/ItakosDeklaracija"
tags: [gov, vtek, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vtek/ataskaitos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/ataskaitos.csv#L22"
    last_modified: "2026-11-11T14:39:20Z"
---

# ItakosDeklaracija — Asmenų, patyrusių lobistinę įtaką, pateiktų deklaracijų skaičius

Pateikiama mėnesinė patirtos lobistinės įtakos deklaracijų statistika.

- **Model:** `datasets/gov/vtek/ataskaita/ItakosDeklaracija`[^manifest]
- **Dataset:** [Lobistinės veiklos statistiniai duomenys](../ataskaita.md) (`datasets/gov/vtek/ataskaita`)
- **Manifest CSV:** [datasets/gov/vtek/ataskaitos.csv#L22](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/ataskaitos.csv#L22)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vtek/ataskaita/ItakosDeklaracija`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `data` | `date` | `D` | `4` | `open` | — | Ataskaitinė data | — |
| `paskelbta` | `integer` | — | `4` | `open` | — | Paskelbtų daklaracijų skaičius per mėnesį | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vtek/ataskaitos.csv
