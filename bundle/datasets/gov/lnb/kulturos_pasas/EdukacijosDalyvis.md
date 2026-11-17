---
type: Table
title: "EdukacijosDalyvis"
description: "Spinta table datasets/gov/lnb/kulturos_pasas/EdukacijosDalyvis (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lnb/kulturos_pasas/EdukacijosDalyvis"
tags: [gov, lnb, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lnb/kulturos_pasas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/kulturos_pasas.csv#L33"
    last_modified: "2026-11-11T14:39:20Z"
---

# EdukacijosDalyvis

- **Model:** `datasets/gov/lnb/kulturos_pasas/EdukacijosDalyvis`[^manifest]
- **Dataset:** [KEIS Kultūros paso edukacijos](../kulturos_pasas.md) (`datasets/gov/lnb/kulturos_pasas`)
- **Manifest CSV:** [datasets/gov/lnb/kulturos_pasas.csv#L33](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/kulturos_pasas.csv#L33)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lnb/kulturos_pasas/EdukacijosDalyvis`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `uzsakymo_id` | `string` | — | `4` | `open` | — | Užsakymo unikalus identitfikatorius | — |
| `dalyvio_id` | `string` | — | `4` | `open` | — | Užsakymo unikalus identitfikatorius | — |
| `dalyvio_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Dalyvio gimimo metai | — |
| `dalyvio_tipas` | `string` | — | `4` | `open` | — | Tipas | — |
| `dalyvio_institucijos_kodas` | `string` | — | `4` | `open` | — | Institucijos unikalus identifikatorius | — |
| `dalyvio_institucija` | `string` | — | `4` | `open` | — | Institucija | — |
| `dalyvio_savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lnb/kulturos_pasas.csv
