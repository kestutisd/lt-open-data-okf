---
type: Table
title: "BlokuSklypas — Sklypas"
description: "Vietovė / Blokas : Sklypas = kadastro numeris"
resource: "https://get.data.gov.lt/datasets/gov/miskai/pvp/BlokuSklypas"
tags: [gov, miskai, blokusklypas, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L33"
    title: "atviriduomenys/manifest — datasets/gov/miskai/pvp.csv#L33"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/916/"
    title: "data.gov.lt DCAT-AP — datasets/gov/miskai/pvp"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# BlokuSklypas — Sklypas

Vietovė / Blokas : Sklypas = kadastro numeris[^manifest]

- **Model:** `datasets/gov/miskai/pvp/BlokuSklypas`[^manifest]
- **Dataset:** [Privačių vidinės miškotvarkos projektų rengėjų sąrašas](../pvp.md) (`datasets/gov/miskai/pvp`)[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/pvp.csv#L33](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L33)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/pvp/BlokuSklypas` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kadblokas_id` | `integer` | — | `3` | `open` | — | Sąsaja su kadastriniu bloku | — |
| `kadsklypas_id` | `integer` | — | `3` | `open` | — | Sąsaja su kadastriniu sklypu | — |
| `sklypas` | `number` | — | `3` | `open` | — | Sklypas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/pvp.csv#L33 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L33)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/miskai/pvp (https://data.gov.lt/datasets/916/)
