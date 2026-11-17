---
type: Table
title: "ByluRegistras — Varėnos globos namų 2023 metų gyventojų bylų registras"
description: "Varėnos globos namų gyventojų asmens bylų registracija"
resource: "https://get.data.gov.lt/datasets/gov/vgn/asmens_bylos/ByluRegistras"
tags: [gov, vgn, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vgn/asmens_bylos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgn/asmens_bylos.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# ByluRegistras — Varėnos globos namų 2023 metų gyventojų bylų registras

Varėnos globos namų gyventojų asmens bylų registracija

- **Model:** `datasets/gov/vgn/asmens_bylos/ByluRegistras`[^manifest]
- **Dataset:** [Varėnos globos namų 2023 metų gyventojų bylų registras](../asmens_bylos.md) (`datasets/gov/vgn/asmens_bylos`)
- **Manifest CSV:** [datasets/gov/vgn/asmens_bylos.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgn/asmens_bylos.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vgn/asmens_bylos/ByluRegistras`
- **Primary Key (`ref`):** `bylos_nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `bylos_nr` | `string` | — | `4` | `open` | — | Globos namų gyventojo asmens bylos numeris | — |
| `asmuo` | `string` | — | `4` | `open` | — | Globos namų gyventojo vardas ir pavardė | — |
| `byla_pradeta` | `date` | `D` | `4` | `open` | — | Data, nuo kada asmuo pradėjo gyventi globos namuose | — |
| `byla_pabaigta` | `date` | `D` | `4` | `open` | — | Data, iki kada asmuo gyveno globos namuose | — |
| `pastabos` | `string` | — | `2` | `open` | — | Pažymima priežastis, dėl kurios asmuo nebegyvena (mirė ar išsikraustė į kitus namus, pasiėmė artimieji, liga) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vgn/asmens_bylos.csv
