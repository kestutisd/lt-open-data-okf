---
type: Table
title: "IndicatorsDimensionsI18N — IndicatorsDimensionsI18N"
description: "Lentelė, kurioje yra saugomas dimensijų aprašymas"
resource: "https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsDimensionsI18N"
tags: [gov, ird, indicatorsdimensionsi18n, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L10"
    title: "atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv#L10"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1235/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ird/nusikalstamumas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# IndicatorsDimensionsI18N — IndicatorsDimensionsI18N

Lentelė, kurioje yra saugomas dimensijų aprašymas[^manifest]

- **Model:** `datasets/gov/ird/nusikalstamumas/IndicatorsDimensionsI18N`[^manifest]
- **Dataset:** [Nusikalstamų veikų statistiniai duomenys](../nusikalstamumas.md) (`datasets/gov/ird/nusikalstamumas`)[^manifest]
- **Manifest CSV:** [datasets/gov/ird/nusikalstamumas.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L10)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsDimensionsI18N` (`deployed`)[^manifest]
- **Provider:** `ird` — Informatikos ir ryšių departamentas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Dimensijos identifikatorius | Dimensijos identifikatorius - kodas |
| `lang` | `string` | — | `3` | `open` | — | Kalba | Duomenų rinkinio kalba (LT/EN) |
| `target` | `ref` | [IndicatorsDimension](IndicatorsDimension.md) (`level=4 UUID`: `target._id`) | `4` | `open` | — | Dimensijos kodas | Dimensijos ID iš IndicatorsDimension lentelės |
| `title` | `string` | — | `4` | `open` | — | Dimensijos aprašymas | Dimensijos aprašymas |

# Related References

- [ISO 639 Language Codes Reference](../../../../references/iso-639-kalbu-kodai.md) — ISO 639-1 / 639-2 / EU NAL codes and special markers `zxx`, `und`, `mul`, `mis`.

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv#L10 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L10)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ird/nusikalstamumas (https://data.gov.lt/datasets/1235/)
