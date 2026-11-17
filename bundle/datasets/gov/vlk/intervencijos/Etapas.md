---
type: Table
title: "Etapas — Stacionarinio gydymo etapai"
description: "Informacija apie stacionarinio gydymo etapus, kurių metu atliktos medicininės intervencijos"
resource: "https://get.data.gov.lt/datasets/gov/vlk/intervencijos/Etapas"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/intervencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/intervencijos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Etapas — Stacionarinio gydymo etapai

Informacija apie stacionarinio gydymo etapus, kurių metu atliktos medicininės intervencijos

- **Model:** `datasets/gov/vlk/intervencijos/Etapas`[^manifest]
- **Dataset:** [datasets/gov/vlk/intervencijos](../intervencijos.md) (`datasets/gov/vlk/intervencijos`)
- **Manifest CSV:** [datasets/gov/vlk/intervencijos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/intervencijos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/intervencijos/Etapas`
- **Primary Key (`ref`):** `ad_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `istaiga` | `ref` | [/datasets/gov/vlk/istaigos/Istaiga](../istaigos/Istaiga.md) | `4` | `open` | — | Įstaigos ID | Įstaigos, kuri suteikė paslaugas, ID |
| `d_chir` | `string` | — | `4` | `open` | — | Dienos chirurgija | „T“ žymima, jei suteikta paslauga atitinka dienos chirurgijos teikimo reikalavimus, kitu atveju žymima „N“ |
| `etapo_tipas` | `string` | — | `4` | `open` | — | Etapo tipas | Etapo tipas (gydymo rūšis) |
| `data` | `date` | `M` | `4` | `open` | — | Laikotarpis | Laikotarpis, kurį baigėsi gydymo etapas (mėnesio tikslumu) |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `d_chir` | `"Ne"` | — | — | — | — |
| `d_chir` | `"Taip"` | — | — | — | — |
| `etapo_tipas` | `"Aktyvus gydymas"` | — | — | — | — |
| `etapo_tipas` | `"Reabilitacija"` | — | — | — | — |
| `etapo_tipas` | `"Ilgalaikis gydymas"` | — | — | — | — |
| `etapo_tipas` | `"Transplantacija"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/intervencijos.csv
