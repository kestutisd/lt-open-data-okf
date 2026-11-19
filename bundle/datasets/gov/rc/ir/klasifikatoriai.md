---
type: Dataset
title: "Įgaliojimų registro (ĮR) įgaliojimų rūšių, terminų ir paslaugų klasifikatoriai"
description: "Įgaliojimų registro įgaliojimų rūšių ir terminų klasifikatoriai (3 vnt.: Įgaliojimų registro informacinių technologijų priemonėmis sudarytų įgaliojimų rūšių klasifikatorius; Įgaliojimų registro viešųjų ir administracinių paslaugų klasifikatorius; Įgaliojimų registro..."
resource: "https://get.data.gov.lt/datasets/gov/rc/ir/klasifikatoriai"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/klasifikatoriai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ir/klasifikatoriai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2167/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ir/klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Įgaliojimų registro (ĮR) įgaliojimų rūšių, terminų ir paslaugų klasifikatoriai

- **Namespace:** `datasets/gov/rc/ir/klasifikatoriai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ir/klasifikatoriai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/klasifikatoriai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ir/klasifikatoriai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2167/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ir/klasifikatoriai`[^dcat]
- **Portal Title (`@lt`):** Įgaliojimų registro (ĮR) įgaliojimų rūšių, terminų ir paslaugų klasifikatoriai[^dcat]
- **Portal Title (`@en`):** Classifiers of authorization types, terms and services of the Register of Authorizations (RA).[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-01-09` .. `2023-06-29`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Įgaliojimų registro įgaliojimų rūšių ir terminų klasifikatoriai (3 vnt.: Įgaliojimų registro informacinių technologijų priemonėmis sudarytų įgaliojimų rūšių klasifikatorius; Įgaliojimų registro viešųjų ir administracinių paslaugų klasifikatorius; Įgaliojimų registro įgaliojimų terminų klasifikatorius).[^dcat]

### Portal Description (`@en`)

Classifiers of types and terms of authorizations of the Register of Powers (3 units: Classifier of types of authorizations created by information technology means of the Register of Powers; Classifier of public and administrative services of the Register of Powers; Classifier of terms of powers of the Register of Powers). The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Terminas](klasifikatoriai/Terminas.md) | Įgaliojimų registro terminų klasifikatorius | `4` | `kodas` | — | `2` | — |
| [IgaliojimoTipas](klasifikatoriai/IgaliojimoTipas.md) | Įgaliojimų registro informacinių technologijų priemonėmis sudarytų įgaliojimų tipų klasifikatorius | `4` | `kodas` | — | `2` | — |
| [Paslauga](klasifikatoriai/Paslauga.md) | Įgaliojimų registro viešųjų ir administracinių paslaugų klasifikatorius | `4` | `id` | — | `5` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ir/klasifikatoriai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/klasifikatoriai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ir/klasifikatoriai (https://data.gov.lt/datasets/2167/)
