---
type: Table
title: "IsregistruotuObjektuSkaicius — Išregistruotų Adresų registro objektų skaičius per mėnesį"
description: "Spinta table datasets/gov/rc/ar/isregobjektusk/IsregistruotuObjektuSkaicius (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/isregobjektusk/IsregistruotuObjektuSkaicius"
tags: [gov, rc, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/isregistruotu_objektu_skaicius.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/isregistruotu_objektu_skaicius.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# IsregistruotuObjektuSkaicius — Išregistruotų Adresų registro objektų skaičius per mėnesį

- **Model:** `datasets/gov/rc/ar/isregobjektusk/IsregistruotuObjektuSkaicius`[^manifest]
- **Dataset:** [Išregistruotų Adresų registro objektų skaičius per mėnesį](../isregobjektusk.md) (`datasets/gov/rc/ar/isregobjektusk`)
- **Manifest CSV:** [datasets/gov/rc/ar/isregistruotu_objektu_skaicius.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/isregistruotu_objektu_skaicius.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/isregobjektusk/IsregistruotuObjektuSkaicius`
- **Primary Key (`ref`):** `savivaldybe, metai, menuo`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `apskritis` | `ref` | [/datasets/gov/rc/ar/apskritis/Apskritis](../apskritis/Apskritis.md) | `4` | `open` | — | Apskrities kodas | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės kodas | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `menuo` | `integer` | — | `2` | `open` | — | Mėnuo | — |
| `patalpos_i` | `integer` | `U` | `4` | `open` | — | Išregistruotų patalpų sk. | — |
| `adresai_i` | `integer` | `U` | `4` | `open` | — | Išregistruotų adresų taškų sk. | — |
| `gatves_i` | `integer` | `U` | `4` | `open` | — | Išregistruotų gatvių sk. | — |
| `gyv_vietoves_i` | `integer` | `U` | `4` | `open` | — | Išregistruotų gyvenamųjų vietovių sk. | — |
| `seniunijos_i` | `integer` | `U` | `4` | `open` | — | Išregistruotų seniūnijų sk. | — |
| `pavadinimai_i` | `integer` | `U` | `4` | `open` | — | Išregistruotų pavadinimų sk. | — |
| `viso_i` | `integer` | `U` | `4` | `open` | — | Išregistruotų objektų sk., iš viso | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/isregistruotu_objektu_skaicius.csv
