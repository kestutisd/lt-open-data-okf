---
type: Table
title: "SkiepytiPadieniui — Pasiskiepiję asmenys pagal dieną ir ligą"
description: "Spinta table datasets/gov/lsd/sveikata/skiepai/SkiepytiPadieniui (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/skiepai/SkiepytiPadieniui"
tags: [gov, lsd, skiepytipadieniui, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/skiepai.csv#L24"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/skiepai.csv#L24"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2777/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/skiepai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# SkiepytiPadieniui — Pasiskiepiję asmenys pagal dieną ir ligą

- **Model:** `datasets/gov/lsd/sveikata/skiepai/SkiepytiPadieniui`[^manifest]
- **Dataset:** [Asmenys, paskiepyti įvairių ligų skiepais](../skiepai.md) (`datasets/gov/lsd/sveikata/skiepai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/skiepai.csv#L24](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/skiepai.csv#L24)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/skiepai/SkiepytiPadieniui` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `date` | `date` | `D` | `4` | `open` | — | Diena, kurią skiepyta | — |
| `liga` | `string` | — | `2` | `open` | — | Liga, nuo kurios skiepijama | — |
| `n_asm` | `integer` | — | `4` | `open` | — | Skaičius asmenų, paskiepytų nuo tos ligos tą dieną | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/skiepai.csv#L24 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/skiepai.csv#L24)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/skiepai (https://data.gov.lt/datasets/2777/)
