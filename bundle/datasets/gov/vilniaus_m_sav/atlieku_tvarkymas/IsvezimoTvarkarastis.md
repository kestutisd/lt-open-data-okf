---
type: Table
title: "IsvezimoTvarkarastis — Konteinerių išvežimo tvarkaraštis"
description: "Informacija apie atliekų surinkimo taškus ir jų aptarnavimo tvarkaraščius."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas/IsvezimoTvarkarastis"
tags: [gov, vilniaus_m_sav, isvezimotvarkarastis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L33"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L33"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3897/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/atlieku_tvarkymas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# IsvezimoTvarkarastis — Konteinerių išvežimo tvarkaraštis

Informacija apie atliekų surinkimo taškus ir jų aptarnavimo tvarkaraščius.[^manifest]

- **Model:** `datasets/gov/vilniaus_m_sav/atlieku_tvarkymas/IsvezimoTvarkarastis`[^manifest]
- **Dataset:** [Vilniaus atliekų sistemos administratoriaus atliekų tvarkymas](../atlieku_tvarkymas.md) (`datasets/gov/vilniaus_m_sav/atlieku_tvarkymas`)[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L33](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L33)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas/IsvezimoTvarkarastis` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `waste_object_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `waste_object_id` | `string` | — | `4` | `open` | — | Atliekų kilmės identifikatorius | — |
| `dumpster_id` | `string` | — | `4` | `open` | — | Konteinerio identifikatorius | — |
| `inventorinis_nr` | `string` | — | `4` | `open` | — | Inventoriaus numeris | — |
| `irengimo_tipas` | `string` | — | `4` | `open` | — | Įrenginio tipas | — |
| `aptarnavimo_pavadinimas` | `string` | — | `2` | `open` | — | Aptarnavimo pavadinimas | — |
| `aptarnavimo_daznumas` | `string` | — | `2` | `open` | — | Aptarnavimo data | — |
| `priklauso` | `string` | — | `4` | `open` | — | Kam priklauso konteineris | — |
| `aptarnaujamas_adresas` | `string` | — | `3` | `open` | — | Aptarnaujamas adresas | — |
| `kitas_aptarnavimas` | `date` | — | `4` | `open` | — | Kada artimiausias kitas aptarnavimas | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Ilgumos koordinatė WGS84 koordinačių sistemoje | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Platumos koordinatė WGS84 koordinačių sistemoje | — |
| `geometrija` | `geometry(point, 4326)` | — | `4` | `open` | — | Geometrija | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `irengimo_tipas` | `"Antžeminis stumdomas"` | — | — | Antžeminis stumdomas | — |
| `irengimo_tipas` | `"Pusiau požeminis"` | — | — | Pusiau požeminis | — |
| `irengimo_tipas` | `"Antžeminis stacionarus"` | — | — | Antžeminis stacionarus | — |
| `irengimo_tipas` | `"Požeminis"` | — | — | Požeminis | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L33 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L33)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/atlieku_tvarkymas (https://data.gov.lt/datasets/3897/)
