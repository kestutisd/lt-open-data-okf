---
type: Dataset
title: "datasets/gov/zuikvc/naudmenos"
description: "Spinta dataset datasets/gov/zuikvc/naudmenos (1 table)."
tags: [gov, zuikvc, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/naudmenos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/naudmenos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/zuikvc/naudmenos

- **Namespace:** `datasets/gov/zuikvc/naudmenos`[^manifest]
- **Manifest CSV:** [datasets/gov/zuikvc/naudmenos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/naudmenos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Naudmena](naudmenos/Naudmena.md) | Naudmenų ribų duomeys | `2` | `aprasymas` | — | 3 | Pasikeitusių apleistų žemės ūkio naudmenų ribų duomeys |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(dataset)` | `create(type: "param", ref: "dist", source: "/datasets/gov/ivpk/adp/catalog/DatasetDistribution")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/naudmenos.csv
