---
type: Table
title: "Suvestine — Teisės aktų suvestinių duomenys"
description: "Pateikiami duomenys apie teisės aktų suvestines."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/teises_aktai/Suvestine"
tags: [gov, lrsk, suvestine, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/teises_aktai.csv#L67"
    title: "atviriduomenys/manifest — datasets/gov/lrsk/teises_aktai.csv#L67"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2613/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrsk/teises_aktai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Suvestine — Teisės aktų suvestinių duomenys

Pateikiami duomenys apie teisės aktų suvestines.[^manifest]

- **Model:** `datasets/gov/lrsk/teises_aktai/Suvestine`[^manifest]
- **Dataset:** [Teisės aktų registro duomenys](../teises_aktai.md) (`datasets/gov/lrsk/teises_aktai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lrsk/teises_aktai.csv#L67](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/teises_aktai.csv#L67)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/teises_aktai/Suvestine` (`deployed`)[^manifest]
- **Provider:** `lrsk` — Lietuvos Respublikos Seimo Kanceliarija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `dokumento_id` | `string` | — | `4` | `open` | — | Dokumento unikalus identifikatorius | — |
| `suvestines_id` | `string` | — | `4` | `open` | — | Suvestinės redakcijos pagal pakeitimą identifikatorius | — |
| `nuoroda` | `string` | — | `4` | `open` | — | Nuoroda į dokumento suvestinę | — |
| `tekstas_lt` | `string` | — | `2` | `open` | — | Dokumento suvestinės tekstas | — |
| `galioja_nuo` | `datetime` | `S` | `4` | `open` | — | Suvestinės redakcijos įsigaliojimo data | — |
| `galioja_iki` | `datetime` | `S` | `4` | `open` | — | Suvestinės redakcijos galiojimo terminas | — |
| `suv_duom_atnaujinimas` | `datetime` | `S` | `4` | `open` | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tekstas_lt` | `update(property: "tekstas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/teises_aktai.csv#L67 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/teises_aktai.csv#L67)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrsk/teises_aktai (https://data.gov.lt/datasets/2613/)
