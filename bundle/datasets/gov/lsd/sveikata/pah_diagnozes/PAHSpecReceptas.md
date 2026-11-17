---
type: Table
title: "PAHSpecReceptas — PAH specifiniam gydymui skiriamų vaistų receptai"
description: "PAH specifiniam gydymui skiriamų vaistų (ambrisentanas, bozentanas, iloprostas, sildenafilis, treprostinilis, macitentanas, seleksipagas) pirmo ir paskutinio galiojančio recepto išrašymo datos (su triukšmu iki 5 dienų), vaisto ATC..."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/pah_diagnozes/PAHSpecReceptas"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/pah_diagnozes.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/pah_diagnozes.csv#L31"
    last_modified: "2026-11-11T14:39:20Z"
---

# PAHSpecReceptas — PAH specifiniam gydymui skiriamų vaistų receptai

PAH specifiniam gydymui skiriamų vaistų (ambrisentanas, bozentanas, iloprostas, sildenafilis, treprostinilis, macitentanas, seleksipagas) pirmo ir paskutinio galiojančio recepto išrašymo datos (su triukšmu iki 5 dienų), vaisto ATC kodas, bendrinis pavadinimas.

- **Model:** `datasets/gov/lsd/sveikata/pah_diagnozes/PAHSpecReceptas`[^manifest]
- **Dataset:** [Pacientų, sergančių plaučių arterine hipertenzija, gydymo duomenys](../pah_diagnozes.md) (`datasets/gov/lsd/sveikata/pah_diagnozes`)
- **Manifest CSV:** [datasets/gov/lsd/sveikata/pah_diagnozes.csv#L31](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/pah_diagnozes.csv#L31)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/pah_diagnozes/PAHSpecReceptas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalios eilutės identifikatorius | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Asmens kodas | — |
| `vaisto_atc_kodas` | `string` | — | `4` | `open` | — | Vaisto ATC kodas | — |
| `vaisto_atc_pav` | `string` | — | `4` | `open` | — | Vaisto ATC pavadinimas | — |
| `first_prescription` | `date` | `D` | `4` | `open` | — | Pirmo recepto išrašymo data | Pirmo recepto išrašymo data, su triukšmu iki 5 d. |
| `last_prescription` | `date` | `D` | `4` | `open` | — | Paskutinio recepto išrašymo data | Paskutinio recepto išrašymo data, su triukšmu iki 5 d. |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/pah_diagnozes.csv
