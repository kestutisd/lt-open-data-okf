---
type: Table
title: "Straipsnis — PSDF biudžeto straipsnių sąrašas"
description: "PSDF biudžeto straipsnių, pagal kuriuos apmokamos asmens sveikatos priežiūros paslaugos, sąrašas"
resource: "https://get.data.gov.lt/datasets/gov/vlk/straipsniai/Straipsnis"
tags: [gov, vlk, straipsnis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/straipsniai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/vlk/straipsniai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2279/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/straipsniai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Straipsnis — PSDF biudžeto straipsnių sąrašas

PSDF biudžeto straipsnių, pagal kuriuos apmokamos asmens sveikatos priežiūros paslaugos, sąrašas[^manifest]

- **Model:** `datasets/gov/vlk/straipsniai/Straipsnis`[^manifest]
- **Dataset:** [PSDF biudžeto išlaidų straipsnių sąrašas](../straipsniai.md) (`datasets/gov/vlk/straipsniai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/straipsniai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/straipsniai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/straipsniai/Straipsnis` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ad_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `kodas` | `string` | — | `4` | `open` | — | Straipsnio kodas | PSDF biudžeto straipsnio kodas pagal Klasifikatorių |
| `pavadinimas` | `string` | — | `4` | `open` | — | Straipsnio pavadinimas | PSDF biudžeto straipsnio pavadinimas pagal Klasifikatorių |
| `nuo` | `date` | `D` | `4` | `open` | — | Strapsnis galioja nuo | PSDF biudžeto straipsnio galiojimo pradžios data. Prie kai kurių PSDF biudžeto straipsnių ši data gali būti nenurodyta, nes IS „Sveidra“ ši data neįvesta |
| `iki` | `date` | `D` | `4` | `open` | — | Straipsnis galioja iki | PSDF biudžeto straipsnio galiojimo pabaigos data. Prie kai kurių PSDF biudžeto straipsnių ši data gali būti nenurodyta, nes IS „Sveidra“ ši data neįvesta |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/straipsniai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/straipsniai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/straipsniai (https://data.gov.lt/datasets/2279/)
