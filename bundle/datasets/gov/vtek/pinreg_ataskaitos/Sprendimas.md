---
type: Table
title: "Sprendimas — Vyriausiosios tarnybinės etikos komisijos (VTEK) priimtų sprendimų statistika"
description: "Tirdama pranešimus, skundus ir prašymus dėl deklaruojančių asmenų veiklos atitikimo Viešųjų ir privačių interesų derinimo įstatymui, VTEK nusprendžia pripažinti pažeidimą, pripažinti pažeidimo nebuvimą arba nutraukti tyrimą."
resource: "https://get.data.gov.lt/datasets/gov/vtek/pinreg_ataskaitos/Sprendimas"
tags: [gov, vtek, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vtek/pinreg_ataskaitos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/pinreg_ataskaitos.csv#L27"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sprendimas — Vyriausiosios tarnybinės etikos komisijos (VTEK) priimtų sprendimų statistika

Tirdama pranešimus, skundus ir prašymus dėl deklaruojančių asmenų veiklos atitikimo Viešųjų ir privačių interesų derinimo įstatymui, VTEK nusprendžia pripažinti pažeidimą, pripažinti pažeidimo nebuvimą arba nutraukti tyrimą. Ataskaitoje pateikiami nuo 2006 m. kaupiami šių sprendimų duomenys pamėnesiui.

- **Model:** `datasets/gov/vtek/pinreg_ataskaitos/Sprendimas`[^manifest]
- **Dataset:** [Privačių interesų registro ataskaitos](../pinreg_ataskaitos.md) (`datasets/gov/vtek/pinreg_ataskaitos`)
- **Manifest CSV:** [datasets/gov/vtek/pinreg_ataskaitos.csv#L27](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/pinreg_ataskaitos.csv#L27)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vtek/pinreg_ataskaitos/Sprendimas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `ataskaitos_data` | `date` | `D` | `4` | `open` | — | Ataskaitinė data | — |
| `nutraukti_tyrima` | `integer` | — | `4` | `open` | — | Bendras priimtų sprendimų nutraukti tyrimą skaičius | — |
| `pripazinti_nepazeidima` | `integer` | — | `4` | `open` | — | Bendras priimtų sprendimų pripažinti pažeidimo nebuvimą skaičius | — |
| `pripazinti_pazeidima` | `integer` | — | `4` | `open` | — | Bendras priimtų sprendimų pripažinti pažeidimą skaičius | — |
| `viso_sprendimu` | `integer` | — | `4` | `open` | — | Bendras VTEK paskelbtų sprendimų skaičius per mėnesį | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vtek/pinreg_ataskaitos.csv
