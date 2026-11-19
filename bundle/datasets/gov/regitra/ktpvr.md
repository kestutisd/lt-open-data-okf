---
type: Dataset
title: "Išduotų galiojančių vairuotojų pažymėjimų duomenys"
description: "AB \"Regitra\" išduotų ir galiojančių vairuotojų pažymėjimų duomenys"
resource: "https://get.data.gov.lt/datasets/gov/regitra/ktpvr"
tags: [gov, regitra, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/ktpvr.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/regitra/ktpvr.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2934/"
    title: "data.gov.lt DCAT-AP — datasets/gov/regitra/ktpvr"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Išduotų galiojančių vairuotojų pažymėjimų duomenys

AB "Regitra" išduotų ir galiojančių vairuotojų pažymėjimų duomenys[^manifest]

- **Namespace:** `datasets/gov/regitra/ktpvr`[^manifest]
- **Manifest CSV:** [datasets/gov/regitra/ktpvr.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/ktpvr.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/regitra/ktpvr` (`deployed`)[^manifest]
- **Provider:** `regitra` — AB „Regitra“ *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2934/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/regitra/ktpvr`[^dcat]
- **Portal Title (`@lt`):** Išduotų galiojančių vairuotojų pažymėjimų duomenys[^dcat]
- **Portal Title (`@en`):** Data on valid driving licences issued[^dcat]
- **Issued (`dct:issued`):** `2025-02-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-02-21` .. `2026-09-30`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiama AB „Regitra“ išduotuose ir šiuo metu galiojančiuose vairuotojo pažymėjimuose esanti informacija – asmens identifikatorius, pažymėjimo galiojimo pradžia, asmens gimimo metai, lytis, gimimo šalis, turimos vairuotojo kategorijos. Duomenys atnaujinami kiekvieno mėnesio 1 d. Duomenų teikėjas – AB „Regitra“. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on valid certificates issued by the Register[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Pazymejimas](ktpvr/Pazymejimas.md) | Išduotų galiojančių vairuotojų pažymėjimų duomenys | `4` | `vairuotojo_pazymejimo_id` | — | `14` | AB "Regitra" išduotų ir galiojančių vairuotojų pažymėjimų duomenys |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/regitra/ktpvr.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/ktpvr.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/regitra/ktpvr (https://data.gov.lt/datasets/2934/)
