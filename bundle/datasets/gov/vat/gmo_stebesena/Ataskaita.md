---
type: Table
title: "Ataskaita — Pateikiama informacija apie ūkio subjekto vardą, pavardę, augalo rūšį, veislę, mainams skirtos sėklos kiekį, g"
description: "Spinta table datasets/gov/vat/gmo_stebesena/Ataskaita (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/gmo_stebesena/Ataskaita"
tags: [gov, vat, ataskaita, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/gmo_stebesena.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/gmo_stebesena.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1861/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/gmo_stebesena"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Ataskaita — Pateikiama informacija apie ūkio subjekto vardą, pavardę, augalo rūšį, veislę, mainams skirtos sėklos kiekį, g

- **Model:** `datasets/gov/vat/gmo_stebesena/Ataskaita`[^manifest]
- **Dataset:** [GMO rizikos kultūrų pasėlių ir siuntų stebėsena](../gmo_stebesena.md) (`datasets/gov/vat/gmo_stebesena`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/gmo_stebesena.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/gmo_stebesena.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/gmo_stebesena/Ataskaita` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Įrašo identifikatorius | — |
| `tipas` | `string` | — | `4` | `open` | — | Mėginio tyrimo rezultatas | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybė, kurioje paimtas mėginys | — |
| `rusis` | `string` | — | `3` | `open` | — | Pasėlių kultūra | — |
| `kilmes_salis` | `string` | — | `3` | `open` | — | Kilmės šalis | — |
| `padalinys` | `string` | — | `4` | `open` | — | Mėginį paėmęs teritorinis padalinys | — |
| `registracija` | `date` | `D` | `4` | `open` | — | Mėginio paėmimo data | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"PASELIS"` | — | — | Pasėlis | — |
| `tipas` | `"SIUNTA"` | — | — | Siunta | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/gmo_stebesena.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/gmo_stebesena.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/gmo_stebesena (https://data.gov.lt/datasets/1861/)
