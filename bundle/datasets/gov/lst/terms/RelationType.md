---
type: Table
title: "RelationType"
description: "Sąsajos tipas (sinonimas; susijęs, pakeistas, neteiktinas, pasenęs)"
resource: "https://get.data.gov.lt/datasets/gov/lst/terms/RelationType"
tags: [gov, lst, relationtype, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L14"
    title: "atviriduomenys/manifest — datasets/gov/lst/terms.csv#L14"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/996/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lst/terms"
    author: "team:vda"
    last_modified: "2026-10-02T00:00:00Z"
---

# RelationType

Sąsajos tipas (sinonimas; susijęs, pakeistas, neteiktinas, pasenęs)[^manifest]

- **Model:** `datasets/gov/lst/terms/RelationType`[^manifest]
- **Dataset:** [Standartų terminų bazė](../terms.md) (`datasets/gov/lst/terms`)[^manifest]
- **Manifest CSV:** [datasets/gov/lst/terms.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L14)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/terms/RelationType` (`deployed`)[^manifest]
- **Provider:** `lst` — Lietuvos standartizacijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-10-02`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | `string` | — | — | `open` | — | — | — |
| `bidirectional` | `boolean` | — | — | `open` | — | — | — |
| `id` | `integer` | — | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/terms.csv#L14 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L14)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lst/terms (https://data.gov.lt/datasets/996/)
