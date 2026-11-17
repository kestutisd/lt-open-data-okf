---
type: Dataset
title: "VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos projektų duomenys"
description: "Duomenų rinkinyje pateikiami duomenys, susiję su VšĮ Centrinės projektų valdymo agentūros administruojamų Ignalinos programos projektų įgyvendinimu."
resource: "https://get.data.gov.lt/datasets/gov/cpva/ignalinos_programos/procesai"
tags: [gov, cpva, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/cpva/ignalinos_programu_procesai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_procesai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos projektų duomenys

Duomenų rinkinyje pateikiami duomenys, susiję su VšĮ Centrinės projektų valdymo agentūros administruojamų Ignalinos programos projektų įgyvendinimu. Duomenys pateikiami iš Projektų valdymo informacinės sistemos „Apecs“, skirtos automatizuotai valdyti Ignalinos programos procesus ir kontrolės sistemą.

Procesai suskirstyti į 3 kategorijas – procesus, subprocesus ir mikroprocesus, kurie ir pateikiami rinkinio atskirose 3-se lentelėse. „Procesas“ yra pati stambiausia procesų hierarchijos dalis. Jam priklauso subprocesai, o savo ruožtu, subprocesams priklauso mikroprocesai. Lentelės tarpusavyje jungiasi: mikroprocesai su subprocesais – mikroprocesai.priklauso_subprocesui = subprocesai.id;

subrocesai su procesais – subprocesai.priklauso_procesui = procesai.id

Duomenų atnaujinimas numatomas kas 3 mėn.

- **Namespace:** `datasets/gov/cpva/ignalinos_programos/procesai`[^manifest]
- **Manifest CSV:** [datasets/gov/cpva/ignalinos_programu_procesai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_procesai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/ignalinos_programos/procesai`
- **Parent Namespace (`ns`):** VšĮ Centrinė projektų valdymo agentūra (`datasets/gov/cpva`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Procesas](procesai/Procesas.md) | VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos informacinės sistemos „Apecs“ procesų sąrašas | `4` | `id` | — | 6 | — |
| [Subprocesas](procesai/Subprocesas.md) | VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos informacinės sistemos „Apecs“ subprocesų sąrašas | `4` | `id` | — | 8 | — |
| [Mikroprocesas](procesai/Mikroprocesas.md) | VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos informacinės sistemos „Apecs“ mikroprocesų sąrašas | `4` | `id` | — | 9 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/ignalinos_programu_procesai.csv
