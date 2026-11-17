---
type: Dataset
title: "datasets/gov/vat/panaikinimai"
description: "Informacija apie panaikintus sertifikatus, kurie skelbiami negaliojančiais"
resource: "https://get.data.gov.lt/datasets/gov/vat/panaikinimai"
tags: [gov, vat, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/r24_panaikinti_sertifikatai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r24_panaikinti_sertifikatai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/vat/panaikinimai

Informacija apie panaikintus sertifikatus, kurie skelbiami negaliojančiais

- **Namespace:** `datasets/gov/vat/panaikinimai`[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r24_panaikinti_sertifikatai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r24_panaikinti_sertifikatai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/panaikinimai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Sertifikatas](panaikinimai/Sertifikatas.md) | Pateikiami duomenys apie tiekėją, dokumento pavadinimą, dokumento Nr. ir datą, augalo rūšį, veislę, dokumento panaikinimo datą, naujai išduoto dokumento datą ir Nr. | `4` | `eiles_nr` | `open` | 8 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r24_panaikinti_sertifikatai.csv
