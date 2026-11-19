---
type: Dataset
title: "DRG sąrašas"
description: "Informacija apie giminingų diagnozių grupes."
resource: "https://get.data.gov.lt/datasets/gov/vlk/drg"
tags: [gov, vlk, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vlk/drg.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1384/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/drg"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# DRG sąrašas

- **Namespace:** `datasets/gov/vlk/drg`[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/drg.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/drg` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1384/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė ligonių kasa prie Sveikatos apsaugos ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vlk/drg`[^dcat]
- **Portal Title (`@lt`):** DRG sąrašas[^dcat]
- **Portal Title (`@en`):** DRG list[^dcat]
- **Issued (`dct:issued`):** `2023-06-30`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-01-17` .. `2026-01-02`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Informacija apie giminingų diagnozių grupes. Kiekvieną ADRG sudaro DRGs, kurios skiriasi pagal sunaudojamus išteklius. DRGs – tai detaliausias klasifikavimo lygmuo. ADRG dažniausiai skirstoma į DRGs pagal gydymo atvejo klinikinio sudėtingumo lygmenis.[^dcat]

### Portal Description (`@en`)

DRG list[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Grupe](drg/Grupe.md) | DRG grupių sąrašas | `4` | — | — | `9` | Informacija apie giminingų diagnozių grupes. |
| [Koeficientai](drg/Koeficientai.md) | DRG koeficientai | `4` | — | — | `8` | Giminingų diagnozių grupių paros/dienos gydymo kainų koeficientai |
| [Trukmes](drg/Trukmes.md) | DRG trukmės | `4` | — | — | `6` | Giminingų diagnozių grupių gydymo trukmės |
| [Versija](drg/Versija.md) | DRG versijos | `4` | — | — | `3` | AR-DRG klasifikacijos versija |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/drg.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/drg (https://data.gov.lt/datasets/1384/)
