---
type: Dataset
title: "Juridinių asmenų dalyvių duomenys pagal juridinio asmens dalyvių šalis ir teisinę formą"
description: "Juridinių asmenų dalyvių informacinės sistemos (JADIS) duomenys apie juridinio asmens dalyvių šalis ir juridinio asmens teisinę formą"
resource: "https://get.data.gov.lt/datasets/gov/rc/jadis/salys_teisines_formos"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/salys_teisines_formos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/jadis/salys_teisines_formos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1733/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jadis/salys_teisines_formos"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Juridinių asmenų dalyvių duomenys pagal juridinio asmens dalyvių šalis ir teisinę formą

Juridinių asmenų dalyvių informacinės sistemos (JADIS) duomenys apie juridinio asmens dalyvių šalis ir juridinio asmens teisinę formą[^manifest]

- **Namespace:** `datasets/gov/rc/jadis/salys_teisines_formos`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jadis/salys_teisines_formos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/salys_teisines_formos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jadis/salys_teisines_formos` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1733/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/jadis/salys_teisines_formos`[^dcat]
- **Portal Title (`@lt`):** Juridinių asmenų dalyvių duomenys pagal juridinio asmens dalyvių šalis ir teisinę formą[^dcat]
- **Portal Title (`@en`):** Data on participants in legal entities by country of legal entity participants and legal form[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2022-01-20` .. `2025-09-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Juridinių asmenų dalyvių informacinės sistemos (JADIS) duomenys apie juridinio asmens dalyvių šalis ir juridinio asmens teisinę formą.[^dcat]

### Portal Description (`@en`)

Data on the Participant Information System for Legal Entities (JADIS) on the participants of legal entities and the legal form of the legal entity. Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SalisTeisineForma](salys_teisines_formos/SalisTeisineForma.md) | Juridinių asmenų dalyvių duomenys pagal juridinio asmens dalyvių šalis ir teisinę formą | `4` | `laikotarpis, salies_kodas, forma` | — | `6` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `locn` | `http://www.w3.org/ns/locn#` |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jadis/salys_teisines_formos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/salys_teisines_formos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jadis/salys_teisines_formos (https://data.gov.lt/datasets/1733/)
