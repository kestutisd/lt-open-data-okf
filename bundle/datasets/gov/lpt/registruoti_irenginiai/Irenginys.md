---
type: Table
title: "Irenginys — Lošimo bendrovių įregistruoti įrenginiai"
description: "Lošimo bendrovių įregistruotų įrenginių ir jų istorijos sąrašas"
resource: "https://get.data.gov.lt/datasets/gov/lpt/registruoti_irenginiai/Irenginys"
tags: [gov, lpt, irenginys, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lpt/registruoti_irenginiai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lpt/registruoti_irenginiai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2670/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lpt/registruoti_irenginiai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Irenginys — Lošimo bendrovių įregistruoti įrenginiai

Lošimo bendrovių įregistruotų įrenginių ir jų istorijos sąrašas[^manifest]

- **Model:** `datasets/gov/lpt/registruoti_irenginiai/Irenginys`[^manifest]
- **Dataset:** [Lošimo bendrovių įregistruoti įrenginiai](../registruoti_irenginiai.md) (`datasets/gov/lpt/registruoti_irenginiai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lpt/registruoti_irenginiai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lpt/registruoti_irenginiai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lpt/registruoti_irenginiai/Irenginys` (`deployed`)[^manifest]
- **Provider:** `lpt` — Lošimų priežiūros tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `irenginio_registracijos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `irenginio_registracijos_id` | `string` | — | `4` | `open` | — | Įrenginio registracijos unikalus identifikatorius | — |
| `leidimo_id` | `string` | — | `4` | `open` | — | Leidimo unikalus identifikatorius | — |
| `leidimo_dokumento_id` | `string` | — | `4` | `open` | — | Leidimo dokumento unikalus identifikatorius | — |
| `irenginio_id` | `string` | — | `4` | `open` | — | Įrenginio identifikatorius | — |
| `irenginio_registracijos_numeris` | `string` | — | `4` | `open` | — | Registracijos numeris | — |
| `irenginio_pavadinimas` | `string` | — | `4` | `open` | — | Įrenginio pavadinimas, pateiktas lošimų bendrovės | — |
| `irenginio_tipo_id` | `string` | — | `4` | `open` | — | Įrenginio tipo unikalus identifikatorius | — |
| `galioja_nuo` | `date` | `D` | `4` | `open` | — | Registracija galioja nuo | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Registracija galioja iki | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `irenginio_pavadinimas` | `update(property: "irenginio_pavadinimas@en", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lpt/registruoti_irenginiai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lpt/registruoti_irenginiai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lpt/registruoti_irenginiai (https://data.gov.lt/datasets/2670/)
