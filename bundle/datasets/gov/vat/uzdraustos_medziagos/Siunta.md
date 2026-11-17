---
type: Table
title: "Siunta — Pateikiami duomenys apie dokumento pavadinimą, datą, Nr., augalo rūšį / sėklos mišinio pavadinimą, veislę, siuntos Nr., panaikinimo / paskelbimo datą"
description: "Spinta table datasets/gov/vat/uzdraustos_medziagos/Siunta (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/uzdraustos_medziagos/Siunta"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/r25_uzdraustos_medziagos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r25_uzdraustos_medziagos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Siunta — Pateikiami duomenys apie dokumento pavadinimą, datą, Nr., augalo rūšį / sėklos mišinio pavadinimą, veislę, siuntos Nr., panaikinimo / paskelbimo datą

- **Model:** `datasets/gov/vat/uzdraustos_medziagos/Siunta`[^manifest]
- **Dataset:** [datasets/gov/vat/uzdraustos_medziagos](../uzdraustos_medziagos.md) (`datasets/gov/vat/uzdraustos_medziagos`)
- **Manifest CSV:** [datasets/gov/vat/r25_uzdraustos_medziagos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r25_uzdraustos_medziagos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/uzdraustos_medziagos/Siunta`
- **Primary Key (`ref`):** `eiles_nr`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eiles_nr` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `dokumentas` | `string` | — | `3` | `open` | — | Dokumento tipas | — |
| `data` | `string` | — | `1` | `open` | — | Dokumento data ir Nr. | — |
| `rusis` | `string` | — | `3` | `open` | — | Augalo rūšis/ sėklos mišinio pavadinimas | — |
| `veisle` | `string` | — | `4` | `open` | — | Veislė | — |
| `siuntos_nr` | `string` | — | `1` | `open` | — | Siuntos numeris | — |
| `pastaba` | `string` | — | `2` | `open` | — | Pastaba | — |
| `paskelbimas` | `date` | `D` | `4` | `open` | — | Panaikinimo paskelbimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r25_uzdraustos_medziagos.csv
