---
type: Dataset
title: "datasets/gov/vsdfv/pkdalyviai"
description: "Lithuanian open data dataset datasets/gov/vsdfv/pkdalyviai (2 lentelės)."
tags: [gov, vsdfv, undeployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/pkdalyviai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/pkdalyviai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/vsdfv/pkdalyviai

- **Namespace:** `datasets/gov/vsdfv/pkdalyviai`[^manifest]
- **Manifest CSV:** [datasets/gov/vsdfv/pkdalyviai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/pkdalyviai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (`undeployed` — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `vsdfv` — Valstybinio socialinio draudimo fondo valdyba („Sodra“) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PkDalyvis](pkdalyviai/PkDalyvis.md) | — | `2` | `metai, menuo` | — | `5` | — |
| [PkItraukimas](pkdalyviai/PkItraukimas.md) | — | `2` | `metai` | — | `3` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(prepare: 'extract("zip")["pk_dalyviai.csv"].file(encoding: "cp1257").tabular(sep: ";")')` | `prepare` | — | — | — | — | — |
| `(model)` | `update(prepare: 'extract("zip")["pk_itraukimas.csv"].file(encoding: "cp1257").tabular(sep: ";")')` | `prepare` | — | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/pkdalyviai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/pkdalyviai.csv#L2)
