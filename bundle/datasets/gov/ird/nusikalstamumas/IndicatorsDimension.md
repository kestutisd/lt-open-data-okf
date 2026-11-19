---
type: Table
title: "IndicatorsDimension — IndicatorsDimension"
description: "Lentelė, kurioje saugomas sąrašas identifikuotų dimensijų ir jų pavadinimai, kodai ir aprašymai"
resource: "https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsDimension"
tags: [gov, ird, indicatorsdimension, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1235/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ird/nusikalstamumas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# IndicatorsDimension — IndicatorsDimension

Lentelė, kurioje saugomas sąrašas identifikuotų dimensijų ir jų pavadinimai, kodai ir aprašymai[^manifest]

- **Model:** `datasets/gov/ird/nusikalstamumas/IndicatorsDimension`[^manifest]
- **Dataset:** [Nusikalstamų veikų statistiniai duomenys](../nusikalstamumas.md) (`datasets/gov/ird/nusikalstamumas`)[^manifest]
- **Manifest CSV:** [datasets/gov/ird/nusikalstamumas.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsDimension` (`deployed`)[^manifest]
- **Provider:** `ird` — Informatikos ir ryšių departamentas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | — | `2` | `open` | — | Dimensijos kodas | Dimensijos kodas - NV tipas, savivaldybė, straipsnis... |
| `id` | `integer` | — | `4` | `open` | — | Dimensijos identifikatorius | Dimensijos identifikatorius - kodas |
| `options` | `string` | — | `2` | `open` | — | Galimybės | Aprašymo ilgis LEFT(`options`, 256) |
| `position` | `integer` | — | `4` | `open` | — | Pozicija ataskaitoje | Pozicija ataskaitoje |

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ird/nusikalstamumas (https://data.gov.lt/datasets/1235/)
