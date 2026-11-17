---
type: Table
title: "IsvezimoTvarkarastis — Konteinerių išvežimo tvarkaraštis"
description: "Informacija apie atliekų surinkimo taškus ir jų aptarnavimo tvarkaraščius."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas/IsvezimoTvarkarastis"
tags: [gov, vilniaus_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L33"
    last_modified: "2026-11-11T14:39:20Z"
---

# IsvezimoTvarkarastis — Konteinerių išvežimo tvarkaraštis

Informacija apie atliekų surinkimo taškus ir jų aptarnavimo tvarkaraščius.

- **Model:** `datasets/gov/vilniaus_m_sav/atlieku_tvarkymas/IsvezimoTvarkarastis`[^manifest]
- **Dataset:** [Vilniaus atliekų sistemos administratoriaus atliekų tvarkymas](../atlieku_tvarkymas.md) (`datasets/gov/vilniaus_m_sav/atlieku_tvarkymas`)
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L33](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L33)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas/IsvezimoTvarkarastis`
- **Primary Key (`ref`):** `waste_object_id`
- **Level:** `4`

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

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `irengimo_tipas` | `"Antžeminis stumdomas"` | — | — | Antžeminis stumdomas | — |
| `irengimo_tipas` | `"Pusiau požeminis"` | — | — | Pusiau požeminis | — |
| `irengimo_tipas` | `"Antžeminis stacionarus"` | — | — | Antžeminis stacionarus | — |
| `irengimo_tipas` | `"Požeminis"` | — | — | Požeminis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv
