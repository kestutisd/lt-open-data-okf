---
type: Table
title: "SchemeOperatorName"
description: "Spinta table datasets/gov/rrt/paslaugu_teikejai/SchemeOperatorName (2 columns)."
tags: [gov, rrt, schemeoperatorname, undeployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/paslaugu_teikejai.csv#L13"
    title: "atviriduomenys/manifest — datasets/gov/rrt/paslaugu_teikejai.csv#L13"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# SchemeOperatorName

- **Model:** `datasets/gov/rrt/paslaugu_teikejai/SchemeOperatorName`[^manifest]
- **Dataset:** [datasets/gov/rrt/paslaugu_teikejai](../paslaugu_teikejai.md) (`datasets/gov/rrt/paslaugu_teikejai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rrt/paslaugu_teikejai.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/paslaugu_teikejai.csv#L13)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `rrt` — Ryšių reguliavimo tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `name`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `scheme_information` | `ref` | [SchemeInformation](SchemeInformation.md) (`level=4 UUID`: `scheme_information._id`) | `4` | `open` | — | Nuoroda į tėvinį elementą | — |
| `name` | `string` | — | `3` | `open` | — | Įstaiga vykdanti schemą | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/paslaugu_teikejai.csv#L13 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/paslaugu_teikejai.csv#L13)
