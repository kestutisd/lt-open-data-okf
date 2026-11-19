---
type: Table
title: "Quantity — Teršalai"
description: "Spinta table datasets/gov/aaa/oro_stociu_matavimai/Quantity (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Quantity"
tags: [gov, aaa, quantity, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L14"
    title: "atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv#L14"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/500/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/oro_stociu_matavimai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Quantity — Teršalai

- **Model:** `datasets/gov/aaa/oro_stociu_matavimai/Quantity`[^manifest]
- **Dataset:** [Lietuvos valstybinio oro monitoringo automatinių stočių matavimo duomenys](../oro_stociu_matavimai.md) (`datasets/gov/aaa/oro_stociu_matavimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/oro_stociu_matavimai.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L14)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Quantity` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `code_quantity`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `code_quantity` | `string` | — | `4` | `open` | — | Teršalo idenfikacinis numeris | — |
| `shortname` | `string` | — | `4` | `open` | — | Teršalo pavadinimo santrumpa | — |
| `longname` | `string` | — | `4` | `open` | — | Teršalo pavadinimas | — |
| `attrib` | `string` | — | `4` | `open` | — | Teršalo tipas | — |
| `code_unit` | `ref` | [Units](Units.md) (`level=4 UUID` via `Units[code_unit]`: `code_unit._id`) | `4` | `open` | — | Matavimo vieneto identifikacinis numeris | — |
| `id` | `string` | — | `4` | `open` | — | Teršalo idenfikacinis numeris | (sutampa su code_quantity) |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv#L14 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L14)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/oro_stociu_matavimai (https://data.gov.lt/datasets/500/)
