---
type: Dataset
title: "Bendrojo pagalbos centro 112 skambučių duomenų rinkinys"
description: "Bendrojo pagalbos centro (BPC) duomenys apie gautus pranešimus apie įvykius."
resource: "https://get.data.gov.lt/datasets/gov/bpc/pagalbos_skambuciai"
tags: [gov, bpc, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/bpc/pagalbos_skambuciai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_skambuciai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Bendrojo pagalbos centro 112 skambučių duomenų rinkinys

Bendrojo pagalbos centro (BPC) duomenys apie gautus pranešimus apie įvykius.

- **Namespace:** `datasets/gov/bpc/pagalbos_skambuciai`[^manifest]
- **Manifest CSV:** [datasets/gov/bpc/pagalbos_skambuciai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_skambuciai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/bpc/pagalbos_skambuciai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [IvykiuKlasifikatorius](pagalbos_skambuciai/IvykiuKlasifikatorius.md) | BPC įvykių klasifikatorius | `4` | `ivykio_tipo_kodas` | — | 3 | Bendrojo pagalbos centro registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, tipų klasifikatorius. |
| [IvykiuKoordinates](pagalbos_skambuciai/IvykiuKoordinates.md) | BPC įvykių koordinatės | `4` | `ivykio_id` | — | 5 | Bendrojo pagalbos centro (BPC) registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, pilnas sąrašas. |
| [IvykiuSavivaldybes](pagalbos_skambuciai/IvykiuSavivaldybes.md) | BPC įvykių savivaldybės | `4` | — | — | 6 | Bendrojo pagalbos centro (BPC) registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, teritorinė statistika pagal savivaldybę. |
| [IvykiuLaikas](pagalbos_skambuciai/IvykiuLaikas.md) | BPC įvykių laikas | `4` | — | — | 7 | Bendrojo pagalbos centro (BPC) pagalbos telefonu registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, paros meto statistika. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/bpc/pagalbos_skambuciai.csv
