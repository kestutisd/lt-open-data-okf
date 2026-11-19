---
type: Table
title: "Balas — Bazinių kainų balais sąrašas"
description: "Asmens sveikatos priežiūros paslaugų bazinių balų sąrašas"
resource: "https://get.data.gov.lt/datasets/gov/vlk/paslaugos/Balas"
tags: [gov, vlk, balas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/paslaugos.csv#L30"
    title: "atviriduomenys/manifest — datasets/gov/vlk/paslaugos.csv#L30"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1385/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/paslaugos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Balas — Bazinių kainų balais sąrašas

Asmens sveikatos priežiūros paslaugų bazinių balų sąrašas[^manifest]

- **Model:** `datasets/gov/vlk/paslaugos/Balas`[^manifest]
- **Dataset:** [Asmens sveikatos priežiūros paslaugų sąrašas](../paslaugos.md) (`datasets/gov/vlk/paslaugos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/paslaugos.csv#L30](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/paslaugos.csv#L30)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/paslaugos/Balas` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ad_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `paslauga` | `ref` | [Paslauga](Paslauga.md) (`level=4 UUID`: `paslauga._id`) | `4` | `open` | — | Nuoroda į paslaugas | — |
| `lovadieniui` | `number` | — | `4` | `open` | — | Balai lovadieniui | — |
| `atvejui` | `number` | — | `4` | `open` | — | Balai atvejui | — |
| `nuo` | `date` | `D` | `4` | `open` | — | Galioja nuo | — |
| `iki` | `date` | `D` | `4` | `open` | — | Galioja iki | — |
| `verte` | `number` | — | `4` | `open` | — | Bazinio balo vertė | — |
| `trukme` | `integer` | `U` | `4` | `open` | — | Vidutinė paslaugos trukmė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/paslaugos.csv#L30 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/paslaugos.csv#L30)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/paslaugos (https://data.gov.lt/datasets/1385/)
