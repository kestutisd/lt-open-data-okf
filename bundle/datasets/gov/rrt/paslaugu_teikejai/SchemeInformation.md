---
type: Table
title: "SchemeInformation"
description: "Spinta table datasets/gov/rrt/paslaugu_teikejai/SchemeInformation (4 columns)."
tags: [gov, rrt, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rrt/paslaugu_teikejai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/paslaugu_teikejai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# SchemeInformation

- **Model:** `datasets/gov/rrt/paslaugu_teikejai/SchemeInformation`[^manifest]
- **Dataset:** [datasets/gov/rrt/paslaugu_teikejai](../paslaugu_teikejai.md) (`datasets/gov/rrt/paslaugu_teikejai`)
- **Manifest CSV:** [datasets/gov/rrt/paslaugu_teikejai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/paslaugu_teikejai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `tsl_version_identifier`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `trust_service_status_list` | `ref` | [TrustServiceStatusList](TrustServiceStatusList.md) | `4` | `open` | — | Nuoroda į tėvinį elementą | — |
| `tsl_version_identifier` | `integer` | — | `3` | `open` | — | TSL versijos identifikatorius | — |
| `tsl_sequence_number` | `integer` | — | `3` | `open` | — | TSL sekos numeris | — |
| `tsl_type` | `string` | — | `3` | `open` | — | TSL tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/paslaugu_teikejai.csv
