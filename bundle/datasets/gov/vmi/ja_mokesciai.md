---
type: Dataset
title: "Juridinių asmenų sumokėti mokesčiai duomenų rinkinys"
description: "Juridinių asmenų sumokėti mokesčiai"
resource: "https://get.data.gov.lt/datasets/gov/vmi/ja_mokesciai"
tags: [gov, vmi, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/ja_sumoketi_mokesciai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmi/ja_sumoketi_mokesciai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/673/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/ja_mokesciai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Juridinių asmenų sumokėti mokesčiai duomenų rinkinys

Juridinių asmenų sumokėti mokesčiai[^manifest]

- **Namespace:** `datasets/gov/vmi/ja_mokesciai`[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/ja_sumoketi_mokesciai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/ja_sumoketi_mokesciai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/ja_mokesciai` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/673/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmi/ja_mokesciai`[^dcat]
- **Portal Title (`@lt`):** Juridinių asmenų sumokėti mokesčiai[^dcat]
- **Portal Title (`@en`):** Amount of taxes paid by the legal entity[^dcat]
- **Issued (`dct:issued`):** `2023-10-11`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-06` .. `2026-10-17`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys apie juridinių asmenų sumokėtus praėjusiais metais ir einamaisiais metais į Valstybinės mokesčių inspekcijos biudžeto pajamų surenkamąsias sąskaitas deklaruojamus mokesčius ir rinkliavas, kurie nurodyti Lietuvos Respublikos Mokesčių administravimo įstatymo 13 straipsnyje. Einamaisiais metais sumokėtos mokesčių sumos skaičiuojamos kaupimo būdu nuo metų pradžios iki ataskaitinio laikotarpio pabaigos. Duomenys atnaujinami vieną kartą per mėnesį. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on taxes and fees declared by legal entities in the previous year and in the current year to the State Tax Inspectorate's budget income collection accounts, which are specified in Article 13 of the Law on Tax Administration of the Republic of Lithuania. Taxes paid in the current year are calculated cumulatively from the beginning of the year to the end of the reporting period. The data is updated once a month.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Moketojas](ja_mokesciai/Moketojas.md) | Mokesčių mokėtojas | `4` | `id` | `open` | `12` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/ja_sumoketi_mokesciai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/ja_sumoketi_mokesciai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/ja_mokesciai (https://data.gov.lt/datasets/673/)
