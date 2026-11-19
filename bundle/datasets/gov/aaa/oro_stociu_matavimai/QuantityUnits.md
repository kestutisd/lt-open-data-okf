---
type: Table
title: "QuantityUnits — Tarpinė lenta"
description: "Spinta table datasets/gov/aaa/oro_stociu_matavimai/QuantityUnits (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/QuantityUnits"
tags: [gov, aaa, quantityunits, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L30"
    title: "atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv#L30"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/500/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/oro_stociu_matavimai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# QuantityUnits — Tarpinė lenta

- **Model:** `datasets/gov/aaa/oro_stociu_matavimai/QuantityUnits`[^manifest]
- **Dataset:** [Lietuvos valstybinio oro monitoringo automatinių stočių matavimo duomenys](../oro_stociu_matavimai.md) (`datasets/gov/aaa/oro_stociu_matavimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/oro_stociu_matavimai.csv#L30](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L30)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/QuantityUnits` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `code_combi`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `code_combi` | `string` | — | `4` | `open` | — | Unikalus teršalo arba meteorologinio rodiklio ir jo matavimo vieneto numeris | — |
| `code_quantity` | `ref` | [Quantity](Quantity.md) (`level=4 UUID` via `Quantity[code_quantity]`: `code_quantity._id`) | `4` | `open` | — | Unikalus teršalo arba meteorologinio rodiklio numeris | — |
| `code_unit` | `ref` | [Units](Units.md) (`level=4 UUID` via `Units[code_unit]`: `code_unit._id`) | `4` | `open` | — | Unikalus matavimo vieneto numeris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv#L30 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L30)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/oro_stociu_matavimai (https://data.gov.lt/datasets/500/)
