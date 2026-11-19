---
type: Table
title: "Paslauga — Asmens sveikatos priežiūros paslaugų, priskirtų PSDF biudžeto straipsniams, sąrašas"
description: "Informacija apie asmens sveikatos priežiūros paslaugų, priskirtų PSDF biudžeto straipsniams, sąrašą"
resource: "https://get.data.gov.lt/datasets/gov/vlk/straipsniai/Paslauga"
tags: [gov, vlk, paslauga, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/straipsniai.csv#L11"
    title: "atviriduomenys/manifest — datasets/gov/vlk/straipsniai.csv#L11"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2279/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/straipsniai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Paslauga — Asmens sveikatos priežiūros paslaugų, priskirtų PSDF biudžeto straipsniams, sąrašas

Informacija apie asmens sveikatos priežiūros paslaugų, priskirtų PSDF biudžeto straipsniams, sąrašą[^manifest]

- **Model:** `datasets/gov/vlk/straipsniai/Paslauga`[^manifest]
- **Dataset:** [PSDF biudžeto išlaidų straipsnių sąrašas](../straipsniai.md) (`datasets/gov/vlk/straipsniai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/straipsniai.csv#L11](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/straipsniai.csv#L11)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/straipsniai/Paslauga` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ad_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `straipsnis` | `integer` | — | `4` | `open` | — | Nuoroda į Straipsnis | — |
| `nuo` | `date` | `D` | `4` | `open` | — | Paslauga galioja nuo | Paslaugos priskyrimo atitinkamam PSDF biudžeto straipsniui pradžios data |
| `iki` | `date` | `D` | `4` | `open` | — | Paslauga galioja iki | Paslaugos priskyrimo atitinkamam PSDF biudžeto išlaidų straipsniui pabaigos data |
| `kodas` | `ref` | [Paslauga](../paslaugos/Paslauga.md) (`level=4 UUID` via `Paslauga[kodas]`: `kodas._id`) | `4` | `open` | — | Nuoroda į Paslauga[kodas] | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/straipsniai.csv#L11 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/straipsniai.csv#L11)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/straipsniai (https://data.gov.lt/datasets/2279/)
