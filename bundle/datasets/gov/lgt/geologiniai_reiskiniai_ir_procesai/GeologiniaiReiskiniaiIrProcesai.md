---
type: Table
title: "GeologiniaiReiskiniaiIrProcesai — Geologiniai reiškiniai ir procesai"
description: "Spinta table datasets/gov/lgt/geologiniai_reiskiniai_ir_procesai/GeologiniaiReiskiniaiIrProcesai (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/geologiniai_reiskiniai_ir_procesai/GeologiniaiReiskiniaiIrProcesai"
tags: [gov, lgt, geologiniaireiskiniaiirprocesai, deployed, level-2, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geo_reiskiniai_procesai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/lgt/geo_reiskiniai_procesai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1324/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lgt/geologiniai_reiskiniai_ir_procesai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# GeologiniaiReiskiniaiIrProcesai — Geologiniai reiškiniai ir procesai

- **Model:** `datasets/gov/lgt/geologiniai_reiskiniai_ir_procesai/GeologiniaiReiskiniaiIrProcesai`[^manifest]
- **Dataset:** [Geologiniai reiškiniai ir procesai](../geologiniai_reiskiniai_ir_procesai.md) (`datasets/gov/lgt/geologiniai_reiskiniai_ir_procesai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lgt/geo_reiskiniai_procesai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geo_reiskiniai_procesai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/geologiniai_reiskiniai_ir_procesai/GeologiniaiReiskiniaiIrProcesai` (`deployed`)[^manifest]
- **Provider:** `lgt` — Lietuvos geologijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/geo_reiskiniai_procesai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geo_reiskiniai_procesai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lgt/geologiniai_reiskiniai_ir_procesai (https://data.gov.lt/datasets/1324/)
