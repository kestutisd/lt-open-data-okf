---
type: Table
title: "Straipsnis — PSDF biudžeto straipsnių sąrašas"
description: "PSDF biudžeto straipsnių, pagal kuriuos apmokamos asmens sveikatos priežiūros paslaugos, sąrašas"
resource: "https://get.data.gov.lt/datasets/gov/vlk/straipsniai/Straipsnis"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/straipsniai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/straipsniai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Straipsnis — PSDF biudžeto straipsnių sąrašas

PSDF biudžeto straipsnių, pagal kuriuos apmokamos asmens sveikatos priežiūros paslaugos, sąrašas

- **Model:** `datasets/gov/vlk/straipsniai/Straipsnis`[^manifest]
- **Dataset:** [datasets/gov/vlk/straipsniai](../straipsniai.md) (`datasets/gov/vlk/straipsniai`)
- **Manifest CSV:** [datasets/gov/vlk/straipsniai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/straipsniai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/straipsniai/Straipsnis`
- **Primary Key (`ref`):** `ad_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `kodas` | `string` | — | `4` | `open` | — | Straipsnio kodas | PSDF biudžeto straipsnio kodas pagal Klasifikatorių |
| `pavadinimas` | `string` | — | `4` | `open` | — | Straipsnio pavadinimas | PSDF biudžeto straipsnio pavadinimas pagal Klasifikatorių |
| `nuo` | `date` | `D` | `4` | `open` | — | Strapsnis galioja nuo | PSDF biudžeto straipsnio galiojimo pradžios data. Prie kai kurių PSDF biudžeto straipsnių ši data gali būti nenurodyta, nes IS „Sveidra“ ši data neįvesta |
| `iki` | `date` | `D` | `4` | `open` | — | Straipsnis galioja iki | PSDF biudžeto straipsnio galiojimo pabaigos data. Prie kai kurių PSDF biudžeto straipsnių ši data gali būti nenurodyta, nes IS „Sveidra“ ši data neįvesta |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/straipsniai.csv
