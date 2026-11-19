---
type: Dataset
title: "Mokamos sumos už ortopedijos technines ir medicinos priemones"
description: "Informacija apie mokamas Privalomojo sveikatos draudimo fondo biudžeto sumas už ortopedinės technikos priemones"
resource: "https://get.data.gov.lt/datasets/gov/vlk/otp_sumos"
tags: [gov, vlk, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/otp_sumos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vlk/otp_sumos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1800/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/otp_sumos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Mokamos sumos už ortopedijos technines ir medicinos priemones

- **Namespace:** `datasets/gov/vlk/otp_sumos`[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/otp_sumos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/otp_sumos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/otp_sumos` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `5` (5 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1800/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė ligonių kasa prie Sveikatos apsaugos ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vlk/otp_sumos`[^dcat]
- **Portal Title (`@lt`):** Mokamos sumos už ortopedijos technines ir medicinos priemones[^dcat]
- **Portal Title (`@en`):** Amounts payable (EUR) for orthopedic appliances[^dcat]
- **Issued (`dct:issued`):** `2023-09-18`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-06-30` .. `2023-09-05`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Informacija apie mokamas Privalomojo sveikatos draudimo fondo biudžeto sumas už ortopedinės technikos priemones[^dcat]

### Portal Description (`@en`)

Information on amounts paid (EUR) for orthopedic appliances[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Uzsakymas](otp_sumos/Uzsakymas.md) | Mokamos sumos už ortopedijos technines ir medicinos priemones | `4` | `ad_id` | — | `5` | Informacija apie PSDF biudžeto išlaidas ortopedijos techninėms priemonėms |
| [Tipas](otp_sumos/Tipas.md) | Ortopedijos techninių ir medicinos priemonių tipai | `4` | `ad_id` | — | `2` | Informacija apie ortopedijos techninių ir medicinos priemonių tipus |
| [Grupe](otp_sumos/Grupe.md) | Ortopedijos techninių ir medicinos priemonių tipai | `4` | `ad_id` | — | `4` | Informacija apie ortopedijos techninių ir medicinos priemonių tipus |
| [Klase](otp_sumos/Klase.md) | Ortopedijos techninių ir medicinos priemonių klasė | `4` | `ad_id` | — | `3` | Informacija apie ortopedijos techninių ir medicinos priemonių klases |
| [Istaiga](otp_sumos/Istaiga.md) | Įstaigų sąrašas | `4` | `istg_id` | — | `1` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/otp_sumos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/otp_sumos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/otp_sumos (https://data.gov.lt/datasets/1800/)
