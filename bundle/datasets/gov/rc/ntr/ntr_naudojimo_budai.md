---
type: Dataset
title: "NTR paskirčių klasifikatoriai"
description: "NTR naudojimo būdų klasifikatoriai (duomenų rinkinių grupė, viso 3 vnt.) (NTR naudojimo būdų klasifikatorius; NTR leistinų naudojimo būdų klasifikatorius, NTR naudojimo pobūdžių klasifikatorius)"
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_naudojimo_budai"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_naudojimo_budai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_naudojimo_budai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1898/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_naudojimo_budai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NTR paskirčių klasifikatoriai

- **Namespace:** `datasets/gov/rc/ntr/ntr_naudojimo_budai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_naudojimo_budai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_naudojimo_budai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_naudojimo_budai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1898/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_naudojimo_budai`[^dcat]
- **Portal Title (`@lt`):** NTR naudojimo būdų klasifikatoriai[^dcat]
- **Portal Title (`@en`):** Classifications of NTR uses[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2022-04-01` .. `2023-06-30`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

NTR naudojimo būdų klasifikatoriai (duomenų rinkinių grupė, viso 3 vnt.) (NTR naudojimo būdų klasifikatorius; NTR leistinų naudojimo būdų klasifikatorius, NTR naudojimo pobūdžių klasifikatorius)[^dcat]

### Portal Description (`@en`)

NTR use classifications (data set group, 3 units in total) (NTR use classification; NTR permitted use classification, NTR use classification) Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NtrNaudojimoBudas](ntr_naudojimo_budai/NtrNaudojimoBudas.md) | NTR naudojimo būdai | `4` | `naub_budas` | — | `7` | — |
| [NtrNaudojimoPubudis](ntr_naudojimo_budai/NtrNaudojimoPubudis.md) | NTR naudojimo pobūdžiai | `4` | `npob_pobudis` | — | `9` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_naudojimo_budai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_naudojimo_budai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_naudojimo_budai (https://data.gov.lt/datasets/1898/)
