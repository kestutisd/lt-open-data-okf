---
type: Table
title: "NtrObjektoStatusas — NTR objektų statusų klasifikatorius"
description: "Spinta table datasets/gov/rc/ntr/ntr_objektai/NtrObjektoStatusas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_objektai/NtrObjektoStatusas"
tags: [gov, rc, ntrobjektostatusas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L45"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_objektai.csv#L45"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1895/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_objektai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NtrObjektoStatusas — NTR objektų statusų klasifikatorius

- **Model:** `datasets/gov/rc/ntr/ntr_objektai/NtrObjektoStatusas`[^manifest]
- **Dataset:** [NTR objektus apibūdinantys klasifikatoriai](../ntr_objektai.md) (`datasets/gov/rc/ntr/ntr_objektai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_objektai.csv#L45](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L45)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_objektai/NtrObjektoStatusas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `osta_statusas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `osta_statusas` | `integer` | — | `4` | `open` | — | Turto objekto statusas | — |
| `osta_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `osta_pav_i` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) | — |
| `osta_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |
| `osta_pav_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai | — |
| `osta_pav_i_en` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) angliškai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_objektai.csv#L45 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L45)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_objektai (https://data.gov.lt/datasets/1895/)
