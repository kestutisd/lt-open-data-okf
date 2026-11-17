---
type: Table
title: "PrivacValduProjektas — Privačių valdų projektas"
description: "Informacija apie projektą, kurį parengė PVP autorius"
resource: "https://get.data.gov.lt/datasets/gov/miskai/vmp/PrivacValduProjektas"
tags: [gov, miskai, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/miskai/vmp.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/vmp.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# PrivacValduProjektas — Privačių valdų projektas

Informacija apie projektą, kurį parengė PVP autorius

- **Model:** `datasets/gov/miskai/vmp/PrivacValduProjektas`[^manifest]
- **Dataset:** [datasets/gov/miskai/vmp](../vmp.md) (`datasets/gov/miskai/vmp`)
- **Manifest CSV:** [datasets/gov/miskai/vmp.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/vmp.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/vmp/PrivacValduProjektas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `3` | `open` | — | Projekto numeris | — |
| `data` | `number` | — | `3` | `open` | — | Projekto data | — |
| `invent_atlikta` | `number` | — | `3` | `open` | — | Inventorizacijos metai | — |
| `autorius` | `ref` | [PVPAutorius](PVPAutorius.md) | `4` | `public` | — | Projekto autorius | — |
| `gal_nuo` | `number` | — | `3` | `open` | — | Projekto galiojimo pradžia | — |
| `gal_iki` | `number` | — | `3` | `open` | — | Projekto galiojimo pabaiga | — |
| `inventorizavo` | `string` | — | `3` | `public` | — | Inventorizavo | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/vmp.csv
