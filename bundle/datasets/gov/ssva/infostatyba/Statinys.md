---
type: Table
title: "Statinys — Valstybinės teritorijų planavimo ir statybos inspekcijos prie aplinkos ministerijos duomenys"
description: "Spinta table datasets/gov/ssva/infostatyba/Statinys (27 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ssva/infostatyba/Statinys"
tags: [gov, ssva, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ssva/infostatyba.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/infostatyba.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Statinys — Valstybinės teritorijų planavimo ir statybos inspekcijos prie aplinkos ministerijos duomenys

- **Model:** `datasets/gov/ssva/infostatyba/Statinys`[^manifest]
- **Dataset:** [Valstybinės teritorijų planavimo ir statybos inspekcijos prie aplinkos ministerijos duomenys](../infostatyba.md) (`datasets/gov/ssva/infostatyba`)
- **Manifest CSV:** [datasets/gov/ssva/infostatyba.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/infostatyba.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/infostatyba/Statinys`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Iraso identifikatorius | — |
| `projekto_id` | `string` | — | `4` | `open` | — | Projekto identifikatorius | — |
| `statinio_id` | `string` | — | `4` | `open` | — | Statinio identifikatorius | — |
| `projekto_pavadinimas` | `string` | — | `4` | `open` | — | Projekto pavadinimas | — |
| `projekto_reg_nr` | `string` | — | `4` | `open` | — | Projekto registracijos numeris | — |
| `projekto_metai` | `integer` | — | `4` | `open` | — | Projekto metai | — |
| `unikalus_numeris` | `string` | — | `4` | `open` | — | Statinio unikalus numeris | — |
| `statinio_paskirtis` | `string` | — | `4` | `open` | — | Statinio paskirties unikalus identifikatorius | — |
| `statinio_pakeista_paskirtis` | `string` | — | `4` | `open` | — | Statinio paskirties unikalus identifikatorius (būsima paskirtis) | — |
| `statinio_kategorija` | `string` | — | `4` | `open` | — | Statinio kategorija | — |
| `adresas` | `string` | — | `4` | `open` | — | Statinio adresas | — |
| `statybos_rusis` | `string` | — | `4` | `open` | — | Statybos rusis | — |
| `statinio_pavadinimas` | `string` | — | `4` | `open` | — | Statinio tipo pavadinimas | — |
| `pastatymo_metai` | `integer` | — | `4` | `open` | — | Statinio pastatymo metai | — |
| `kadastro_nr` | `string` | — | `4` | `open` | — | Statinio kadastrinis numeris | — |
| `ploto_reg_tipas` | `string` | — | `4` | `open` | — | Pastato ploto registracija | — |
| `sklypo_reg_statusas` | `string` | — | `4` | `open` | — | Sklypo registracijos statusas | — |
| `dokumento_reg_nr` | `string` | — | `4` | `open` | — | Projekto dokumento registracijos numeris | — |
| `dokumento_reg_data` | `date` | `D` | `4` | `open` | — | Pastato dokumento registracijos data | — |
| `iraso_data` | `date` | `D` | `4` | `open` | — | Dokumento iraso data | — |
| `dok_statusas` | `string` | — | `4` | `open` | — | Dokumento statusas | — |
| `dok_tipo_kodas` | `string` | — | `4` | `open` | — | Dokumento kodas | — |
| `dokumento_kategorija` | `string` | — | `4` | `open` | — | Dokumento kategorija | — |
| `dok_irasas` | `string` | — | `4` | `open` | — | Dokumento irasas | — |
| `taskas_lks` | `geometry(3346)` | — | `4` | `open` | — | Koordinate LKS94 formatu | — |
| `taskas_wgs` | `geometry(4326)` | — | `4` | `open` | — | Koordinate WGS84 formatu | — |
| `uuid` | `string` | — | `4` | `open` | — | Dokumento identifikatorius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/infostatyba.csv
