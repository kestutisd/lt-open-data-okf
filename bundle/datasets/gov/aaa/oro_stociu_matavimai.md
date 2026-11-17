---
type: Dataset
title: "Lietuvos valstybinio oro monitoringo automatinių stočių matavimo duomenys"
description: "Spinta dataset datasets/gov/aaa/oro_stociu_matavimai (5 tables)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai"
tags: [gov, aaa, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Lietuvos valstybinio oro monitoringo automatinių stočių matavimo duomenys

- **Namespace:** `datasets/gov/aaa/oro_stociu_matavimai`[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/oro_stociu_matavimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Station](oro_stociu_matavimai/Station.md) | Oro kokybės matavimo stotys | `4` | `stat_num` | — | 3 | — |
| [Units](oro_stociu_matavimai/Units.md) | Matavimo vienetai | `4` | `code_unit` | — | 3 | — |
| [Quantity](oro_stociu_matavimai/Quantity.md) | Teršalai | `4` | `code_quantity` | — | 6 | — |
| [Averages](oro_stociu_matavimai/Averages.md) | Valandiniai oro kokybės matavimai | `4` | `id` | — | 6 | — |
| [QuantityUnits](oro_stociu_matavimai/QuantityUnits.md) | Tarpinė lenta | `4` | `code_combi` | — | 3 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv
