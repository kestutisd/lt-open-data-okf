---
type: Dataset
title: "datasets/gov/vsdfv/nedarbo_ismokos"
description: "Lithuanian open data dataset datasets/gov/vsdfv/nedarbo_ismokos (1 lentelė)."
tags: [gov, vsdfv, undeployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/nedarbo_ismokos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/nedarbo_ismokos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/vsdfv/nedarbo_ismokos

- **Namespace:** `datasets/gov/vsdfv/nedarbo_ismokos`[^manifest]
- **Manifest CSV:** [datasets/gov/vsdfv/nedarbo_ismokos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/nedarbo_ismokos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (`undeployed` — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `vsdfv` — Valstybinio socialinio draudimo fondo valdyba („Sodra“) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NedarboIsmoka](nedarbo_ismokos/NedarboIsmoka.md) | — | `2` | `metu_menuo` | — | `9` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(prepare: 'extract("zip")["nedarbo_ismokos.csv"].file(encoding: "cp1257").tabular(sep: ";")')` | `prepare` | — | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/nedarbo_ismokos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/nedarbo_ismokos.csv#L2)
