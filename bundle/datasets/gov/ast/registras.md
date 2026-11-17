---
type: Dataset
title: "Alytaus šilumos tinklų iškvietimų, nusiskundimų ir konsultacijų registras"
description: "Duomenų rininyje pateikiami nuo 2024 m. kaupiami Alytaus šilumos tinklų klientų nusiskundimų, konsultacijų ir iškvietimų žurnalo duomenys."
resource: "https://get.data.gov.lt/datasets/gov/ast/registras"
tags: [gov, ast, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ast/konsultacijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/konsultacijos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Alytaus šilumos tinklų iškvietimų, nusiskundimų ir konsultacijų registras

Duomenų rininyje pateikiami nuo 2024 m. kaupiami Alytaus šilumos tinklų klientų nusiskundimų, konsultacijų ir iškvietimų žurnalo duomenys. Rinkinio objektas – įmonės kliento kreipimasis į Alytaus šilumos tinklus. Rinkinyje nurodoma iškvietimo informacija – gatvė, namo numeris ir iškvietimo priežastis. Taip pat pateikiama pagal iškvietimą vykdytų darbų informacija: darbus atlikusio asmens identifikatorius (sudarytas užšifravus atsakingo darbuotojo vardą ir pavardę), darbų trukmė valandos ir minučių tikslumu, pabaigos žyma, identifikuota gedimo priežastis ir bendra darbų trukmė nuo iškvietimo momento iki darbų užbaigimo.

- **Namespace:** `datasets/gov/ast/registras`[^manifest]
- **Manifest CSV:** [datasets/gov/ast/konsultacijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/konsultacijos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ast/registras`
- **Parent Namespace (`ns`):** Alytaus šilumos tinklai (`datasets/gov/ast`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Iskvietimas](registras/Iskvietimas.md) | Alytaus šilumos tinklų iškvietimų, nusiskundimų ir konsultacijų registras | `4` | `vda_id` | — | 11 | Duomenų rininyje pateikiami nuo 2024 m. kaupiami Alytaus šilumos tinklų klientų nusiskundimų, konsultacijų ir iškvietimų žurnalo duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ast/konsultacijos.csv
