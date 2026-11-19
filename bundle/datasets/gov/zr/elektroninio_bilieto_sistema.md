---
type: Dataset
title: "VšĮ Žaliojo Regiono elektroninių bilietų pardavimai"
description: "Lentelėje pateikti elektroninio bilieto sistemos duomenys apie elektroninių bilietų pardavimus nuo 2023 metų."
resource: "https://get.data.gov.lt/datasets/gov/zr/elektroninio_bilieto_sistema"
tags: [gov, zr, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zr/elektroninio_bilieto_sistema.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/zr/elektroninio_bilieto_sistema.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4060/"
    title: "data.gov.lt DCAT-AP — datasets/gov/zr/elektroninio_bilieto_sistema"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# VšĮ Žaliojo Regiono elektroninių bilietų pardavimai

- **Namespace:** `datasets/gov/zr/elektroninio_bilieto_sistema`[^manifest]
- **Manifest CSV:** [datasets/gov/zr/elektroninio_bilieto_sistema.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zr/elektroninio_bilieto_sistema.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/zr/elektroninio_bilieto_sistema` (`deployed`)[^manifest]
- **Provider:** `zr` — VšĮ Žaliojo Regiono sistemų duomenys *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/4060/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/zr/elektroninio_bilieto_sistema`[^dcat]
- **Portal Title (`@lt`):** Žaliojo regiono elektroninių bilietų pardavimų duomenys[^dcat]
- **Portal Title (`@en`):** Sales data for Green Region Electronic Tickets[^dcat]
- **Issued (`dct:issued`):** `2026-01-09`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-12-22` .. `2026-01-22`[^dcat]

### Portal Description (`@lt`)

Lentelėje pateikti elektroninio bilieto sistemos duomenys apie elektroninių bilietų pardavimus nuo 2023 metų. Teikiami VšĮ Žaliojo regiono duomenys apie Jurbarko, Šilalės, Tauragės rajonus ir Pagėgius. Informacija atnaujinama kas mėnesį. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The table provides electronic ticket system data on e-ticket sales from 2023, provided by the Green Region of the SE about the districts of Jurbarkas, Šilalė, Tauragė and Pagegiai. The information shall be updated monthly. Contact the atverimas@stat.gov.lt for technical questions or possible errors. Please contact atviriduomenys@vssa.lt by e-mail for technical problems with the portal.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Kortele](elektroninio_bilieto_sistema/Kortele.md) | VšĮ Žaliojo regiono elektroninių bilietų kortelių duomenys | — | `korteles_id` | — | `12` | Lentelėje pateikti elektroninio bilieto sistemos duomenys apie elektroninių bilietų korteles nuo 2023 metų, teikiami VšĮ Žaliojo regiono apie Jurbarko... |
| [BilietuPardavimas](elektroninio_bilieto_sistema/BilietuPardavimas.md) | VšĮ Žaliojo regiono elektroninių bilietų pardavimų duomenys | — | `bilieto_id` | — | `12` | Lentelėje pateikti elektroninio bilieto sistemos duomenys apie elektroninių bilietų pardavimus nuo 2023 metų, teikiami VšĮ Žaliojo regiono apie Jurbarko... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/zr/elektroninio_bilieto_sistema.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zr/elektroninio_bilieto_sistema.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/zr/elektroninio_bilieto_sistema (https://data.gov.lt/datasets/4060/)
