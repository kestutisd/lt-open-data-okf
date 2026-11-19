---
type: Table
title: "Etapas — Stacionarinio gydymo etapai"
description: "Informacija apie stacionarinio gydymo etapus, kurių metu atliktos medicininės intervencijos"
resource: "https://get.data.gov.lt/datasets/gov/vlk/intervencijos/Etapas"
tags: [gov, vlk, etapas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/intervencijos.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vlk/intervencijos.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1509/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/intervencijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Etapas — Stacionarinio gydymo etapai

Informacija apie stacionarinio gydymo etapus, kurių metu atliktos medicininės intervencijos[^manifest]

- **Model:** `datasets/gov/vlk/intervencijos/Etapas`[^manifest]
- **Dataset:** [Medicininės intervencijos, atliktos taikant stacionarinį gydymą ar teikiant dienos chirurgijos...](../intervencijos.md) (`datasets/gov/vlk/intervencijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/intervencijos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/intervencijos.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/intervencijos/Etapas` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ad_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `istaiga` | `ref` | [Istaiga](../istaigos/Istaiga.md) (`level=4 UUID`: `istaiga._id`) | `4` | `open` | — | Įstaigos ID | Įstaigos, kuri suteikė paslaugas, ID |
| `d_chir` | `string` | — | `4` | `open` | — | Dienos chirurgija | „T“ žymima, jei suteikta paslauga atitinka dienos chirurgijos teikimo reikalavimus, kitu atveju žymima „N“ |
| `etapo_tipas` | `string` | — | `4` | `open` | — | Etapo tipas | Etapo tipas (gydymo rūšis) |
| `data` | `date` | `M` | `4` | `open` | — | Laikotarpis | Laikotarpis, kurį baigėsi gydymo etapas (mėnesio tikslumu) |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `d_chir` | `"Ne"` | — | — | — | — |
| `d_chir` | `"Taip"` | — | — | — | — |
| `etapo_tipas` | `"Aktyvus gydymas"` | — | — | — | — |
| `etapo_tipas` | `"Reabilitacija"` | — | — | — | — |
| `etapo_tipas` | `"Ilgalaikis gydymas"` | — | — | — | — |
| `etapo_tipas` | `"Transplantacija"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/intervencijos.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/intervencijos.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/intervencijos (https://data.gov.lt/datasets/1509/)
