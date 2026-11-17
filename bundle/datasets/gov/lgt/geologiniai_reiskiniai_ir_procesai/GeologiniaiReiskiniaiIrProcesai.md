---
type: Table
title: "GeologiniaiReiskiniaiIrProcesai — Geologiniai reiškiniai ir procesai"
description: "Spinta table datasets/gov/lgt/geologiniai_reiskiniai_ir_procesai/GeologiniaiReiskiniaiIrProcesai (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/geologiniai_reiskiniai_ir_procesai/GeologiniaiReiskiniaiIrProcesai"
tags: [gov, lgt, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lgt/geo_reiskiniai_procesai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geo_reiskiniai_procesai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# GeologiniaiReiskiniaiIrProcesai — Geologiniai reiškiniai ir procesai

- **Model:** `datasets/gov/lgt/geologiniai_reiskiniai_ir_procesai/GeologiniaiReiskiniaiIrProcesai`[^manifest]
- **Dataset:** [Geologiniai reiškiniai ir procesai](../geologiniai_reiskiniai_ir_procesai.md) (`datasets/gov/lgt/geologiniai_reiskiniai_ir_procesai`)
- **Manifest CSV:** [datasets/gov/lgt/geo_reiskiniai_procesai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geo_reiskiniai_procesai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/geologiniai_reiskiniai_ir_procesai/GeologiniaiReiskiniaiIrProcesai`
- **Level:** `2`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_data` | `date` | `D` | `4` | `open` | — | Įrašo data | — |
| `ivykio_data` | `date` | `D` | `4` | `open` | — | Įvykio data | — |
| `tipas` | `string` | — | `3` | `open` | — | Tipas | — |
| `koord` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Taškas | — |
| `pavadinimas` | `string` | — | `2` | `open` | — | Geologinio reiškinio pavadinimas | — |
| `adresas` | `string` | — | `2` | `open` | — | Adresas | — |
| `aprasas` | `string` | — | `2` | `open` | — | Geologinio reiškinio aprašas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pavadinimas` | `update(property: "pavadinimas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `aprasas` | `update(property: "aprasas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/geo_reiskiniai_procesai.csv
