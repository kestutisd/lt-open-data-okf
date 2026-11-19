---
type: Table
title: "Priemone — Poveikio priemonės"
description: "Spinta table datasets/gov/ssva/rangovu_atestatai/Priemone (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ssva/rangovu_atestatai/Priemone"
tags: [gov, ssva, priemone, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv#L24"
    title: "atviriduomenys/manifest — datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv#L24"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1314/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ssva/rangovu_atestatai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Priemone — Poveikio priemonės

- **Model:** `datasets/gov/ssva/rangovu_atestatai/Priemone`[^manifest]
- **Dataset:** [Duomenys apie statinio statybos ir ekspertizės rangovų atestatus, apie statinio statybos...](../rangovu_atestatai.md) (`datasets/gov/ssva/rangovu_atestatai`)[^manifest]
- **Manifest CSV:** [datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv#L24](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv#L24)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/rangovu_atestatai/Priemone` (`deployed`)[^manifest]
- **Provider:** `ssva` — Statybos sektoriaus vystymo agentūra (SSVA) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by-nc-nd/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Unikalus ID | — |
| `dok_id` | `ref` | [Dokumentas](Dokumentas.md) (`level=4 UUID`: `dok_id._id`) | `4` | `open` | — | Teisės dokumento ID | — |
| `nr` | `string` | — | `4` | `open` | — | Sprendimo dėl poveikio taikymo numeris | — |
| `data` | `date` | `D` | `4` | `open` | — | Sprendimo dėl poveikio taikymo data | — |
| `tipas` | `string` | — | `4` | `open` | — | Poveikio priemonės tipas | — |
| `registruota` | `date` | `D` | `4` | `open` | — | Poveikio priemonės taikymo pradžia | — |
| `galiojimas` | `date` | `D` | `4` | `open` | — | Poveikio priemonės taikymo pabaiga | — |
| `tekstas` | `string` | — | `4` | `open` | — | Poveikio priemonės aprašymas | — |
| `pastabos` | `string` | — | `4` | `open` | — | Pastaba dėl poveikio priemonės taikymo | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Naikinimas"` | — | — | — | — |
| `tipas` | `"Stabdymas"` | — | — | — | — |
| `tipas` | `"Įspejimas"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv#L24 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv#L24)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ssva/rangovu_atestatai (https://data.gov.lt/datasets/1314/)
