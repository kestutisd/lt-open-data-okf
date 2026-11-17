---
type: Table
title: "Suma — PSDF biudžeto vykdymo ataskaitos duomenys"
description: "Informacija apie PSDF biudžeto vykdymą"
resource: "https://get.data.gov.lt/datasets/gov/vlk/vykdymas/Suma"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/vykdymas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/vykdymas.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Suma — PSDF biudžeto vykdymo ataskaitos duomenys

Informacija apie PSDF biudžeto vykdymą

- **Model:** `datasets/gov/vlk/vykdymas/Suma`[^manifest]
- **Dataset:** [datasets/gov/vlk/vykdymas](../vykdymas.md) (`datasets/gov/vlk/vykdymas`)
- **Manifest CSV:** [datasets/gov/vlk/vykdymas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/vykdymas.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/vykdymas/Suma`
- **Primary Key (`ref`):** `ad_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `str_kodas` | `string` | — | `3` | `open` | — | Išlaidų straipsnio kodas | — |
| `str_pavadinimas` | `string` | — | `3` | `open` | — | Išlaidų straipsnio pavadinimas | — |
| `tlk` | `string` | — | `4` | `open` | — | Teritorinė ligonių kasa | — |
| `gautina_suma_pradzioje` | `number` | — | `2` | `open` | — | Ataskaitinio laikotarpio pradžioje - gautina suma | — |
| `moketina_suma_pradzioje` | `number` | — | `2` | `open` | — | Ataskaitinio laikotarpio pradžioje - mokėtina suma | — |
| `suma_biudzeto_lesos` | `number` | — | `2` | `open` | — | Ataskaitiniam laikotarpiui skirta suma - biudžeto lėšos | — |
| `suma_virsplanines_biudzeto_lesos` | `number` | — | `2` | `open` | — | Ataskaitiniam laikotarpiui skirta suma - viršplaninės biudžeto lėšos | — |
| `suma_rezervo_lesos` | `number` | — | `2` | `open` | — | Ataskaitiniam laikotarpiui skirta suma - rezervo lėšos | — |
| `suma_prisiimti_isipareigojimai` | `number` | — | `2` | `open` | — | Suma pagal prisiimtus įsipareigojimus | — |
| `gauti_asignavimai` | `number` | — | `2` | `open` | — | Gauti asignavimai | — |
| `sumoketa_suma_biudzeto_lesos` | `number` | — | `2` | `open` | — | Sumokėta suma - biudžeto lėšos (kartu su viršplaninėmis biudžeto lėšomis) | — |
| `sumoketa_suma_rezervo_lesos` | `number` | — | `2` | `open` | — | Sumokėta suma - rezervo lėšos | — |
| `gautina_suma_pabaigoje` | `number` | — | `2` | `open` | — | Ataskaitinio laikotarpio pabaigoje - gautina suma | — |
| `moketina_suma_pabaigoje` | `number` | — | `2` | `open` | — | Ataskaitinio laikotarpio pabaigoje - mokėtina suma | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | `open` | — | — | — |
| `gautina_suma_pradzioje` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `moketina_suma_pradzioje` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `suma_biudzeto_lesos` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `suma_virsplanines_biudzeto_lesos` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `suma_rezervo_lesos` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `suma_prisiimti_isipareigojimai` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `gauti_asignavimai` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `sumoketa_suma_biudzeto_lesos` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `sumoketa_suma_rezervo_lesos` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `gautina_suma_pabaigoje` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `moketina_suma_pabaigoje` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/vykdymas.csv
