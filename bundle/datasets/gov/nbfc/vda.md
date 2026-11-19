---
type: Dataset
title: "Valstybės duomenų agentūros darbuotojai"
description: "Institucijų darbuotojų informacija pagal gimimo metus, lytį, darbo pradžią, pabaigą, skyrių, instituciją."
resource: "https://get.data.gov.lt/datasets/gov/nbfc/vda"
tags: [gov, nbfc, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/vda.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/nbfc/vda.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Valstybės duomenų agentūros darbuotojai

Institucijų darbuotojų informacija pagal gimimo metus, lytį, darbo pradžią, pabaigą, skyrių, instituciją. Gimimo metai apvalinami iki dešimties. Priimti ir atleisti iki 2022-01-01 dienos į rinkinį nepatenka. Priimti prieš 2022-01-01, ir atleisti po 2022-01-01 arba dirbantys iki dabar - yra rinkinyje.[^manifest]

- **Namespace:** `datasets/gov/nbfc/vda`[^manifest]
- **Manifest CSV:** [datasets/gov/nbfc/vda.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/vda.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nbfc/vda` (`deployed`)[^manifest]
- **Provider:** `nbfc` — Nacionalinis bendrųjų funkcijų centras *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [InstitucijosDarbuotojas](vda/InstitucijosDarbuotojas.md) | Valstybės duomenų agentūros darbuotojai | `4` | `tabelio_nr` | — | `12` | Institucijų darbuotojų informacija pagal gimimo metus, lytį, darbo pradžią, pabaigą, skyrių, instituciją. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/nbfc/vda.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/vda.csv#L3)
