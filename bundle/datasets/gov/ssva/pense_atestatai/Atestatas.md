---
type: Table
title: "Atestatas — PENS Ekspertų Atestatai"
description: "Spinta table datasets/gov/ssva/pense_atestatai/Atestatas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ssva/pense_atestatai/Atestatas"
tags: [gov, ssva, atestatas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/atestatai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/ssva/atestatai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2287/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ssva/pense_atestatai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Atestatas — PENS Ekspertų Atestatai

- **Model:** `datasets/gov/ssva/pense_atestatai/Atestatas`[^manifest]
- **Dataset:** [Duomenys apie pastatų energinio naudingumo sertifikavimo ekspertų kvalifikacijos atestatus...](../pense_atestatai.md) (`datasets/gov/ssva/pense_atestatai`)[^manifest]
- **Manifest CSV:** [datasets/gov/ssva/atestatai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/atestatai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/pense_atestatai/Atestatas` (`deployed`)[^manifest]
- **Provider:** `ssva` — Statybos sektoriaus vystymo agentūra (SSVA) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by-nc-nd/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Kvalifikacijos atestato numeris | — |
| `gavejas` | `string` | — | `4` | `public` | — | Ekspertas | — |
| `isdavimas` | `date` | `D` | `4` | `open` | — | Pirmojo atestato išdavimo data | — |
| `atnaujinimas` | `date` | `D` | `4` | `open` | — | Naujausiojo atestato išdavimo data | — |
| `statusas` | `integer` | — | `4` | `open` | — | Atestato statusas | — |
| `galiojimas` | `string` | — | `2` | `open` | — | Atestato galiojimo laiko ribos (jei taikoma) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `statusas` | `0` | — | — | Negalioja | — |
| `statusas` | `1` | — | — | Galioja | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/atestatai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/atestatai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ssva/pense_atestatai (https://data.gov.lt/datasets/2287/)
