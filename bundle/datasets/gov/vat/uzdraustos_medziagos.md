---
type: Dataset
title: "Informacija apie uždraustas tiekti rinkai dauginamosios medžiagos siuntas"
description: "Informacija apie uždraustas tiekti rinkai dauginamosios medžiagos siuntas"
resource: "https://get.data.gov.lt/datasets/gov/vat/uzdraustos_medziagos"
tags: [gov, vat, deployed, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r25_uzdraustos_medziagos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vat/r25_uzdraustos_medziagos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1881/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/uzdraustos_medziagos"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Informacija apie uždraustas tiekti rinkai dauginamosios medžiagos siuntas

Informacija apie uždraustas tiekti rinkai dauginamosios medžiagos siuntas[^manifest]

- **Namespace:** `datasets/gov/vat/uzdraustos_medziagos`[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r25_uzdraustos_medziagos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r25_uzdraustos_medziagos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/uzdraustos_medziagos` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1881/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė augalininkystės tarnyba prie Žemės ūkio ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vat/uzdraustos_medziagos`[^dcat]
- **Portal Title (`@lt`):** Informacija apie uždraustas tiekti rinkai dauginamosios medžiagos siuntas[^dcat]
- **Portal Title (`@en`):** Information on prohibited consignments of propagating material to be placed on the market[^dcat]
- **Issued (`dct:issued`):** `2023-05-09`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-19`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `IRREG` (`http://publications.europa.eu/resource/authority/frequency/IRREG`)[^dcat]
- **Distribution Date Span:** `2023-04-26` .. `2023-05-09`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pateikiami duomenys apie dokumento pavadinimą, datą, Nr., augalo rūšį / sėklos mišinio pavadinimą, veislę, siuntos Nr., panaikinimo / paskelbimo datą. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Provide details of document title, date, number, plant species / name of seed mixture, variety, lot number, date of cancellation / publication[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Siunta](uzdraustos_medziagos/Siunta.md) | Pateikiami duomenys apie dokumento pavadinimą, datą, Nr., augalo rūšį / sėklos mišinio pavadinimą, veislę, siuntos Nr., panaikinimo / paskelbimo datą | `4` | `eiles_nr` | `open` | `8` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r25_uzdraustos_medziagos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r25_uzdraustos_medziagos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/uzdraustos_medziagos (https://data.gov.lt/datasets/1881/)
