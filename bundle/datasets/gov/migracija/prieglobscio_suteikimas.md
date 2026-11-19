---
type: Dataset
title: "Duomenys apie prieglobsčio suteikimą"
description: "Duomenys apie prieglobsčio prašytojus, prieglobstį gavusius užsieniečius, pateiktus prašymus suteikti prieglobstį ir priimtus sprendimus, duomenys apie užsieniečius, dėl kurių buvo išsiųsti ar gauti paklausimai (ir/ar atsakymai) dėl jų perėmimo savo žinion ar atsiėmimo pagal..."
resource: "https://get.data.gov.lt/datasets/gov/migracija/prieglobscio_suteikimas"
tags: [gov, migracija, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/prieglobscio_suteikimas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/migracija/prieglobscio_suteikimas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1941/"
    title: "data.gov.lt DCAT-AP — datasets/gov/migracija/prieglobscio_suteikimas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Duomenys apie prieglobsčio suteikimą

Duomenys apie prieglobsčio prašytojus, prieglobstį gavusius užsieniečius, pateiktus prašymus suteikti prieglobstį ir priimtus sprendimus, duomenys apie užsieniečius, dėl kurių buvo išsiųsti ar gauti paklausimai (ir/ar atsakymai) dėl jų perėmimo savo žinion ar atsiėmimo pagal Dublino III reglamentą, duomenys apie užsieniečių perdavimą pagal Dublino III reglamentą.[^manifest]

- **Namespace:** `datasets/gov/migracija/prieglobscio_suteikimas`[^manifest]
- **Manifest CSV:** [datasets/gov/migracija/prieglobscio_suteikimas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/prieglobscio_suteikimas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/migracija/prieglobscio_suteikimas` (`deployed`)[^manifest]
- **Provider:** `migracija` — Migracijos departamentas *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1941/`[^dcat]
- **Publisher (`dct:publisher`):** Migracijos departamentas prie Lietuvos Respublikos vidaus reikalų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/migracija/prieglobscio_suteikimas`[^dcat]
- **Portal Title (`@lt`):** Duomenys apie prieglobsčio suteikimą[^dcat]
- **Portal Title (`@en`):** Data on granting of asylum[^dcat]
- **Issued (`dct:issued`):** `2023-04-03`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-03` .. `2026-06-03`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys apie pateiktus prašymus suteikti prieglobstį ir priimtus sprendimus. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on asylum applications submitted and decisions taken.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Prasytojas](prieglobscio_suteikimas/Prasytojas.md) | Duomenys apie prieglobsčio prašytojus | `3` | `id` | `open` | `5` | — |
| [Gavejas](prieglobscio_suteikimas/Gavejas.md) | Duomenys apie prieglobsčio gavėjus | `3` | `id` | `open` | `6` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/migracija/prieglobscio_suteikimas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/prieglobscio_suteikimas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/migracija/prieglobscio_suteikimas (https://data.gov.lt/datasets/1941/)
