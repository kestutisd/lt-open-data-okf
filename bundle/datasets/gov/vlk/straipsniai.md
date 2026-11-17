---
type: Dataset
title: "datasets/gov/vlk/straipsniai"
description: "Spinta dataset datasets/gov/vlk/straipsniai (2 tables)."
resource: "https://get.data.gov.lt/datasets/gov/vlk/straipsniai"
tags: [gov, vlk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/straipsniai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/straipsniai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/vlk/straipsniai

- **Namespace:** `datasets/gov/vlk/straipsniai`[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/straipsniai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/straipsniai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/straipsniai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Straipsnis](straipsniai/Straipsnis.md) | PSDF biudžeto straipsnių sąrašas | `4` | `ad_id` | — | 5 | PSDF biudžeto straipsnių, pagal kuriuos apmokamos asmens sveikatos priežiūros paslaugos, sąrašas |
| [Paslauga](straipsniai/Paslauga.md) | Asmens sveikatos priežiūros paslaugų, priskirtų PSDF biudžeto straipsniams, sąrašas | `4` | `ad_id` | — | 5 | Informacija apie asmens sveikatos priežiūros paslaugų, priskirtų PSDF biudžeto straipsniams, sąrašą |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/straipsniai.csv
