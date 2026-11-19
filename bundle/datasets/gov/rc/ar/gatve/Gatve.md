---
type: Table
title: "Gatve — Adresų registro gatvių tekstinių duomenų rinkinys"
description: "Gatvių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos gatves apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/gatve/Gatve"
tags: [gov, rc, gatve, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gatve.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/gatve.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1293/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/gatve"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Gatve — Adresų registro gatvių tekstinių duomenų rinkinys

Gatvių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos gatves apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.[^manifest]

- **Model:** `datasets/gov/rc/ar/gatve/Gatve`[^manifest]
- **Dataset:** [Adresų registras](../gatve.md) (`datasets/gov/rc/ar/gatve`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/gatve.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gatve.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/gatve/Gatve` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `gat_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gat_kodas` | `integer` | — | `4` | `open` | — | Gatvės identifikavimo kodas | — |
| `tipas` | `string` | — | `3` | `open` | — | Gatvės tipas | — |
| `tipo_santrumpa` | `string` | — | `3` | `open` | — | Gatvės tipo trumpinys | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Gatvės pavadinimas (kilmininko linksnyje) | — |
| `gyvenamoji_vietove` | `ref` | [GyvenamojiVietove](../gyvenamojivietove/GyvenamojiVietove.md) (`level=4 UUID`: `gyvenamoji_vietove._id`) | `4` | `open` | — | Gyvenamosios vietovės, kurioje yra gatvė, identifikavimo kodas | — |
| `nuo` | `date` | `D` | `4` | `open` | — | Atributų rinkinio pradžios galiojimo data | — |
| `gat_nuo` | `date` | `D` | `4` | `open` | — | Objekto įregistravimo data | — |
| `gat_iki` | `date` | `D` | `4` | `open` | — | Objekto išregistravimo data | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/gatve.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gatve.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/gatve (https://data.gov.lt/datasets/1293/)
