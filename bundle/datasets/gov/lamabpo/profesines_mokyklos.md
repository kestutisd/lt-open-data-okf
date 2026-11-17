---
type: Dataset
title: "Priėmimo į profesinio mokymo įstaigas prašymų duomenys"
description: "Rinkinyje pateikiama informacija apie nuo 2024 m. pateiktus priėmimo prašymus į profesinio mokymo įstaigas Lietuvoje."
resource: "https://get.data.gov.lt/datasets/gov/lamabpo/profesines_mokyklos"
tags: [gov, lamabpo, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lamabpo/profesiniu_prasymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/profesiniu_prasymai.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Priėmimo į profesinio mokymo įstaigas prašymų duomenys

Rinkinyje pateikiama informacija apie nuo 2024 m. pateiktus priėmimo prašymus į profesinio mokymo įstaigas Lietuvoje. Rinkinį sudaro trys komponentai:

1. Profesinio mokymo programų duomenys,

2. Priėmimo prašymų duomenys,

3. Priėmimo prašymus teikusių asmenų duomenys.

Duomenų teikėjas: Lietuvos aukštųjų mokyklų asociacija bendrajam priėmimui organizuoti (LAMA BPO).

- **Namespace:** `datasets/gov/lamabpo/profesines_mokyklos`[^manifest]
- **Manifest CSV:** [datasets/gov/lamabpo/profesiniu_prasymai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/profesiniu_prasymai.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lamabpo/profesines_mokyklos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Programa](profesines_mokyklos/Programa.md) | Profesinio mokymo programų duomenys | `4` | `programos_id` | — | 20 | Pateikiami profesinio mokymo programų duomenys Lietuvos profesinio mokymo įstaigose. |
| [Prasymas](profesines_mokyklos/Prasymas.md) | Priėmimo prašymų į profesines mokyklas duomenys | `4` | `prasymo_id` | — | 11 | Lentelėje pateikiami priėmimo į profesinio mokymo įstaigas duomenys. |
| [Profilis](profesines_mokyklos/Profilis.md) | Priėmimo prašymus į profesinio mokymo įstaigas teikusių asmenų profilis | `4` | `asmens_id` | — | 10 | Lentelėje pateikiami demografiniai duomenys apie asmenis, teikusius priėmimo prašymus į profesinio mokymo įstaigas. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lamabpo/profesiniu_prasymai.csv
