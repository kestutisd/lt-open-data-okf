---
type: Table
title: "SavivaldybeDiena — Statistika apie sumedžiotus vilkus Lietuvos savivaldybėse"
description: "Pateikiama sumedžiotų vilkų statistika savivaldybės ir datos tikslumu."
resource: "https://get.data.gov.lt/datasets/gov/vstt/vilku_medziokles/SavivaldybeDiena"
tags: [gov, vstt, savivaldybediena, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/medziokles.csv#L9"
    title: "atviriduomenys/manifest — datasets/gov/vstt/medziokles.csv#L9"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2889/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vstt/vilku_medziokles"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# SavivaldybeDiena — Statistika apie sumedžiotus vilkus Lietuvos savivaldybėse

Pateikiama sumedžiotų vilkų statistika savivaldybės ir datos tikslumu. Duomenų teikėjas: Valstybinė saugomų teritorijų tarnyba prie Aplinkos ministerijos. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/vstt/vilku_medziokles/SavivaldybeDiena`[^manifest]
- **Dataset:** [Sumedžioti vilkai Lietuvoje](../vilku_medziokles.md) (`datasets/gov/vstt/vilku_medziokles`)[^manifest]
- **Manifest CSV:** [datasets/gov/vstt/medziokles.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/medziokles.csv#L9)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/vilku_medziokles/SavivaldybeDiena` (`deployed`)[^manifest]
- **Provider:** `vstt` — Valstybinė saugomų teritorijų tarnyba prie Aplinkos ministerijos *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `data` | `date` | `D` | `4` | `open` | — | Medžioklės data | — |
| `sumedziota_vnt` | `integer` | `U` | `4` | `open` | — | Bendras sumedžiotų vilkų skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/medziokles.csv#L9 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/medziokles.csv#L9)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vstt/vilku_medziokles (https://data.gov.lt/datasets/2889/)
