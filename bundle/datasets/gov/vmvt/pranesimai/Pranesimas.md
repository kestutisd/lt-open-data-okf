---
type: Table
title: "Pranesimas — Pranešimų duomenys"
description: "Pateikiami pranešimai apie nustatytus pažeidimus, pažeidimo rūšį, pavojų, pažeidimo tipą, aptikimo tipą, išplatinimo ribas, rizikos tipą ir rizikos taikymo ribas."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/pranesimai/Pranesimas"
tags: [gov, vmvt, pranesimas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/rasff/pranesimai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vmvt/rasff/pranesimai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3817/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmvt/pranesimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pranesimas — Pranešimų duomenys

Pateikiami pranešimai apie nustatytus pažeidimus, pažeidimo rūšį, pavojų, pažeidimo tipą, aptikimo tipą, išplatinimo ribas, rizikos tipą ir rizikos taikymo ribas.[^manifest]

- **Model:** `datasets/gov/vmvt/pranesimai/Pranesimas`[^manifest]
- **Dataset:** [Pranešimai](../pranesimai.md) (`datasets/gov/vmvt/pranesimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmvt/rasff/pranesimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/rasff/pranesimai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/pranesimai/Pranesimas` (`deployed`)[^manifest]
- **Provider:** `vmvt` — Valstybinė maisto ir veterinarijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `pranesimo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pranesimo_id` | `string` | — | `4` | `open` | — | Unikalus pranešimo identifikatorius | — |
| `rasff_id` | `string` | — | `4` | `open` | — | Unikalus pranešimo identifikatorius | — |
| `pranesimo_data` | `date` | — | `4` | `open` | — | Pranešimo data | — |
| `nustatytas_pazeidimas` | `string` | — | `4` | `open` | — | Nustatytas pažeidimas | — |
| `pazeidimo_rusis` | `string` | — | `4` | `open` | — | Pažeidimo rūšis | — |
| `pavojus` | `string` | — | `4` | `open` | — | Pavojus | — |
| `pazeidimo_tipas` | `string` | — | `4` | `open` | — | Pažeidimo tipas | — |
| `aptikimo_tipas` | `string` | — | `4` | `open` | — | Aptikimo tipas | — |
| `isplatinimo_ribos` | `string` | — | `4` | `open` | — | Išplatinimo ribos | — |
| `rizikos_tipas` | `string` | — | `4` | `open` | — | Rizikos tipas | — |
| `rizikos_taikymo_ribos` | `string` | — | `4` | `open` | — | Rizikos taikymo ribos | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `isplatinimo_ribos` | `"Išplatinta rinkoje"` | — | — | Išplatinta rinkoje | — |
| `isplatinimo_ribos` | `"Nėra informacijos apie išplatinimą"` | — | — | Nėra informacijos apie išplatinimą | — |
| `isplatinimo_ribos` | `"Pasibaigęs tinkamumo vartoti laikas"` | — | — | Pasibaigęs tinkamumo vartoti laikas | — |
| `isplatinimo_ribos` | `"Suvartota"` | — | — | Suvartota | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/rasff/pranesimai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/rasff/pranesimai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmvt/pranesimai (https://data.gov.lt/datasets/3817/)
