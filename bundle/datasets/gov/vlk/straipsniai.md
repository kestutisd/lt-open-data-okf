---
type: Dataset
title: "PSDF biudžeto išlaidų straipsnių sąrašas"
description: "Privalomojo sveikatos draudimo fondo biudžeto straipsnių pagal VLK direktoriaus 2005 m. birželio 30 d."
resource: "https://get.data.gov.lt/datasets/gov/vlk/straipsniai"
tags: [gov, vlk, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/straipsniai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vlk/straipsniai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2279/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/straipsniai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PSDF biudžeto išlaidų straipsnių sąrašas

- **Namespace:** `datasets/gov/vlk/straipsniai`[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/straipsniai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/straipsniai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/straipsniai` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2279/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė ligonių kasa prie Sveikatos apsaugos ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vlk/straipsniai`[^dcat]
- **Portal Title (`@lt`):** PSDF biudžeto išlaidų straipsnių sąrašas[^dcat]
- **Portal Title (`@en`):** Articles of the budget for services paid for with PSDF budget funds[^dcat]
- **Issued (`dct:issued`):** `2023-06-30`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-06-27` .. `2026-01-02`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Privalomojo sveikatos draudimo fondo biudžeto straipsnių pagal VLK direktoriaus 2005 m. birželio 30 d. įsakymą Nr. 1K-81 "Dėl asmens sveikatos priežiūros paslaugų ir sveikatos programose numatytų paslaugų, už kurias mokama iš Privalomojo sveikatos draudimo fondo biudžeto, klasifikatoriaus patvirtinimo" klasifikatorius[^dcat]

### Portal Description (`@en`)

Compulsory health insurance fund budget articles in accordance with the 2005 decision of the Director of the Health Insurance Fund. June 30 order no. 1K-81 &quot;On the approval of the classification of personal health care services and services provided for in health programs, which are paid from the budget of the Compulsory Health Insurance Fund&quot;[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Straipsnis](straipsniai/Straipsnis.md) | PSDF biudžeto straipsnių sąrašas | `4` | `ad_id` | — | `5` | PSDF biudžeto straipsnių, pagal kuriuos apmokamos asmens sveikatos priežiūros paslaugos, sąrašas |
| [Paslauga](straipsniai/Paslauga.md) | Asmens sveikatos priežiūros paslaugų, priskirtų PSDF biudžeto straipsniams, sąrašas | `4` | `ad_id` | — | `5` | Informacija apie asmens sveikatos priežiūros paslaugų, priskirtų PSDF biudžeto straipsniams, sąrašą |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/straipsniai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/straipsniai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/straipsniai (https://data.gov.lt/datasets/2279/)
