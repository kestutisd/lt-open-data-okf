---
type: Dataset
title: "NTR teisių tipų ir teisių potipių klasifikatoriai"
description: "NTR teisių tipų ir teisių potipių klasifikatoriai (duomenų rinkinių grupė, viso 2vnt.) (NTR teisių ir suvaržymų tipų klasifikatorius; NTR teisių ir suvaržymų potipių klasifikatorius)"
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_teises"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_teises.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_teises.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1899/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_teises"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NTR teisių tipų ir teisių potipių klasifikatoriai

- **Namespace:** `datasets/gov/rc/ntr/ntr_teises`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_teises.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_teises.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_teises` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1899/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_teises`[^dcat]
- **Portal Title (`@lt`):** NTR teisių tipų ir teisių potipių klasifikatoriai[^dcat]
- **Portal Title (`@en`):** Classifications of NTR entitlement types and entitlement subtypes[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2022-04-01` .. `2025-05-21`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

NTR teisių tipų ir teisių potipių klasifikatoriai (duomenų rinkinių grupė, viso 2vnt.) (NTR teisių ir suvaržymų tipų klasifikatorius; NTR teisių ir suvaržymų potipių klasifikatorius)[^dcat]

### Portal Description (`@en`)

Classifications of NTR rights types and rights subtypes (data set group, 2 units in total) (NTR rights and restrictions types classification; NTR rights and restrictions subtype classification) Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NtrTeisesTipas](ntr_teises/NtrTeisesTipas.md) | NTR teisių ir suvaržymų tipai | `4` | `teit_tipas` | — | `8` | — |
| [NtrTeisesPotipis](ntr_teises/NtrTeisesPotipis.md) | NTR teisių ir suvaržymų potipiai | `4` | `teit_tipas, teip_potipis` | — | `14` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_teises.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_teises.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_teises (https://data.gov.lt/datasets/1899/)
