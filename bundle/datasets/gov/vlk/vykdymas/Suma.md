---
type: Table
title: "Suma — PSDF biudžeto vykdymo ataskaitos duomenys"
description: "Informacija apie PSDF biudžeto vykdymą"
resource: "https://get.data.gov.lt/datasets/gov/vlk/vykdymas/Suma"
tags: [gov, vlk, suma, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/vykdymas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vlk/vykdymas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1803/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/vykdymas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Suma — PSDF biudžeto vykdymo ataskaitos duomenys

Informacija apie PSDF biudžeto vykdymą[^manifest]

- **Model:** `datasets/gov/vlk/vykdymas/Suma`[^manifest]
- **Dataset:** [PSDF biudžeto vykdymo ataskaitos duomenys](../vykdymas.md) (`datasets/gov/vlk/vykdymas`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/vykdymas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/vykdymas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/vykdymas/Suma` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ad_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/vykdymas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/vykdymas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/vykdymas (https://data.gov.lt/datasets/1803/)
