---
type: Dataset
title: "Adresų registras"
description: "Žemės sklypams, pastatams ir patalpoms suteiktų adresų tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (žemės sklypams ar pastatams suteiktus adresus apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/adresai"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/adresai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/adresai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2369/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/adresai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Adresų registras

- **Namespace:** `datasets/gov/rc/ar/adresai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/adresai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/adresai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/adresai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2369/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ar/adresai`[^dcat]
- **Portal Title (`@lt`):** Adresų registro žemės sklypams, pastatams ir patalpoms suteiktų adresų tekstiniai duomenys[^dcat]
- **Portal Title (`@en`):** Text data of addresses given to land parcels, buildings and premises in the Address Register[^dcat]
- **Issued (`dct:issued`):** `2023-10-09`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-10-09` .. `2026-10-22`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Žemės sklypams, pastatams ir patalpoms suteiktų adresų tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (žemės sklypams ar pastatams suteiktus adresus apibūdinantys duomenys). Duomenų geografinė imtis — visa Lietuvos teritorija.[^dcat]

### Portal Description (`@en`)

A set of text data of addresses given to land parcels, buildings and premises from the Address Register of the Republic of Lithuania (data describing addresses assigned to land parcels or buildings). The geographical sample of the data shall be the entire territory of Lithuania.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Adresas](adresai/Adresas.md) | Adresų registro žemės sklypams ir pastatams suteiktų adresų tekstiniai duomenys | `4` | `aob_kodas` | — | `4` | Žemės sklypams ir pastatams suteiktų adresų tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (žemės sklypams ar pastatams suteiktus... |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/adresai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/adresai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/adresai (https://data.gov.lt/datasets/2369/)
