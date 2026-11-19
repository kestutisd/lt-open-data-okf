---
type: Table
title: "AsmuoDeklaracija — Privačių interesų deklaracijų statistika pagal pateiktas deklaracijas ir deklaruojančius asmenis"
description: "Ataskaitoje nurodomi duomenys apie per ataskaitinį laikotarpį pateiktas deklaracijas ir jas teikusius asmenis."
resource: "https://get.data.gov.lt/datasets/gov/vtek/pinreg_ataskaitos/AsmuoDeklaracija"
tags: [gov, vtek, asmuodeklaracija, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/pinreg_ataskaitos.csv#L15"
    title: "atviriduomenys/manifest — datasets/gov/vtek/pinreg_ataskaitos.csv#L15"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3798/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vtek/pinreg_ataskaitos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# AsmuoDeklaracija — Privačių interesų deklaracijų statistika pagal pateiktas deklaracijas ir deklaruojančius asmenis

Ataskaitoje nurodomi duomenys apie per ataskaitinį laikotarpį pateiktas deklaracijas ir jas teikusius asmenis. Ataskaitoje pateikiami nuo 2012 m. kaupiami duomenys pamėnesiui.[^manifest]

- **Model:** `datasets/gov/vtek/pinreg_ataskaitos/AsmuoDeklaracija`[^manifest]
- **Dataset:** [Privačių interesų registro ataskaitos](../pinreg_ataskaitos.md) (`datasets/gov/vtek/pinreg_ataskaitos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vtek/pinreg_ataskaitos.csv#L15](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/pinreg_ataskaitos.csv#L15)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vtek/pinreg_ataskaitos/AsmuoDeklaracija` (`deployed`)[^manifest]
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
| `viso_asmenu` | `integer` | — | `4` | `open` | — | Bendras asmenų, pateikusių deklaracijas per ataskaitinį mėnesį, skaičius | — |
| `viso_deklaraciju` | `integer` | — | `4` | `open` | — | Bendras aktyvių juridinių asmenų lobistų skaičius įskaičiuojant ir ankstesnių mėnesių duomenis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vtek/pinreg_ataskaitos.csv#L15 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/pinreg_ataskaitos.csv#L15)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vtek/pinreg_ataskaitos (https://data.gov.lt/datasets/3798/)
