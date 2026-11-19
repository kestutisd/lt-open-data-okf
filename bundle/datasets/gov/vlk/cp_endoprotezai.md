---
type: Dataset
title: "Centralizuotai apmokamų endoprotezų panaudojimas"
description: "Informacija apie mokamas Privalomojo sveikatos draudimo fondo biudžeto sumas už centralizuotai perkamus endoprotezus"
resource: "https://get.data.gov.lt/datasets/gov/vlk/cp_endoprotezai"
tags: [gov, vlk, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/cp_endoprotezai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vlk/cp_endoprotezai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1798/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/cp_endoprotezai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Centralizuotai apmokamų endoprotezų panaudojimas

- **Namespace:** `datasets/gov/vlk/cp_endoprotezai`[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/cp_endoprotezai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/cp_endoprotezai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/cp_endoprotezai` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `6` (6 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1798/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė ligonių kasa prie Sveikatos apsaugos ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vlk/cp_endoprotezai`[^dcat]
- **Portal Title (`@lt`):** Centralizuotai apmokamų endoprotezų panaudojimas[^dcat]
- **Portal Title (`@en`):** Amounts paid (EUR) for centrally purchased endoprostheses[^dcat]
- **Issued (`dct:issued`):** `2023-09-18`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-06-27` .. `2024-04-16`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Informacija apie mokamas Privalomojo sveikatos draudimo fondo biudžeto sumas už centralizuotai perkamus endoprotezus[^dcat]

### Portal Description (`@en`)

Information on amounts paid (EUR) for centrally purchased endoprostheses[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Operacija](cp_endoprotezai/Operacija.md) | Centralizuotai perkamų endoprotezų panaudojimas | `4` | — | — | `4` | Informacija apie PSDF biudžeto lėšomis atliktų centralizuotai perkamų sąnarių endoprotezavimo operacijų skaičių |
| [Istaiga](cp_endoprotezai/Istaiga.md) | Įstaigų sąrašas | `4` | — | — | `1` | Gydymo įstaigų, kuriose atliktos endoprotezavimo operacijos, klasifikatorius |
| [Tipas](cp_endoprotezai/Tipas.md) | Operacijų tipų klasifikatorius | `4` | — | — | `3` | Operacijų tipų klasifikatorius |
| [Lokalizacija](cp_endoprotezai/Lokalizacija.md) | Protezų lokalizacijų klasifikatorius | `4` | — | — | `3` | Protezų lokalizacijų klasifikatorius |
| [ProtezoTipas](cp_endoprotezai/ProtezoTipas.md) | Protezų tipų pagal patologiją klasifikatorius | `4` | — | — | `3` | Protezų tipų pagal patologiją klasifikatorius |
| [Prasymas](cp_endoprotezai/Prasymas.md) | Endoprotezavimo prašymų lentelė | `4` | — | — | `2` | Endoprotezavimo prašymų lentelė |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/cp_endoprotezai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/cp_endoprotezai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/cp_endoprotezai (https://data.gov.lt/datasets/1798/)
