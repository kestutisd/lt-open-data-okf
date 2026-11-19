---
type: Table
title: "NtrLeistinaPaskirtis — NTR leistinos paskirtys pagal objekto tipus"
description: "Spinta table datasets/gov/rc/ntr/ntr_paskirtys/NtrLeistinaPaskirtis (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_paskirtys/NtrLeistinaPaskirtis"
tags: [gov, rc, ntrleistinapaskirtis, deployed, level-3, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_paskirtys.csv#L17"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_paskirtys.csv#L17"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1897/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_paskirtys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NtrLeistinaPaskirtis — NTR leistinos paskirtys pagal objekto tipus

- **Model:** `datasets/gov/rc/ntr/ntr_paskirtys/NtrLeistinaPaskirtis`[^manifest]
- **Dataset:** [NTR paskirčių klasifikatoriai](../ntr_paskirtys.md) (`datasets/gov/rc/ntr/ntr_paskirtys`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_paskirtys.csv#L17](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_paskirtys.csv#L17)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_paskirtys/NtrLeistinaPaskirtis` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `obje_tipas`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `obje_tipas` | `integer` | — | `3` | `open` | — | Turto objekto tipas | — |
| `pask_tipas` | `ref` | [NtrPaskirtiesTipas](NtrPaskirtiesTipas.md) (`level=4 UUID`: `pask_tipas._id`) | `4` | `open` | — | Turto paskirties tipas | — |
| `lpas_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_paskirtys.csv#L17 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_paskirtys.csv#L17)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_paskirtys (https://data.gov.lt/datasets/1897/)
