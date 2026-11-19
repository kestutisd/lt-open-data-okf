---
type: Table
title: "IstorineGatve — Adresų registro istorinių gatvių tekstinių duomenų rinkinys"
description: "Istorinių gatvių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (istorines (panaikintas) apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/istorinegatve/IstorineGatve"
tags: [gov, rc, istorinegatve, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/istorinegatve.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/istorinegatve.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# IstorineGatve — Adresų registro istorinių gatvių tekstinių duomenų rinkinys

Istorinių gatvių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (istorines (panaikintas) apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.[^manifest]

- **Model:** `datasets/gov/rc/ar/istorinegatve/IstorineGatve`[^manifest]
- **Dataset:** [Adresų registras](../istorinegatve.md) (`datasets/gov/rc/ar/istorinegatve`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/istorinegatve.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/istorinegatve.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/istorinegatve/IstorineGatve` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `gat_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gat_kodas` | `integer` | — | `4` | `open` | — | Gatvės identifikavimo kodas | — |
| `tipas` | `string` | — | `3` | `open` | — | Gatvės tipas | — |
| `tipo_santrumpa` | `string` | — | `3` | `open` | — | Gatvės tipo trumpinys | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Gatvės pavadinimas (kilmininko linksnyje) | — |
| `gyv_kodas` | `integer` | — | `2` | `open` | — | Gyvenamosios vietovės, kurioje yra gatvė, kodas | — |
| `gyv_pavadinimas` | `string` | — | `2` | `open` | — | Gyvenamosios vietovės, kurioje yra gatvė, pavadinimas | — |
| `nuo` | `date` | `D` | `4` | `open` | — | Atributų rinkinio pradžios galiojimo data | — |
| `gat_nuo` | `date` | `D` | `4` | `open` | — | Objekto įregistravimo data | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/istorinegatve.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/istorinegatve.csv#L3)
