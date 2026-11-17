---
type: Table
title: "Misle — Mįslės su atsakymais"
description: "Lentelėje pateiktos mįslės su jų įminimais (atsakymais) iš Lietuvių literatūros ir tautosakos instituto Lituanistikos paveldo informacinės sistemos „Aruodai“ (https://www.aruodai.lt/)."
resource: "https://get.data.gov.lt/datasets/gov/llti/misles_su_atsakymais/Misle"
tags: [gov, llti, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/llti/misles_su_atsakymais.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/misles_su_atsakymais.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Misle — Mįslės su atsakymais

Lentelėje pateiktos mįslės su jų įminimais (atsakymais) iš Lietuvių literatūros ir tautosakos instituto Lituanistikos paveldo informacinės sistemos „Aruodai“ (https://www.aruodai.lt/). Pateikiami visi duomenys nuo jų įvedimo į sistemą datos (2013 metų) atnaujinant kas metus.

- **Model:** `datasets/gov/llti/misles_su_atsakymais/Misle`[^manifest]
- **Dataset:** [Mįslės su atsakymais](../misles_su_atsakymais.md) (`datasets/gov/llti/misles_su_atsakymais`)
- **Manifest CSV:** [datasets/gov/llti/misles_su_atsakymais.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/misles_su_atsakymais.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/llti/misles_su_atsakymais/Misle`
- **Primary Key (`ref`):** `misles_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `misles_id` | `string` | — | `4` | `open` | — | Mįslės identifikacinis kodas | — |
| `misles_signatura` | `string` | — | `4` | `open` | — | Mįslės signatūra | — |
| `misle` | `string` | — | `4` | `open` | — | Mįslės tekstas | — |
| `misles_iminimas` | `string` | — | `4` | `open` | — | Mįslės įminimo tekstas arba mįslės atsakymas | — |
| `uzrasymo_vietove` | `string` | — | `4` | `open` | — | Mįslės užrašymo vietovė | — |
| `uzrasymo_vietoves_pastabos` | `string` | — | `4` | `open` | — | Mįslės užrašymo vietovės pastabos | — |
| `misles_gimimo_data` | `date` | `Y` | `4` | `open` | — | Mįslės kilimo metai | — |
| `misles_pateikejo_amzius` | `integer` | — | `4` | `open` | — | Mįslės pateikėjo amžius | — |
| `busena` | `string` | — | `4` | `open` | — | Įrašo būsena | — |
| `ar_aktyvus` | `string` | — | `4` | `open` | — | Ar aktyvus | — |
| `sukurimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo sukūrimo data | — |
| `patvirtinimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo patvirtinimo data | — |
| `atmetimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo atmetimo data | — |
| `modifikavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo modifikavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/llti/misles_su_atsakymais.csv
