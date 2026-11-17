---
type: Table
title: "TSPAddress"
description: "Spinta table datasets/gov/rrt/paslaugu_teikejai/TSPAddress (5 columns)."
tags: [gov, rrt, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rrt/paslaugu_teikejai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/paslaugu_teikejai.csv#L39"
    last_modified: "2026-11-11T14:39:20Z"
---

# TSPAddress

- **Model:** `datasets/gov/rrt/paslaugu_teikejai/TSPAddress`[^manifest]
- **Dataset:** [datasets/gov/rrt/paslaugu_teikejai](../paslaugu_teikejai.md) (`datasets/gov/rrt/paslaugu_teikejai`)
- **Manifest CSV:** [datasets/gov/rrt/paslaugu_teikejai.csv#L39](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/paslaugu_teikejai.csv#L39)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `postal_code`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `street_address` | `string` | — | `3` | `open` | — | Gatvės adresas | — |
| `locality` | `string` | — | `3` | `open` | — | Gyvenvietė | — |
| `postal_code` | `string` | — | `3` | `open` | — | Pašto kodas | — |
| `country_name` | `string` | — | `3` | `open` | — | Šalies kodas | — |
| `tsp_information` | `ref` | [TSPInformation](TSPInformation.md) | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/paslaugu_teikejai.csv
