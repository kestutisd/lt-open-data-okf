---
type: Table
title: "Zymejimas — Rinkėjų žymėjimai"
description: "Rinkėjų balsų žymėjimų lentelė."
resource: "https://get.data.gov.lt/datasets/gov/vrk/rinkeju_demografiniai_duomenys/Zymejimas"
tags: [gov, vrk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L14"
    last_modified: "2026-11-11T14:39:20Z"
---

# Zymejimas — Rinkėjų žymėjimai

Rinkėjų balsų žymėjimų lentelė. Vienas įrašas atitinka vieno rinkėjo (ne)balsavimo žymėjimą konkrečiuose rinkimuose. Lentelė sudaryta iš pseudonimizuoto rinkėjo asmens kodo, vykdomų rinkimų turo ir balsavimo apygardos dentifikatorių.

- **Model:** `datasets/gov/vrk/rinkeju_demografiniai_duomenys/Zymejimas`[^manifest]
- **Dataset:** [Rinkėjų demografiniai duomenys](../rinkeju_demografiniai_duomenys.md) (`datasets/gov/vrk/rinkeju_demografiniai_duomenys`)
- **Manifest CSV:** [datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L14)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vrk/rinkeju_demografiniai_duomenys/Zymejimas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `rinkejo_asm_k` | `string` | — | `4` | `open` | — | Rinkėjo pseudonimizuotas asmens kodas | — |
| `rinkimu_turo_id` | `string` | — | `4` | `open` | — | Vykdomų rinkimų turo identifikatorius | — |
| `faktines_apygardos_id` | `string` | — | `4` | `open` | — | Apygardos, kurioje nubalsuota, identifikatorius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv
