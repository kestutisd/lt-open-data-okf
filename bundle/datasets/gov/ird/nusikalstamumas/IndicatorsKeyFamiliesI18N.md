---
type: Table
title: "IndicatorsKeyFamiliesI18N — IndicatorsKeyFamiliesI18N"
description: "Lentelė, kurioje yra saugomas dimensijų aprašymas"
resource: "https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsKeyFamiliesI18N"
tags: [gov, ird, indicatorskeyfamiliesi18n, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L47"
    title: "atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv#L47"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1235/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ird/nusikalstamumas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# IndicatorsKeyFamiliesI18N — IndicatorsKeyFamiliesI18N

Lentelė, kurioje yra saugomas dimensijų aprašymas[^manifest]

- **Model:** `datasets/gov/ird/nusikalstamumas/IndicatorsKeyFamiliesI18N`[^manifest]
- **Dataset:** [Nusikalstamų veikų statistiniai duomenys](../nusikalstamumas.md) (`datasets/gov/ird/nusikalstamumas`)[^manifest]
- **Manifest CSV:** [datasets/gov/ird/nusikalstamumas.csv#L47](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L47)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsKeyFamiliesI18N` (`deployed`)[^manifest]
- **Provider:** `ird` — Informatikos ir ryšių departamentas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Identifikacijos kodas | Identifikacijos kodas |
| `lang` | `string` | — | `3` | `open` | — | Kalba | Duomenų rinkinio kalba (LT/EN) |
| `target` | `ref` | [IndicatorsKeyFamilie](IndicatorsKeyFamilie.md) (`level=4 UUID`: `target._id`) | `4` | `open` | — | Kodas | Nusikalstama veika ar asmuo |
| `title` | `string` | — | `3` | `open` | — | Rinkinio pavadinimas | Duomenų rinkinys apie nusikalstamas veikas Lietuvoje/ Duomenų rinkinys pagal įtariamus / kaltinamus ir nukentėjusius asmenis |

# Related References

- [ISO 639 Language Codes Reference](../../../../references/iso-639-kalbu-kodai.md) — ISO 639-1 / 639-2 / EU NAL codes and special markers `zxx`, `und`, `mul`, `mis`.

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv#L47 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L47)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ird/nusikalstamumas (https://data.gov.lt/datasets/1235/)
