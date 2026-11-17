---
type: Table
title: "Paslauga — Asmens sveikatos priežiūros paslaugų, priskirtų PSDF biudžeto straipsniams, sąrašas"
description: "Informacija apie asmens sveikatos priežiūros paslaugų, priskirtų PSDF biudžeto straipsniams, sąrašą"
resource: "https://get.data.gov.lt/datasets/gov/vlk/straipsniai/Paslauga"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/straipsniai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/straipsniai.csv#L11"
    last_modified: "2026-11-11T14:39:20Z"
---

# Paslauga — Asmens sveikatos priežiūros paslaugų, priskirtų PSDF biudžeto straipsniams, sąrašas

Informacija apie asmens sveikatos priežiūros paslaugų, priskirtų PSDF biudžeto straipsniams, sąrašą

- **Model:** `datasets/gov/vlk/straipsniai/Paslauga`[^manifest]
- **Dataset:** [datasets/gov/vlk/straipsniai](../straipsniai.md) (`datasets/gov/vlk/straipsniai`)
- **Manifest CSV:** [datasets/gov/vlk/straipsniai.csv#L11](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/straipsniai.csv#L11)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/straipsniai/Paslauga`
- **Primary Key (`ref`):** `ad_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `straipsnis` | `integer` | — | `4` | `open` | — | Nuoroda į Straipsnis | — |
| `nuo` | `date` | `D` | `4` | `open` | — | Paslauga galioja nuo | Paslaugos priskyrimo atitinkamam PSDF biudžeto straipsniui pradžios data |
| `iki` | `date` | `D` | `4` | `open` | — | Paslauga galioja iki | Paslaugos priskyrimo atitinkamam PSDF biudžeto išlaidų straipsniui pabaigos data |
| `kodas` | `ref` | [/datasets/gov/vlk/paslaugos/Paslauga[kodas]](../paslaugos/Paslauga.md) | `4` | `open` | — | Nuoroda į Paslauga[kodas] | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/straipsniai.csv
