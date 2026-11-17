---
type: Table
title: "SchemeOperatorName"
description: "Spinta table datasets/gov/rrt/paslaugu_teikejai/SchemeOperatorName (2 columns)."
tags: [gov, rrt, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rrt/paslaugu_teikejai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/paslaugu_teikejai.csv#L13"
    last_modified: "2026-11-11T14:39:20Z"
---

# SchemeOperatorName

- **Model:** `datasets/gov/rrt/paslaugu_teikejai/SchemeOperatorName`[^manifest]
- **Dataset:** [datasets/gov/rrt/paslaugu_teikejai](../paslaugu_teikejai.md) (`datasets/gov/rrt/paslaugu_teikejai`)
- **Manifest CSV:** [datasets/gov/rrt/paslaugu_teikejai.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/paslaugu_teikejai.csv#L13)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `name`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `scheme_information` | `ref` | [SchemeInformation](SchemeInformation.md) | `4` | `open` | — | Nuoroda į tėvinį elementą | — |
| `name` | `string` | — | `3` | `open` | — | Įstaiga vykdanti schemą | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/paslaugu_teikejai.csv
