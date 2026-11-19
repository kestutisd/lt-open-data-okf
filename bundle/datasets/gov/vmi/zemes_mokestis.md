---
type: Dataset
title: "Žemės mokesčio deklaracijų duomenys"
description: "Žemės mokesčio apskaičiavimo deklaracijų duomenys (pagal savivaldybes) apie apskaičiuotas mokesčio sumas, pritaikytas lengvatas, apmokestinamus plotus."
resource: "https://get.data.gov.lt/datasets/gov/vmi/zemes_mokestis"
tags: [gov, vmi, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/zemes_mokestis.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmi/zemes_mokestis.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1125/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/zemes_mokestis"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Žemės mokesčio deklaracijų duomenys

- **Namespace:** `datasets/gov/vmi/zemes_mokestis`[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/zemes_mokestis.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/zemes_mokestis.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/zemes_mokestis` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1125/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė mokesčių inspekcija prie Finansų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmi/zemes_mokestis`[^dcat]
- **Portal Title (`@lt`):** Žemės mokestis[^dcat]
- **Portal Title (`@en`):** Data on land plots subject to land tax[^dcat]
- **Issued (`dct:issued`):** `2022-10-07`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2022-09-05` .. `2026-10-13`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Žemės mokesčio apskaičiavimo deklaracijų duomenys (pagal savivaldybes) apie apskaičiuotas mokesčio sumas, pritaikytas lengvatas, apmokestinamus plotus. Mokestinis laikotarpis - kalendoriniai metai. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Areas, values and tax amounts of FA and JA taxable land plots by groups of assets, purpose, methods of use and types for 2014, 2015[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Deklaracijos](zemes_mokestis/Deklaracijos.md) | Žemės mokečio deklaracijų duomenys | `3` | — | — | `11` | — |
| [Priedai](zemes_mokestis/Priedai.md) | Žemės mokesčio deklaracijų priedų duomenys | `3` | — | — | `15` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/zemes_mokestis.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/zemes_mokestis.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/zemes_mokestis (https://data.gov.lt/datasets/1125/)
