---
type: Dataset
title: "datasets/gov/zuikvc/sklypu_ribos"
description: "Lithuanian open data dataset datasets/gov/zuikvc/sklypu_ribos (1 lentelė)."
tags: [gov, zuikvc, undeployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/sklypu_ribos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/sklypu_ribos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/zuikvc/sklypu_ribos

- **Namespace:** `datasets/gov/zuikvc/sklypu_ribos`[^manifest]
- **Manifest CSV:** [datasets/gov/zuikvc/sklypu_ribos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/sklypu_ribos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (`undeployed` — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `zuikvc` — VĮ Žemės ūkio duomenų centras (buv. VĮ Žemės ūkio informacijos ir kaimo verslo centras) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SklypoRiba](sklypu_ribos/SklypoRiba.md) | KŽS ribų pasikeitimų duomeys | `3` | — | — | `3` | Išankstinių kontrolinių žemės sklypų (KŽS) ribų pasikeitimų duomeys |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `create(type: "param", ref: "dist", source: "/datasets/gov/ivpk/adp/catalog/DatasetDistribution")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/sklypu_ribos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/sklypu_ribos.csv#L2)
