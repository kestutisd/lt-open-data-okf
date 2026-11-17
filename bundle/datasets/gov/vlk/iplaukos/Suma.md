---
type: Table
title: "Suma — Privalomojo sveikatos draudimo fondo biudžeto įplaukų plano vykdymo ataskaita"
description: "Informacija apie Privalomojo sveikatos draudimo fondo biudžeto įplaukas"
resource: "https://get.data.gov.lt/datasets/gov/vlk/iplaukos/Suma"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/iplaukos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/iplaukos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Suma — Privalomojo sveikatos draudimo fondo biudžeto įplaukų plano vykdymo ataskaita

Informacija apie Privalomojo sveikatos draudimo fondo biudžeto įplaukas

- **Model:** `datasets/gov/vlk/iplaukos/Suma`[^manifest]
- **Dataset:** [datasets/gov/vlk/iplaukos](../iplaukos.md) (`datasets/gov/vlk/iplaukos`)
- **Manifest CSV:** [datasets/gov/vlk/iplaukos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/iplaukos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/iplaukos/Suma`
- **Primary Key (`ref`):** `ad_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `str_kodas` | `string` | — | `3` | `open` | — | Įplaukų straipsnio kodas | — |
| `str_pavadinimas` | `string` | — | `3` | `open` | — | Įplaukų straipsnio pavadinimas | — |
| `tikslinimas` | `string` | — | `3` | `open` | — | Patikslinimas | — |
| `gautinos_sumos_pradzioje` | `number` | — | `2` | `open` | — | Ataskaitinio laikotarpio pradžioje - gautinos sumos | — |
| `moketinos_sumos_pradzioje` | `number` | — | `2` | `open` | — | Ataskaitinio laikotarpio pradžioje - mokėtinos sumos | — |
| `planuotos_sumos` | `number` | — | `2` | `open` | — | Ataskaitinį laikotarpį - planuotos sumos | — |
| `gautinos_sumos` | `number` | — | `2` | `open` | — | Ataskaitinį laikotarpį - gautinos sumos | — |
| `gautos_sumos` | `number` | — | `2` | `open` | — | Ataskaitinį laikotarpį - gautos sumos | — |
| `gautinos_sumos_pabaigoje` | `number` | — | `2` | `open` | — | Ataskaitinio laikotarpio pabaigoje - gautinos sumos | — |
| `moketinos_sumos_pabaigoje` | `number` | — | `2` | `open` | — | Ataskaitinio laikotarpio pabaigoje - mokėtinos sumos | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | `open` | — | — | — |
| `gautinos_sumos_pradzioje` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `moketinos_sumos_pradzioje` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `planuotos_sumos` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `gautinos_sumos` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `gautos_sumos` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `gautinos_sumos_pabaigoje` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `moketinos_sumos_pabaigoje` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/iplaukos.csv
