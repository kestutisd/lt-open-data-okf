---
type: Table
title: "Savivaldybe — Adresų registro savivaldybių tekstinių duomenų rinkinys"
description: "Savivaldybių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - savivaldybes apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/savivaldybe/Savivaldybe"
tags: [gov, rc, savivaldybe, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/savivaldybe.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/savivaldybe.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1286/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/savivaldybe"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Savivaldybe — Adresų registro savivaldybių tekstinių duomenų rinkinys

Savivaldybių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - savivaldybes apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.[^manifest]

- **Model:** `datasets/gov/rc/ar/savivaldybe/Savivaldybe`[^manifest]
- **Dataset:** [Adresų registras](../savivaldybe.md) (`datasets/gov/rc/ar/savivaldybe`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/savivaldybe.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/savivaldybe.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/savivaldybe/Savivaldybe` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `sav_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sav_kodas` | `integer` | — | `4` | `open` | — | Savivaldybės identifikavimo kodas | — |
| `tipas` | `string` | — | `3` | `open` | — | Administracinio vieneto tipas | — |
| `tipo_santrumpa` | `string` | — | `3` | `open` | — | Administracinio vieneto tipo trumpinys | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Savivaldybės pavadinimas | — |
| `apskritis` | `ref` | [Apskritis](../apskritis/Apskritis.md) (`level=4 UUID`: `apskritis._id`) | `4` | `open` | — | Apskrities, kurioje yra savivaldybė, identifikavimo kodas | — |
| `sav_nuo` | `date` | `D` | `4` | `open` | — | Objekto įregistravimo data | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/savivaldybe.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/savivaldybe.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/savivaldybe (https://data.gov.lt/datasets/1286/)
