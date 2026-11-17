---
type: Table
title: "Subjektas — Medinės pakavimo medžiagos ir (arba) medienos, skirtos jai gaminti, gamintoju sąrašas"
description: "Spinta table datasets/gov/vat/medienos_gamintojai/Subjektas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/medienos_gamintojai/Subjektas"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/medienos_gamintojai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/medienos_gamintojai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Subjektas — Medinės pakavimo medžiagos ir (arba) medienos, skirtos jai gaminti, gamintoju sąrašas

- **Model:** `datasets/gov/vat/medienos_gamintojai/Subjektas`[^manifest]
- **Dataset:** [Pateikiama informacija apie ūkio subjektus, kuriems suteikta teisė medinę pakavimo medžiagą ir (arba) medieną, skirtos jai gaminti, ženklinti Tarptautinio fitosanitarijos priemonių standarto Nr. 15 nustatytu ženklu...](../medienos_gamintojai.md) (`datasets/gov/vat/medienos_gamintojai`)
- **Manifest CSV:** [datasets/gov/vat/medienos_gamintojai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/medienos_gamintojai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/medienos_gamintojai/Subjektas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

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

| Property | Value (`prepare`) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/medienos_gamintojai.csv
