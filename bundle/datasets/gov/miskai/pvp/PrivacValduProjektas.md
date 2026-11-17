---
type: Table
title: "PrivacValduProjektas — Privačių miškų vidinės miškotvarkos projektas"
description: "Spinta table datasets/gov/miskai/pvp/PrivacValduProjektas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/pvp/PrivacValduProjektas"
tags: [gov, miskai, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/miskai/pvp.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# PrivacValduProjektas — Privačių miškų vidinės miškotvarkos projektas

- **Model:** `datasets/gov/miskai/pvp/PrivacValduProjektas`[^manifest]
- **Dataset:** [datasets/gov/miskai/pvp](../pvp.md) (`datasets/gov/miskai/pvp`)
- **Manifest CSV:** [datasets/gov/miskai/pvp.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/pvp/PrivacValduProjektas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `3` | `open` | — | Projekto numeris | — |
| `reg_nr` | `string` | — | `3` | `open` | — | Projekto registravimo numeris | — |
| `kaimas` | `string` | — | `3` | `open` | — | Valdos kaimas | — |
| `invent_atlikta` | `number` | — | `3` | `open` | — | Inventorizacijos metai | — |
| `autorius` | `ref` | [PVPAutorius](PVPAutorius.md) | `4` | `public` | — | Projekto autorius | — |
| `gal_nuo` | `number` | — | `3` | `open` | — | Projekto galiojimo pradžia | — |
| `gal_iki` | `number` | — | `3` | `open` | — | Projekto galiojimo pabaiga | — |
| `inventorizavo` | `string` | — | `3` | `public` | — | Inventorizavo | — |
| `pastabos` | `string` | — | `3` | `open` | — | Pastabos | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/pvp.csv
