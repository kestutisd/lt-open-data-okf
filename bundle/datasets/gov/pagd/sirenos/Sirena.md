---
type: Table
title: "Sirena"
description: "Sirenų informacija"
resource: "https://get.data.gov.lt/datasets/gov/pagd/sirenos/Sirena"
tags: [gov, pagd, sirena, deployed, level-4, cadence-other]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/sirenos.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/pagd/sirenos.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2880/"
    title: "data.gov.lt DCAT-AP — datasets/gov/pagd/sirenos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sirena

Sirenų informacija[^manifest]

- **Model:** `datasets/gov/pagd/sirenos/Sirena`[^manifest]
- **Dataset:** [pagd sirenos](../sirenos.md) (`datasets/gov/pagd/sirenos`)[^manifest]
- **Manifest CSV:** [datasets/gov/pagd/sirenos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/sirenos.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pagd/sirenos/Sirena` (`deployed`)[^manifest]
- **Provider:** `pagd` — Priešgaisrinės apsaugos ir gelbėjimo departamentas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `OTHER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | "valstybės duomenų agentūros įrašų identifikatorius" | — |
| `apskritis` | `string` | — | `4` | `open` | — | "Apskrities pavadinimas" | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | "Savivaldybės pavadinimas" | — |
| `seniunija` | `string` | — | `4` | `open` | — | "Seniūnijos pavadinimas" | — |
| `gyvenviete` | `string` | — | `4` | `open` | — | "Gyvenvietės pavadinimas" | — |
| `taskas_lks` | `geometry(3346)` | — | `4` | `open` | — | "Kordinate lks 94 formatu" | — |
| `taskas_wgs` | `geometry(4326)` | — | `4` | `open` | — | "Kordinate wgs 84 formatu" | — |
| `lks_x` | `integer` | — | `4` | `open` | — | "Sunormuota LKS x koordinatė (7 skaitmenys)" | — |
| `lks_y` | `integer` | — | `4` | `open` | — | "Sunormuota LKS y koordinatė (6 skaitmenys)" | — |
| `wgs_lon_ilguma` | `number` | — | `4` | `open` | — | "WGS koordinatė (ilguma) paskaičiuota iš normuotų LKS koordinačių" | — |
| `wgs_lat_platuma` | `number` | — | `4` | `open` | — | "WGS koordinatė (platuma) paskaičiuota iš normuotų LKS koordinačių" | — |
| `sirenos_sumontavimo_adresas` | `string` | — | `4` | `open` | — | "Sirenos sumontavimo adresas" | — |
| `garso_spindulys` | `number` | — | `4` | `open` | — | — | — |
| `savininkas` | `string` | — | `4` | `open` | — | — | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | — | — |
| `atnaujinimo_data` | `date` | `D` | `4` | `open` | — | — | — |
| `gyventoju_skaicius` | `integer` | — | `4` | `open` | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/pagd/sirenos.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/sirenos.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/pagd/sirenos (https://data.gov.lt/datasets/2880/)
