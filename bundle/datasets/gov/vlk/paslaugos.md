---
type: Dataset
title: "Asmens sveikatos priežiūros paslaugų sąrašas"
description: "Asmens sveikatos priežiūros paslaugų ir sveikatos programose numatytų paslaugų, už kurias mokama iš Privalomojo sveikatos draudimo fondo biudžeto, klasifikatorius, patvirtintas VLK direktoriaus 2005 m. birželio 30 d."
resource: "https://get.data.gov.lt/datasets/gov/vlk/paslaugos"
tags: [gov, vlk, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/paslaugos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vlk/paslaugos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1385/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/paslaugos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Asmens sveikatos priežiūros paslaugų sąrašas

- **Namespace:** `datasets/gov/vlk/paslaugos`[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/paslaugos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/paslaugos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/paslaugos` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1385/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė ligonių kasa prie Sveikatos apsaugos ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vlk/paslaugos`[^dcat]
- **Portal Title (`@lt`):** Asmens sveikatos priežiūros paslaugų sąrašas[^dcat]
- **Portal Title (`@en`):** List of services[^dcat]
- **Issued (`dct:issued`):** `2023-09-11`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2021-11-16` .. `2026-03-28`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Asmens sveikatos priežiūros paslaugų ir sveikatos programose numatytų paslaugų, už kurias mokama iš Privalomojo sveikatos draudimo fondo biudžeto, klasifikatorius, patvirtintas VLK direktoriaus 2005 m. birželio 30 d. įsakymu Nr. 1K-81 „Dėl Asmens sveikatos priežiūros paslaugų ir sveikatos programose numatytų paslaugų, už kurias mokama iš Privalomojo sveikatos draudimo fondo biudžeto, klasifikatoriaus patvirtinimo“[^dcat]

### Portal Description (`@en`)

Classification of Personal Health Care Services, approved by the Director of the State Health Insurance Fund under the Ministry of Health in 2005. June 30 by order no. 1K-81 “On Approval of the Classification of Personal Health Care Services and Services Provided in Health Programs Paid from the Budget of the Compulsory Health Insurance Fund”[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Paslauga](paslaugos/Paslauga.md) | Asmens sveikatos priežiūros paslaugų sąrašas | `4` | `ad_id` | — | `10` | Asmens sveikatos priežiūros paslaugų klasifikatorius, patvirtintas Valstybinės ligonių kasos prie Sveikatos apsaugos ministerijos direktoriaus 2005 m.... |
| [Balas](paslaugos/Balas.md) | Bazinių kainų balais sąrašas | `4` | `ad_id` | — | `8` | Asmens sveikatos priežiūros paslaugų bazinių balų sąrašas |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/paslaugos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/paslaugos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/paslaugos (https://data.gov.lt/datasets/1385/)
