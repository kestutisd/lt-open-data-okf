---
type: Dataset
title: "Medicininės intervencijos, atliktos taikant stacionarinį gydymą ar teikiant dienos chirurgijos paslaugas"
description: "Informacija apie stacionarinio gydymo metu ar teikiant dienos chirurgijos paslaugas atliktas medicinines intervencijas."
resource: "https://get.data.gov.lt/datasets/gov/vlk/intervencijos"
tags: [gov, vlk, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/intervencijos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vlk/intervencijos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1509/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/intervencijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Medicininės intervencijos, atliktos taikant stacionarinį gydymą ar teikiant dienos chirurgijos paslaugas

- **Namespace:** `datasets/gov/vlk/intervencijos`[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/intervencijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/intervencijos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/intervencijos` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1509/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė ligonių kasa prie Sveikatos apsaugos ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vlk/intervencijos`[^dcat]
- **Portal Title (`@lt`):** Medicininės intervencijos, atliktos taikant stacionarinį gydymą ar teikiant dienos chirurgijos paslaugas[^dcat]
- **Portal Title (`@en`):** Medical interventions performed in the context of inpatient treatment or the provision of day surgery services[^dcat]
- **Issued (`dct:issued`):** `2023-09-18`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-06-27` .. `2026-09-22`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Informacija apie stacionarinio gydymo metu ar teikiant dienos chirurgijos paslaugas atliktas medicinines intervencijas.[^dcat]

### Portal Description (`@en`)

Information on medical interventions performed in an inpatient or day inpatient service.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Etapas](intervencijos/Etapas.md) | Stacionarinio gydymo etapai | `4` | `ad_id` | — | `5` | Informacija apie stacionarinio gydymo etapus, kurių metu atliktos medicininės intervencijos |
| [Intervencija](intervencijos/Intervencija.md) | Medicininės intervencijos, atliktos taikant stacionarinį gydymą ar teikiant dienos chirurgijos paslaugas | `4` | `ad_id` | — | `4` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/intervencijos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/intervencijos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/intervencijos (https://data.gov.lt/datasets/1509/)
