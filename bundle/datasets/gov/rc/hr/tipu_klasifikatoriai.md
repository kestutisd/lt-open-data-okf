---
type: Dataset
title: "Likviduoto Lietuvos Respublikos HR archyviniai klasifikatoriai"
description: "Likviduoto Lietuvos Respublikos HR archyviniai klasifikatoriai (HR turto tipų archyvinis klasifikatorius; HR sandorių tipų archyvinis klasifikatorius)."
resource: "https://get.data.gov.lt/datasets/gov/rc/hr/tipu_klasifikatoriai"
tags: [gov, rc, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/tipu_klasifikatoriai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/hr/tipu_klasifikatoriai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2131/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/hr/tipu_klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Likviduoto Lietuvos Respublikos HR archyviniai klasifikatoriai

- **Namespace:** `datasets/gov/rc/hr/tipu_klasifikatoriai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/hr/tipu_klasifikatoriai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/tipu_klasifikatoriai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/hr/tipu_klasifikatoriai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2131/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/hr/tipu_klasifikatoriai`[^dcat]
- **Portal Title (`@lt`):** Likviduoto Lietuvos Respublikos HR archyviniai klasifikatoriai[^dcat]
- **Portal Title (`@en`):** Archival classifications of the liquidated HR of the Republic of Lithuania[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2023-01-04` .. `2023-07-12`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Likviduoto Lietuvos Respublikos HR archyviniai klasifikatoriai (HR turto tipų archyvinis klasifikatorius; HR sandorių tipų archyvinis klasifikatorius).[^dcat]

### Portal Description (`@en`)

Archival classifiers of the liquidated HR of the Republic of Lithuania (archival classifier of HR asset types; archival classifier of HR transaction types). The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TurtoTipas](tipu_klasifikatoriai/TurtoTipas.md) | Hr turto tipų archyvinis klasifikatorius | `4` | `kodas` | — | `2` | — |
| [SandorioTipas](tipu_klasifikatoriai/SandorioTipas.md) | Hr sandorių tipų archyvinis klasifikatorius | `4` | `kodas` | — | `2` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/hr/tipu_klasifikatoriai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/tipu_klasifikatoriai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/hr/tipu_klasifikatoriai (https://data.gov.lt/datasets/2131/)
