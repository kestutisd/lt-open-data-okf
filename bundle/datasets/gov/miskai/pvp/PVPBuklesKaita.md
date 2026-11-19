---
type: Table
title: "PVPBuklesKaita — Projekto būklės data"
description: "Spinta table datasets/gov/miskai/pvp/PVPBuklesKaita (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/pvp/PVPBuklesKaita"
tags: [gov, miskai, pvpbukleskaita, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L24"
    title: "atviriduomenys/manifest — datasets/gov/miskai/pvp.csv#L24"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/916/"
    title: "data.gov.lt DCAT-AP — datasets/gov/miskai/pvp"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PVPBuklesKaita — Projekto būklės data

- **Model:** `datasets/gov/miskai/pvp/PVPBuklesKaita`[^manifest]
- **Dataset:** [Privačių vidinės miškotvarkos projektų rengėjų sąrašas](../pvp.md) (`datasets/gov/miskai/pvp`)[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/pvp.csv#L24](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L24)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/pvp/PVPBuklesKaita` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `bukle` | `ref` | [PVPBukle](PVPBukle.md) (`level=4 UUID`: `bukle._id`) | `4` | `open` | — | Būklė | — |
| `bukles_data` | `datetime` | — | `4` | `open` | — | Būklės data | — |
| `pvproj` | `ref` | [PrivacValduProjektas](PrivacValduProjektas.md) (`level=4 UUID`: `pvproj._id`) | `4` | `open` | — | Projektas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/pvp.csv#L24 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L24)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/miskai/pvp (https://data.gov.lt/datasets/916/)
