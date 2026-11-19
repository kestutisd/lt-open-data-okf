---
type: Dataset
title: "Leidimai platinti augalų apsaugos produktus"
description: "Pateikiama informacija apie išduotus, patikslintus ar panaikintus leidimus platinti augalų apsaugos produktus per tam tikrą laikotarpį (išdavimo data; leidimo numeris; būsena; ūkio subjekto pavadinimas, adresas)."
resource: "https://get.data.gov.lt/datasets/gov/vat/prekyba_aap"
tags: [gov, vat, deployed, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r10_prekyba_aap.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vat/r10_prekyba_aap.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1866/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/prekyba_aap"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Leidimai platinti augalų apsaugos produktus

- **Namespace:** `datasets/gov/vat/prekyba_aap`[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r10_prekyba_aap.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r10_prekyba_aap.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/prekyba_aap` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1866/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė augalininkystės tarnyba prie Žemės ūkio ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vat/prekyba_aap`[^dcat]
- **Portal Title (`@lt`):** Leidimai platinti augalų apsaugos produktus[^dcat]
- **Portal Title (`@en`):** Authorizations for distribution of plant protection products[^dcat]
- **Issued (`dct:issued`):** `2023-05-24`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-19`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `IRREG` (`http://publications.europa.eu/resource/authority/frequency/IRREG`)[^dcat]
- **Distribution Date Span:** `2023-05-24` .. `2026-10-13`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pateikiama informacija apie išduotus, patikslintus ar panaikintus leidimus platinti augalų apsaugos produktus per tam tikrą laikotarpį (išdavimo data; leidimo numeris; būsena; ūkio subjekto pavadinimas, adresas). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Information on authorizations granted, revised or revoked for the distribution of plant protection products during a certain period (date of issue; authorization number; status; name, address of the operator)[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Leidimas](prekyba_aap/Leidimas.md) | Pateikiama informacija apie išduotus, patikslintus ar panaikintus leidimus platinti augalų apsaugos produktus per tam tikrą laikotarpį (išdavimo data; leidimo numeris; būsena; ūkio subjekto pavadinimas, adresas) | `4` | `id` | `open` | `6` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r10_prekyba_aap.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r10_prekyba_aap.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/prekyba_aap (https://data.gov.lt/datasets/1866/)
