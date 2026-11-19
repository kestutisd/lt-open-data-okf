---
type: Dataset
title: "Stacionarinio aktyviojo gydymo atvejų skaičius pagal DRG"
description: "Informacija apie PSDF biudžeto lėšomis apmokamą stacionarinio aktyviojo gydymo atvejų skaičių pagal DRG."
resource: "https://get.data.gov.lt/datasets/gov/vlk/drg_atvejai"
tags: [gov, vlk, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg_atvejai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vlk/drg_atvejai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2259/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/drg_atvejai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Stacionarinio aktyviojo gydymo atvejų skaičius pagal DRG

- **Namespace:** `datasets/gov/vlk/drg_atvejai`[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/drg_atvejai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg_atvejai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/drg_atvejai` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2259/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė ligonių kasa prie Sveikatos apsaugos ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vlk/drg_atvejai`[^dcat]
- **Portal Title (`@lt`):** Stacionarinio aktyviojo gydymo atvejų skaičius pagal DRG[^dcat]
- **Portal Title (`@en`):** Number of inpatient active treatment cases by DRG[^dcat]
- **Issued (`dct:issued`):** `2023-09-18`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-03-15` .. `2026-04-29`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Informacija apie PSDF biudžeto lėšomis apmokamą stacionarinio aktyviojo gydymo atvejų skaičių pagal DRG. Agreguota mėnesinė informacija. Ankstesnių metų duomenys nesikeičiantys.[^dcat]

### Portal Description (`@en`)

Information on the number of inpatient active treatment cases paid for by the PSDF budget according to DRG. Aggregated monthly information. Data from previous years are unchanged.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Atvejis](drg_atvejai/Atvejis.md) | Stacionarinio aktyviojo gydymo atvejų skaičius pagal DRG | `4` | `ad_id` | — | `8` | Informacija apie stacionarinio aktyviojo gydymo atvejų skaičių pagal DRG |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/drg_atvejai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg_atvejai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/drg_atvejai (https://data.gov.lt/datasets/2259/)
