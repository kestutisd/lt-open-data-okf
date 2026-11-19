---
type: Dataset
title: "Pacientų valios pareiškimo duomenys"
description: "Duomenys apie pacientų valios pareiškimą (donorystės ir kiti duomenys) pagal amžiaus grupes, lytį ir gyvenamąją vietą"
resource: "https://get.data.gov.lt/datasets/gov/ntb/pacientu_valios_pareiskimai"
tags: [gov, ntb, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1210/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ntb/pacientu_valios_pareiskimai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Pacientų valios pareiškimo duomenys

- **Namespace:** `datasets/gov/ntb/pacientu_valios_pareiskimai`[^manifest]
- **Manifest CSV:** [datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ntb/pacientu_valios_pareiskimai` (`deployed`)[^manifest]
- **Provider:** `ntb` — Nacionalinis transplantacijos biuras prie Sveikatos apsaugos ministerijos *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1210/`[^dcat]
- **Publisher (`dct:publisher`):** Nacionalinis transplantacijos biuras prie Sveikatos apsaugos ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ntb/pacientu_valios_pareiskimai`[^dcat]
- **Portal Title (`@lt`):** Pacientų valios pareiškimo duomenys[^dcat]
- **Portal Title (`@en`):** Patient declaration data[^dcat]
- **Issued (`dct:issued`):** `2023-06-20`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-06-20` .. `2026-08-31`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys apie pacientų valios pareiškimą (donorystės ir kiti duomenys) pagal amžiaus grupes, lytį ir gyvenamąją vietą[^dcat]

### Portal Description (`@en`)

Patient declaration data (donation and other data) by age group, sex and place of residence[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [ValiosPareiskimas](pacientu_valios_pareiskimai/ValiosPareiskimas.md) | — | `4` | — | — | `7` | — |
| [ValiosPareiskimoOrganas](pacientu_valios_pareiskimai/ValiosPareiskimoOrganas.md) | — | `4` | `sutikimas` | — | `2` | — |
| [Organas](pacientu_valios_pareiskimai/Organas.md) | — | `4` | — | — | `2` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ntb/pacientu_valios_pareiskimai (https://data.gov.lt/datasets/1210/)
