---
type: Table
title: "Priemone — Priemonių skirtų projektams įgyvendinti duomenys"
description: "Spinta table datasets/gov/sppd/socialiniu_projektu_duomenys/Priemone (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/sppd/socialiniu_projektu_duomenys/Priemone"
tags: [gov, sppd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/sppd/socialiniu_projektu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L52"
    last_modified: "2026-11-11T14:39:20Z"
---

# Priemone — Priemonių skirtų projektams įgyvendinti duomenys

- **Model:** `datasets/gov/sppd/socialiniu_projektu_duomenys/Priemone`[^manifest]
- **Dataset:** [Socialinių projektu duomenys](../socialiniu_projektu_duomenys.md) (`datasets/gov/sppd/socialiniu_projektu_duomenys`)
- **Manifest CSV:** [datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L52](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L52)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sppd/socialiniu_projektu_duomenys/Priemone`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus eilutės identifikatorius | — |
| `priemones_id` | `string` | — | `4` | `open` | — | Unikalus priemonės identifikatorius | Priemonei priskirta id reikšmė kuri unikaliai identifikuoja eilutę lentelėje |
| `priemones_kodas` | `string` | — | `4` | `open` | — | Priemonės kodas | Priemonės kodas kuris įeina į projekto kodo sudarymą |
| `pavadinimas` | `string` | — | `4` | `open` | — | Priemonės pavadinimas | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Priemonės aprašymas | Keli sakiniai apie priemonę |
| `tikslas` | `string` | — | `4` | `open` | — | Priemonės tikslas | Priemone siekiamas įgyvendinti uždavinys |
| `paskirtas_biudzetas` | `number` | — | `4` | `open` | — | Priemonės paskirtas biudžetas | Paskirtas biudžetas kuris išskirstomas kiekvienam projektui |
| `paraiskos_teikimo_nuo_data` | `date` | `D` | `4` | `open` | — | Paraiškų teikimo pradžios data | — |
| `paraiskos_teikimo_iki_data` | `date` | `D` | `4` | `open` | — | Paraiškų teikimo pabaigos data | — |
| `vykdymo_nuo_data` | `date` | `D` | `4` | `open` | — | Projektų su šia priemonė vykdymo pradžios data | — |
| `vykdymo_iki_data` | `date` | `D` | `4` | `open` | — | Projektų su šia priemonė vykdymo pabaigos data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paskirtas_biudzetas` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sppd/socialiniu_projektu_duomenys.csv
