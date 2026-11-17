---
type: Dataset
title: "Projekto „Mokykis visą gyvenimą!“ dalyvių ir kursų duomenys"
description: "Rinkinyje pateikiama informacija apie projekto „Mokykis visą gyvenimą!“ (MVG) dalyvius ir vykdomas kursų programas."
resource: "https://get.data.gov.lt/datasets/gov/lamabpo/mvg_programa"
tags: [gov, lamabpo, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lamabpo/mvg_programa.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/mvg_programa.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Projekto „Mokykis visą gyvenimą!“ dalyvių ir kursų duomenys

Rinkinyje pateikiama informacija apie projekto „Mokykis visą gyvenimą!“ (MVG) dalyvius ir vykdomas kursų programas. Rinkinį sudaro dvi lentelės – „MVG dalyvių duomenys“ ir „MVG kursų duomenys“.

Duomenų teikėjas – Lietuvos aukštųjų mokyklų asociacija bendram priėmimui organizuoti (LAMA BPO).

- **Namespace:** `datasets/gov/lamabpo/mvg_programa`[^manifest]
- **Manifest CSV:** [datasets/gov/lamabpo/mvg_programa.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/mvg_programa.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lamabpo/mvg_programa`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [KursoDalyvis](mvg_programa/KursoDalyvis.md) | MVG dalyvių duomenys | `4` | `vda_prime_key` | — | 10 | Lentelėje pateikiami MVG programoje dalyvaujančių ar praeityje dalyvavusių dalyvių duomenys. |
| [KursoGrupe](mvg_programa/KursoGrupe.md) | MVG kursų duomenys | `4` | `kursu_grupes_id` | — | 22 | Lentelėje pateikiami projekte „Mokykis visą gyvenimą!“ (MVG) vykdomus kursus. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lamabpo/mvg_programa.csv
