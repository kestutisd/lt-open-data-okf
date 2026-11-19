---
type: Dataset
title: "STSR duomenys apie įkeitimo ir hipotekos sandorių skolininkus"
description: "STSR duomenys apie įkeitimo ir hipotekos sandorių skolininkus (skolininko tipą, amžių, formą sandorių rūšis, sudarymo vietas, vertes, terminus)."
resource: "https://get.data.gov.lt/datasets/gov/rc/stsr/skolininkai"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/skolininkai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/stsr/skolininkai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2136/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/stsr/skolininkai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# STSR duomenys apie įkeitimo ir hipotekos sandorių skolininkus

- **Namespace:** `datasets/gov/rc/stsr/skolininkai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/stsr/skolininkai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/skolininkai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/stsr/skolininkai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2136/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/stsr/skolininkai`[^dcat]
- **Portal Title (`@lt`):** STSR duomenys apie įkeitimo ir hipotekos sandorių skolininkus[^dcat]
- **Portal Title (`@en`):** STSR data on debtors of pledge and mortgage transactions[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-01-04` .. `2025-07-09`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

STSR duomenys apie įkeitimo ir hipotekos sandorių skolininkus (skolininko tipą, amžių, formą sandorių rūšis, sudarymo vietas, vertes, terminus). Sutarčių ir teisių suvaržymo registro duomenys.[^dcat]

### Portal Description (`@en`)

STSR data on borrowers of pledge and mortgage transactions (type of borrower, age, form, types of transactions, places of conclusion, values, terms). Data from the Register of Contracts and Encumbrances. The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Skolininkas](skolininkai/Skolininkas.md) | Duomenys apie įkeitimo ir hipotekos sandorių skolininkus (skolininko tipą, amžių, formą sandorių rūšis, sudarymo vietas, vertes, terminus) | `2` | `skolininko_id` | — | `23` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/stsr/skolininkai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/skolininkai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/stsr/skolininkai (https://data.gov.lt/datasets/2136/)
