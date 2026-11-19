---
type: Table
title: "Subjektas — Subjektų duomenys"
description: "Pateikiama informacija apie ukio subjektus: subjekto pavadinimas, tipas ir šalis."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/pranesimai/Subjektas"
tags: [gov, vmvt, subjektas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/rasff/pranesimai.csv#L33"
    title: "atviriduomenys/manifest — datasets/gov/vmvt/rasff/pranesimai.csv#L33"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3817/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmvt/pranesimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Subjektas — Subjektų duomenys

Pateikiama informacija apie ukio subjektus: subjekto pavadinimas, tipas ir šalis.[^manifest]

- **Model:** `datasets/gov/vmvt/pranesimai/Subjektas`[^manifest]
- **Dataset:** [Pranešimai](../pranesimai.md) (`datasets/gov/vmvt/pranesimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmvt/rasff/pranesimai.csv#L33](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/rasff/pranesimai.csv#L33)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/pranesimai/Subjektas` (`deployed`)[^manifest]
- **Provider:** `vmvt` — Valstybinė maisto ir veterinarijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus subjekto identifikatorius | — |
| `siuntos_id` | `string` | — | `4` | `open` | — | Siuntos identifikatorius | — |
| `pranesimo_id` | `string` | — | `4` | `open` | — | Pranešimo identifikatorius | — |
| `ukio_subjektas` | `string` | — | `4` | `open` | — | ūkio subjekto pavadinimas | — |
| `subjekto_tipas` | `string` | — | `4` | `open` | — | Subjekto tipas | — |
| `ukio_subjekto_salis` | `string` | — | `4` | `open` | — | ūkio subjekto šalis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/rasff/pranesimai.csv#L33 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/rasff/pranesimai.csv#L33)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmvt/pranesimai (https://data.gov.lt/datasets/3817/)
