---
type: Table
title: "Monitoringas — Saugomų teritorijų lankytojų duomenys"
description: "Spinta table datasets/gov/vstt/lankytojai/Monitoringas (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vstt/lankytojai/Monitoringas"
tags: [gov, vstt, monitoringas, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/lankytoju_monitoringas.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/vstt/lankytoju_monitoringas.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2303/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vstt/lankytojai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Monitoringas — Saugomų teritorijų lankytojų duomenys

- **Model:** `datasets/gov/vstt/lankytojai/Monitoringas`[^manifest]
- **Dataset:** [Saugomų teritorijų lankytojų duomenys](../lankytojai.md) (`datasets/gov/vstt/lankytojai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vstt/lankytoju_monitoringas.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/lankytoju_monitoringas.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/lankytojai/Monitoringas` (`deployed`)[^manifest]
- **Provider:** `vstt` — Valstybinė saugomų teritorijų tarnyba prie Aplinkos ministerijos *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `teritorija`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `teritorija` | `string` | — | `2` | `open` | — | Saugoma teritorija vieta | — |
| `lankytojai` | `integer` | `U` | `4` | `open` | — | Lankytoju skaičius | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `geometrija` | `geometry(polygon,3346)` | — | `3` | `open` | — | Lankomos vietos geometrija | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref:"Y")` | `type` | `4` | `open` | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/lankytoju_monitoringas.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/lankytoju_monitoringas.csv#L8)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vstt/lankytojai (https://data.gov.lt/datasets/2303/)
