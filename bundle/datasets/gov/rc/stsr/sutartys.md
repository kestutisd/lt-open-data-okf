---
type: Dataset
title: "STSR duomenys apie sutartis"
description: "STSR duomenys apie sutartis (sutarčių rūšys ir kiti duomenys: data, sutarties šalių požymiai, daikto rūšis)."
resource: "https://get.data.gov.lt/datasets/gov/rc/stsr/sutartys"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/sutartys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/stsr/sutartys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2134/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/stsr/sutartys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# STSR duomenys apie sutartis

- **Namespace:** `datasets/gov/rc/stsr/sutartys`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/stsr/sutartys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/sutartys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/stsr/sutartys` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2134/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/stsr/sutartys`[^dcat]
- **Portal Title (`@lt`):** STSR duomenys apie sutartis[^dcat]
- **Portal Title (`@en`):** STSR data on contracts[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-01-04` .. `2025-06-16`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

STSR duomenys apie sutartis (sutarčių rūšys ir kiti duomenys: data, sutarties šalių požymiai, daikto rūšis). Sutarčių ir teisių suvaržymo registro duomenys.[^dcat]

### Portal Description (`@en`)

STSR data on contracts (types of contracts and other data: date, characteristics of the parties to the contract, type of item). Data from the Register of Contracts and Encumbrances.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Sutartis](sutartys/Sutartis.md) | Duomenys apie sutartis (sutarčių rūšys ir kiti duomenys: data, sutarties šalių požymiai, daikto rūšis) | `4` | `nr` | — | `13` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/stsr/sutartys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/sutartys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/stsr/sutartys (https://data.gov.lt/datasets/2134/)
