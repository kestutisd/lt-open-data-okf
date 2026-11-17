---
type: Table
title: "GyvenamojiVietove — Adresų registro gyvenamųjų vietovių tekstinių duomenų rinkinys"
description: "Gyvenamųjų vietovių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - gyvenamąsias vietoves apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/gyvenamojivietove/GyvenamojiVietove"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/gyvenamojivietove.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gyvenamojivietove.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# GyvenamojiVietove — Adresų registro gyvenamųjų vietovių tekstinių duomenų rinkinys

Gyvenamųjų vietovių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - gyvenamąsias vietoves apibūdinantys duomenys).

- **Model:** `datasets/gov/rc/ar/gyvenamojivietove/GyvenamojiVietove`[^manifest]
- **Dataset:** [Adresų registras](../gyvenamojivietove.md) (`datasets/gov/rc/ar/gyvenamojivietove`)
- **Manifest CSV:** [datasets/gov/rc/ar/gyvenamojivietove.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gyvenamojivietove.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/gyvenamojivietove/GyvenamojiVietove`
- **Primary Key (`ref`):** `gyv_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gyv_kodas` | `integer` | — | `4` | `open` | — | Gyvenamosios vietovės identifikavimo kodas | — |
| `tipas` | `string` | — | `3` | `open` | — | Gyvenamosios vietovės tipas (miestas, miestelis, kaimas, viensėdis ir pan.) | — |
| `tipo_santrumpa` | `string` | — | `3` | `open` | — | Gyvenamosios vietovės tipo trumpinys | — |
| `pavadinimas_k` | `string` | — | `3` | `open` | — | Gyvenamosios vietovės pavadinimas (kilmininko linksnyje) | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Gyvenamosios vietovės pavadinimas (vardininko linksnyje) | — |
| `seniunija` | `ref` | [/datasets/gov/rc/ar/seniunija/Seniunija](../seniunija/Seniunija.md) | `4` | `open` | — | Seniūnijos, kurios teritorijoje yra gyvenamoji vietovė, identifikavimo kodas | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės, kurios teritorijoje yra gyvenamoji vietovė, identifikavimo kodas | — |
| `gyv_nuo` | `date` | `D` | `4` | `open` | — | Objekto įregistravimo data | — |
| `gyv_iki` | `date` | `D` | `4` | `open` | — | Objekto išregistravimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/gyvenamojivietove.csv
