---
type: Dataset
title: "Stacionaro lovų skaičius ir jų veiklos rodikliai"
description: "Pagal asmens sveikatos priežiūros įstaigą, lovų specialybės grupes, savivaldybes"
resource: "https://get.data.gov.lt/datasets/gov/hi/lovos"
tags: [gov, hi, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/lovos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/lovos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Stacionaro lovų skaičius ir jų veiklos rodikliai

Pagal asmens sveikatos priežiūros įstaigą, lovų specialybės grupes, savivaldybes

- **Namespace:** `datasets/gov/hi/lovos`[^manifest]
- **Manifest CSV:** [datasets/gov/hi/lovos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/lovos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/lovos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Istaiga](lovos/Istaiga.md) | Įstaigos | `4` | `istg_id` | — | 3 | — |
| [Savivaldybe](lovos/Savivaldybe.md) | Savivaldybės | `4` | `kod` | — | 3 | — |
| [LovosProfilis](lovos/LovosProfilis.md) | Lovų profiliai | `4` | `prof_kod` | — | 4 | — |
| [VeiklosRodiklis](lovos/VeiklosRodiklis.md) | Lovos veiklos rodikliai | `3` | — | — | 18 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/lovos.csv
