---
type: Table
title: "SchemeInformation"
description: "Spinta table datasets/gov/rrt/paslaugu_teikejai/SchemeInformation (4 columns)."
tags: [gov, rrt, schemeinformation, undeployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/paslaugu_teikejai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/rrt/paslaugu_teikejai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# SchemeInformation

- **Model:** `datasets/gov/rrt/paslaugu_teikejai/SchemeInformation`[^manifest]
- **Dataset:** [datasets/gov/rrt/paslaugu_teikejai](../paslaugu_teikejai.md) (`datasets/gov/rrt/paslaugu_teikejai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rrt/paslaugu_teikejai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/paslaugu_teikejai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `rrt` — Ryšių reguliavimo tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `tsl_version_identifier`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `trust_service_status_list` | `ref` | [TrustServiceStatusList](TrustServiceStatusList.md) (`level=4 UUID`: `trust_service_status_list._id`) | `4` | `open` | — | Nuoroda į tėvinį elementą | — |
| `tsl_version_identifier` | `integer` | — | `3` | `open` | — | TSL versijos identifikatorius | — |
| `tsl_sequence_number` | `integer` | — | `3` | `open` | — | TSL sekos numeris | — |
| `tsl_type` | `string` | — | `3` | `open` | — | TSL tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/paslaugu_teikejai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/paslaugu_teikejai.csv#L7)
