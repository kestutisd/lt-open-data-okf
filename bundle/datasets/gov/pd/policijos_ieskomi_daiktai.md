---
type: Dataset
title: "Policijos ieškomų daiktų duomenys"
description: "Lentelėje pateikiami Policijos departamento prie LR vidaus reikalų ministerijos Ieškomų ir rastų numeruotų bei individualius požymius turinčių daiktų ir dokumentų registro (INDR) duomenys."
resource: "https://get.data.gov.lt/datasets/gov/pd/policijos_ieskomi_daiktai"
tags: [gov, pd, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/policijos_ieskomi_daiktai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/pd/policijos_ieskomi_daiktai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3805/"
    title: "data.gov.lt DCAT-AP — datasets/gov/pd/policijos_ieskomi_daiktai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Policijos ieškomų daiktų duomenys

- **Namespace:** `datasets/gov/pd/policijos_ieskomi_daiktai`[^manifest]
- **Manifest CSV:** [datasets/gov/pd/policijos_ieskomi_daiktai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/policijos_ieskomi_daiktai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pd/policijos_ieskomi_daiktai` (`deployed`)[^manifest]
- **Provider:** `pd` — Policijos departamentas *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3805/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/pd/policijos_ieskomi_daiktai`[^dcat]
- **Portal Title (`@lt`):** Policijos ieškomų daiktų duomenys[^dcat]
- **Portal Title (`@en`):** Data on items searched by police[^dcat]
- **Issued (`dct:issued`):** `2025-03-24`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-01-05` .. `2026-04-05`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lentelėje pateikiami Policijos departamento prie LR vidaus reikalų ministerijos Ieškomų ir rastų numeruotų bei individualius požymius turinčių daiktų ir dokumentų registro (INDR) duomenys. Informacija lentelėje atnaujinama kas mėnesį. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The table presents the data of the Register of Items and Documents (INDRIUS), which are searched and found by the Police Department under the Ministry of the Interior of the Republic of Lithuania and have individual characteristics. The information in the table is updated monthly. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [DaiktoPaieska](policijos_ieskomi_daiktai/DaiktoPaieska.md) | Policijos ieškomų daiktų duomenys | `4` | `id` | — | `20` | Lentelėje pateikiami Policijos departamento prie LR vidaus reikalų ministerijos Ieškomų ir rastų numeruotų bei individualius požymius turinčių daiktų ir... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/pd/policijos_ieskomi_daiktai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/policijos_ieskomi_daiktai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/pd/policijos_ieskomi_daiktai (https://data.gov.lt/datasets/3805/)
