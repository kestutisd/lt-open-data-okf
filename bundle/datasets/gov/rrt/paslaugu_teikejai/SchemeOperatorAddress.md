---
type: Table
title: "SchemeOperatorAddress"
description: "Spinta table datasets/gov/rrt/paslaugu_teikejai/SchemeOperatorAddress (5 columns)."
tags: [gov, rrt, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rrt/paslaugu_teikejai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/paslaugu_teikejai.csv#L17"
    last_modified: "2026-11-11T14:39:20Z"
---

# SchemeOperatorAddress

- **Model:** `datasets/gov/rrt/paslaugu_teikejai/SchemeOperatorAddress`[^manifest]
- **Dataset:** [datasets/gov/rrt/paslaugu_teikejai](../paslaugu_teikejai.md) (`datasets/gov/rrt/paslaugu_teikejai`)
- **Manifest CSV:** [datasets/gov/rrt/paslaugu_teikejai.csv#L17](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/paslaugu_teikejai.csv#L17)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `postal_code`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `street_address` | `string` | — | `3` | `open` | — | Gatvės adresas | — |
| `locality` | `string` | — | `3` | `open` | — | Gyvenvietė | — |
| `postal_code` | `string` | — | `3` | `open` | — | Pašto kodas | — |
| `country_name` | `string` | — | `3` | `open` | — | Šalies kodas | — |
| `scheme_information` | `ref` | [SchemeInformation](SchemeInformation.md) | `4` | `open` | — | Nuoroda į tėvinį elementą | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/paslaugu_teikejai.csv
