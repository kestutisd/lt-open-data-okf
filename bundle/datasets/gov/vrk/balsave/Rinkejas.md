---
type: Table
title: "Rinkejas"
description: "Spinta table datasets/gov/vrk/balsave/Rinkejas (16 columns)."
tags: [gov, vrk, rinkejas, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/balsave.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vrk/balsave.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Rinkejas

- **Model:** `datasets/gov/vrk/balsave/Rinkejas`[^manifest]
- **Dataset:** [datasets/gov/vrk/balsave](../balsave.md) (`datasets/gov/vrk/balsave`)[^manifest]
- **Manifest CSV:** [datasets/gov/vrk/balsave.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/balsave.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `vrk` — Vyriausioji rinkimų komisija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `apyg_id, rink_turo_apyl_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rink_turo_id` | `integer` | — | `4` | `open` | — | Rinkimų turo apylinkės identifikatorius | — |
| `rink_turo_pavad` | `string` | — | `4` | `open` | — | Rinkimų turo pavadinimas | — |
| `apyg_id` | `integer` | — | `4` | `open` | — | Apygardos identifikatorius | — |
| `apyg_nr` | `integer` | — | `4` | `open` | — | Apygardos numeris | — |
| `apyg_pavad` | `string` | — | `4` | `open` | — | Apygardos pavadinimas | — |
| `rink_turo_apyl_id` | `integer` | — | `4` | `open` | — | Rinkimų turo apylinkės identifikatorius | — |
| `apyl_id` | `integer` | — | `4` | `open` | — | Apylinkės identifikatorius | — |
| `apyl_unik_nr` | `integer` | — | `4` | `open` | — | Unikalus apylinkės numeris | — |
| `apyl_nr` | `integer` | — | `4` | `open` | — | Apylinkės numeris | — |
| `apyl_pavad` | `string` | — | `4` | `open` | — | Apylinkės pavadinimas | — |
| `sav_kodas` | `integer` | — | `4` | `open` | — | Savivaldybės identifikavimo kodas | — |
| `sav_pavadinimas` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `lytis` | `string` | — | `4` | `open` | — | Rinkėjų lytis | — |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Rinkėjų amžiaus grupė (rinkimų dieną) | — |
| `rinkeju_sarase` | `integer` | `U` | `4` | `open` | — | Rinkėjų skaičius galutiniame rinkėjų sąraše | — |
| `atvyko_balsuoti` | `integer` | `U` | `4` | `open` | — | Atvykusių balsuoti rinkėjų skaičius | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |
| `amziaus_grupe` | `"18-24"` | — | — | Amžiaus grupė nuo 18 iki 24 metų | — |
| `amziaus_grupe` | `"25-29"` | — | — | Amžiaus grupė nuo 25 iki 29 metų | — |
| `amziaus_grupe` | `"30-34"` | — | — | Amžiaus grupė nuo 30 iki 34 metų | — |
| `amziaus_grupe` | `"35-39"` | — | — | Amžiaus grupė nuo 35 iki 39 metų | — |
| `amziaus_grupe` | `"40-44"` | — | — | Amžiaus grupė nuo 40 iki 44 metų | — |
| `amziaus_grupe` | `"45-49"` | — | — | Amžiaus grupė nuo 45 iki 49 metų | — |
| `amziaus_grupe` | `"50-54"` | — | — | Amžiaus grupė nuo 50 iki 54 metų | — |
| `amziaus_grupe` | `"55-59"` | — | — | Amžiaus grupė nuo 55 iki 59 metų | — |
| `amziaus_grupe` | `"60-64"` | — | — | Amžiaus grupė nuo 60 iki 64 metų | — |
| `amziaus_grupe` | `"65-69"` | — | — | Amžiaus grupė nuo 65 iki 69 metų | — |
| `amziaus_grupe` | `"70-74"` | — | — | Amžiaus grupė nuo 70 iki 74 metų | — |
| `amziaus_grupe` | `"75-79"` | — | — | Amžiaus grupė nuo 75 iki 79 metų | — |
| `amziaus_grupe` | `"80+"` | — | — | Amžiaus grupė nuo 80 metų | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sav_kodas` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gpv/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `sav_kodas` | `update(property: "savivaldybe.sav_kodas", type: "")` | `property` | `4` | `open` | — | — | — |
| `sav_pavadinimas` | `update(property: "savivaldybe.sav_pavadinimas", type: "")` | `property` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/balsave.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/balsave.csv#L6)
