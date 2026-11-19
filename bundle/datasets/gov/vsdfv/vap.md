---
type: Dataset
title: "datasets/gov/vsdfv/vap"
description: "Lithuanian open data dataset datasets/gov/vsdfv/vap (3 lentelės)."
tags: [gov, vsdfv, undeployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/vap.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/vap.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/vsdfv/vap

- **Namespace:** `datasets/gov/vsdfv/vap`[^manifest]
- **Manifest CSV:** [datasets/gov/vsdfv/vap.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/vap.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (`undeployed` — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `vsdfv` — Valstybinio socialinio draudimo fondo valdyba („Sodra“) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Apdraustasis](vap/Apdraustasis.md) | — | `2` | `metu_menuo, darbo_uzmok_eur` | — | `10` | — |
| [PajamuAnalize](vap/PajamuAnalize.md) | — | `2` | `metai, menuo` | — | `6` | — |
| [ApdraustiejiPagalProfesija](vap/ApdraustiejiPagalProfesija.md) | — | `2` | `metai, menuo, profesija` | — | `4` | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(prepare: 'self.extract("zip")["apdraustieji_det.csv"].file(encoding: "cp1257").tabular(sep: ";")')` | `prepare` | — | — | — | — | — |
| `(model)` | `update(prepare: 'self.extract("zip")["apdraustuju_pajamu_analize.csv"].file(encoding: "cp1257").tabular(sep: ";")')` | `prepare` | — | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/vap.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/vap.csv#L2)
