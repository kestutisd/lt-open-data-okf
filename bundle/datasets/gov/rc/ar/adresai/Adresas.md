---
type: Table
title: "Adresas — Adresų registro žemės sklypams ir pastatams suteiktų adresų tekstiniai duomenys"
description: "Žemės sklypams ir pastatams suteiktų adresų tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (žemės sklypams ar pastatams suteiktus adresus apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/adresai/Adresas"
tags: [gov, rc, adresas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/adresai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/adresai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2369/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/adresai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Adresas — Adresų registro žemės sklypams ir pastatams suteiktų adresų tekstiniai duomenys

Žemės sklypams ir pastatams suteiktų adresų tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (žemės sklypams ar pastatams suteiktus adresus apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.[^manifest]

- **Model:** `datasets/gov/rc/ar/adresai/Adresas`[^manifest]
- **Dataset:** [Adresų registras](../adresai.md) (`datasets/gov/rc/ar/adresai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/adresai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/adresai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/adresai/Adresas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `aob_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tipas` | `integer` | — | `4` | `open` | — | Adreso tipas (1 -žemės sklypas, pastatas, 2 - patalpa) | — |
| `aob_kodas` | `integer` | — | `4` | `open` | — | Adreso (sklypo, statinio, patalpos) identifikavimo kodas | — |
| `aob_data_nuo` | `date` | `D` | `4` | `open` | — | Objekto įregistravimo data | — |
| `aob_data_iki` | `date` | `D` | `4` | `open` | — | Objekto išregistravimo data | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/adresai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/adresai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/adresai (https://data.gov.lt/datasets/2369/)
