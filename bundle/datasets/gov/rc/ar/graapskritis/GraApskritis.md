---
type: Table
title: "GraApskritis — Adresų registro apskričių erdvinių duomenys"
description: "Apskričių erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - apskritis apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/graapskritis/GraApskritis"
tags: [gov, rc, graapskritis, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/graapskritis.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/graapskritis.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1344/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/graapskritis"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# GraApskritis — Adresų registro apskričių erdvinių duomenys

Apskričių erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - apskritis apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.[^manifest]

- **Model:** `datasets/gov/rc/ar/graapskritis/GraApskritis`[^manifest]
- **Dataset:** [Adresų registras](../graapskritis.md) (`datasets/gov/rc/ar/graapskritis`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/graapskritis.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/graapskritis.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/graapskritis/GraApskritis` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `aps_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aps_kodas` | `integer` | — | `4` | `open` | — | Apskrities kodas Registre (nekeičiamas apskrities egzistavimo laiką) | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Apskrities pavadinimas | — |
| `aps_plotas` | `number` | `ha` | `4` | `open` | — | Apskrities grafinis plotas (ha) | — |
| `aps_r` | `date` | `D` | `4` | `open` | — | Apskrities įrašymo į Adresų registrą data | — |
| `formavimo_data` | `date` | `D` | `4` | `open` | — | Duomenų formavimo data | — |
| `apskritys` | `geometry(3346)` | — | `4` | `open` | — | Apskričių ribos | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/graapskritis.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/graapskritis.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/graapskritis (https://data.gov.lt/datasets/1344/)
