---
type: Dataset
title: "Pacientų anoniminės apklausos"
description: "Spinta dataset datasets/gov/lsd/sveikata/apklausos (2 tables)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/apklausos"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/apklausos/apklausos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pacientų anoniminės apklausos

- **Namespace:** `datasets/gov/lsd/sveikata/apklausos`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/apklausos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [StacionaroPacientuApklausa](apklausos/StacionaroPacientuApklausa.md) | Stacionaro pacientų anoniminės apklausos | — | `vda_id` | — | 8 | Anketų, pateiktų pacientams po gydymo stacionare, skirtų įvertinti gautų sveikatos paslaugų kokybę, duomenys su atsakymais. |
| [AmbulatorijosPacientuApklausa](apklausos/AmbulatorijosPacientuApklausa.md) | Ambulatorijos pacientų anoniminės apklausos | — | `vda_id` | — | 9 | Anketų, pateiktų pacientams po gautų ambulatorinių paslaugų, skirtų įvertinti gautų sveikatos paslaugų kokybę, duomenys su atsakymais. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/apklausos/apklausos.csv
