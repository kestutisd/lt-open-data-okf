---
type: Table
title: "Priemone — Poveikio priemonės"
description: "Spinta table datasets/gov/ssva/vadovu_atestatai/Priemone (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ssva/vadovu_atestatai/Priemone"
tags: [gov, ssva, priemone, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/vadovu_kvalifikacijos_atestatai.csv#L22"
    title: "atviriduomenys/manifest — datasets/gov/ssva/vadovu_kvalifikacijos_atestatai.csv#L22"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1315/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ssva/vadovu_atestatai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Priemone — Poveikio priemonės

- **Model:** `datasets/gov/ssva/vadovu_atestatai/Priemone`[^manifest]
- **Dataset:** [Duomenys apie statinio statybos techninės veiklos pagrindinių sričių vadovų kvalifikacijos...](../vadovu_atestatai.md) (`datasets/gov/ssva/vadovu_atestatai`)[^manifest]
- **Manifest CSV:** [datasets/gov/ssva/vadovu_kvalifikacijos_atestatai.csv#L22](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/vadovu_kvalifikacijos_atestatai.csv#L22)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/vadovu_atestatai/Priemone` (`deployed`)[^manifest]
- **Provider:** `ssva` — Statybos sektoriaus vystymo agentūra (SSVA) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by-nc-nd/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Poveikio priemonės ID | — |
| `nr` | `ref` | [Atestatas](Atestatas.md) (`level=4 UUID`: `nr._id`) | `4` | `open` | — | Teisės dokumento numeris | — |
| `spr_nr` | `integer` | — | `4` | `open` | — | Sprendimo dėl poveikio taikymo numeris | — |
| `data` | `date` | `D` | `4` | `open` | — | Sprendimo dėl poveikio taikymo data | — |
| `tipas` | `integer` | — | `4` | `open` | — | Poveikio priemonės tipas | — |
| `isdavimas` | `date` | `D` | `4` | `open` | — | Poveikio priemonės taikymo pradžia | — |
| `galiojimas` | `date` | `D` | `4` | `open` | — | Poveikio priemonės taikymo pabaiga | — |
| `aprasas` | `string` | — | `4` | `open` | — | Poveikio priemonės aprašymas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `1` | — | — | Panaikintas | — |
| `tipas` | `2` | — | — | Sustabdytas | — |
| `tipas` | `3` | — | — | Stabdyti | — |
| `tipas` | `4` | — | — | Įspėjimas | — |
| `tipas` | `5` | — | — | Pastaba | — |
| `tipas` | `6` | — | — | Įspėti | — |
| `tipas` | `7` | — | — | Atšauktas panaikinimas | — |
| `tipas` | `8` | — | — | Atšaukimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/vadovu_kvalifikacijos_atestatai.csv#L22 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/vadovu_kvalifikacijos_atestatai.csv#L22)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ssva/vadovu_atestatai (https://data.gov.lt/datasets/1315/)
