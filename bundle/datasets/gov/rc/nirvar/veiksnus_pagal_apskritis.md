---
type: Dataset
title: "NIRVAR statistika apie teismo tvarka ribotai veiksniais pripažintus asmenis pagal apskritis ir registracijos metus"
description: "Agreguoti duomenys pagal apskritis ir registracijos metus."
resource: "https://get.data.gov.lt/datasets/gov/rc/nirvar/veiksnus_pagal_apskritis"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/nirvar/veiksnus_pagal_apskritis.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/nirvar/veiksnus_pagal_apskritis.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2149/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/nirvar/veiksnus_pagal_apskritis"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NIRVAR statistika apie teismo tvarka ribotai veiksniais pripažintus asmenis pagal apskritis ir registracijos metus

- **Namespace:** `datasets/gov/rc/nirvar/veiksnus_pagal_apskritis`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/nirvar/veiksnus_pagal_apskritis.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/nirvar/veiksnus_pagal_apskritis.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/nirvar/veiksnus_pagal_apskritis` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2149/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/nirvar/veiksnus_pagal_apskritis`[^dcat]
- **Portal Title (`@lt`):** NIRVAR statistika apie teismo tvarka ribotai veiksniais pripažintus asmenis pagal apskritis ir registracijos metus[^dcat]
- **Portal Title (`@en`):** NIRVAR statistics on persons recognized as limited factors by court order by county and year of registration[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-01-04` .. `2025-09-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Agreguoti duomenys pagal apskritis ir registracijos metus. NIRVAR statistika apie teismo tvarka neveiksniais pripažintus asmenis. Neveiksnių ir ribotai veiksnių asmenų registro (NIRVAR) statistiniai duomenys.[^dcat]

### Portal Description (`@en`)

Aggregated data by county and year of registration. NIRVAR statistics on persons declared incompetent by court procedure. Statistical data of the Register of Inactive and Limitedly Active Persons (NIRVAR). The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [RibotaiVeiksnusApskritis](veiksnus_pagal_apskritis/RibotaiVeiksnusApskritis.md) | NIRVAR statistika apie teismo tvarka ribotai veiksniais pripažintus asmenis pagal apskritis ir registracijos metus | `3` | `apskritis, reg_met` | — | `3` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/nirvar/veiksnus_pagal_apskritis.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/nirvar/veiksnus_pagal_apskritis.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/nirvar/veiksnus_pagal_apskritis (https://data.gov.lt/datasets/2149/)
