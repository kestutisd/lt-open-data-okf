---
type: Table
title: "GraGatve — Adresų registro gatvių ašinių linijų erdviniai duomenys"
description: "Gatvių ašinių linijų erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (gatvių ašinių linijas apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/gragatve/GraGatve"
tags: [gov, rc, gragatve, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gragatve.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/gragatve.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1349/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/gragatve"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# GraGatve — Adresų registro gatvių ašinių linijų erdviniai duomenys

Gatvių ašinių linijų erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (gatvių ašinių linijas apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.[^manifest]

- **Model:** `datasets/gov/rc/ar/gragatve/GraGatve`[^manifest]
- **Dataset:** [Adresų registras](../gragatve.md) (`datasets/gov/rc/ar/gragatve`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/gragatve.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gragatve.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/gragatve/GraGatve` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `gat_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gat_kodas` | `integer` | — | `4` | `open` | — | Gatvės kodas Registre | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Sutrumpintas gatvės vardas su tipu (nuolat palaikomas) | — |
| `gat_r` | `date` | `D` | `4` | `open` | — | Gatvės ašinės linijos įvedimo į Adresų registrą data | — |
| `gat_ilgis` | `number` | `m` | `4` | `open` | — | Gatvės ilgis metrais | — |
| `gyvenamoji_vietove` | `ref` | [GraGyvenamojiVietove](../gragyvenamojivietove/GraGyvenamojiVietove.md) (`level=4 UUID`: `gyvenamoji_vietove._id`) | `4` | `open` | — | Gyvenamosios vietovės, į kurią patenka gatvė, išorinis kodas | — |
| `formavimo_data` | `date` | `D` | `4` | `open` | — | Duomenų formavimo data | — |
| `gatves` | `geometry(3346)` | `m` | `4` | `open` | — | Gatvės ašinė linija su pradžia, pabaiga ir posūkio taškai | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/gragatve.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gragatve.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/gragatve (https://data.gov.lt/datasets/1349/)
