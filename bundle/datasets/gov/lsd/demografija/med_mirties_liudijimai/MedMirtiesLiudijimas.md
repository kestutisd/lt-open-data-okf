---
type: Table
title: "MedMirtiesLiudijimas — Mirčių skaičiai pagal elektroninius medicininius mirties liudijimus"
description: "Spinta table datasets/gov/lsd/demografija/med_mirties_liudijimai/MedMirtiesLiudijimas (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/demografija/med_mirties_liudijimai/MedMirtiesLiudijimas"
tags: [gov, lsd, medmirtiesliudijimas, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/demografija/demografija.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/lsd/demografija/demografija.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2025/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/demografija/med_mirties_liudijimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# MedMirtiesLiudijimas — Mirčių skaičiai pagal elektroninius medicininius mirties liudijimus

- **Model:** `datasets/gov/lsd/demografija/med_mirties_liudijimai/MedMirtiesLiudijimas`[^manifest]
- **Dataset:** [Mirčių skaičius pagal skaitmeninius medicininius mirties liudijimus](../med_mirties_liudijimai.md) (`datasets/gov/lsd/demografija/med_mirties_liudijimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/demografija/demografija.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/demografija/demografija.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/demografija/med_mirties_liudijimai/MedMirtiesLiudijimas` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus įdentifikatorius | — |
| `data` | `date` | `D` | `4` | `open` | — | Faktinė asmens mirties data | — |
| `amzius` | `integer` | — | `3` | `open` | — | Asmens amžius mirties datą | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `mirtys` | `integer` | — | `4` | `open` | — | Mirčių skaičius pagal mirties datą, asmens amžių ir lytį | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"mot"` | — | — | Moteris | — |
| `lytis` | `"vyr"` | — | — | Vyras | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amzius` | `update(ref: "Y")` | `ref` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/demografija/demografija.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/demografija/demografija.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/demografija/med_mirties_liudijimai (https://data.gov.lt/datasets/2025/)
