---
type: Table
title: "ZemesSklypas — Sutartys dėl žemės sklypų"
description: "Informacija apie Marijampolės savivaldybės sudarytas sutartis dėl žemės sklypų"
resource: "https://get.data.gov.lt/datasets/gov/marijampoles_sav/savivaldybes_objektai/ZemesSklypas"
tags: [gov, marijampoles_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/marijampoles_sav/savivaldybes_objektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/savivaldybes_objektai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# ZemesSklypas — Sutartys dėl žemės sklypų

Informacija apie Marijampolės savivaldybės sudarytas sutartis dėl žemės sklypų

- **Model:** `datasets/gov/marijampoles_sav/savivaldybes_objektai/ZemesSklypas`[^manifest]
- **Dataset:** [Sutartys dėl nekilnojamo turto objektų](../savivaldybes_objektai.md) (`datasets/gov/marijampoles_sav/savivaldybes_objektai`)
- **Manifest CSV:** [datasets/gov/marijampoles_sav/savivaldybes_objektai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/savivaldybes_objektai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/marijampoles_sav/savivaldybes_objektai/ZemesSklypas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA eilutes identifikatorius | — |
| `objekto_id` | `string` | — | `4` | `open` | — | Objekto identifikatorius | — |
| `ntr_kodas` | `string` | — | `4` | `open` | — | Nekilnojamo turto registro kodas | — |
| `objekto_aprasymas` | `string` | — | `4` | `open` | — | Objekto aprašymas | — |
| `plotas_ha` | `number` | — | `4` | `open` | — | Plotas hektarais | — |
| `sutarties_numeris` | `string` | — | `4` | `open` | — | Sutarties numeris | — |
| `sutarties_pasirasymo_data` | `date` | `D` | `4` | `open` | — | Sutarties pasirašymo data | — |
| `sutarties_galiojimo_pabaiga` | `date` | `D` | `4` | `open` | — | Sutarties galiojimo pabaigos data | — |
| `sutarties_tipas` | `string` | — | `4` | `open` | — | Sutarties tipas | — |
| `miestas` | `string` | — | `4` | `open` | — | Miestas arba miestelis, kuriame yra objektas | — |
| `gatve` | `string` | — | `4` | `open` | — | Gatvė, kurioje yra objektas | — |
| `seniunija` | `string` | — | `4` | `open` | — | Seniūnija, kurioje yra objektas | — |
| `namo_numeris` | `string` | — | `4` | `open` | — | Objekto namo numeris | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `objekto_aprasymas` | `"Žemės sklypas"` | — | — | — | — |
| `objekto_aprasymas` | `"Žemės sklypo dalis"` | — | — | — | — |
| `sutarties_tipas` | `"Patikėjimo teisė"` | — | — | Patikėjimo teise valdomas objektas | — |
| `sutarties_tipas` | `"Nuoma"` | — | — | Išnuomojamas objektas | — |
| `sutarties_tipas` | `"Panauda"` | — | — | Panaudos sutartimi valdomas objektas | — |
| `sutarties_tipas` | `"Subnuoma"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/marijampoles_sav/savivaldybes_objektai.csv
