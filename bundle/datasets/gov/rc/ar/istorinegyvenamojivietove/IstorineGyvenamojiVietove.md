---
type: Table
title: "IstorineGyvenamojiVietove — Adresų registro istorinių gatvių tekstinių duomenų rinkinys"
description: "Istorinių (panaikintų) gyvenamųjų vietovių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - istorines gyvenamąsias vietoves apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/istorinegyvenamojivietove/IstorineGyvenamojiVietove"
tags: [gov, rc, istorinegyvenamojivietove, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/istorinegyvenamojivietove.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/istorinegyvenamojivietove.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# IstorineGyvenamojiVietove — Adresų registro istorinių gatvių tekstinių duomenų rinkinys

Istorinių (panaikintų) gyvenamųjų vietovių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - istorines gyvenamąsias vietoves apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.[^manifest]

- **Model:** `datasets/gov/rc/ar/istorinegyvenamojivietove/IstorineGyvenamojiVietove`[^manifest]
- **Dataset:** [Adresų registras](../istorinegyvenamojivietove.md) (`datasets/gov/rc/ar/istorinegyvenamojivietove`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/istorinegyvenamojivietove.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/istorinegyvenamojivietove.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/istorinegyvenamojivietove/IstorineGyvenamojiVietove` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `gyv_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/istorinegyvenamojivietove.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/istorinegyvenamojivietove.csv#L3)
