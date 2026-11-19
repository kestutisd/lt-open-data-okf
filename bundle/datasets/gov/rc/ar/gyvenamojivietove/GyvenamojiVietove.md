---
type: Table
title: "GyvenamojiVietove — Adresų registro gyvenamųjų vietovių tekstinių duomenų rinkinys"
description: "Gyvenamųjų vietovių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - gyvenamąsias vietoves apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/gyvenamojivietove/GyvenamojiVietove"
tags: [gov, rc, gyvenamojivietove, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gyvenamojivietove.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/gyvenamojivietove.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1287/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/gyvenamojivietove"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# GyvenamojiVietove — Adresų registro gyvenamųjų vietovių tekstinių duomenų rinkinys

Gyvenamųjų vietovių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - gyvenamąsias vietoves apibūdinantys duomenys).[^manifest]

- **Model:** `datasets/gov/rc/ar/gyvenamojivietove/GyvenamojiVietove`[^manifest]
- **Dataset:** [Adresų registras](../gyvenamojivietove.md) (`datasets/gov/rc/ar/gyvenamojivietove`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/gyvenamojivietove.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gyvenamojivietove.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/gyvenamojivietove/GyvenamojiVietove` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `gyv_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gyv_kodas` | `integer` | — | `4` | `open` | — | Gyvenamosios vietovės identifikavimo kodas | — |
| `tipas` | `string` | — | `3` | `open` | — | Gyvenamosios vietovės tipas (miestas, miestelis, kaimas, viensėdis ir pan.) | — |
| `tipo_santrumpa` | `string` | — | `3` | `open` | — | Gyvenamosios vietovės tipo trumpinys | — |
| `pavadinimas_k` | `string` | — | `3` | `open` | — | Gyvenamosios vietovės pavadinimas (kilmininko linksnyje) | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Gyvenamosios vietovės pavadinimas (vardininko linksnyje) | — |
| `seniunija` | `ref` | [Seniunija](../seniunija/Seniunija.md) (`level=4 UUID`: `seniunija._id`) | `4` | `open` | — | Seniūnijos, kurios teritorijoje yra gyvenamoji vietovė, identifikavimo kodas | — |
| `savivaldybe` | `ref` | [Savivaldybe](../savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybės, kurios teritorijoje yra gyvenamoji vietovė, identifikavimo kodas | — |
| `gyv_nuo` | `date` | `D` | `4` | `open` | — | Objekto įregistravimo data | — |
| `gyv_iki` | `date` | `D` | `4` | `open` | — | Objekto išregistravimo data | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/gyvenamojivietove.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gyvenamojivietove.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/gyvenamojivietove (https://data.gov.lt/datasets/1287/)
