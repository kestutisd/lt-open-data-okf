---
type: Dataset
title: "Fitosanitarinio registro viešieji duomenys"
description: "Pateikiama informacija apie ūkio subjektus, įregistruotus Fitosanitariniame registre (ūkio subjekto pavadinimas; veiklos vykdymo adresas; specializacija)."
resource: "https://get.data.gov.lt/datasets/gov/vat/fitosanitarinis_registras"
tags: [gov, vat, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r2_fitosanitarinis_registras.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vat/r2_fitosanitarinis_registras.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1858/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/fitosanitarinis_registras"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Fitosanitarinio registro viešieji duomenys

- **Namespace:** `datasets/gov/vat/fitosanitarinis_registras`[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r2_fitosanitarinis_registras.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r2_fitosanitarinis_registras.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/fitosanitarinis_registras` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1858/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė augalininkystės tarnyba prie Žemės ūkio ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vat/fitosanitarinis_registras`[^dcat]
- **Portal Title (`@lt`):** Fitosanitarinio registro viešieji duomenys[^dcat]
- **Portal Title (`@en`):** Public data from the phytosanitary register[^dcat]
- **Issued (`dct:issued`):** `2023-05-09`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2023-05-09` .. `2026-10-28`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pateikiama informacija apie ūkio subjektus, įregistruotus Fitosanitariniame registre (ūkio subjekto pavadinimas; veiklos vykdymo adresas; specializacija). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Information on economic entities registered in the Phytosanitary Register shall be provided (identification code of the economic entity; name; address of the activity; type of activity and production)[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Subjektas](fitosanitarinis_registras/Subjektas.md) | Pateikiama informacija apie ūkio subjektus, įregistruotus Fitosanitariniame registe (ūkio subjekto atpažinties kodas; pavadinimas; veiklos vykdymo adresas; veiklos ir produkcijos rūšis) | `4` | `id` | `open` | `8` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r2_fitosanitarinis_registras.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r2_fitosanitarinis_registras.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/fitosanitarinis_registras (https://data.gov.lt/datasets/1858/)
