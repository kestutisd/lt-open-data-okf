---
type: Dataset
title: "Juridinių asmenų dalyvių sąrašų duomenys"
description: "Juridinių asmenų dalyvių informacinsė sistemos (JADIS) duomenys apie juridinių asmenų dalyvių sąrašus."
resource: "https://get.data.gov.lt/datasets/gov/rc/jadis/dalyviu_sarasas"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/dalyviu_sarasas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/jadis/dalyviu_sarasas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1710/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jadis/dalyviu_sarasas"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Juridinių asmenų dalyvių sąrašų duomenys

Juridinių asmenų dalyvių informacinsė sistemos (JADIS) duomenys apie juridinių asmenų dalyvių sąrašus.[^manifest]

- **Namespace:** `datasets/gov/rc/jadis/dalyviu_sarasas`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jadis/dalyviu_sarasas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/dalyviu_sarasas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jadis/dalyviu_sarasas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1710/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/jadis/dalyviu_sarasas`[^dcat]
- **Portal Title (`@lt`):** Juridinių asmenų dalyvių sąrašų duomenys[^dcat]
- **Portal Title (`@en`):** Data on lists of participants in legal entities[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2022-01-20` .. `2025-09-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Juridinių asmenų dalyvių informacinės sistemos (JADIS) duomenys apie registro tvarkytojui pateikiamus juridinių asmenų dalyvių sąrašus, jų turinį.[^dcat]

### Portal Description (`@en`)

Data on the lists of participants in legal entities (JADIS). Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [DalyviuSarasas](dalyviu_sarasas/DalyviuSarasas.md) | Juridinių asmenų dalyvių sąrašų duomenys | `4` | `juridinis_asmuo` | — | `6` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jadis/dalyviu_sarasas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/dalyviu_sarasas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jadis/dalyviu_sarasas (https://data.gov.lt/datasets/1710/)
