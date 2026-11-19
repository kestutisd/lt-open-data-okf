---
type: Dataset
title: "Testamentų registro (TR) klasifikatoriai"
description: "TR klasifikatoriai (TR testamentų rūšių klasifikatorius; TR testamentų žymų klasifikatorius)."
resource: "https://get.data.gov.lt/datasets/gov/rc/tr/tr_klasifikatoriai"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/tr_klasifikatoriai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/tr/tr_klasifikatoriai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2158/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/tr/tr_klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Testamentų registro (TR) klasifikatoriai

- **Namespace:** `datasets/gov/rc/tr/tr_klasifikatoriai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/tr/tr_klasifikatoriai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/tr_klasifikatoriai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/tr/tr_klasifikatoriai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2158/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/tr/tr_klasifikatoriai`[^dcat]
- **Portal Title (`@lt`):** Testamentų registro (TR) klasifikatoriai[^dcat]
- **Portal Title (`@en`):** Register of Wills (TR) Classifiers[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-01-05` .. `2025-04-14`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

TR klasifikatoriai (TR testamentų rūšių klasifikatorius; TR testamentų žymų klasifikatorius). Testamentų registro (TR) duomenys.[^dcat]

### Portal Description (`@en`)

TR classifiers (TR wills types classifier; TR wills mark classifier). Data from the Register of Wills (TR). The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TrRusis](tr_klasifikatoriai/TrRusis.md) | Testamentų registro testamentų rūšių klasifikatorius | `4` | `id` | — | `2` | — |
| [TrZyma](tr_klasifikatoriai/TrZyma.md) | Testamentų registro testamentų žymų klasifikatorius | `4` | `tipas` | — | `2` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/tr/tr_klasifikatoriai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/tr_klasifikatoriai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/tr/tr_klasifikatoriai (https://data.gov.lt/datasets/2158/)
