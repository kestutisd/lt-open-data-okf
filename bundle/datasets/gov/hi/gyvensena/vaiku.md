---
type: Dataset
title: "Vaikų gyvensenos duomenys"
description: "Pateikiami nuo 2016 m. visose Lietuvos savivaldybėse atliekamo mokyklinio amžiaus 5, 7 ir 9 (pirmų gimnazijos) klasių mokinių gyvensenos tyrimo rezultatai."
resource: "https://get.data.gov.lt/datasets/gov/hi/gyvensena/vaiku"
tags: [gov, hi, deployed, cadence-quadrennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/gyvensena/vaiku.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/hi/gyvensena/vaiku.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1225/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/gyvensena/vaiku"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Vaikų gyvensenos duomenys

- **Namespace:** `datasets/gov/hi/gyvensena/vaiku`[^manifest]
- **Manifest CSV:** [datasets/gov/hi/gyvensena/vaiku.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/gyvensena/vaiku.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/gyvensena/vaiku` (`deployed`)[^manifest]
- **Provider:** `hi` — Suaugusiųjų ir vaikų gyvensenos duomenys *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1225/`[^dcat]
- **Publisher (`dct:publisher`):** Higienos institutas[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/hi/gyvensena/vaiku`[^dcat]
- **Portal Title (`@lt`):** Vaikų gyvensenos duomenys[^dcat]
- **Portal Title (`@en`):** Children health behaviour[^dcat]
- **Issued (`dct:issued`):** `2023-06-12`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUADRENNIAL` (`http://publications.europa.eu/resource/authority/frequency/QUADRENNIAL`)[^dcat]
- **Distribution Date Span:** `2023-06-08` .. `2023-06-12`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pateikiami nuo 2016 m. visose Lietuvos savivaldybėse atliekamo mokyklinio amžiaus 5, 7 ir 9 (pirmų gimnazijos) klasių mokinių gyvensenos tyrimo rezultatai. Tyrimo koordinatorius – Higienos institutas. Tyrimas vykdomas vadovaujantis metodinėmis rekomendacijomis „Gyvensenos tyrimų organizavimas ir vykdymas savivaldybėse“. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

It presents data of school-aged children of 5th, 7th, 9th (first gymnasium) grades health behaviour research in all Lithuanian municipalities since 2016. The research coordinator – Institute of Hygiene. The research is conducted following the methodological recommendations “Organization and Implementation of Health Behaviour Research in Municipalities”.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Gyvensena2016](vaiku/Gyvensena2016.md) | Vaikų gyvensenos 2016 metų duomenys | `4` | `resp_kodas` | — | `42` | — |
| [Gyvensena2020](vaiku/Gyvensena2020.md) | Vaikų gyvensenos 2020 metų duomenys | `4` | `resp_kodas` | — | `43` | — |
| [Gyvensena2024](vaiku/Gyvensena2024.md) | Vaikų gyvensenos 2024 metų duomenys | `4` | `resp_kodas` | — | `52` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/gyvensena/vaiku.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/gyvensena/vaiku.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/gyvensena/vaiku (https://data.gov.lt/datasets/1225/)
