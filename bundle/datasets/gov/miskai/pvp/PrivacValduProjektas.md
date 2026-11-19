---
type: Table
title: "PrivacValduProjektas — Privačių miškų vidinės miškotvarkos projektas"
description: "Spinta table datasets/gov/miskai/pvp/PrivacValduProjektas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/pvp/PrivacValduProjektas"
tags: [gov, miskai, privacvalduprojektas, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/miskai/pvp.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/916/"
    title: "data.gov.lt DCAT-AP — datasets/gov/miskai/pvp"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PrivacValduProjektas — Privačių miškų vidinės miškotvarkos projektas

- **Model:** `datasets/gov/miskai/pvp/PrivacValduProjektas`[^manifest]
- **Dataset:** [Privačių vidinės miškotvarkos projektų rengėjų sąrašas](../pvp.md) (`datasets/gov/miskai/pvp`)[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/pvp.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/pvp/PrivacValduProjektas` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `3` | `open` | — | Projekto numeris | — |
| `reg_nr` | `string` | — | `3` | `open` | — | Projekto registravimo numeris | — |
| `kaimas` | `string` | — | `3` | `open` | — | Valdos kaimas | — |
| `invent_atlikta` | `number` | — | `3` | `open` | — | Inventorizacijos metai | — |
| `autorius` | `ref` | [PVPAutorius](PVPAutorius.md) (`level=4 UUID`: `autorius._id`) | `4` | `public` | — | Projekto autorius | — |
| `gal_nuo` | `number` | — | `3` | `open` | — | Projekto galiojimo pradžia | — |
| `gal_iki` | `number` | — | `3` | `open` | — | Projekto galiojimo pabaiga | — |
| `inventorizavo` | `string` | — | `3` | `public` | — | Inventorizavo | — |
| `pastabos` | `string` | — | `3` | `open` | — | Pastabos | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/pvp.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/miskai/pvp (https://data.gov.lt/datasets/916/)
