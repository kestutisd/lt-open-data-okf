---
type: Dataset
title: "Alytaus šilumos tinklų sutarčių su įmonėmis duomenys"
description: "Lentelėje pateikti Alytaus šilumos tinklų sutarčių su įmonėmis duomenys iš Įmonių sutarčių registro."
resource: "https://get.data.gov.lt/datasets/gov/ast/imoniu_sutartys"
tags: [gov, ast, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/imoniu_sutartys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ast/imoniu_sutartys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2770/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ast/imoniu_sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Alytaus šilumos tinklų sutarčių su įmonėmis duomenys

- **Namespace:** `datasets/gov/ast/imoniu_sutartys`[^manifest]
- **Manifest CSV:** [datasets/gov/ast/imoniu_sutartys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/imoniu_sutartys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ast/imoniu_sutartys` (`deployed`)[^manifest]
- **Provider:** `ast` — Alytaus šilumos tinklai *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2770/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ast/imoniu_sutartys`[^dcat]
- **Portal Title (`@lt`):** Alytaus šilumos tinklų sutarčių su įmonėmis duomenys[^dcat]
- **Portal Title (`@en`):** Data on Alytus heat network contracts with companies[^dcat]
- **Issued (`dct:issued`):** `2024-08-30`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2024-08-30` .. `2024-08-30`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lentelėje pateikti Alytaus šilumos tinklų sutarčių su įmonėmis duomenys iš Įmonių sutarčių registro. Duomenų turinys: įmonių JAR kodai, adresai, pavadinimai, tarp įmonių ir Alytaus šilumos tinklų sudarytų sutarčių pradžios datos. Lentelėje vienas juridinis asmuo (viena įmonė) gali turėti kelis objektus (pvz.: pastatus) dėl kurių sudaroma sutartis, todėl ta pati įmonė gali turėti kelis skirtingus kliento kodus. Kaupiamų duomenų aprėptis laike – nuo 1993 m., atnaujinant kas metus. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The table provides data on contracts of Alytus heat networks with enterprises from the Register of Enterprise Contracts. Content of the data: Jaris codes, addresses, names of enterprises, starting dates of contracts concluded between undertakings and Alytus heat networks. In the table, one legal entity (one company) may have several objects (such as buildings) that are the subject of a contract, so the same company may have several different customer codes. The coverage of the data collected in time has been in place since 1993, updated on a yearly basis. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [AstSutartis](imoniu_sutartys/AstSutartis.md) | Alytaus šilumos tinklų sutarčių su įmonėmis duomenys | `4` | `iraso_id` | — | `6` | Lentelėje pateikti Alytaus šilumos tinklų sutarčių su įmonėmis duomenys iš Įmonių sutarčių registro. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ast/imoniu_sutartys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/imoniu_sutartys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ast/imoniu_sutartys (https://data.gov.lt/datasets/2770/)
