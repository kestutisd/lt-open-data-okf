---
type: Dataset
title: "Kauno miesto savivaldybės teikiami duomenys"
description: "Kauno miesto daugiabučiai namai (3 ir daugiau butų), kuriems reikalingi bendro naudojimo objektų valdytojai"
resource: "https://get.data.gov.lt/datasets/gov/kaunas/daugiabuciai"
tags: [gov, kaunas, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kaunas/daugiabuciai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/kaunas/daugiabuciai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1361/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kaunas/daugiabuciai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Kauno miesto savivaldybės teikiami duomenys

Kauno miesto daugiabučiai namai (3 ir daugiau butų), kuriems reikalingi bendro naudojimo objektų valdytojai[^manifest]

- **Namespace:** `datasets/gov/kaunas/daugiabuciai`[^manifest]
- **Manifest CSV:** [datasets/gov/kaunas/daugiabuciai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kaunas/daugiabuciai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kaunas/daugiabuciai` (`deployed`)[^manifest]
- **Provider:** `kaunas` — Kauno miesto savivaldybė *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1361/`[^dcat]
- **Publisher (`dct:publisher`):** Kauno miesto savivaldybės administracija[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/kaunas/daugiabuciai`[^dcat]
- **Portal Title (`@lt`):** Daugiabučiai[^dcat]
- **Portal Title (`@en`):** Daugiabučiai[^dcat]
- **Issued (`dct:issued`):** `2022-04-13`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2021-05-17` .. `2026-10-29`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@en`)

Kaunas city apartment buildings (3 and more apartments), which require managers of common use objects[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [InformacijaApiePastatus](daugiabuciai/InformacijaApiePastatus.md) | Daugiabučiai, valdytojai | — | `id` | — | `31` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kaunas/daugiabuciai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kaunas/daugiabuciai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kaunas/daugiabuciai (https://data.gov.lt/datasets/1361/)
