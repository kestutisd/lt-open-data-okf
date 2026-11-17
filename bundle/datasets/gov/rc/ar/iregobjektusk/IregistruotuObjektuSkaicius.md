---
type: Table
title: "IregistruotuObjektuSkaicius — Naujai įregistruotų Adresų registro objektų skaičius per mėnesį"
description: "Spinta table datasets/gov/rc/ar/iregobjektusk/IregistruotuObjektuSkaicius (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/iregobjektusk/IregistruotuObjektuSkaicius"
tags: [gov, rc, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/iregistruotu_objektu_skaicius.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/iregistruotu_objektu_skaicius.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# IregistruotuObjektuSkaicius — Naujai įregistruotų Adresų registro objektų skaičius per mėnesį

- **Model:** `datasets/gov/rc/ar/iregobjektusk/IregistruotuObjektuSkaicius`[^manifest]
- **Dataset:** [Naujai įregistruotų Adresų registro objektų skaičius per mėnesį](../iregobjektusk.md) (`datasets/gov/rc/ar/iregobjektusk`)
- **Manifest CSV:** [datasets/gov/rc/ar/iregistruotu_objektu_skaicius.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/iregistruotu_objektu_skaicius.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/iregobjektusk/IregistruotuObjektuSkaicius`
- **Primary Key (`ref`):** `savivaldybe, metai, menuo`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `apskritis` | `ref` | [/datasets/gov/rc/ar/apskritis/Apskritis](../apskritis/Apskritis.md) | `4` | `open` | — | Apskrities kodas | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės kodas | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `menuo` | `integer` | — | `2` | `open` | — | Mėnuo | — |
| `patalpos_n` | `integer` | — | `4` | `open` | — | Naujai įregistruotų patalpų sk. | — |
| `adresai_n` | `integer` | `U` | `4` | `open` | — | Naujai įregistruotų adresų taškų sk. | — |
| `gatves_n` | `integer` | `U` | `4` | `open` | — | Naujai įregistruotų gatvių sk. | — |
| `gyv_vietoves_n` | `integer` | `U` | `4` | `open` | — | Naujai įregistruotų gyvenamųjų vietovių sk. | — |
| `seniunijos_n` | `integer` | `U` | `4` | `open` | — | Naujai įregistruotų seniūnijų sk. | — |
| `pavadinimai_n` | `integer` | `U` | `4` | `open` | — | Naujai įregistruotų pavadinimų sk. | — |
| `viso` | `integer` | `U` | `4` | `open` | — | Naujai įregistruotų objektų sk., iš viso | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/iregistruotu_objektu_skaicius.csv
