---
type: Table
title: "Veisle — Pateikiama informacija apie į Nacionalinį sąrašą įrašytas veisles, išbrauktas veisles, veislių palaikytojų ir selekcininkų įgaliotųjų atstovų sąrašus."
description: "Spinta table datasets/gov/vat/saugomos_veisles/Veisle (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/saugomos_veisles/Veisle"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/saugomos_veisles.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/saugomos_veisles.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Veisle — Pateikiama informacija apie į Nacionalinį sąrašą įrašytas veisles, išbrauktas veisles, veislių palaikytojų ir selekcininkų įgaliotųjų atstovų sąrašus.

- **Model:** `datasets/gov/vat/saugomos_veisles/Veisle`[^manifest]
- **Dataset:** [datasets/gov/vat/saugomos_veisles](../saugomos_veisles.md) (`datasets/gov/vat/saugomos_veisles`)
- **Manifest CSV:** [datasets/gov/vat/saugomos_veisles.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/saugomos_veisles.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/saugomos_veisles/Veisle`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `grupe` | `string` | — | `4` | `open` | — | Augalų grupė | — |
| `gentis` | `string` | — | `4` | `open` | — | Augalų genčių ir rūšių grupė | — |
| `veisle` | `string` | — | `4` | `open` | — | Augalo veislės pavadinimas | — |
| `rusis` | `string` | — | `2` | `open` | — | Augalo rūšis | — |
| `atnaujinimo_metai` | `integer` | — | `2` | `open` | — | Įrašymo atnaujinimo metai | — |
| `galioja_iki` | `integer` | — | `2` | `open` | — | Metai, iki kurių gruodžio 31 d. galioja įrašymas | — |
| `atstovas` | `string` | — | `1` | `open` | — | Atstovo pavadinimas | — |
| `atstovo_adresas` | `string` | — | `2` | `open` | — | Atstovo adresas | — |
| `metai` | `integer` | — | `2` | `open` | — | Įrašymo metai | — |
| `palaikytojas` | `string` | — | `1` | `open` | — | Veislės palaikytojas | — |
| `pastabos` | `string` | — | `2` | `open` | — | Pastabos | — |
| `buveine` | `string` | — | `1` | `open` | — | Palaikytojo adresas | — |
| `koord` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Palaikytojo adreso koordinatės (LKS) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `grupe` | `"ŽEMĖS ŪKIO AUGALAI"` | — | — | — | — |
| `grupe` | `"DARŽOVĖS"` | — | — | — | — |
| `grupe` | `"Sodo augalai"` | — | — | — | — |
| `grupe` | `"Dekoratyviniai augalai"` | — | — | — | — |
| `gentis` | `"Javai"` | — | — | — | — |
| `gentis` | `"Aliejiniai ir pluoštiniai augalai"` | — | — | — | — |
| `gentis` | `"Runkeliai"` | — | — | — | — |
| `gentis` | `"Pašariniai pupiniai augalai"` | — | — | — | — |
| `gentis` | `"Pašariniai migliniai augalai"` | — | — | — | — |
| `gentis` | `"Daržovės"` | — | — | — | — |
| `gentis` | `"Bulvės"` | — | — | — | — |
| `gentis` | `"Serbentai"` | — | — | — | — |
| `gentis` | `"Trešnės, Vyšnios"` | — | — | — | — |
| `gentis` | `"Braškės, žemuogės"` | — | — | — | — |
| `gentis` | `"Obelys"` | — | — | — | — |
| `gentis` | `"Pašariniai kitų rūšių augalai"` | — | — | — | — |
| `gentis` | `"Kriaušės"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `atnaujinimo_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `galioja_iki` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/saugomos_veisles.csv
