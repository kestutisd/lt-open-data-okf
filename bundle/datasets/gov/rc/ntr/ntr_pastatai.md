---
type: Dataset
title: "Nekilnojamojo turto registre įregistruotų pastatų duomenys pagal savivaldybes"
description: "Nekilnojamojo turto registre (NTR) įregistruotų pastatų duomenys pagal savivaldybes (rinkinių grupė, viso 60 vnt.)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_pastatai"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_pastatai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_pastatai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1812/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_pastatai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Nekilnojamojo turto registre įregistruotų pastatų duomenys pagal savivaldybes

- **Namespace:** `datasets/gov/rc/ntr/ntr_pastatai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_pastatai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_pastatai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_pastatai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1812/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_pastatai`[^dcat]
- **Portal Title (`@lt`):** Nekilnojamojo turto registre įregistruotų pastatų duomenys pagal savivaldybes[^dcat]
- **Portal Title (`@en`):** Data on buildings registered in the Real Estate Register by municipalities[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2022-02-07` .. `2025-05-21`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Nekilnojamojo turto registre (NTR) įregistruotų pastatų duomenys pagal savivaldybes (rinkinių grupė, viso 60 vnt.). NTR įregistruotų pastatų kategorija (rūšis pagal Statybos įstatymą), tipas, paskirtis, įvairūs plotai (užstatytas, bendras, naudingas, gyvenamas, verslo, pagalbinis nenaudingas ir t. t.), patalpų skaičius pagal paskirtį, aukštų skaičius, statybos ir modernizavimo metai, energetinė klasė, konstrukcinių dalių medžiagos, būtiniausi gerbūvio elementų duomenys.[^dcat]

### Portal Description (`@en`)

Data on buildings registered in the Real Estate Register (NTR) by municipalities (group of collections, 60 units in total). Category of buildings registered in the NTR (type according to the Law on Construction), type, purpose, various areas (built-up, common, useful, residential, business, ancillary, etc.), number of premises by purpose, number of storeys, year of construction and modernization, energy class, materials of structural parts, minimum data of welfare elements. Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NtrPastatas](ntr_pastatai/NtrPastatas.md) | — | `4` | `id` | — | `43` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_pastatai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_pastatai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_pastatai (https://data.gov.lt/datasets/1812/)
