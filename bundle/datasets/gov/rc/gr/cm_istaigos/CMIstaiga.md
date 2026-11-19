---
type: Table
title: "CMIstaiga — Gyventojų registro civilinės metrikacijos įstaigų klasifikatorius"
description: "Spinta table datasets/gov/rc/gr/cm_istaigos/CMIstaiga (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/gr/cm_istaigos/CMIstaiga"
tags: [gov, rc, cmistaiga, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/cm_istaigos.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/gr/cm_istaigos.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1769/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/gr/cm_istaigos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# CMIstaiga — Gyventojų registro civilinės metrikacijos įstaigų klasifikatorius

- **Model:** `datasets/gov/rc/gr/cm_istaigos/CMIstaiga`[^manifest]
- **Dataset:** [Gyventojų registro civilinės metrikacijos įstaigų klasifikatorius](../cm_istaigos.md) (`datasets/gov/rc/gr/cm_istaigos`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/gr/cm_istaigos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/cm_istaigos.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/gr/cm_istaigos/CMIstaiga` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tipo_kodas` | `string` | — | `4` | `open` | — | Įstaigos tipo kodas | — |
| `tipo_aprasymas` | `string` | — | `3` | `open` | — | Įstaigos tipo aprašymas | — |
| `kodas` | `string` | — | `4` | `open` | — | Įstaigos kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Įstaigos pavadinimas | — |
| `data_nuo` | `date` | `D` | `4` | `open` | — | Įstaigos galiojimo data nuo | — |
| `data_iki` | `date` | `D` | `4` | `open` | — | Įstaigos galiojimo data iki | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/gr/cm_istaigos.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/cm_istaigos.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/gr/cm_istaigos (https://data.gov.lt/datasets/1769/)
