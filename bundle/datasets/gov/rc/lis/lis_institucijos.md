---
type: Dataset
title: "Licencijų informacinės sistemos licencijas išduodančių institucijų klasifikatorius"
description: "Licencijų informacinės sistemos licencijas išduodančių institucijų klasifikatorius."
resource: "https://get.data.gov.lt/datasets/gov/rc/lis/lis_institucijos"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_institucijos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/lis/lis_institucijos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1807/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/lis/lis_institucijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Licencijų informacinės sistemos licencijas išduodančių institucijų klasifikatorius

- **Namespace:** `datasets/gov/rc/lis/lis_institucijos`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/lis/lis_institucijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_institucijos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/lis/lis_institucijos` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1807/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/lis/lis_institucijos`[^dcat]
- **Portal Title (`@lt`):** Licencijų informacinės sistemos licencijas išduodančių institucijų klasifikatorius[^dcat]
- **Portal Title (`@en`):** Classification of Licensing Authorities for the License Information System[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2022-02-04` .. `2026-03-09`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Licencijų informacinės sistemos licencijas išduodančių institucijų klasifikatorius.[^dcat]

### Portal Description (`@en`)

Classification of Licensing Authorities for the License Information System. Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [LisInstitucija](lis_institucijos/LisInstitucija.md) | Licencijas išduodančių institucijų klasifikatorius | `4` | `juridinis_asmuo` | — | `1` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/lis/lis_institucijos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_institucijos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/lis/lis_institucijos (https://data.gov.lt/datasets/1807/)
