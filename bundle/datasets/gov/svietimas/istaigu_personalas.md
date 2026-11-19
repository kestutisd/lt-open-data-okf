---
type: Dataset
title: "Lietuvos savivaldybių švietimo įstaigų personalas"
description: "Rinkinyje pateikti Lietuvos savivaldybių švietimo įstaigų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/svietimas/istaigu_personalas"
tags: [gov, svietimas, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/svietimas/istaigu_personalas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/svietimas/istaigu_personalas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3815/"
    title: "data.gov.lt DCAT-AP — datasets/gov/svietimas/istaigu_personalas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Lietuvos savivaldybių švietimo įstaigų personalas

- **Namespace:** `datasets/gov/svietimas/istaigu_personalas`[^manifest]
- **Manifest CSV:** [datasets/gov/svietimas/istaigu_personalas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/svietimas/istaigu_personalas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/svietimas/istaigu_personalas` (`deployed`)[^manifest]
- **Provider:** `svietimas`[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3815/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/svietimas/istaigu_personalas`[^dcat]
- **Portal Title (`@lt`):** Lietuvos savivaldybių švietimo įstaigų personalas[^dcat]
- **Portal Title (`@en`):** The heads of the heads of the institutions of the institutions of the institutions of the institutions of[^dcat]
- **Issued (`dct:issued`):** `2025-03-26`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-03-26` .. `2025-10-06`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikti Lietuvos savivaldybių švietimo įstaigų duomenys. Duomenų rinkinį sudaro: Tabelio numeris, šifruotas asmens kodas, gimimo dešimtmetis, asmens lytis, įdarbinimo ir atleidimo mėnuo, pareigybės, ugdymo įstaiga ir savivaldybė. Duomenų teikėjai: Pakruojo savivaldybė - Pakruojo suaugusiųjų ir jaunimo švietimo centras; Vilniaus rajono savivaldybė; Rokiškio rajono savivaldybė. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The collection contains data from educational institutions of the municipalities of Lithuania. The dataset consists of: Tabel number, encrypted personal number, decade of birth, sex of person, month of recruitment and dismissal, positions, educational institution and municipality. Data providers: The municipalities of Pakruojis Pakruojis for Adult and Youth Education. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Personalas](istaigu_personalas/Personalas.md) | — | `4` | `vda_prime_key` | — | `14` | Lietuvos savivaldybių švietimo įstaigų personalo duomenys |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/svietimas/istaigu_personalas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/svietimas/istaigu_personalas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/svietimas/istaigu_personalas (https://data.gov.lt/datasets/3815/)
