---
type: Dataset
title: "LIBIS egzempliorių sąrašas"
description: "Duomenų rinkinyje pateikiamas bibliotekų turimų egzempliorių sąrašas, kurį sudaro: bibliografinio įrašo ID (referuoja į bibliografinių įrašų rinkinį), bibliotekų savininkų ir saugotojų ID (referuoja į bibliotekų rinkinį), inventorizacijos ir nurašymo datos, spaudos ženklai..."
resource: "https://get.data.gov.lt/datasets/gov/lnb/egzemplioriai"
tags: [gov, lnb, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/egzemplioriai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lnb/egzemplioriai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2796/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lnb/egzemplioriai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# LIBIS egzempliorių sąrašas

- **Namespace:** `datasets/gov/lnb/egzemplioriai`[^manifest]
- **Manifest CSV:** [datasets/gov/lnb/egzemplioriai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/egzemplioriai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lnb/egzemplioriai` (`deployed`)[^manifest]
- **Provider:** `lnb` — Lietuvos nacionalinė Martyno Mažvydo biblioteka *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2796/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lnb/egzemplioriai`[^dcat]
- **Portal Title (`@lt`):** Lietuvos integralios bibliotekų informacinės sistemos egzempliorių sąrašas[^dcat]
- **Portal Title (`@en`):** List of copies of Lithuania's integrated library information system[^dcat]
- **Issued (`dct:issued`):** `2024-09-17`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-09-17` .. `2025-10-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiamas bibliotekų turimų egzempliorių sąrašas, kurį sudaro: bibliografinio įrašo ID (referuoja į bibliografinių įrašų rinkinį), bibliotekų savininkų ir saugotojų ID (referuoja į bibliotekų rinkinį), inventorizacijos ir nurašymo datos, spaudos ženklai, būkšninis kodas, inventorinis numeris, pradinės ir dabartinės kainos. Dėl Valstybės skaitmeninių sprendimų agentūros (VSSA) resursų ribotumo rinkinys apribotas inventoriaus tipais – „Inventorinis“ ir „Periodinis inventorinis“. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

List of copies held by libraries. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Sarasas](egzemplioriai/Sarasas.md) | LIBIS egzempliorių sąrašas | `4` | `id` | — | `26` | Bibliotekų turimų egzempliorių sąrašas |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lnb/egzemplioriai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/egzemplioriai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lnb/egzemplioriai (https://data.gov.lt/datasets/2796/)
