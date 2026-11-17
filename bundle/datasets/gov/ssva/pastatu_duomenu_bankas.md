---
type: Dataset
title: "Pastatų ir jo elementų nusidėvėjimas ir rizikos"
description: "Informacija apie pastatų charakteristikas, pastatų ir jų elementų būklę."
resource: "https://get.data.gov.lt/datasets/gov/ssva/pastatu_duomenu_bankas"
tags: [gov, ssva, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ssva/pastatu_duomenu_bankas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pastatu_duomenu_bankas.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pastatų ir jo elementų nusidėvėjimas ir rizikos

Informacija apie pastatų charakteristikas, pastatų ir jų elementų būklę.

- **Namespace:** `datasets/gov/ssva/pastatu_duomenu_bankas`[^manifest]
- **Manifest CSV:** [datasets/gov/ssva/pastatu_duomenu_bankas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pastatu_duomenu_bankas.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/pastatu_duomenu_bankas`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PastatoElementoRizika](pastatu_duomenu_bankas/PastatoElementoRizika.md) | — | `4` | `rizikos_vertinimo_id` | — | 14 | — |
| [PastatoElementoNusidevejimas](pastatu_duomenu_bankas/PastatoElementoNusidevejimas.md) | — | `4` | `elemento_id` | — | 9 | — |
| [PastatoRizikaNusidevejimas](pastatu_duomenu_bankas/PastatoRizikaNusidevejimas.md) | — | — | `objekto_id` | — | 8 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/pastatu_duomenu_bankas.csv
