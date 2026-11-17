---
type: Table
title: "NtrPaskirtiesGrupe — NTR paskirčių grupės"
description: "Spinta table datasets/gov/rc/ntr/ntr_paskirtys/NtrPaskirtiesGrupe (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_paskirtys/NtrPaskirtiesGrupe"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_paskirtys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_paskirtys.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# NtrPaskirtiesGrupe — NTR paskirčių grupės

- **Model:** `datasets/gov/rc/ntr/ntr_paskirtys/NtrPaskirtiesGrupe`[^manifest]
- **Dataset:** [NTR paskirčių klasifikatoriai](../ntr_paskirtys.md) (`datasets/gov/rc/ntr/ntr_paskirtys`)
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_paskirtys.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_paskirtys.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_paskirtys/NtrPaskirtiesGrupe`
- **Primary Key (`ref`):** `pasg_grupe`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pasg_grupe` | `integer` | — | `4` | `open` | — | Paskirties grupė | — |
| `pasg_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `pasg_pav_i` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) | — |
| `pasg_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_paskirtys.csv
