---
type: Table
title: "ByluRegistras — Varėnos globos namų 2023 metų gyventojų bylų registras"
description: "Varėnos globos namų gyventojų asmens bylų registracija"
resource: "https://get.data.gov.lt/datasets/gov/vgn/asmens_bylos/ByluRegistras"
tags: [gov, vgn, byluregistras, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgn/asmens_bylos.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/vgn/asmens_bylos.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2751/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vgn/asmens_bylos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ByluRegistras — Varėnos globos namų 2023 metų gyventojų bylų registras

Varėnos globos namų gyventojų asmens bylų registracija[^manifest]

- **Model:** `datasets/gov/vgn/asmens_bylos/ByluRegistras`[^manifest]
- **Dataset:** [Varėnos globos namų 2023 metų gyventojų bylų registras](../asmens_bylos.md) (`datasets/gov/vgn/asmens_bylos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vgn/asmens_bylos.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgn/asmens_bylos.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vgn/asmens_bylos/ByluRegistras` (`deployed`)[^manifest]
- **Provider:** `vgn` — Varėnos globos namai *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `bylos_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `bylos_nr` | `string` | — | `4` | `open` | — | Globos namų gyventojo asmens bylos numeris | — |
| `asmuo` | `string` | — | `4` | `open` | — | Globos namų gyventojo vardas ir pavardė | — |
| `byla_pradeta` | `date` | `D` | `4` | `open` | — | Data, nuo kada asmuo pradėjo gyventi globos namuose | — |
| `byla_pabaigta` | `date` | `D` | `4` | `open` | — | Data, iki kada asmuo gyveno globos namuose | — |
| `pastabos` | `string` | — | `2` | `open` | — | Pažymima priežastis, dėl kurios asmuo nebegyvena (mirė ar išsikraustė į kitus namus, pasiėmė artimieji, liga) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vgn/asmens_bylos.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgn/asmens_bylos.csv#L8)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vgn/asmens_bylos (https://data.gov.lt/datasets/2751/)
