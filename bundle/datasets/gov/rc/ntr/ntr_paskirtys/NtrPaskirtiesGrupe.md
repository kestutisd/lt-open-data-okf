---
type: Table
title: "NtrPaskirtiesGrupe — NTR paskirčių grupės"
description: "Spinta table datasets/gov/rc/ntr/ntr_paskirtys/NtrPaskirtiesGrupe (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_paskirtys/NtrPaskirtiesGrupe"
tags: [gov, rc, ntrpaskirtiesgrupe, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_paskirtys.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_paskirtys.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1897/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_paskirtys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NtrPaskirtiesGrupe — NTR paskirčių grupės

- **Model:** `datasets/gov/rc/ntr/ntr_paskirtys/NtrPaskirtiesGrupe`[^manifest]
- **Dataset:** [NTR paskirčių klasifikatoriai](../ntr_paskirtys.md) (`datasets/gov/rc/ntr/ntr_paskirtys`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_paskirtys.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_paskirtys.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_paskirtys/NtrPaskirtiesGrupe` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `pasg_grupe`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pasg_grupe` | `integer` | — | `4` | `open` | — | Paskirties grupė | — |
| `pasg_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `pasg_pav_i` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) | — |
| `pasg_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_paskirtys.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_paskirtys.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_paskirtys (https://data.gov.lt/datasets/1897/)
