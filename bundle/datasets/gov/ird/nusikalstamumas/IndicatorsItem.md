---
type: Table
title: "IndicatorsItem — IndicatorsItem"
description: "Lentelė, kurioje apibrėžiami statistinių reikšmių rodikliai"
resource: "https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsItem"
tags: [gov, ird, indicatorsitem, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L30"
    title: "atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv#L30"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1235/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ird/nusikalstamumas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# IndicatorsItem — IndicatorsItem

Lentelė, kurioje apibrėžiami statistinių reikšmių rodikliai[^manifest]

- **Model:** `datasets/gov/ird/nusikalstamumas/IndicatorsItem`[^manifest]
- **Dataset:** [Nusikalstamų veikų statistiniai duomenys](../nusikalstamumas.md) (`datasets/gov/ird/nusikalstamumas`)[^manifest]
- **Manifest CSV:** [datasets/gov/ird/nusikalstamumas.csv#L30](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L30)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsItem` (`deployed`)[^manifest]
- **Provider:** `ird` — Informatikos ir ryšių departamentas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | — | `2` | `open` | — | Dimensijos kodas | Nusikalstamos veikos padarytos LR pagal LR BK, tyrimo stadijas |
| `id` | `integer` | — | `4` | `open` | — | Dimensijos kodas | Kodas priskirtas pagal nusikalstamos veikos padarytos LR pagal LR BK, tyrimo stadiją |
| `position` | `integer` | — | `4` | `open` | — | Pozicija | Ataskaitos pozicija |

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv#L30 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L30)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ird/nusikalstamumas (https://data.gov.lt/datasets/1235/)
