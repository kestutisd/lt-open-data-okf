---
type: Table
title: "Zymejimas — Rinkėjų žymėjimai"
description: "Rinkėjų balsų žymėjimų lentelė."
resource: "https://get.data.gov.lt/datasets/gov/vrk/rinkeju_demografiniai_duomenys/Zymejimas"
tags: [gov, vrk, zymejimas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L14"
    title: "atviriduomenys/manifest — datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L14"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2808/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vrk/rinkeju_demografiniai_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Zymejimas — Rinkėjų žymėjimai

Rinkėjų balsų žymėjimų lentelė. Vienas įrašas atitinka vieno rinkėjo (ne)balsavimo žymėjimą konkrečiuose rinkimuose. Lentelė sudaryta iš pseudonimizuoto rinkėjo asmens kodo, vykdomų rinkimų turo ir balsavimo apygardos dentifikatorių.[^manifest]

- **Model:** `datasets/gov/vrk/rinkeju_demografiniai_duomenys/Zymejimas`[^manifest]
- **Dataset:** [Rinkėjų demografiniai duomenys](../rinkeju_demografiniai_duomenys.md) (`datasets/gov/vrk/rinkeju_demografiniai_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L14)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vrk/rinkeju_demografiniai_duomenys/Zymejimas` (`deployed`)[^manifest]
- **Provider:** `vrk` — Vyriausioji rinkimų komisija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `rinkejo_asm_k` | `string` | — | `4` | `open` | — | Rinkėjo pseudonimizuotas asmens kodas | — |
| `rinkimu_turo_id` | `string` | — | `4` | `open` | — | Vykdomų rinkimų turo identifikatorius | — |
| `faktines_apygardos_id` | `string` | — | `4` | `open` | — | Apygardos, kurioje nubalsuota, identifikatorius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L14 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L14)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vrk/rinkeju_demografiniai_duomenys (https://data.gov.lt/datasets/2808/)
