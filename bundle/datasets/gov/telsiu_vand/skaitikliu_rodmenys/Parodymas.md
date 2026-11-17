---
type: Table
title: "Parodymas — Vandens skaitiklių parodymai"
description: "Geriamojo vandens skaitiklių parodymai Telšių rajono savivaldybėje"
resource: "https://get.data.gov.lt/datasets/gov/telsiu_vand/skaitikliu_rodmenys/Parodymas"
tags: [gov, telsiu_vand, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/telsiu_vand/skaitikliu_rodmenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/telsiu_vand/skaitikliu_rodmenys.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Parodymas — Vandens skaitiklių parodymai

Geriamojo vandens skaitiklių parodymai Telšių rajono savivaldybėje

- **Model:** `datasets/gov/telsiu_vand/skaitikliu_rodmenys/Parodymas`[^manifest]
- **Dataset:** [Vandens skaitiklių parodymai](../skaitikliu_rodmenys.md) (`datasets/gov/telsiu_vand/skaitikliu_rodmenys`)
- **Manifest CSV:** [datasets/gov/telsiu_vand/skaitikliu_rodmenys.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/telsiu_vand/skaitikliu_rodmenys.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/telsiu_vand/skaitikliu_rodmenys/Parodymas`
- **Primary Key (`ref`):** `operacijos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `operacijos_id` | `string` | — | `4` | `open` | — | Operacijos identifikatorius | — |
| `skaitiklio_id` | `string` | — | `4` | `open` | — | Šifruotas skaitiklio identifikatorius | — |
| `abonento_id` | `string` | — | `4` | `open` | — | Šifruotas abonento identifikatorius | — |
| `triuksminta_objekto_koordinate_lks` | `string` | — | `4` | `open` | — | Triukšminta objekto koordinatė LKS sistemoje | — |
| `koordinates_patikimumas_balais` | `number` | — | `4` | `open` | — | Koordinatės patikimumas balais | — |
| `nuo_data` | `date` | `D` | `4` | `open` | — | Skaitiklio deklaravimo periodo data nuo | — |
| `iki_data` | `date` | `D` | `4` | `open` | — | Skaitiklio deklaravimo periodo data iki | — |
| `skaitiklio_rodmuo_nuo` | `number` | — | `4` | `open` | — | Skaitiklio deklaruojami rodmenys nuo m^3 | — |
| `skaitiklio_rodmuo_iki` | `number` | — | `4` | `open` | — | Skaitiklio deklaruojami duomenys iki m^3 | — |
| `vandens_kiekis` | `number` | — | `4` | `open` | — | Sunaudoto vandens kiekis m^3 | — |
| `deklaravimo_data` | `date` | `D` | `4` | `open` | — | Skaitiklio deklaravimo data | — |
| `deklaracijos_tipas` | `string` | — | `4` | `open` | — | Deklaravimo tipas | — |
| `tarifo_pavadinimas` | `string` | — | `4` | `open` | — | Tarifo pavadinimas | — |
| `moketojo_tipas` | `string` | — | `4` | `open` | — | Mokėtojo tipas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `deklaracijos_tipas` | `"Iš failo"` | — | — | — | — |
| `deklaracijos_tipas` | `"Įvesta ranka"` | — | — | — | — |
| `deklaracijos_tipas` | `"Internetu"` | — | — | — | — |
| `moketojo_tipas` | `"Gyventojas"` | — | — | — | — |
| `moketojo_tipas` | `"Įmonė"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/telsiu_vand/skaitikliu_rodmenys.csv
