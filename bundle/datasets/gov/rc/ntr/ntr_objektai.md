---
type: Dataset
title: "NTR objektus apibūdinantys klasifikatoriai"
description: "NTR objektus apibūdinantys klasifikatoriai (duomenų rinkinių grupė, viso 5 vnt.) (NTR turto objektų grupių klasifikatorius, NTR objektų tipų klasifikatorius; NTR leistinų objektų tipų klasifikatorius; NTR objektų būklių klasifikatorius; NTR objektų statusų klasifikatorius)"
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_objektai"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_objektai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1895/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_objektai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NTR objektus apibūdinantys klasifikatoriai

- **Namespace:** `datasets/gov/rc/ntr/ntr_objektai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_objektai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_objektai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `5` (5 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1895/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_objektai`[^dcat]
- **Portal Title (`@lt`):** NTR objektus apibūdinantys klasifikatoriai[^dcat]
- **Portal Title (`@en`):** Classifiers describing NTR objects[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2022-04-01` .. `2025-05-21`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

NTR objektus apibūdinantys klasifikatoriai (duomenų rinkinių grupė, viso 5 vnt.) (NTR turto objektų grupių klasifikatorius, NTR objektų tipų klasifikatorius; NTR leistinų objektų tipų klasifikatorius; NTR objektų būklių klasifikatorius; NTR objektų statusų klasifikatorius)[^dcat]

### Portal Description (`@en`)

Classifiers describing NTR objects (data set group, 5 units in total) (NTR asset object group classification, NTR object type classification; NTR object object classification; NTR object status classification; NTR object status classification) Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NtrObjektoTipas](ntr_objektai/NtrObjektoTipas.md) | NT objektų tipų klasifikatorius | `4` | `obje_tipas` | — | `16` | — |
| [NtrLeisinasObjektoTipas](ntr_objektai/NtrLeisinasObjektoTipas.md) | Nurodytam registro tipui leistinų objektų tipų sąrašas - klasifikatorius | `3` | `regt_tipas, obje_tipas, loti_priklauso` | — | `6` | — |
| [NtrTurtoGrupe](ntr_objektai/NtrTurtoGrupe.md) | NTR turto objektų grupių klasifikatorius | `4` | `objg_grupe` | — | `4` | — |
| [NtrObjektoBukle](ntr_objektai/NtrObjektoBukle.md) | NTR objektų būklių klasifikatorius | `4` | `obuk_bukle` | — | `6` | — |
| [NtrObjektoStatusas](ntr_objektai/NtrObjektoStatusas.md) | NTR objektų statusų klasifikatorius | `4` | `osta_statusas` | — | `6` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_objektai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_objektai (https://data.gov.lt/datasets/1895/)
