---
type: Table
title: "PVPAutorius — PVP autorius"
description: "Informacija apie privačių miškų vidinės miškotvarkos projektų autorius"
resource: "https://get.data.gov.lt/datasets/gov/miskai/vmp/PVPAutorius"
tags: [gov, miskai, pvpautorius, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/vmp.csv#L16"
    title: "atviriduomenys/manifest — datasets/gov/miskai/vmp.csv#L16"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/916/"
    title: "data.gov.lt DCAT-AP — datasets/gov/miskai/vmp"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PVPAutorius — PVP autorius

Informacija apie privačių miškų vidinės miškotvarkos projektų autorius[^manifest]

- **Model:** `datasets/gov/miskai/vmp/PVPAutorius`[^manifest]
- **Dataset:** [Privačių vidinės miškotvarkos projektų rengėjų sąrašas](../vmp.md) (`datasets/gov/miskai/vmp`)[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/vmp.csv#L16](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/vmp.csv#L16)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/vmp/PVPAutorius` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aut_vard` | `string` | — | `3` | `public` | — | Privačių miškų vidinės miškotvarkos projektų autoriaus vardas pavardė | — |
| `telefonas` | `string` | — | `3` | `public` | — | Privačių miškų vidinės miškotvarkos projektų autoriaus telefono nr. | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/vmp.csv#L16 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/vmp.csv#L16)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/miskai/vmp (https://data.gov.lt/datasets/916/)
