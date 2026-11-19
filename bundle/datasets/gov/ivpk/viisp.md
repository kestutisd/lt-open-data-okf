---
type: Dataset
title: "datasets/gov/ivpk/viisp"
description: "Lithuanian open data dataset datasets/gov/ivpk/viisp (3 lentelės)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/viisp"
tags: [gov, ivpk, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/viisp.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ivpk/viisp.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/ivpk/viisp

- **Namespace:** `datasets/gov/ivpk/viisp`[^manifest]
- **Manifest CSV:** [datasets/gov/ivpk/viisp.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/viisp.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/viisp` (`deployed`)[^manifest]
- **Provider:** `ivpk` — Valstybės skaitmeninių sprendimų agentūra (VSSA, buv. IVPK) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [ServiceDescription](viisp/ServiceDescription.md) | Išoriniai ir vidiniai paslaugų aprašai | `4` | `id` | — | `9` | Paslaugų aprašai. Trumpi, ilgi pavadinimai. |
| [AuditLogin](viisp/AuditLogin.md) | Prisijungimų sekimas | `4` | `id` | — | `5` | Kiekvieno prisijungimo metu sukuriamas įrašas, atsekti koks naudotojas prisijungė, su kokia priemone. |
| [AuditOrder](viisp/AuditOrder.md) | Užsakymų lenta | `4` | `id` | — | `3` | Kiekvieno užsakymu metu yra sukuriamas įrašas. |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/viisp.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/viisp.csv#L2)
