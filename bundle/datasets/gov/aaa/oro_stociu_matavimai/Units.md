---
type: Table
title: "Units — Matavimo vienetai"
description: "Spinta table datasets/gov/aaa/oro_stociu_matavimai/Units (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Units"
tags: [gov, aaa, units, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L9"
    title: "atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv#L9"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/500/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/oro_stociu_matavimai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Units — Matavimo vienetai

- **Model:** `datasets/gov/aaa/oro_stociu_matavimai/Units`[^manifest]
- **Dataset:** [Lietuvos valstybinio oro monitoringo automatinių stočių matavimo duomenys](../oro_stociu_matavimai.md) (`datasets/gov/aaa/oro_stociu_matavimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/oro_stociu_matavimai.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L9)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Units` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `code_unit`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `code_unit` | `string` | — | `4` | `open` | — | Matavimo vieneto identifikacinis numeris | — |
| `unitname` | `string` | — | `4` | `open` | — | Matavimo vieneto pavadinimas | — |
| `id` | `string` | — | `4` | `open` | — | Matavimo vieneto identifikacinis numeris | (sutampa su code_unit) |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv#L9 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L9)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/oro_stociu_matavimai (https://data.gov.lt/datasets/500/)
