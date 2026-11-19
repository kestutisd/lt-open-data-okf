---
type: Table
title: "IndicatorsMetadata — IndicatorsMetadata"
description: "Lentelė, kurioje yra saugomos rodiklių metaduomenys"
resource: "https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsMetadata"
tags: [gov, ird, indicatorsmetadata, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L59"
    title: "atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv#L59"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1235/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ird/nusikalstamumas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# IndicatorsMetadata — IndicatorsMetadata

Lentelė, kurioje yra saugomos rodiklių metaduomenys[^manifest]

- **Model:** `datasets/gov/ird/nusikalstamumas/IndicatorsMetadata`[^manifest]
- **Dataset:** [Nusikalstamų veikų statistiniai duomenys](../nusikalstamumas.md) (`datasets/gov/ird/nusikalstamumas`)[^manifest]
- **Manifest CSV:** [datasets/gov/ird/nusikalstamumas.csv#L59](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L59)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsMetadata` (`deployed`)[^manifest]
- **Provider:** `ird` — Informatikos ir ryšių departamentas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Identifikacijos kodas | Identifikacijos kodas |
| `item` | `ref` | [IndicatorsItem](IndicatorsItem.md) (`level=4 UUID`: `item._id`) | `4` | `open` | — | Kodas | Dimensijos ID iš Indicatorsitem lentelės |
| `key` | `string` | — | `2` | `open` | — | Dimensijos raktas | Dimensijų kodiniai pavadinimai |
| `value` | `string` | — | `2` | `open` | — | Dimensijos reikšmė | Pasirinktos dimensijos reikšmė |

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv#L59 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L59)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ird/nusikalstamumas (https://data.gov.lt/datasets/1235/)
