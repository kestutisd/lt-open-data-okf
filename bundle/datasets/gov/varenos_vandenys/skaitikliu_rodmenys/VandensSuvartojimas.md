---
type: Table
title: "VandensSuvartojimas — Vandens suvartojimo skaitiklių rodmenys"
description: "Lentelėje pateikiami vandens suvartojimo skaitiklių rodmenys nuo 2005 metų iš UAB „Varėnos vandenys“ apskaitos sistemos PROGRA."
resource: "https://get.data.gov.lt/datasets/gov/varenos_vandenys/skaitikliu_rodmenys/VandensSuvartojimas"
tags: [gov, varenos_vandenys, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/varenos_vandenys/skaitikliu_rodmenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/varenos_vandenys/skaitikliu_rodmenys.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# VandensSuvartojimas — Vandens suvartojimo skaitiklių rodmenys

Lentelėje pateikiami vandens suvartojimo skaitiklių rodmenys nuo 2005 metų iš UAB „Varėnos vandenys“ apskaitos sistemos PROGRA. Duomenys atnaujinami kas mėnesį.

- **Model:** `datasets/gov/varenos_vandenys/skaitikliu_rodmenys/VandensSuvartojimas`[^manifest]
- **Dataset:** [Vandens suvartojimo skaitiklių rodmenys](../skaitikliu_rodmenys.md) (`datasets/gov/varenos_vandenys/skaitikliu_rodmenys`)
- **Manifest CSV:** [datasets/gov/varenos_vandenys/skaitikliu_rodmenys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/varenos_vandenys/skaitikliu_rodmenys.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/varenos_vandenys/skaitikliu_rodmenys/VandensSuvartojimas`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `abonento_id` | `string` | — | `4` | `open` | — | Abonento identifikatorius | — |
| `abonento_miestas` | `string` | — | `4` | `open` | — | Abonento miestas | — |
| `abonento_tipas` | `string` | — | `4` | `open` | — | Abonento tipas | — |
| `ivado_id` | `string` | — | `4` | `open` | — | Įvado identifikatorius | — |
| `skaitiklio_id` | `string` | — | `4` | `open` | — | Skaitiklio identifikatorius | — |
| `ivadosk_pastatymo_vieta` | `string` | — | `4` | `open` | — | Įvado skaitiklio pastatymo vieta | — |
| `nuo` | `number` | `m³` | `4` | `open` | — | Skaitiklio rodmuo "nuo" (m3) | — |
| `iki` | `number` | `m³` | `4` | `open` | — | Skaitiklio rodmuo "iki" (m3) | — |
| `skirtumas` | `number` | `m³` | `4` | `open` | — | Skaitiklio rodmenų skirtumas ("iki" - "nuo") (m3) | — |
| `nuotek_poz` | `string` | — | `4` | `open` | — | Požymis, ar rodmenys apima nuotekas | — |
| `salt_karst` | `boolean` | — | `4` | `open` | — | Požymis, ar vanduo šaltas ("true" - taip, "false" - ne) | — |
| `dekl_men` | `date` | `M` | `4` | `open` | — | Vandens suvartojimo deklaravimo mėnuo | — |
| `apsk_men` | `date` | `M` | `4` | `open` | — | Vandens suvartojimo apskaitos mėnuo | — |
| `kor_data_laikas` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data ir laikas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/varenos_vandenys/skaitikliu_rodmenys.csv
