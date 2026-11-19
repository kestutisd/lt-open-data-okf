---
type: Table
title: "SchemeOperatorAddress"
description: "Spinta table datasets/gov/rrt/paslaugu_teikejai/SchemeOperatorAddress (5 columns)."
tags: [gov, rrt, schemeoperatoraddress, undeployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/paslaugu_teikejai.csv#L17"
    title: "atviriduomenys/manifest — datasets/gov/rrt/paslaugu_teikejai.csv#L17"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# SchemeOperatorAddress

- **Model:** `datasets/gov/rrt/paslaugu_teikejai/SchemeOperatorAddress`[^manifest]
- **Dataset:** [datasets/gov/rrt/paslaugu_teikejai](../paslaugu_teikejai.md) (`datasets/gov/rrt/paslaugu_teikejai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rrt/paslaugu_teikejai.csv#L17](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/paslaugu_teikejai.csv#L17)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `rrt` — Ryšių reguliavimo tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `postal_code`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `street_address` | `string` | — | `3` | `open` | — | Gatvės adresas | — |
| `locality` | `string` | — | `3` | `open` | — | Gyvenvietė | — |
| `postal_code` | `string` | — | `3` | `open` | — | Pašto kodas | — |
| `country_name` | `string` | — | `3` | `open` | — | Šalies kodas | — |
| `scheme_information` | `ref` | [SchemeInformation](SchemeInformation.md) (`level=4 UUID`: `scheme_information._id`) | `4` | `open` | — | Nuoroda į tėvinį elementą | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/paslaugu_teikejai.csv#L17 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/paslaugu_teikejai.csv#L17)
