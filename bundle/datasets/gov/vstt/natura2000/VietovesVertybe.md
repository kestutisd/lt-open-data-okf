---
type: Table
title: "VietovesVertybe — Natura 2000 teritorijų vietovių sąrašo duomenys"
description: "Spinta table datasets/gov/vstt/natura2000/VietovesVertybe (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vstt/natura2000/VietovesVertybe"
tags: [gov, vstt, vietovesvertybe, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/natura2000.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/vstt/natura2000.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2270/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vstt/natura2000"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# VietovesVertybe — Natura 2000 teritorijų vietovių sąrašo duomenys

- **Model:** `datasets/gov/vstt/natura2000/VietovesVertybe`[^manifest]
- **Dataset:** [Natura 2000 teritorijų apsaugos tikslų duomenys](../natura2000.md) (`datasets/gov/vstt/natura2000`)[^manifest]
- **Manifest CSV:** [datasets/gov/vstt/natura2000.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/natura2000.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/natura2000/VietovesVertybe` (`deployed`)[^manifest]
- **Provider:** `vstt` — Valstybinė saugomų teritorijų tarnyba prie Aplinkos ministerijos *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `kodas` | `ref` | [BuveiniuApsaugaiSvarbiTeritorija](../teritorijos/BuveiniuApsaugaiSvarbiTeritorija.md) (`level=4 UUID` via `BuveiniuApsaugaiSvarbiTeritorija[bast_kodas]`: `kodas._id`) | `4` | `open` | — | Buveinės kodas | Buveinių apsaugai svarbios teritorijos kodas |
| `kodas.pavadinimas` | `string` | — | `4` | `open` | — | Pavadinimas | Buveinių apsaugai svarbios teritorijos pavadinimas |
| `rusis` | `string` | — | `4` | `open` | — | Rūšis | Rūšies lotyniškas pavadinimas |
| `buveine` | `string` | — | `4` | `open` | — | Buveinės pavadinimas | — |
| `tipas` | `string` | — | `4` | `open` | — | Buveinių ekosistemos grupė | — |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Geometrija | Geometrijos tipas, koordinačių sistemos kodas |
| `data` | `date` | `D` | `4` | `open` | — | Inventorizacijos data | — |
| `plotas` | `number` | `ha` | `4` | `open` | — | Plotas | Plotas hektarais |
| `sluoksnis` | `string` | — | `4` | `open` | — | Sluoksnis | Geometrijos tipas, sluoksnis iš kurio suformuoti duomenys |
| `statusas` | `string` | — | `4` | `open` | — | Objekto teisinis statusas | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/natura2000.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/natura2000.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vstt/natura2000 (https://data.gov.lt/datasets/2270/)
