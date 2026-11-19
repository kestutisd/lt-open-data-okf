---
type: Dataset
title: "Kiti Įgaliojimų registro (ĮR) klasifikatoriai"
description: "Kiti Įgaliojimų registro klasifikatoriai (4 vnt.: Įgaliojimų registrui teikiamų pranešimų klasifikatorius; Įgaliojimų registro įgaliojimo duomenų pakeitimo pagrindų klasifikatorius; Įgaliojimų registro įgaliojimo pasibaigimo pagrindų klasifikatorius; Įgaliojimų registro..."
resource: "https://get.data.gov.lt/datasets/gov/rc/ir/kiti_klasifikatoriai"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/kiti_klasifikatoriai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ir/kiti_klasifikatoriai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2168/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ir/kiti_klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Kiti Įgaliojimų registro (ĮR) klasifikatoriai

- **Namespace:** `datasets/gov/rc/ir/kiti_klasifikatoriai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ir/kiti_klasifikatoriai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/kiti_klasifikatoriai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ir/kiti_klasifikatoriai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2168/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ir/kiti_klasifikatoriai`[^dcat]
- **Portal Title (`@lt`):** Kiti Įgaliojimų registro (ĮR) klasifikatoriai[^dcat]
- **Portal Title (`@en`):** Other classifications of the Register of Authorizations (RA).[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-01-09` .. `2025-09-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Kiti Įgaliojimų registro klasifikatoriai (4 vnt.: Įgaliojimų registrui teikiamų pranešimų klasifikatorius; Įgaliojimų registro įgaliojimo duomenų pakeitimo pagrindų klasifikatorius; Įgaliojimų registro įgaliojimo pasibaigimo pagrindų klasifikatorius; Įgaliojimų registro atsisakymo įregistruoti įgaliojimą priežasčių klasifikatorius). Įgaliojimų registro (ĮR) duomenys.[^dcat]

### Portal Description (`@en`)

Other Classifiers of the Powers of Attorney Register (4 units: Classifier of messages submitted to the Powers of Attorneys Register; Classifier of the grounds for changing authorization data in the Powers of Attorneys Register; Classifier of the grounds for the expiration of the Powers of Attorneys Register; Classifier of reasons for refusing to register a power of attorney in the Powers of Attorneys Register). Data of the Register of Authorizations (RA). The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [AtsisakymoPriezastis](kiti_klasifikatoriai/AtsisakymoPriezastis.md) | Įgaliojimų registro atsisakymo įregistruoti įgaliojimą priežasčių klasifikatorius | `4` | `kodas` | — | `2` | — |
| [PakeitimoPagrindas](kiti_klasifikatoriai/PakeitimoPagrindas.md) | Įgaliojimų registro įgaliojimo duomenų pakeitimo pagrindų klasifikatorius | `4` | `kodas` | — | `2` | — |
| [PasibaigimoPagrinas](kiti_klasifikatoriai/PasibaigimoPagrinas.md) | Įgaliojimų registro įgaliojimo pasibaigimo pagrindų klasifikatorius | `4` | `kodas` | — | `2` | — |
| [PranesimoTipas](kiti_klasifikatoriai/PranesimoTipas.md) | Įgaliojimų registrui teikiamų pranešimų klasifikatorius | `4` | `kodas` | — | `2` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ir/kiti_klasifikatoriai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/kiti_klasifikatoriai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ir/kiti_klasifikatoriai (https://data.gov.lt/datasets/2168/)
