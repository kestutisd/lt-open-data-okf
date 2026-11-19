---
type: Table
title: "Patalpa — Sutartys dėl gyvenamųjų ir negyvenamųjų patalpų"
description: "Informacija apie Marijampolės savivaldybės sudarytas sutartis dėl gyvenamųjų ir negyvenamųjų patalpų"
resource: "https://get.data.gov.lt/datasets/gov/marijampoles_sav/savivaldybes_objektai/Patalpa"
tags: [gov, marijampoles_sav, patalpa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/savivaldybes_objektai.csv#L28"
    title: "atviriduomenys/manifest — datasets/gov/marijampoles_sav/savivaldybes_objektai.csv#L28"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Patalpa — Sutartys dėl gyvenamųjų ir negyvenamųjų patalpų

Informacija apie Marijampolės savivaldybės sudarytas sutartis dėl gyvenamųjų ir negyvenamųjų patalpų[^manifest]

- **Model:** `datasets/gov/marijampoles_sav/savivaldybes_objektai/Patalpa`[^manifest]
- **Dataset:** [Sutartys dėl nekilnojamo turto objektų](../savivaldybes_objektai.md) (`datasets/gov/marijampoles_sav/savivaldybes_objektai`)[^manifest]
- **Manifest CSV:** [datasets/gov/marijampoles_sav/savivaldybes_objektai.csv#L28](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/savivaldybes_objektai.csv#L28)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/marijampoles_sav/savivaldybes_objektai/Patalpa` (`deployed`)[^manifest]
- **Provider:** `marijampoles_sav` — Marijampolės savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA eilutes identifikatorius | — |
| `objekto_id` | `string` | — | `4` | `open` | — | Objekto identifikatorius | — |
| `ntr_kodas` | `string` | — | `4` | `open` | — | Nekilnojamo turto registro kodas | — |
| `objekto_aprasymas` | `string` | — | `4` | `open` | — | Objekto aprašymas | — |
| `objekto_plotas` | `number` | — | `4` | `open` | — | Objekto plotas kvadratiniais metrais | — |
| `registro_tipas` | `string` | — | `4` | `open` | — | Objekto registro tipas | — |
| `statybos_metai` | `date` | `Y` | `4` | `open` | — | Objekto statybos metai | — |
| `sutarties_numeris` | `string` | — | `4` | `open` | — | Sutarties numeris | — |
| `sutarties_pasirasymo_data` | `date` | `D` | `4` | `open` | — | Sutarties pasirašymo data | — |
| `sutarties_galiojimo_pabaiga` | `date` | `D` | `4` | `open` | — | Sutarties galiojimo pabaigos data | — |
| `sutarties_tipas` | `string` | — | `4` | `open` | — | Sutarties tipas | — |
| `miestas` | `string` | — | `4` | `open` | — | Miestas arba miestelis, kuriame yra objektas | — |
| `gatve` | `string` | — | `4` | `open` | — | Gatvė, kurioje yra objektas | — |
| `seniunija` | `string` | — | `4` | `open` | — | Seniūnija, kurioje yra objektas | — |
| `namo_numeris` | `string` | — | `4` | `open` | — | Objekto namo numeris | — |
| `buto_numeris` | `string` | — | `4` | `open` | — | Objekto buto numeris | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `registro_tipas` | `"Patalpos/butai"` | — | — | — | — |
| `sutarties_tipas` | `"Nuoma"` | — | — | — | — |
| `sutarties_tipas` | `"Panauda"` | — | — | — | — |
| `sutarties_tipas` | `"Patikėjimo teisė"` | — | — | — | — |
| `sutarties_tipas` | `"Subnuoma"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/marijampoles_sav/savivaldybes_objektai.csv#L28 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/savivaldybes_objektai.csv#L28)
