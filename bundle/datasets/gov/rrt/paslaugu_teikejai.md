---
type: Dataset
title: "datasets/gov/rrt/paslaugu_teikejai"
description: "Lithuanian open data dataset datasets/gov/rrt/paslaugu_teikejai (9 lentelės)."
tags: [gov, rrt, undeployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/paslaugu_teikejai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rrt/paslaugu_teikejai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/rrt/paslaugu_teikejai

- **Namespace:** `datasets/gov/rrt/paslaugu_teikejai`[^manifest]
- **Manifest CSV:** [datasets/gov/rrt/paslaugu_teikejai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/paslaugu_teikejai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (`undeployed` — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `rrt` — Ryšių reguliavimo tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `9` (9 lentelės)[^manifest]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TrustServiceStatusList](paslaugu_teikejai/TrustServiceStatusList.md) | Patikimumo užtikrinimo paslaugų teikėjai | — | `id` | — | `1` | — |
| [SchemeInformation](paslaugu_teikejai/SchemeInformation.md) | — | — | `tsl_version_identifier` | — | `4` | — |
| [SchemeOperatorName](paslaugu_teikejai/SchemeOperatorName.md) | — | — | `name` | — | `2` | — |
| [SchemeOperatorAddress](paslaugu_teikejai/SchemeOperatorAddress.md) | — | — | `postal_code` | — | `5` | — |
| [SchemeName](paslaugu_teikejai/SchemeName.md) | — | — | `name` | — | `2` | — |
| [TSPInformation](paslaugu_teikejai/TSPInformation.md) | Informacija apie paslaugos teikėją | — | `id` | — | `1` | — |
| [TSPName](paslaugu_teikejai/TSPName.md) | — | — | `name` | — | `2` | — |
| [TSPTradeName](paslaugu_teikejai/TSPTradeName.md) | — | — | `name` | — | `2` | — |
| [TSPAddress](paslaugu_teikejai/TSPAddress.md) | — | — | `postal_code` | — | `5` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/paslaugu_teikejai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/paslaugu_teikejai.csv#L2)
