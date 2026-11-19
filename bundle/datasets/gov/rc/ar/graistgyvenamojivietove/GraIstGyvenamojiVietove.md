---
type: Table
title: "GraIstGyvenamojiVietove — Adresų registro gyvenamųjų vietovių erdviniai duomenys"
description: "Gyvenamųjų vietovių erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus – gyvenamąsias vietoves apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/graistgyvenamojivietove/GraIstGyvenamojiVietove"
tags: [gov, rc, graistgyvenamojivietove, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/graistgyvenamojivietove.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/graistgyvenamojivietove.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# GraIstGyvenamojiVietove — Adresų registro gyvenamųjų vietovių erdviniai duomenys

Gyvenamųjų vietovių erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus – gyvenamąsias vietoves apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.[^manifest]

- **Model:** `datasets/gov/rc/ar/graistgyvenamojivietove/GraIstGyvenamojiVietove`[^manifest]
- **Dataset:** [Adresų registras](../graistgyvenamojivietove.md) (`datasets/gov/rc/ar/graistgyvenamojivietove`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/graistgyvenamojivietove.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/graistgyvenamojivietove.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/graistgyvenamojivietove/GraIstGyvenamojiVietove` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `gyv_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gyv_kodas` | `integer` | — | `4` | `open` | — | Gyvenamosios vietovės kodas Registre (nekeičiamas gyvenamosios vietovės egzistavimo laiką) | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Gyvenamosios vietovės vardas su sutrumpintu tipu | — |
| `plotas` | `number` | `ha` | `4` | `open` | — | Gyvenamosios vietovės grafinis plotas (ha) | — |
| `gyv_r` | `date` | `D` | `4` | `open` | — | Gyvenamosios vietovės įrašymo į Adresų registrą data | — |
| `gyv_p` | `date` | `D` | `4` | `open` | — | Istorinės gyvenamosios vietovės pakeitimo data | — |
| `savivaldybe` | `ref` | [GraSavivaldybe](../grasavivaldybe/GraSavivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybės į kurią patenka gyvenamosios vietovės teritorija, išorinis kodas | — |
| `formavimo_data` | `date` | `D` | `4` | `open` | — | Duomenų formavimo data | — |
| `ist_gyv_vietoves` | `geometry(3346)` | `m` | `4` | `open` | — | Gyvenamųjų vietovių ribos | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/graistgyvenamojivietove.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/graistgyvenamojivietove.csv#L3)
