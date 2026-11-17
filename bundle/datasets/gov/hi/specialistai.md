---
type: Dataset
title: "Visuomenės sveikatos priežiūros specialistų duomenys"
description: "Specialistai, atliekantys visuomenės sveikatos priežiūros funkcijas Lietuvos nacionalinės sveikatos sistemos visuomenės sveikatos priežiūros įstaigose (amžiaus grupė, išsilavinimas, lytis, įstaigų grupė)."
resource: "https://get.data.gov.lt/datasets/gov/hi/specialistai"
tags: [gov, hi, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/specialistai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Visuomenės sveikatos priežiūros specialistų duomenys

Specialistai, atliekantys visuomenės sveikatos priežiūros funkcijas Lietuvos nacionalinės sveikatos sistemos visuomenės sveikatos priežiūros įstaigose (amžiaus grupė, išsilavinimas, lytis, įstaigų grupė).

- **Namespace:** `datasets/gov/hi/specialistai`[^manifest]
- **Manifest CSV:** [datasets/gov/hi/specialistai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/specialistai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Issilavinimas](specialistai/Issilavinimas.md) | Visuomenės sveikatos specialistų duomenys pagal išsilavinimą | `3` | — | — | 7 | — |
| [Etatas](specialistai/Etatas.md) | Visuomenės sveikatos specialistų duomenys pagal darbo etatus | `4` | `m_id` | — | 6 | — |
| [Juridinis](specialistai/Juridinis.md) | Juridiniai asmenys | `3` | — | — | 8 | Kuriuose dirba visuomenės sveikatos specialistai |
| [Programa](specialistai/Programa.md) | Studijų programos | `3` | — | — | 3 | Kurias yra baigę visuomenės sveikatos specialistai |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/specialistai.csv
