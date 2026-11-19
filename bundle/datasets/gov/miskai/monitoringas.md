---
type: Dataset
title: "datasets/gov/miskai/monitoringas"
description: "Lithuanian open data dataset datasets/gov/miskai/monitoringas (1 lentelė)."
tags: [gov, miskai, undeployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/monitoringas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/miskai/monitoringas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/miskai/monitoringas

- **Namespace:** `datasets/gov/miskai/monitoringas`[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/monitoringas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/monitoringas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (`undeployed` — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Rodiklis](monitoringas/Rodiklis.md) | Miškų sveikumo monitoringo duomenys | `3` | — | — | `21` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `create(type: "param", ref: "dist", source: "/datasets/gov/ivpk/adp/catalog/DatasetDistribution")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/monitoringas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/monitoringas.csv#L2)
