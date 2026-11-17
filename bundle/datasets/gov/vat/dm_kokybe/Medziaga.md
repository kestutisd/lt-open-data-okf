---
type: Table
title: "Medziaga — Pateikiama informacija apie sertifikuotos sodo augalų dauginamosios medžiagos augalo rūšį"
description: "Spinta table datasets/gov/vat/dm_kokybe/Medziaga (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/dm_kokybe/Medziaga"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/r21_dm_kokybe.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r21_dm_kokybe.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Medziaga — Pateikiama informacija apie sertifikuotos sodo augalų dauginamosios medžiagos augalo rūšį

- **Model:** `datasets/gov/vat/dm_kokybe/Medziaga`[^manifest]
- **Dataset:** [datasets/gov/vat/dm_kokybe](../dm_kokybe.md) (`datasets/gov/vat/dm_kokybe`)
- **Manifest CSV:** [datasets/gov/vat/r21_dm_kokybe.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r21_dm_kokybe.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/dm_kokybe/Medziaga`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikacinis numeris | — |
| `veisle` | `string` | — | `3` | `open` | — | Veislė | — |
| `skiepuglis_uglis_daigas` | `number` | `U` | `4` | `open` | — | Iš viso skiepūglių, ūglių ir daigų | — |
| `skiepuglis_supelitine` | `number` | `U` | `4` | `open` | — | Skiepūglių, ūglių ir daigų superelitinės medžiagos kiekis | — |
| `skiepuglis_elitine` | `number` | `U` | `4` | `open` | — | Skiepūglių, ūglių ir daigų elitinės medžiagos kiekis | — |
| `skiepuglis_sertifikuota` | `number` | `U` | `4` | `open` | — | Skiepūglių, ūglių ir daigų sertifikuotos medžiagos kiekis | — |
| `sodinukas` | `number` | `U` | `4` | `open` | — | Iš viso sodinukų | — |
| `sodinukas_elitine` | `number` | `U` | `4` | `open` | — | Sodinukų elitinės medžiagos kiekis | — |
| `sodinukas_sertifikuota` | `number` | `U` | `4` | `open` | — | Sodinukų sertifikuotos medžiagos kiekis | — |
| `nuo` | `date` | `D` | `4` | `open` | — | Galiojimo pradžia | — |
| `iki` | `date` | `D` | `4` | `open` | — | Galiojimo pabaiga | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r21_dm_kokybe.csv
