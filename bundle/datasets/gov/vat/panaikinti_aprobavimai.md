---
type: Dataset
title: "Informacija apie panaikintus aprobavimo aktus, kurie skelbiami negaliojančiais"
description: "Pateikiami duomenys apie tiekėją, dokumento pavadinimą, dokumento Nr. ir datą, augalo rūšį, veislę, dokumento panaikinimo datą, naujai išduoto dokumento datą ir Nr."
resource: "https://get.data.gov.lt/datasets/gov/vat/panaikinti_aprobavimai"
tags: [gov, vat, deployed, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/panaikinti_aprobavimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vat/panaikinti_aprobavimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1886/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/panaikinti_aprobavimai"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Informacija apie panaikintus aprobavimo aktus, kurie skelbiami negaliojančiais

Pateikiami duomenys apie tiekėją, dokumento pavadinimą, dokumento Nr. ir datą, augalo rūšį, veislę, dokumento panaikinimo datą, naujai išduoto dokumento datą ir Nr.[^manifest]

- **Namespace:** `datasets/gov/vat/panaikinti_aprobavimai`[^manifest]
- **Manifest CSV:** [datasets/gov/vat/panaikinti_aprobavimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/panaikinti_aprobavimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/panaikinti_aprobavimai` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1886/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė augalininkystės tarnyba prie Žemės ūkio ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vat/panaikinti_aprobavimai`[^dcat]
- **Portal Title (`@lt`):** Informacija apie panaikintus aprobavimo aktus, kurie skelbiami negaliojančiais[^dcat]
- **Portal Title (`@en`):** Information on revoked approval acts which are declared invalid[^dcat]
- **Issued (`dct:issued`):** `2023-05-09`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-19`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `IRREG` (`http://publications.europa.eu/resource/authority/frequency/IRREG`)[^dcat]
- **Distribution Date Span:** `2023-05-09` .. `2026-10-14`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pateikiami duomenys apie tiekėją, dokumento pavadinimą, dokumento Nr. ir datą, augalo rūšį, veislę, dokumento panaikinimo datą, naujai išduoto dokumento datą ir Nr. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Details about the supplier, document name, document no. and date, plant species, variety, date of cancellation of the document, date of the newly issued document and no.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Aktas](panaikinti_aprobavimai/Aktas.md) | — | `4` | `eiles_nr` | `open` | `9` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/panaikinti_aprobavimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/panaikinti_aprobavimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/panaikinti_aprobavimai (https://data.gov.lt/datasets/1886/)
