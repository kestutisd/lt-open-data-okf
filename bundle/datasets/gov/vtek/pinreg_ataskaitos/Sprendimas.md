---
type: Table
title: "Sprendimas — Vyriausiosios tarnybinės etikos komisijos (VTEK) priimtų sprendimų statistika"
description: "Tirdama pranešimus, skundus ir prašymus dėl deklaruojančių asmenų veiklos atitikimo Viešųjų ir privačių interesų derinimo įstatymui, VTEK nusprendžia pripažinti pažeidimą, pripažinti pažeidimo nebuvimą arba nutraukti tyrimą."
resource: "https://get.data.gov.lt/datasets/gov/vtek/pinreg_ataskaitos/Sprendimas"
tags: [gov, vtek, sprendimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/pinreg_ataskaitos.csv#L27"
    title: "atviriduomenys/manifest — datasets/gov/vtek/pinreg_ataskaitos.csv#L27"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3798/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vtek/pinreg_ataskaitos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sprendimas — Vyriausiosios tarnybinės etikos komisijos (VTEK) priimtų sprendimų statistika

Tirdama pranešimus, skundus ir prašymus dėl deklaruojančių asmenų veiklos atitikimo Viešųjų ir privačių interesų derinimo įstatymui, VTEK nusprendžia pripažinti pažeidimą, pripažinti pažeidimo nebuvimą arba nutraukti tyrimą. Ataskaitoje pateikiami nuo 2006 m. kaupiami šių sprendimų duomenys pamėnesiui.[^manifest]

- **Model:** `datasets/gov/vtek/pinreg_ataskaitos/Sprendimas`[^manifest]
- **Dataset:** [Privačių interesų registro ataskaitos](../pinreg_ataskaitos.md) (`datasets/gov/vtek/pinreg_ataskaitos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vtek/pinreg_ataskaitos.csv#L27](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/pinreg_ataskaitos.csv#L27)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vtek/pinreg_ataskaitos/Sprendimas` (`deployed`)[^manifest]
- **Provider:** `vtek` — Vyriausioji tarnybinės etikos komisija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `ataskaitos_data` | `date` | `D` | `4` | `open` | — | Ataskaitinė data | — |
| `nutraukti_tyrima` | `integer` | — | `4` | `open` | — | Bendras priimtų sprendimų nutraukti tyrimą skaičius | — |
| `pripazinti_nepazeidima` | `integer` | — | `4` | `open` | — | Bendras priimtų sprendimų pripažinti pažeidimo nebuvimą skaičius | — |
| `pripazinti_pazeidima` | `integer` | — | `4` | `open` | — | Bendras priimtų sprendimų pripažinti pažeidimą skaičius | — |
| `viso_sprendimu` | `integer` | — | `4` | `open` | — | Bendras VTEK paskelbtų sprendimų skaičius per mėnesį | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vtek/pinreg_ataskaitos.csv#L27 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/pinreg_ataskaitos.csv#L27)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vtek/pinreg_ataskaitos (https://data.gov.lt/datasets/3798/)
