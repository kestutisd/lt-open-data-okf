---
type: Table
title: "Misle — Mįslės su atsakymais"
description: "Lentelėje pateiktos mįslės su jų įminimais (atsakymais) iš Lietuvių literatūros ir tautosakos instituto Lituanistikos paveldo informacinės sistemos „Aruodai“ (https://www.aruodai.lt/)."
resource: "https://get.data.gov.lt/datasets/gov/llti/misles_su_atsakymais/Misle"
tags: [gov, llti, misle, deployed, level-4, cadence-weekly_3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/misles_su_atsakymais.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/llti/misles_su_atsakymais.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2835/"
    title: "data.gov.lt DCAT-AP — datasets/gov/llti/misles_su_atsakymais"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Misle — Mįslės su atsakymais

Lentelėje pateiktos mįslės su jų įminimais (atsakymais) iš Lietuvių literatūros ir tautosakos instituto Lituanistikos paveldo informacinės sistemos „Aruodai“ (https://www.aruodai.lt/). Pateikiami visi duomenys nuo jų įvedimo į sistemą datos (2013 metų) atnaujinant kas metus. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/llti/misles_su_atsakymais/Misle`[^manifest]
- **Dataset:** [Mįslės su atsakymais](../misles_su_atsakymais.md) (`datasets/gov/llti/misles_su_atsakymais`)[^manifest]
- **Manifest CSV:** [datasets/gov/llti/misles_su_atsakymais.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/misles_su_atsakymais.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/llti/misles_su_atsakymais/Misle` (`deployed`)[^manifest]
- **Provider:** `llti` — Lietuvių literatūros ir tautosakos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `misles_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY_3`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/llti/misles_su_atsakymais.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/misles_su_atsakymais.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/llti/misles_su_atsakymais (https://data.gov.lt/datasets/2835/)
