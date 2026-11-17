---
type: Dataset
title: "Valstybės pajamų ir išlaidų duomenys"
description: "Lietuvos Respublikos finansų ministerijos Atvirų finansų informacinėje sistemoje (AFIS) nuo 2015 m. kaupiami, kas 3 mėnesius atnaujinami ir atvėrimui numatyti automatiškai apdorojami viešųjų finansų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/finmin/afis"
tags: [gov, finmin, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/afis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/afis.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Valstybės pajamų ir išlaidų duomenys

Lietuvos Respublikos finansų ministerijos Atvirų finansų informacinėje sistemoje (AFIS) nuo 2015 m. kaupiami, kas 3 mėnesius atnaujinami ir atvėrimui numatyti automatiškai apdorojami viešųjų finansų duomenys. Sudaryti du duomenų rinkiniai tiek valstybinėms pajamoms, tiek išlaidoms.

- **Namespace:** `datasets/gov/finmin/afis`[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/afis.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/afis.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/afis`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PajamuEilute](afis/PajamuEilute.md) | Valstybės pajamų duomenys | `4` | `vda_id` | — | 11 | Lietuvos Respublikos finansų ministerijos Atvirų finansų informacinėje sistemoje (AFIS) nuo 2015 m. kaupiami, kas 3 mėnesius atnaujinami ir atvėrimui... |
| [IslaiduEilute](afis/IslaiduEilute.md) | Valstybės išlaidų duomenys | `4` | `vda_id` | — | 25 | Lietuvos Respublikos finansų ministerijos Atvirų finansų informacinėje sistemoje (AFIS) nuo 2015 m. kaupiami, kas 3 mėnesius atnaujinami ir atvėrimui... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/afis.csv
