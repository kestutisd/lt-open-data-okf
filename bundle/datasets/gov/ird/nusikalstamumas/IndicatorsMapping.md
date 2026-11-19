---
type: Table
title: "IndicatorsMapping — IndicatorsMapping"
description: "Lentelė, kurioje yra saugomi duomenys apie ataskaitas"
resource: "https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsMapping"
tags: [gov, ird, indicatorsmapping, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L53"
    title: "atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv#L53"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1235/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ird/nusikalstamumas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# IndicatorsMapping — IndicatorsMapping

Lentelė, kurioje yra saugomi duomenys apie ataskaitas[^manifest]

- **Model:** `datasets/gov/ird/nusikalstamumas/IndicatorsMapping`[^manifest]
- **Dataset:** [Nusikalstamų veikų statistiniai duomenys](../nusikalstamumas.md) (`datasets/gov/ird/nusikalstamumas`)[^manifest]
- **Manifest CSV:** [datasets/gov/ird/nusikalstamumas.csv#L53](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L53)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsMapping` (`deployed`)[^manifest]
- **Provider:** `ird` — Informatikos ir ryšių departamentas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `date_from` | `date` | `M` | `4` | `open` | — | Data nuo | Ataskaitos galiojimo data nuo |
| `date_to` | `date` | `M` | `4` | `open` | — | Data iki | Ataskaitos galiojimo data iki |
| `form_code` | `string` | — | `4` | `open` | — | Ataskaitos kodas | Iš kokios ataskaitos pateikiami duomenys |
| `id` | `integer` | — | `4` | `open` | — | Identifikatorius | Ataskaitai priskirtas kodas |

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv#L53 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L53)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ird/nusikalstamumas (https://data.gov.lt/datasets/1235/)
