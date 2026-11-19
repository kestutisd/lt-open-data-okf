---
type: Dataset
title: "Vedybų sutarčių registro (VSR) klasifikatoriai"
description: "Vedybų sutarčių registro (VSR) klasifikatoriai (VSR sutarčių statuso klasifikatorius; VSR sutarčių porūšių klasifikatorius)."
resource: "https://get.data.gov.lt/datasets/gov/rc/vsr/klasifikatoriai"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/klasifikatoriai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/vsr/klasifikatoriai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2157/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/vsr/klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Vedybų sutarčių registro (VSR) klasifikatoriai

- **Namespace:** `datasets/gov/rc/vsr/klasifikatoriai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/vsr/klasifikatoriai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/klasifikatoriai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/vsr/klasifikatoriai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2157/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/vsr/klasifikatoriai`[^dcat]
- **Portal Title (`@lt`):** Vedybų sutarčių registro (VSR) klasifikatoriai[^dcat]
- **Portal Title (`@en`):** Classifiers of the Register of Marriage Contracts (VSR).[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-01-05` .. `2025-05-16`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Vedybų sutarčių registro (VSR) klasifikatoriai (VSR sutarčių statuso klasifikatorius; VSR sutarčių porūšių klasifikatorius). Vedybų sutarčių registro (VSR) duomenys.[^dcat]

### Portal Description (`@en`)

Classifiers of the Register of Marriage Contracts (VSR) (classifier of status of VSR contracts; classifier of subtypes of VSR contracts). Data from the Register of Marriage Contracts (VSR). The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Statusas](klasifikatoriai/Statusas.md) | Sutarčių statuso klasifikatorius | `4` | `statusas` | — | `2` | — |
| [Porusis](klasifikatoriai/Porusis.md) | Sutarčių porūšių klasifikatorius | `4` | `porusis` | — | `2` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/vsr/klasifikatoriai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/klasifikatoriai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/vsr/klasifikatoriai (https://data.gov.lt/datasets/2157/)
