---
type: Table
title: "AsmuoDeklaracija — Privačių interesų deklaracijų statistika pagal pateiktas deklaracijas ir deklaruojančius asmenis"
description: "Ataskaitoje nurodomi duomenys apie per ataskaitinį laikotarpį pateiktas deklaracijas ir jas teikusius asmenis."
resource: "https://get.data.gov.lt/datasets/gov/vtek/pinreg_ataskaitos/AsmuoDeklaracija"
tags: [gov, vtek, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vtek/pinreg_ataskaitos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/pinreg_ataskaitos.csv#L15"
    last_modified: "2026-11-11T14:39:20Z"
---

# AsmuoDeklaracija — Privačių interesų deklaracijų statistika pagal pateiktas deklaracijas ir deklaruojančius asmenis

Ataskaitoje nurodomi duomenys apie per ataskaitinį laikotarpį pateiktas deklaracijas ir jas teikusius asmenis. Ataskaitoje pateikiami nuo 2012 m. kaupiami duomenys pamėnesiui.

- **Model:** `datasets/gov/vtek/pinreg_ataskaitos/AsmuoDeklaracija`[^manifest]
- **Dataset:** [Privačių interesų registro ataskaitos](../pinreg_ataskaitos.md) (`datasets/gov/vtek/pinreg_ataskaitos`)
- **Manifest CSV:** [datasets/gov/vtek/pinreg_ataskaitos.csv#L15](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/pinreg_ataskaitos.csv#L15)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vtek/pinreg_ataskaitos/AsmuoDeklaracija`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `ataskaitos_data` | `date` | `D` | `4` | `open` | — | Ataskaitinė data | — |
| `viso_asmenu` | `integer` | — | `4` | `open` | — | Bendras asmenų, pateikusių deklaracijas per ataskaitinį mėnesį, skaičius | — |
| `viso_deklaraciju` | `integer` | — | `4` | `open` | — | Bendras aktyvių juridinių asmenų lobistų skaičius įskaičiuojant ir ankstesnių mėnesių duomenis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vtek/pinreg_ataskaitos.csv
