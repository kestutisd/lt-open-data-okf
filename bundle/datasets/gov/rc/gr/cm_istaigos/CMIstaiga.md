---
type: Table
title: "CMIstaiga — Gyventojų registro civilinės metrikacijos įstaigų klasifikatorius"
description: "Spinta table datasets/gov/rc/gr/cm_istaigos/CMIstaiga (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/gr/cm_istaigos/CMIstaiga"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/gr/cm_istaigos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/cm_istaigos.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# CMIstaiga — Gyventojų registro civilinės metrikacijos įstaigų klasifikatorius

- **Model:** `datasets/gov/rc/gr/cm_istaigos/CMIstaiga`[^manifest]
- **Dataset:** [Gyventojų registro civilinės metrikacijos įstaigų klasifikatorius](../cm_istaigos.md) (`datasets/gov/rc/gr/cm_istaigos`)
- **Manifest CSV:** [datasets/gov/rc/gr/cm_istaigos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/cm_istaigos.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/gr/cm_istaigos/CMIstaiga`
- **Primary Key (`ref`):** `kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tipo_kodas` | `string` | — | `4` | `open` | — | Įstaigos tipo kodas | — |
| `tipo_aprasymas` | `string` | — | `3` | `open` | — | Įstaigos tipo aprašymas | — |
| `kodas` | `string` | — | `4` | `open` | — | Įstaigos kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Įstaigos pavadinimas | — |
| `data_nuo` | `date` | `D` | `4` | `open` | — | Įstaigos galiojimo data nuo | — |
| `data_iki` | `date` | `D` | `4` | `open` | — | Įstaigos galiojimo data iki | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/gr/cm_istaigos.csv
