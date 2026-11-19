---
type: Dataset
title: "Valstybės institucijų ūkio subjektams išduoti LEIDIMAI"
description: "Licencijų informacinės sistemos (LIS) duomenys apie valstybės institucijų ūkio subjektams išduotus leidimus (LIS dokumentų rūšis)."
resource: "https://get.data.gov.lt/datasets/gov/rc/lis/lis_leidimai"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_leidimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/lis/lis_leidimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1708/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/lis/lis_leidimai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Valstybės institucijų ūkio subjektams išduoti LEIDIMAI

- **Namespace:** `datasets/gov/rc/lis/lis_leidimai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/lis/lis_leidimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_leidimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/lis/lis_leidimai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1708/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/lis/lis_leidimai`[^dcat]
- **Portal Title (`@lt`):** Valstybės institucijų ūkio subjektams išduoti LEIDIMAI[^dcat]
- **Portal Title (`@en`):** PERMITS issued by state institutions to economic entities[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2021-11-24` .. `2026-03-09`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Licencijų informacinės sistemos (LIS) duomenys apie valstybės institucijų ūkio subjektams išduotus leidimus (LIS dokumentų rūšis).[^dcat]

### Portal Description (`@en`)

Data of the License Information System (LIS) on permits issued to economic entities by state institutions. Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [LisLeidimas](lis_leidimai/LisLeidimas.md) | Licencijų informacinės sistemos duomenys apie valstybės institucijų ūkio subjektams išduotus leidimus | `4` | `id` | — | `10` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/lis/lis_leidimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_leidimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/lis/lis_leidimai (https://data.gov.lt/datasets/1708/)
