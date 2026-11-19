---
type: Dataset
title: "OSS specialiųjų schemų naudotojų deklaracijų duomenys"
description: "Agreguoti „ONE STOP SHOP“ (OSS) specialiųjų schemų Lietuvos naudotojų PVM deklaracijų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vmi/oss_deklaracijos"
tags: [gov, vmi, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/oss.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmi/oss.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1910/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/oss_deklaracijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# OSS specialiųjų schemų naudotojų deklaracijų duomenys

- **Namespace:** `datasets/gov/vmi/oss_deklaracijos`[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/oss.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/oss.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/oss_deklaracijos` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1910/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė mokesčių inspekcija prie Finansų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmi/oss_deklaracijos`[^dcat]
- **Portal Title (`@lt`):** OSS specialiųjų schemų naudotojų deklaracijų duomenys[^dcat]
- **Portal Title (`@en`):** Data on declarations of users of OSS special schemes[^dcat]
- **Issued (`dct:issued`):** `2022-12-15`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2022-12-15` .. `2026-10-17`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Agreguoti „ONE STOP SHOP“ (OSS) specialiųjų schemų Lietuvos naudotojų PVM deklaracijų duomenys. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on VAT declarations of Lithuanian users of ONE STOP SHOP (OSS) special schemes have been aggregated[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [OssDeklaracija](oss_deklaracijos/OssDeklaracija.md) | OSS Deklaracijoas | `4` | — | — | `19` | One Stop Shop (OSS) - tai sistema, kuri palengvina mokestinių PVM prievolių vykdymą ūkio subjektams, parduodantiems neapmokestinamiesiems asmenims tam... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://atviriduomenys.readthedocs.io/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/oss.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/oss.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/oss_deklaracijos (https://data.gov.lt/datasets/1910/)
