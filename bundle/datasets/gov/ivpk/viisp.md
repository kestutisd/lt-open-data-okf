---
type: Dataset
title: "datasets/gov/ivpk/viisp"
description: "Spinta dataset datasets/gov/ivpk/viisp (3 tables)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/viisp"
tags: [gov, ivpk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/viisp.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/viisp.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/ivpk/viisp

- **Namespace:** `datasets/gov/ivpk/viisp`[^manifest]
- **Manifest CSV:** [datasets/gov/ivpk/viisp.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/viisp.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/viisp`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [ServiceDescription](viisp/ServiceDescription.md) | Išoriniai ir vidiniai paslaugų aprašai | `4` | `id` | — | 9 | Paslaugų aprašai. |
| [AuditLogin](viisp/AuditLogin.md) | Prisijungimų sekimas | `4` | `id` | — | 5 | Kiekvieno prisijungimo metu sukuriamas įrašas, atsekti koks naudotojas prisijungė, su kokia priemone. |
| [AuditOrder](viisp/AuditOrder.md) | Užsakymų lenta | `4` | `id` | — | 3 | Kiekvieno užsakymu metu yra sukuriamas įrašas. |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/viisp.csv
