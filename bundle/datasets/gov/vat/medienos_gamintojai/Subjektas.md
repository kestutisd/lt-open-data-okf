---
type: Table
title: "Subjektas — Medinės pakavimo medžiagos ir (arba) medienos, skirtos jai gaminti, gamintoju sąrašas"
description: "Spinta table datasets/gov/vat/medienos_gamintojai/Subjektas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/medienos_gamintojai/Subjektas"
tags: [gov, vat, subjektas, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/medienos_gamintojai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/medienos_gamintojai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1859/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/medienos_gamintojai"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Subjektas — Medinės pakavimo medžiagos ir (arba) medienos, skirtos jai gaminti, gamintoju sąrašas

- **Model:** `datasets/gov/vat/medienos_gamintojai/Subjektas`[^manifest]
- **Dataset:** [Pateikiama informacija apie ūkio subjektus, kuriems suteikta teisė medinę pakavimo medžiagą ir...](../medienos_gamintojai.md) (`datasets/gov/vat/medienos_gamintojai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/medienos_gamintojai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/medienos_gamintojai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/medienos_gamintojai/Subjektas` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikacinis numeris | — |
| `imone` | `string` | — | `2` | `open` | — | Įmonės pavadinimas | — |
| `veikla` | `string` | — | `2` | `open` | — | Vykdoma veikla | — |
| `busena` | `string` | — | `4` | `open` | — | Licencijos būsena | — |
| `adresas` | `string` | — | `2` | `open` | — | Veiklos adresas | — |
| `el_pastas` | `string` | — | `2` | `open` | — | Elektroninis paštas kontaktinei informacijai | — |
| `telefonas` | `string` | — | `2` | `open` | — | Telefono numeris kontaktinei informacijai | — |
| `regionas` | `string` | — | `2` | `open` | — | Veiklos regionas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `veikla` | `"A"` | — | — | Apdorotojas/treatment | — |
| `veikla` | `"G"` | — | — | MPM gamintojas/WPM producer | — |
| `veikla` | `"T"` | — | — | MPM taisytojai, atnaujintojai/ WPM repairers, remanufacturers | — |
| `busena` | `"Galioja"` | — | — | Galioja - Valid | — |
| `busena` | `"Sustabdyta"` | — | — | Sustabdyta - suspended | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `veikla` | `update(property: "veikla[]", type: "array", source: "Veikla")` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/medienos_gamintojai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/medienos_gamintojai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/medienos_gamintojai (https://data.gov.lt/datasets/1859/)
