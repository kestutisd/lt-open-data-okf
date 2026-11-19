---
type: Dataset
title: "Informacija apie panaikintus sertifikatus, kurie skelbiami negaliojančiais"
description: "Informacija apie panaikintus sertifikatus, kurie skelbiami negaliojančiais"
resource: "https://get.data.gov.lt/datasets/gov/vat/panaikinimai"
tags: [gov, vat, deployed, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r24_panaikinti_sertifikatai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vat/r24_panaikinti_sertifikatai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1880/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/panaikinimai"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Informacija apie panaikintus sertifikatus, kurie skelbiami negaliojančiais

Informacija apie panaikintus sertifikatus, kurie skelbiami negaliojančiais[^manifest]

- **Namespace:** `datasets/gov/vat/panaikinimai`[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r24_panaikinti_sertifikatai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r24_panaikinti_sertifikatai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/panaikinimai` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1880/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė augalininkystės tarnyba prie Žemės ūkio ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vat/panaikinimai`[^dcat]
- **Portal Title (`@lt`):** Informacija apie panaikintus sertifikatus, kurie skelbiami negaliojančiais[^dcat]
- **Portal Title (`@en`):** Information about revoked certificates that are declared invalid[^dcat]
- **Issued (`dct:issued`):** `2023-05-09`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-19`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `IRREG` (`http://publications.europa.eu/resource/authority/frequency/IRREG`)[^dcat]
- **Distribution Date Span:** `2023-04-26` .. `2023-05-09`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pateikiami duomenys apie tiekėją, dokumento pavadinimą, dokumento Nr. ir datą, augalo rūšį, veislę, dokumento panaikinimo datą, naujai išduoto dokumento datą ir Nr. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Details about the supplier, document name, document no. and date, plant species, variety, date of cancellation of the document, date of the newly issued document and no.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Sertifikatas](panaikinimai/Sertifikatas.md) | Pateikiami duomenys apie tiekėją, dokumento pavadinimą, dokumento Nr. ir datą, augalo rūšį, veislę, dokumento panaikinimo datą, naujai išduoto dokumento datą ir Nr. | `4` | `eiles_nr` | `open` | `8` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r24_panaikinti_sertifikatai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r24_panaikinti_sertifikatai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/panaikinimai (https://data.gov.lt/datasets/1880/)
