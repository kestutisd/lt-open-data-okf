---
type: Table
title: "Parodymas — Vandens skaitiklių parodymai"
description: "Geriamojo vandens skaitiklių parodymai Telšių rajono savivaldybėje"
resource: "https://get.data.gov.lt/datasets/gov/telsiu_vand/skaitikliu_rodmenys/Parodymas"
tags: [gov, telsiu_vand, parodymas, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/telsiu_vand/skaitikliu_rodmenys.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/telsiu_vand/skaitikliu_rodmenys.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3842/"
    title: "data.gov.lt DCAT-AP — datasets/gov/telsiu_vand/skaitikliu_rodmenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Parodymas — Vandens skaitiklių parodymai

Geriamojo vandens skaitiklių parodymai Telšių rajono savivaldybėje[^manifest]

- **Model:** `datasets/gov/telsiu_vand/skaitikliu_rodmenys/Parodymas`[^manifest]
- **Dataset:** [Vandens skaitiklių parodymai](../skaitikliu_rodmenys.md) (`datasets/gov/telsiu_vand/skaitikliu_rodmenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/telsiu_vand/skaitikliu_rodmenys.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/telsiu_vand/skaitikliu_rodmenys.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/telsiu_vand/skaitikliu_rodmenys/Parodymas` (`deployed`)[^manifest]
- **Provider:** `telsiu_vand` — UAB "Telšių vandenys" *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `operacijos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `deklaracijos_tipas` | `"Iš failo"` | — | — | — | — |
| `deklaracijos_tipas` | `"Įvesta ranka"` | — | — | — | — |
| `deklaracijos_tipas` | `"Internetu"` | — | — | — | — |
| `moketojo_tipas` | `"Gyventojas"` | — | — | — | — |
| `moketojo_tipas` | `"Įmonė"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/telsiu_vand/skaitikliu_rodmenys.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/telsiu_vand/skaitikliu_rodmenys.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/telsiu_vand/skaitikliu_rodmenys (https://data.gov.lt/datasets/3842/)
