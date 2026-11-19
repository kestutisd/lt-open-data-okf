---
type: Dataset
title: "Visuomenės sveikatos priežiūros specialistų duomenys"
description: "Specialistai, atliekantys visuomenės sveikatos priežiūros funkcijas Lietuvos nacionalinės sveikatos sistemos visuomenės sveikatos priežiūros įstaigose (amžiaus grupė, išsilavinimas, lytis, įstaigų grupė)."
resource: "https://get.data.gov.lt/datasets/gov/hi/specialistai"
tags: [gov, hi, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/hi/specialistai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1106/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/specialistai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Visuomenės sveikatos priežiūros specialistų duomenys

Specialistai, atliekantys visuomenės sveikatos priežiūros funkcijas Lietuvos nacionalinės sveikatos sistemos visuomenės sveikatos priežiūros įstaigose (amžiaus grupė, išsilavinimas, lytis, įstaigų grupė).[^manifest]

- **Namespace:** `datasets/gov/hi/specialistai`[^manifest]
- **Manifest CSV:** [datasets/gov/hi/specialistai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/specialistai` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1106/`[^dcat]
- **Publisher (`dct:publisher`):** Higienos institutas[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/hi/specialistai`[^dcat]
- **Portal Title (`@lt`):** Visuomenės sveikatos priežiūros specialistų duomenys[^dcat]
- **Portal Title (`@en`):** Data of public health specialists[^dcat]
- **Issued (`dct:issued`):** `2023-06-20`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-06-12` .. `2026-05-09`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Specialistai, atliekantys visuomenės sveikatos priežiūros funkcijas Lietuvos nacionalinės sveikatos sistemos visuomenės sveikatos priežiūros įstaigose (amžiaus grupė, išsilavinimas, lytis, įstaigų grupė). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Specialists, who perform public health care functions in public health institutions of the Lithuanian national health system (age groups, education, gender, group of institutions).[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Issilavinimas](specialistai/Issilavinimas.md) | Visuomenės sveikatos specialistų duomenys pagal išsilavinimą | `3` | — | — | `7` | — |
| [Etatas](specialistai/Etatas.md) | Visuomenės sveikatos specialistų duomenys pagal darbo etatus | `4` | `m_id` | — | `6` | — |
| [Juridinis](specialistai/Juridinis.md) | Juridiniai asmenys | `3` | — | — | `8` | Kuriuose dirba visuomenės sveikatos specialistai |
| [Programa](specialistai/Programa.md) | Studijų programos | `3` | — | — | `3` | Kurias yra baigę visuomenės sveikatos specialistai |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/specialistai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/specialistai (https://data.gov.lt/datasets/1106/)
