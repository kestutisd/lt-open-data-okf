---
type: Table
title: "AdresoTaskas — Adresų registro žemės sklypams ir pastatams suteiktų adresų erdviniai duomenysAdresų registro žemės sklypams ir pastatams suteiktų adresų erdviniai duomenys"
description: "Žemės sklypams ir pastatams suteiktų adresų erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (žemės sklypams ir pastatams suteiktus adresus apibūdinantys duomenys (duomenų rinkinių grupė, 60 vnt.))."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/adresotaskas/AdresoTaskas"
tags: [gov, rc, adresotaskas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/adresotaskas.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/adresotaskas.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1351/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/adresotaskas"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# AdresoTaskas — Adresų registro žemės sklypams ir pastatams suteiktų adresų erdviniai duomenysAdresų registro žemės sklypams ir pastatams...

Žemės sklypams ir pastatams suteiktų adresų erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (žemės sklypams ir pastatams suteiktus adresus apibūdinantys duomenys (duomenų rinkinių grupė, 60 vnt.)). Duomenų geografinė imtis — visa šalies teritorija.[^manifest]

- **Model:** `datasets/gov/rc/ar/adresotaskas/AdresoTaskas`[^manifest]
- **Dataset:** [Adresų registras](../adresotaskas.md) (`datasets/gov/rc/ar/adresotaskas`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/adresotaskas.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/adresotaskas.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/adresotaskas/AdresoTaskas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `aob_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aob_kodas` | `integer` | — | `4` | `open` | — | Adreso kodas, unikalus Respublikos mastu (nuolat palaikomas) | — |
| `gyvenamoji_vietove` | `ref` | [GraGyvenamojiVietove](../gragyvenamojivietove/GraGyvenamojiVietove.md) (`level=4 UUID`: `gyvenamoji_vietove._id`) | `4` | `open` | — | Gyvenamosios vietovės kodas Registre (nekeičiamas gyvenamosios vietovės egzistavimo laiką) | — |
| `gatve` | `ref` | [GraGatve](../gragatve/GraGatve.md) (`level=4 UUID`: `gatve._id`) | `4` | `open` | — | Gatvės kodas Registre | — |
| `x_koord` | `number` | `m` | `4` | `open` | — | Adreso taško Y koordinatė LKS-94 koordinačių sistemoje | — |
| `y_koord` | `number` | `m` | `4` | `open` | — | Adreso taško X koordinatė LKS-94 koordinačių sistemoje | — |
| `lks` | `geometry(point, 3346)` | — | — | — | — | — | — |
| `aob_r` | `date` | `D` | `4` | `open` | — | Adreso taško įvedimo į Adresų registrą data | — |
| `aob_rk` | `date` | `D` | `4` | `open` | — | Adreso taško pakeitimo registre data | — |
| `aob_atr_ko` | `date` | `D` | `4` | `open` | — | Adreso taško geometrinių charakteristikų pakeitimo data | — |
| `pasto_koda` | `string` | — | `4` | `open` | — | Pašto kodas | — |
| `n_koord` | `number` | `m` | `4` | `open` | — | Adreso taško platuma WGS-84 koordinačių sistemoje | — |
| `e_koord` | `number` | `m` | `4` | `open` | — | Adreso taško ilguma WGS-84 koordinačių sistemoje | — |
| `wgs` | `geometry(point, 4326)` | — | — | — | — | — | — |
| `formavimo_data` | `date` | `D` | `4` | `open` | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/adresotaskas.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/adresotaskas.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/adresotaskas (https://data.gov.lt/datasets/1351/)
