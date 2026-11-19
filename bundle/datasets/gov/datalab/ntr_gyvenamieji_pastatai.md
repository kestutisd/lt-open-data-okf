---
type: Dataset
title: "NTR pastatų atributai"
description: "Duomenų rinkinį sudaro duomenys apie gyvenamuosius pastatus pagal savivaldybę, seniūniją, pastato pagrindinius požymius (statybos metai, užbaigtumas, plotas ir kt.), energetinį efektyvumą, šiluminės energijos sąnaudas bei išmetamą CO2 kiekį."
resource: "https://get.data.gov.lt/datasets/gov/datalab/ntr_gyvenamieji_pastatai"
tags: [gov, datalab, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/datalab/ntr_gyvenamieji_pastatai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/datalab/ntr_gyvenamieji_pastatai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3916/"
    title: "data.gov.lt DCAT-AP — datasets/gov/datalab/ntr_gyvenamieji_pastatai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NTR pastatų atributai

- **Namespace:** `datasets/gov/datalab/ntr_gyvenamieji_pastatai`[^manifest]
- **Manifest CSV:** [datasets/gov/datalab/ntr_gyvenamieji_pastatai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/datalab/ntr_gyvenamieji_pastatai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/datalab/ntr_gyvenamieji_pastatai` (`deployed`)[^manifest]
- **Provider:** `datalab` — Valstybės duomenų agentūra (DataLab) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3916/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/datalab/ntr_gyvenamieji_pastatai`[^dcat]
- **Portal Title (`@lt`):** Savivaldos Datalab aplikacijos „Pastatų būklė“ duomenys (gyvenamieji pastatai)[^dcat]
- **Portal Title (`@en`):** Data on the application of municipal Datalab “State of Buildings” (residential buildings)[^dcat]
- **Issued (`dct:issued`):** `2025-10-21`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2025-10-21` .. `2025-11-30`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinį sudaro duomenys apie gyvenamuosius pastatus pagal savivaldybę, seniūniją, pastato pagrindinius požymius (statybos metai, užbaigtumas, plotas ir kt.), energetinį efektyvumą, šiluminės energijos sąnaudas bei išmetamą CO2 kiekį. Duomenų šaltiniai: Lietuvos Respublikos nekilnojamojo turto registras Pastatų energetinio naudingumo sertifikatų ir pastatų energetinio naudingumo sertifikavimo ekspertų informacinė sistema Lietuvos Respublikos statybos leidimų ir statybos valstybinės priežiūros informacinė sistema „Infostatyba“. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt[^dcat]

### Portal Description (`@en`)

The dataset consists of data on residential buildings by municipality, neighborhood, main features of the building (year of construction, completeness, area, etc.), energy efficiency, thermal energy consumption and CO2 emissions. Data sources: Real estate Register of the Republic of Lithuania Information System of Experts on Energy Performance Certificates of Buildings and Energy Performance Certificates of Buildings Infostatyba information system of state supervision of construction permits and construction of the Republic of Lithuania. For data-related issues please contact atverimas@stat.gov.lt by e-mail For technical problems with the portal, please contact atviriduomenys@vssa.lt by e-mail[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [GyvenamojoPastatoAtributas](ntr_gyvenamieji_pastatai/GyvenamojoPastatoAtributas.md) | Pastatų atributas | `4` | `vda_id` | — | `41` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/datalab/ntr_gyvenamieji_pastatai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/datalab/ntr_gyvenamieji_pastatai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/datalab/ntr_gyvenamieji_pastatai (https://data.gov.lt/datasets/3916/)
