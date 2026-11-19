---
type: Table
title: "Priemone"
description: "Spinta table datasets/gov/ssva/tpv_atestatai/Priemone (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ssva/tpv_atestatai/Priemone"
tags: [gov, ssva, priemone, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv#L14"
    title: "atviriduomenys/manifest — datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv#L14"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1317/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ssva/tpv_atestatai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Priemone

- **Model:** `datasets/gov/ssva/tpv_atestatai/Priemone`[^manifest]
- **Dataset:** [Duomenys apie teritorijų planavimo vadovų atestatus (fiziniai asmenys)](../tpv_atestatai.md) (`datasets/gov/ssva/tpv_atestatai`)[^manifest]
- **Manifest CSV:** [datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv#L14)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/tpv_atestatai/Priemone` (`deployed`)[^manifest]
- **Provider:** `ssva` — Statybos sektoriaus vystymo agentūra (SSVA) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by-nc-nd/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `nr` | `ref` | [Atestatas](Atestatas.md) (`level=4 UUID`: `nr._id`) | `4` | `open` | — | Atestato numeris | — |
| `tipas` | `string` | — | `4` | `open` | — | Poveikio priemonės tipas | — |
| `isdavimas` | `date` | `D` | `4` | `open` | — | Poveikio priemonės taikymo pradžia | — |
| `galiojimas` | `date` | `D` | `4` | `open` | — | Poveikio priemonės taikymo pabaiga | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Poveikio priemonės aprašymas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Panaikintas"` | — | — | — | — |
| `tipas` | `"Sustabdytas"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv#L14 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv#L14)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ssva/tpv_atestatai (https://data.gov.lt/datasets/1317/)
