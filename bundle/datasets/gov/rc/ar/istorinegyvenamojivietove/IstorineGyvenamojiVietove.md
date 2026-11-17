---
type: Table
title: "IstorineGyvenamojiVietove — Adresų registro istorinių gatvių tekstinių duomenų rinkinys"
description: "Istorinių (panaikintų) gyvenamųjų vietovių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - istorines gyvenamąsias vietoves apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/istorinegyvenamojivietove/IstorineGyvenamojiVietove"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/istorinegyvenamojivietove.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/istorinegyvenamojivietove.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# IstorineGyvenamojiVietove — Adresų registro istorinių gatvių tekstinių duomenų rinkinys

Istorinių (panaikintų) gyvenamųjų vietovių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - istorines gyvenamąsias vietoves apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.

- **Model:** `datasets/gov/rc/ar/istorinegyvenamojivietove/IstorineGyvenamojiVietove`[^manifest]
- **Dataset:** [Adresų registras](../istorinegyvenamojivietove.md) (`datasets/gov/rc/ar/istorinegyvenamojivietove`)
- **Manifest CSV:** [datasets/gov/rc/ar/istorinegyvenamojivietove.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/istorinegyvenamojivietove.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/istorinegyvenamojivietove/IstorineGyvenamojiVietove`
- **Primary Key (`ref`):** `gyv_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gyv_kodas` | `integer` | — | `4` | `open` | — | Gyvenamosios vietovės identifikavimo kodas | — |
| `tipas` | `string` | — | `3` | `open` | — | Gyvenamosios vietovės tipas (miestas, miestelis, kaimas, viensėdis ir pan.) | — |
| `tipo_santrumpa` | `string` | — | `3` | `open` | — | Gyvenamosios vietovės tipo trumpinys | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Gyvenamosios vietovės pavadinimas (vardininko linksnyje) | — |
| `sen_kodas` | `integer` | — | `2` | `open` | — | Seniūnijos, kurios teritorijoje yra gyvenamoji vietovė, kodas | — |
| `sen_pavadinimas` | `string` | — | `2` | `open` | — | Seniūnijos, kurios teritorijoje yra gyvenamoji vietovė, pavadinimas | — |
| `sav_kodas` | `integer` | — | `2` | `open` | — | Savivaldybės, kurios teritorijoje yra gyvenamoji vietovė, kodas | — |
| `sav_pavadinimas` | `string` | — | `2` | `open` | — | Savivaldybės, kurios teritorijoje yra gyvenamoji vietovė, pavadinimas | — |
| `gyv_nuo` | `date` | `D` | `4` | `open` | — | Objekto įregistravimo data | — |
| `gyv_iki` | `date` | `D` | `4` | `open` | — | Objekto išregistravimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/istorinegyvenamojivietove.csv
