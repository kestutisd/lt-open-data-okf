---
type: Dataset
title: "NIRVAR statistika apie teismo tvarka neveiksniais pripažintus asmenis pagal amžiaus grupes ir lytį"
description: "Agreguoti NIRVAR duomenys pagal amžiaus grupes ir lytį."
resource: "https://get.data.gov.lt/datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2147/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NIRVAR statistika apie teismo tvarka neveiksniais pripažintus asmenis pagal amžiaus grupes ir lytį

- **Namespace:** `datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2147/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti`[^dcat]
- **Portal Title (`@lt`):** NIRVAR statistika apie teismo tvarka neveiksniais pripažintus asmenis pagal amžiaus grupes ir lytį[^dcat]
- **Portal Title (`@en`):** NIRVAR statistics on persons recognized as incompetent by court by age group and gender[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-01-04` .. `2025-09-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Agreguoti NIRVAR duomenys pagal amžiaus grupes ir lytį. NIRVAR statistika apie teismo tvarka neveiksniais pripažintus asmenis. Neveiksnių ir ribotai veiksnių asmenų registro (NIRVAR) statistiniai duomenys.[^dcat]

### Portal Description (`@en`)

Aggregated NIRVAR data by age group and sex. NIRVAR statistics on persons declared incompetent by court procedure. Statistical data of the Register of Inactive and Limitedly Active Persons (NIRVAR). The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NeveiksnusAmziusLytis](neveiksnus_pagal_amziu_lyti/NeveiksnusAmziusLytis.md) | NIRVAR statistika apie teismo tvarka neveiksniais pripažintus asmenis pagal amžiaus grupes ir lytį | `4` | `amziaus_grupe, asm_lytis` | — | `3` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti (https://data.gov.lt/datasets/2147/)
