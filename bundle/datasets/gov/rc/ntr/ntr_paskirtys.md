---
type: Dataset
title: "NTR paskirčių klasifikatoriai"
description: "NTR paskirčių klasifikatoriai (duomenų rinkinių grupė, viso 3 vnt.) ( NTR paskirčių grupių klasifikatorius; NTR paskirčių tipų klasifikatorius; NTR leistinų paskirčių klasifikatorius )"
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_paskirtys"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_paskirtys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_paskirtys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1897/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_paskirtys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NTR paskirčių klasifikatoriai

- **Namespace:** `datasets/gov/rc/ntr/ntr_paskirtys`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_paskirtys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_paskirtys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_paskirtys` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1897/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_paskirtys`[^dcat]
- **Portal Title (`@lt`):** NTR paskirčių klasifikatoriai[^dcat]
- **Portal Title (`@en`):** NTR purpose classifiers[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2022-04-01` .. `2025-05-21`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

NTR paskirčių klasifikatoriai (duomenų rinkinių grupė, viso 3 vnt.) ( NTR paskirčių grupių klasifikatorius; NTR paskirčių tipų klasifikatorius; NTR leistinų paskirčių klasifikatorius )[^dcat]

### Portal Description (`@en`)

Classifications of NTR uses (data set group, 3 units in total) (Classification of NTR purpose groups; Classification of NTR purpose types; NTR classification of permitted uses) Geographical sample of the data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NtrPaskirtiesGrupe](ntr_paskirtys/NtrPaskirtiesGrupe.md) | NTR paskirčių grupės | `4` | `pasg_grupe` | — | `4` | — |
| [NtrPaskirtiesTipas](ntr_paskirtys/NtrPaskirtiesTipas.md) | NTR paskirčių tipai | `4` | `pask_tipas` | — | `6` | — |
| [NtrLeistinaPaskirtis](ntr_paskirtys/NtrLeistinaPaskirtis.md) | NTR leistinos paskirtys pagal objekto tipus | `3` | `obje_tipas` | — | `3` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_paskirtys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_paskirtys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_paskirtys (https://data.gov.lt/datasets/1897/)
