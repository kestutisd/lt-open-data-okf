---
type: Table
title: "KaunasAugustowWFL1AugustowKanalSluz — Augustavo kanalo geoerdviniai duomenys"
description: "Šiame sluoksnyje pateikiami Augustavo kanalo šliuzų geoerdviniai duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/KaunasAugustowWFL1AugustowKanalSluz"
tags: [gov, vvkd, kaunasaugustowwfl1augustowkanalsluz, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L59"
    title: "atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv#L59"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1983/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vvkd/e_zemelapiai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# KaunasAugustowWFL1AugustowKanalSluz — Augustavo kanalo geoerdviniai duomenys

Šiame sluoksnyje pateikiami Augustavo kanalo šliuzų geoerdviniai duomenys. Nurodomi šliuzų pavadinimai, kampai ir geoerdvinės lokacijos.[^manifest]

- **Model:** `datasets/gov/vvkd/e_zemelapiai/KaunasAugustowWFL1AugustowKanalSluz`[^manifest]
- **Dataset:** [Vidaus vandenų e-navigacinių žemėlapių informacija](../e_zemelapiai.md) (`datasets/gov/vvkd/e_zemelapiai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vvkd/e_zemelapiai.csv#L59](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L59)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/KaunasAugustowWFL1AugustowKanalSluz` (`deployed`)[^manifest]
- **Provider:** `vvkd` — AB Vidaus vandens kelių direkcija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `objectid`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `objectid` | `string` | — | `4` | `open` | — | Atributinės lentelės objekto numeris | — |
| `name` | `string` | — | `4` | `open` | — | Pavadinimas | — |
| `angle` | `number` | `°` | `4` | `open` | — | Sutartinio ženklo pasūkimo kampas | — |
| `geometry` | `geometry(3857)` | — | `4` | `open` | — | Geometrijos tipas | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv#L59 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L59)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vvkd/e_zemelapiai (https://data.gov.lt/datasets/1983/)
