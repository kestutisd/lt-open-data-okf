---
type: Dataset
title: "Oro Navigacijos skrydžių statistikos duomenys"
description: "Rinkinyje pateikiami Lietuvos oro erdvėje vykusių skrydžių duomenys iš Oro Navigacijos skrydžių statistikos duomenų bazės."
resource: "https://get.data.gov.lt/datasets/gov/on/statistika"
tags: [gov, on, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/on/flight_data.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/on/flight_data.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Oro Navigacijos skrydžių statistikos duomenys

Rinkinyje pateikiami Lietuvos oro erdvėje vykusių skrydžių duomenys iš Oro Navigacijos skrydžių statistikos duomenų bazės. Nurodoma su skrydžiais susijusi informacija: skrydžio data, orlaivio tipas, skrydį operavęs oro vežėjas, išvykimo ir atvykimo laikai bei išvykimo ir atvykimo oro uostai.

- **Namespace:** `datasets/gov/on/statistika`[^manifest]
- **Manifest CSV:** [datasets/gov/on/flight_data.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/on/flight_data.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/on/statistika`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Skrydis](statistika/Skrydis.md) | Oro Navigacijos skrydžių statistikos duomenys | `4` | `vda_id` | — | 21 | Rinkinyje pateikiami Lietuvos oro erdvėje vykusių skrydžių duomenys iš Oro Navigacijos skrydžių statistikos duomenų bazės. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/on/flight_data.csv
