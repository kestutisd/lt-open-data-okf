---
type: Dataset
title: "Laboratorinių tyrimų agreguoti skaičiai"
description: "Pacientams atliktų laboratorinių tyrimų agreguotas skaičius iš VDV IS integruotų ligoninių ir poliklinikų laboratorinių tyrimų rinkinių."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/lab_tyrimai"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/lab_tyrimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/lab_tyrimai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Laboratorinių tyrimų agreguoti skaičiai

Pacientams atliktų laboratorinių tyrimų agreguotas skaičius iš VDV IS integruotų ligoninių ir poliklinikų laboratorinių tyrimų rinkinių. Laboratorinių tyrimų agreguotas skaičius, koduojamų su LOINC ir be LOINC, pateiktas atskirai.

- **Namespace:** `datasets/gov/lsd/sveikata/lab_tyrimai`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/lab_tyrimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/lab_tyrimai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/lab_tyrimai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [LaboratorinisTyrimas](lab_tyrimai/LaboratorinisTyrimas.md) | Laboratorinių tyrimų agreguoti skaičiai | `4` | `vda_id` | — | 5 | Pacientams atliktų laboratorinių tyrimų agreguotas skaičius iš VDV IS integruotų ligoninių ir poliklinikų laboratorinių tyrimų rinkinių. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/lab_tyrimai.csv
