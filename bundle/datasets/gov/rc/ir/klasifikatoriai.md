---
type: Dataset
title: "Įgaliojimų registro (ĮR) įgaliojimų rūšių, terminų ir paslaugų klasifikatoriai"
description: "Spinta dataset datasets/gov/rc/ir/klasifikatoriai (3 tables)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ir/klasifikatoriai"
tags: [gov, rc, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ir/klasifikatoriai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/klasifikatoriai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Įgaliojimų registro (ĮR) įgaliojimų rūšių, terminų ir paslaugų klasifikatoriai

- **Namespace:** `datasets/gov/rc/ir/klasifikatoriai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ir/klasifikatoriai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/klasifikatoriai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ir/klasifikatoriai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Terminas](klasifikatoriai/Terminas.md) | Įgaliojimų registro terminų klasifikatorius | `4` | `kodas` | — | 2 | — |
| [IgaliojimoTipas](klasifikatoriai/IgaliojimoTipas.md) | Įgaliojimų registro informacinių technologijų priemonėmis sudarytų įgaliojimų tipų klasifikatorius | `4` | `kodas` | — | 2 | — |
| [Paslauga](klasifikatoriai/Paslauga.md) | Įgaliojimų registro viešųjų ir administracinių paslaugų klasifikatorius | `4` | `id` | — | 5 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ir/klasifikatoriai.csv
