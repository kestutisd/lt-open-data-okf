---
type: Table
title: "FinansinesBuklesAtaskaita — Finansinės būklės ataskaita"
description: "Valstybės kontrolės finansinės būklės ataskaitos duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vk/fba/FinansinesBuklesAtaskaita"
tags: [gov, vk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vk/fba.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/fba.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# FinansinesBuklesAtaskaita — Finansinės būklės ataskaita

Valstybės kontrolės finansinės būklės ataskaitos duomenys

- **Model:** `datasets/gov/vk/fba/FinansinesBuklesAtaskaita`[^manifest]
- **Dataset:** [datasets/gov/vk/fba](../fba.md) (`datasets/gov/vk/fba`)
- **Manifest CSV:** [datasets/gov/vk/fba.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/fba.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/fba/FinansinesBuklesAtaskaita`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ataskaitiniai_metai` | `integer` | — | `2` | `open` | — | Metai | Metai |
| `grupe_i_pavadinimas` | `string` | — | `3` | `open` | — | Straipsnio I grupės pavadinimas | Straipsnio I grupės pavadinimas |
| `grupe_ii_kodas` | `string` | — | `3` | `open` | — | Straipsnio II grupės kodas | Straipsnio II grupės kodas |
| `grupe_ii_pavadinimas` | `string` | — | `3` | `open` | — | Straipsnio II grupės pavadinimas | Straipsnio II grupės pavadinimas |
| `grupe_iii_kodas` | `string` | — | `3` | `open` | — | Straipsnio III grupės kodas | Straipsnio III grupės kodas |
| `grupe_iii_pavadinimas` | `string` | — | `3` | `open` | — | Straipsnio III grupės pavadinimas | Straipsnio III grupės pavadinimas |
| `grupe_iv_kodas` | `string` | — | `3` | `open` | — | Straipsnio IV grupės kodas | Straipsnio IV grupės kodas |
| `grupe_iv_pavadinimas` | `string` | — | `3` | `open` | — | Straipsnio IV grupės pavadinimas | Straipsnio IV grupės pavadinimas |
| `grupe_v_kodas` | `string` | — | `3` | `open` | — | Straipsnio V grupės kodas | Straipsnio V grupės kodas |
| `grupe_v_pavadinimas` | `string` | — | `3` | `open` | — | Straipsnio V grupės pavadinimas | Straipsnio V grupės pavadinimas |
| `paskutine_ataskaitinio_laikotarpio_diena` | `number` | — | `2` | `open` | — | Paskutinė ataskaitinio laikotarpio diena | Paskutinė ataskaitinio laikotarpio diena, suma Eur |
| `paskutine_praejusio_ataskaitinio_laikotarpio_diena` | `number` | — | `2` | `open` | — | Paskutinė praėjusio ataskaitinio laikotarpio diena | Paskutinė praėjusio ataskaitinio laikotarpio diena, suma Eur |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ataskaitiniai_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `paskutine_ataskaitinio_laikotarpio_diena` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `paskutine_praejusio_ataskaitinio_laikotarpio_diena` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/fba.csv
