---
type: Dataset
title: "Licencijų informacinė sistemos tipų ir rūšių klasifikatoriai"
description: "Licencijų informacinės sistemos tipų ir rūšių klasifikatoriai (duomenų rinkinių grupė, viso 2 vnt.) (LIS tipų (sąryšis su rūšimis) klasifikatorius; LIS rūšių klasifikatorius)"
resource: "https://get.data.gov.lt/datasets/gov/rc/lis/lis_rusys_tipai"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_rusys_tipai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/lis/lis_rusys_tipai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1808/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/lis/lis_rusys_tipai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Licencijų informacinė sistemos tipų ir rūšių klasifikatoriai

- **Namespace:** `datasets/gov/rc/lis/lis_rusys_tipai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/lis/lis_rusys_tipai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_rusys_tipai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/lis/lis_rusys_tipai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1808/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/lis/lis_rusys_tipai`[^dcat]
- **Portal Title (`@lt`):** Licencijų informacinės sistemos tipų ir rūšių klasifikatoriai[^dcat]
- **Portal Title (`@en`):** Classifiers of types and types of license information system[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2022-02-04` .. `2026-03-09`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Licencijų informacinės sistemos tipų ir rūšių klasifikatoriai (duomenų rinkinių grupė, viso 2 vnt.) (LIS tipų (sąryšis su rūšimis) klasifikatorius; LIS rūšių klasifikatorius)[^dcat]

### Portal Description (`@en`)

License information system types and species classifiers (group of data sets, 2 units in total) (LIS types (relationship with species) classifier; LIS species classifier) Geographic sample of data — the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [LisRusis](lis_rusys_tipai/LisRusis.md) | Licencijų rūšių klasifikatorius | `4` | `kodas` | — | `2` | — |
| [LisTipas](lis_rusys_tipai/LisTipas.md) | Licencijų tipų klasifikatorius | `4` | `kodas` | — | `2` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/lis/lis_rusys_tipai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_rusys_tipai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/lis/lis_rusys_tipai (https://data.gov.lt/datasets/1808/)
