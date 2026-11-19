---
type: Dataset
title: "Miškų sanitarinė būklė"
description: "Informacija apie miškų sanitarinę būklę, užregistruotus abiotinių veiksnių, miško ligų, vabzdžių ir žvėrių padarytus pažeidimus bei atliktas priemones."
resource: "https://get.data.gov.lt/datasets/gov/miskai/sanitarine"
tags: [gov, miskai, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sanitarine.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/miskai/sanitarine.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/827/"
    title: "data.gov.lt DCAT-AP — datasets/gov/miskai/sanitarine"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Miškų sanitarinė būklė

- **Namespace:** `datasets/gov/miskai/sanitarine`[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/sanitarine.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sanitarine.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/sanitarine` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `11` (11 lentelių)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/827/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė miškų tarnyba[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/miskai/sanitarine`[^dcat]
- **Portal Title (`@lt`):** Miškų sanitarinė būklė[^dcat]
- **Portal Title (`@en`):** Overview of the sanitary condition of forests[^dcat]
- **Issued (`dct:issued`):** `2023-06-21`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-06-20` .. `2025-07-29`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Informacija apie miškų sanitarinę būklę, užregistruotus abiotinių veiksnių, miško ligų, vabzdžių ir žvėrių padarytus pažeidimus bei atliktas priemones.[^dcat]

### Portal Description (`@en`)

Overview of the sanitary condition of forests[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PreparatoGrupe](sanitarine/PreparatoGrupe.md) | — | `4` | — | — | `2` | — |
| [KenkejoGrupe](sanitarine/KenkejoGrupe.md) | — | `4` | — | — | `3` | — |
| [PriemonesTipas](sanitarine/PriemonesTipas.md) | — | `4` | — | — | `2` | — |
| [Savininkas](sanitarine/Savininkas.md) | — | `4` | — | — | `1` | — |
| [Tipas](sanitarine/Tipas.md) | — | `4` | — | — | `1` | — |
| [Vieta](sanitarine/Vieta.md) | — | `4` | — | — | `1` | — |
| [Preparatas](sanitarine/Preparatas.md) | — | `4` | — | — | `3` | — |
| [KenkejoPogrupis](sanitarine/KenkejoPogrupis.md) | — | `4` | — | — | `3` | — |
| [Priemone](sanitarine/Priemone.md) | — | `4` | — | — | `4` | — |
| [Kenkejas](sanitarine/Kenkejas.md) | — | `4` | — | — | `3` | — |
| [SanitarineApzvalga](sanitarine/SanitarineApzvalga.md) | — | `4` | — | — | `17` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/sanitarine.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sanitarine.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/miskai/sanitarine (https://data.gov.lt/datasets/827/)
