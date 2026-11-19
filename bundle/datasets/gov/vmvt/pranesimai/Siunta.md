---
type: Table
title: "Siunta — Siuntų duomenys"
description: "Pateikiami siuntų duomenys: kilmės šalis, produkto grupė, produkto pavadinimas, partijos numeris, tinkamumo terminas ir tinkamumo tipas."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/pranesimai/Siunta"
tags: [gov, vmvt, siunta, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/rasff/pranesimai.csv#L23"
    title: "atviriduomenys/manifest — datasets/gov/vmvt/rasff/pranesimai.csv#L23"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3817/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmvt/pranesimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Siunta — Siuntų duomenys

Pateikiami siuntų duomenys: kilmės šalis, produkto grupė, produkto pavadinimas, partijos numeris, tinkamumo terminas ir tinkamumo tipas.[^manifest]

- **Model:** `datasets/gov/vmvt/pranesimai/Siunta`[^manifest]
- **Dataset:** [Pranešimai](../pranesimai.md) (`datasets/gov/vmvt/pranesimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmvt/rasff/pranesimai.csv#L23](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/rasff/pranesimai.csv#L23)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/pranesimai/Siunta` (`deployed`)[^manifest]
- **Provider:** `vmvt` — Valstybinė maisto ir veterinarijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `siuntos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `siuntos_id` | `string` | — | `4` | `open` | — | Unikalus siuntos identifikatorius | — |
| `pranesimo_id` | `string` | — | `4` | `open` | — | Pranešimo identifikatorius | — |
| `kilmes_salis` | `string` | — | `4` | `open` | — | Kilmės šalis | — |
| `produkto_grupe` | `string` | — | `4` | `open` | — | Produkto grupė | — |
| `produkto_pavadinimas` | `string` | — | `4` | `open` | — | Produkto pavadinimas | — |
| `partijos_numeris` | `string` | — | `4` | `open` | — | Partijos numeris | — |
| `tinkamumo_terminas` | `date` | — | `4` | `open` | — | Tinkamumo terminas | — |
| `tinkamumo_tipas` | `string` | — | `4` | `open` | — | Tinkamumo tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/rasff/pranesimai.csv#L23 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/rasff/pranesimai.csv#L23)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmvt/pranesimai (https://data.gov.lt/datasets/3817/)
