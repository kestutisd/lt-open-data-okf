---
type: Table
title: "Produktas — Pateikiama informacija apie produkto tipą, pavadinimą, galiojimo datą (ūkio subjekto pavadinimas, kontaktinė informacija)"
description: "Spinta table datasets/gov/vat/trasos/Produktas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/trasos/Produktas"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/r9_trasos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r9_trasos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Produktas — Pateikiama informacija apie produkto tipą, pavadinimą, galiojimo datą (ūkio subjekto pavadinimas, kontaktinė informacija)

- **Model:** `datasets/gov/vat/trasos/Produktas`[^manifest]
- **Dataset:** [datasets/gov/vat/trasos](../trasos.md) (`datasets/gov/vat/trasos`)
- **Manifest CSV:** [datasets/gov/vat/r9_trasos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r9_trasos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/trasos/Produktas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikacinis stulpelis | — |
| `kodas` | `string` | — | `2` | `open` | — | Ūkio subjekto JAR kodas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Ūkio subjekto pavadinimas | — |
| `pateikimas` | `date` | `D` | `4` | `open` | — | Pateikimo data | — |
| `tel_nr` | `string` | — | `1` | `open` | — | Ūkio subjektas telefono numeris | — |
| `email` | `string` | — | `2` | `open` | — | Ūkio subjekto kontaktinis el. paštas | — |
| `adresas` | `string` | — | `2` | `open` | — | Ūkio subjekto adresas | — |
| `trasa` | `string` | — | `1` | `open` | — | Trąšos ir/arba dirvožemio gerinimo priemonės pavadinimas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tel_nr` | `update(property: "tel_nr[]", type: "array", source: "Tel_nr")` | `property` | `1` | — | — | — | — |
| `email` | `update(property: "email[]", type: "array", source: "Email")` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r9_trasos.csv
