---
type: Table
title: "Renginys — Kauno miesto savivaldybės organizuojami renginiai"
description: "Kauno miesto savivaldybės išduoti leidimai organizuoti renginį ar pramoginę paslaugą Kauno miesto viešoje vietoje."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/miesto_renginiai/Renginys"
tags: [gov, kauno_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/miesto_renginiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/miesto_renginiai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Renginys — Kauno miesto savivaldybės organizuojami renginiai

Kauno miesto savivaldybės išduoti leidimai organizuoti renginį ar pramoginę paslaugą Kauno miesto viešoje vietoje. Rinkinyje pateikti duomenys nuo 2020 metų liepos mėnesio.

- **Model:** `datasets/gov/kauno_m_sav/miesto_renginiai/Renginys`[^manifest]
- **Dataset:** [Kauno miesto savivaldybės organizuojami renginiai](../miesto_renginiai.md) (`datasets/gov/kauno_m_sav/miesto_renginiai`)
- **Manifest CSV:** [datasets/gov/kauno_m_sav/miesto_renginiai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/miesto_renginiai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/miesto_renginiai/Renginys`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `ivykio_pavadinimas` | `string` | — | `4` | `open` | — | Renginio ar įvykio pavadinimas | — |
| `aprasymas_lt` | `string` | — | `4` | `open` | — | Renginio ar įvykio aprašymas | — |
| `nuo` | `datetime` | `T` | `4` | `open` | — | Renginio ar įvykio data | — |
| `iki` | `datetime` | `T` | `4` | `open` | — | Renginio ar įvykio pabaigos data | — |
| `vieta` | `string` | — | `4` | `open` | — | Renginio ar įvykio vieta | — |
| `organizatorius` | `string` | — | `4` | `open` | — | Renginio ar įvykio organizatorius | — |
| `pobudis` | `string` | — | `4` | `open` | — | Renginio ar įvykio pobūdis | — |
| `renginio_leidimas` | `string` | — | `4` | `open` | — | Renginio leidimo duomenys | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pobudis` | `"Renginys"` | — | — | Renginys | — |
| `pobudis` | `"Vizitas"` | — | — | Vizitas | — |
| `pobudis` | `"Savivaldybės renginys"` | — | — | Savivaldybės renginys | — |
| `pobudis` | `"Kita"` | — | — | Kita | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aprasymas_lt` | `update(property: "aprasymas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/miesto_renginiai.csv
