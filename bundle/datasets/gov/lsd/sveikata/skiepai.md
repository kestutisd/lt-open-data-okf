---
type: Dataset
title: "Asmenys, paskiepyti įvairių ligų skiepais"
description: "Duomenys apie skiepijimus nuo šaltojo sezono ir kitų ligų (gripo, ŽPV infekcijos, pneumokokinės infekcijos, erkinio encefalito, hepatito B) iš ESPBI IS E063 formos."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/skiepai"
tags: [gov, lsd, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/skiepai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/skiepai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2777/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/skiepai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Asmenys, paskiepyti įvairių ligų skiepais

- **Namespace:** `datasets/gov/lsd/sveikata/skiepai`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/skiepai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/skiepai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/skiepai` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2777/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/skiepai`[^dcat]
- **Portal Title (`@lt`):** Asmenys, paskiepyti įvairių ligų skiepais[^dcat]
- **Portal Title (`@en`):** Vaccination data for infectious diseases other than COVID-19[^dcat]
- **Issued (`dct:issued`):** `2024-09-06`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-09-06` .. `2026-10-28`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys apie skiepijimus nuo šaltojo sezono ir kitų ligų (gripo, ŽPV infekcijos, pneumokokinės infekcijos, erkinio encefalito, hepatito B) iš ESPBI IS E063 formos. Pašalinti įrašai, kuriuose trūksta skiepijimo datos, paciento amžiaus arba lyties. (COVID-19 skiepijimai jau yra atverti čia: https://data.gov.lt/datasets/1670/) Šių duomenų pagrindu parengta vieša VDA skiepų švieslentė (https://osp.stat.gov.lt/skiepu-svieslente). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on vaccinations related to cold season and other diseases (flu, HPV infection, pneumococcal infection, tick-borne encephalitis, hepatitis B) from the E063 form of ESPBI IS („e-health“). Records with missing vaccination date, patient age or sex have been removed. (COVID-19 vaccinations are already open here: https://data.gov.lt/datasets/1670/) The present data were used to prepare the SDA‘s public vaccination dashboard (https://osp.stat.gov.lt/skiepu-svieslente).[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SkiepytiGripo](skiepai/SkiepytiGripo.md) | Asmenys, paskiepyti šaltojo sezono ligų (gripo) skiepais, pagal ligą (gripas), įstaigą lytį ir amžiaus grupę | — | `vda_prime_key` | — | `11` | Kol kas pateikti tik gripo duomenys |
| [SkiepytiPadieniui](skiepai/SkiepytiPadieniui.md) | Pasiskiepiję asmenys pagal dieną ir ligą | — | `vda_prime_key` | — | `4` | — |
| [SkiepytiVakcina](skiepai/SkiepytiVakcina.md) | Pasiskiepiję asmenys pagal laikotarpį, ligą, vakciną ir įstaigą | — | `vda_prime_key` | — | `10` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/skiepai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/skiepai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/skiepai (https://data.gov.lt/datasets/2777/)
