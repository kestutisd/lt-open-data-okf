---
type: Table
title: "Apygarda — Rinkimų apygardos"
description: "Rinkimų apygardų lentelė."
resource: "https://get.data.gov.lt/datasets/gov/vrk/rinkeju_demografiniai_duomenys/Apygarda"
tags: [gov, vrk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L20"
    last_modified: "2026-11-11T14:39:20Z"
---

# Apygarda — Rinkimų apygardos

Rinkimų apygardų lentelė. Vienas įrašas atitinka vieną apygardą tam tikrų rinkimų metu. Lentelė sudaryta iš apygardos identifikatoriaus ir pavadinimo.

- **Model:** `datasets/gov/vrk/rinkeju_demografiniai_duomenys/Apygarda`[^manifest]
- **Dataset:** [Rinkėjų demografiniai duomenys](../rinkeju_demografiniai_duomenys.md) (`datasets/gov/vrk/rinkeju_demografiniai_duomenys`)
- **Manifest CSV:** [datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L20](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L20)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vrk/rinkeju_demografiniai_duomenys/Apygarda`
- **Primary Key (`ref`):** `apygardos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `apygardos_id` | `string` | — | `4` | `open` | — | Apygardos identifikatorius | — |
| `apygardos_pav` | `string` | — | `4` | `open` | — | Apygardos pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv
