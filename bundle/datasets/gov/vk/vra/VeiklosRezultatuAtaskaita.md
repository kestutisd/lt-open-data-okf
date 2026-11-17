---
type: Table
title: "VeiklosRezultatuAtaskaita — Veiklos rezultatų ataskaita"
description: "Valstybės kontrolės veiklos rezultatų ataskaitos duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vk/vra/VeiklosRezultatuAtaskaita"
tags: [gov, vk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vk/vra.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/vra.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# VeiklosRezultatuAtaskaita — Veiklos rezultatų ataskaita

Valstybės kontrolės veiklos rezultatų ataskaitos duomenys

- **Model:** `datasets/gov/vk/vra/VeiklosRezultatuAtaskaita`[^manifest]
- **Dataset:** [datasets/gov/vk/vra](../vra.md) (`datasets/gov/vk/vra`)
- **Manifest CSV:** [datasets/gov/vk/vra.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/vra.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/vra/VeiklosRezultatuAtaskaita`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ataskaitiniai_metai` | `integer` | — | `2` | `open` | — | Metai | Metai |
| `grupe_i_kodas` | `string` | — | `3` | `open` | — | Straipsnio I grupės kodas | Straipsnio I grupės kodas |
| `grupe_i_pavadinimas` | `string` | — | `3` | `open` | — | Straipsnio I grupės pavadinimas | Straipsnio I grupės pavadinimas |
| `grupe_ii_kodas` | `string` | — | `3` | `open` | — | Straipsnio II grupės kodas | Straipsnio II grupės kodas |
| `grupe_ii_pavadinimas` | `string` | — | `3` | `open` | — | Straipsnio II grupės pavadinimas | Straipsnio II grupės pavadinimas |
| `grupe_iii_kodas` | `string` | — | `3` | `open` | — | Straipsnio III grupės kodas | Straipsnio III grupės kodas |
| `grupe_iii_pavadinimas` | `string` | — | `3` | `open` | — | Straipsnio III grupės pavadinimas | Straipsnio III grupės pavadinimas |
| `eur_ataskaskaitinio_laikotarpio` | `number` | — | `2` | `open` | — | Ataskaitinis laikotarpis | Ataskaitinis laikotarpis, suma Eur |
| `eur_praejusio_ataskaitinio_laikotarpio` | `number` | — | `2` | `open` | — | Praėjęs ataskaitinis laikotarpis | Praėjęs ataskaitinis laikotarpis, suma Eur |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ataskaitiniai_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `eur_ataskaskaitinio_laikotarpio` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `eur_praejusio_ataskaitinio_laikotarpio` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/vra.csv
