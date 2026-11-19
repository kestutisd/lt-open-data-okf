---
type: Dataset
title: "VLKK terminų banko terminų duomenys"
description: "Valstybinės lietuvių kalbos komisijos Lietuvos Respublikos terminų banke kaupiami įvairių sričių terminai lietuvių bei kitomis Europos kalbomis, kaip vokiečių, prancūzų, lenkų."
resource: "https://get.data.gov.lt/datasets/gov/vlkk/lrtb"
tags: [gov, vlkk, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlkk/lrtb.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vlkk/lrtb.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2636/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlkk/lrtb"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# VLKK terminų banko terminų duomenys

- **Namespace:** `datasets/gov/vlkk/lrtb`[^manifest]
- **Manifest CSV:** [datasets/gov/vlkk/lrtb.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlkk/lrtb.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlkk/lrtb` (`deployed`)[^manifest]
- **Provider:** `vlkk` — Valstybinė lietuvių kalbos komisija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2636/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vlkk/lrtb`[^dcat]
- **Portal Title (`@lt`):** VLKK terminų banko terminų duomenys[^dcat]
- **Portal Title (`@en`):** VLKK Term Bank Term Data[^dcat]
- **Issued (`dct:issued`):** `2024-04-29`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-07` .. `2026-06-30`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Valstybinės lietuvių kalbos komisijos Lietuvos Respublikos terminų banke kaupiami įvairių sričių terminai lietuvių bei kitomis Europos kalbomis, kaip vokiečių, prancūzų, lenkų. Duomenys kaupiami nuo 2005 m. ir atnaujinami kas mėnesį. Apimami duomenys yra patys terminai, jų sritys, kalba, statusas: teiktinas, neteiktinas arba aprobuotas, įvedimo data bei organizacija, pateikusi patį terminą. Tarp tokių organizacijų patenka VLKK, Užsienio reikalų ministerija, Policijos departamentas. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The time limits of the Terms Bank of the Republic of Lithuania shall be submitted.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TerminuBankas](lrtb/TerminuBankas.md) | VLKK terminų banko terminų duomenys | `4` | `termino_id` | — | `7` | Valstybinės lietuvių kalbos komisijos Lietuvos Respublikos terminų banke kaupiami įvairių sričių terminai lietuvių bei kitomis Europos kalbomis, kaip... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlkk/lrtb.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlkk/lrtb.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlkk/lrtb (https://data.gov.lt/datasets/2636/)
