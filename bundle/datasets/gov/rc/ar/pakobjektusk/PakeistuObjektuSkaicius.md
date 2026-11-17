---
type: Table
title: "PakeistuObjektuSkaicius — Pakeistų Adresų registro objektų skaičius per mėnesį"
description: "Spinta table datasets/gov/rc/ar/pakobjektusk/PakeistuObjektuSkaicius (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/pakobjektusk/PakeistuObjektuSkaicius"
tags: [gov, rc, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/pakeistu_objektu_skaicius.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/pakeistu_objektu_skaicius.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# PakeistuObjektuSkaicius — Pakeistų Adresų registro objektų skaičius per mėnesį

- **Model:** `datasets/gov/rc/ar/pakobjektusk/PakeistuObjektuSkaicius`[^manifest]
- **Dataset:** [Pakeistų Adresų registro objektų skaičius per mėnesį](../pakobjektusk.md) (`datasets/gov/rc/ar/pakobjektusk`)
- **Manifest CSV:** [datasets/gov/rc/ar/pakeistu_objektu_skaicius.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/pakeistu_objektu_skaicius.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/pakobjektusk/PakeistuObjektuSkaicius`
- **Primary Key (`ref`):** `savivaldybe, metai, menuo`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `apskritis` | `ref` | [/datasets/gov/rc/ar/apskritis/Apskritis](../apskritis/Apskritis.md) | `4` | `open` | — | Apskrities kodas | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės kodas | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `menuo` | `integer` | — | `2` | `open` | — | Mėnuo | — |
| `patalpos_k` | `integer` | `U` | `4` | `open` | — | Pakeistų patalpų sk. | — |
| `adresai_k` | `integer` | `U` | `4` | `open` | — | Pakeistų adresų taškų sk. | — |
| `gatves_k` | `integer` | `U` | `4` | `open` | — | Pakeistų gatvių sk. | — |
| `gyv_vietoves_k` | `integer` | `U` | `4` | `open` | — | Pakeistų gyvenamųjų vietovių sk. | — |
| `seniunijos_k` | `integer` | `U` | `4` | `open` | — | Pakeistų seniūnijų sk. | — |
| `pavadinimai_k` | `integer` | `U` | `4` | `open` | — | Pakeistų pavadinimų sk. | — |
| `viso` | `integer` | `U` | `4` | `open` | — | Pakeistų objektų sk., iš viso | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/pakeistu_objektu_skaicius.csv
