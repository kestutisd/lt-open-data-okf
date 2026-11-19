---
type: Dataset
title: "Apdraustųjų skaičius, pagal DPSDR nustatytas draudimo grupes"
description: "Informacija apie PSD apdraustų asmenų skaičių pagal DPSDR nustatytas draudimo grupes"
resource: "https://get.data.gov.lt/datasets/gov/vlk/dpsdr_apdraustieji"
tags: [gov, vlk, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/dpsdr_apdraustieji.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vlk/dpsdr_apdraustieji.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1591/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/dpsdr_apdraustieji"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Apdraustųjų skaičius, pagal DPSDR nustatytas draudimo grupes

- **Namespace:** `datasets/gov/vlk/dpsdr_apdraustieji`[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/dpsdr_apdraustieji.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/dpsdr_apdraustieji.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/dpsdr_apdraustieji` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1591/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė ligonių kasa prie Sveikatos apsaugos ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vlk/dpsdr_apdraustieji`[^dcat]
- **Portal Title (`@lt`):** Apdraustųjų skaičius, pagal DPSDR nustatytas draudimo grupes[^dcat]
- **Portal Title (`@en`):** Number of insured persons, by groups DPSDR[^dcat]
- **Issued (`dct:issued`):** `2023-09-18`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-06-30` .. `2024-03-22`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Informacija apie PSD apdraustų asmenų skaičių pagal DPSDR nustatytas draudimo grupes[^dcat]

### Portal Description (`@en`)

Number of insured persons, by groups DPSDR[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Apdraustasis](dpsdr_apdraustieji/Apdraustasis.md) | Apdraustųjų skaičius | `4` | — | — | `4` | — |
| [Pagrindas](dpsdr_apdraustieji/Pagrindas.md) | Draudžiamųjų grupės | `4` | `kodas` | — | `2` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/dpsdr_apdraustieji.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/dpsdr_apdraustieji.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/dpsdr_apdraustieji (https://data.gov.lt/datasets/1591/)
