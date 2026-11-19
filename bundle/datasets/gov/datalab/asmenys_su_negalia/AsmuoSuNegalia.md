---
type: Table
title: "AsmuoSuNegalia — Asmuo su negalia"
description: "Spinta table datasets/gov/datalab/asmenys_su_negalia/AsmuoSuNegalia (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/datalab/asmenys_su_negalia/AsmuoSuNegalia"
tags: [gov, datalab, asmuosunegalia, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/datalab/asmenys_su_negalia.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/datalab/asmenys_su_negalia.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3912/"
    title: "data.gov.lt DCAT-AP — datasets/gov/datalab/asmenys_su_negalia"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# AsmuoSuNegalia — Asmuo su negalia

- **Model:** `datasets/gov/datalab/asmenys_su_negalia/AsmuoSuNegalia`[^manifest]
- **Dataset:** [Asmenys su negalia](../asmenys_su_negalia.md) (`datasets/gov/datalab/asmenys_su_negalia`)[^manifest]
- **Manifest CSV:** [datasets/gov/datalab/asmenys_su_negalia.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/datalab/asmenys_su_negalia.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/datalab/asmenys_su_negalia/AsmuoSuNegalia` (`deployed`)[^manifest]
- **Provider:** `datalab` — Valstybės duomenų agentūra (DataLab) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | VDA ID | — |
| `sav_pav` | `string` | — | `4` | `open` | — | Savivaldybė | — |
| `sen_pav` | `string` | — | `4` | `open` | — | Seniūnija | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `amzius` | `string` | — | `4` | `open` | — | Amžius | — |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Amžiaus grupė | — |
| `neig_darb` | `string` | — | `4` | `open` | — | Neįgalumo statusas | — |
| `gimimo_salis` | `string` | — | `4` | `open` | — | Gimimo šalis | — |
| `pasto_kodas` | `string` | — | `4` | `open` | — | Pašto kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/datalab/asmenys_su_negalia.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/datalab/asmenys_su_negalia.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/datalab/asmenys_su_negalia (https://data.gov.lt/datasets/3912/)
