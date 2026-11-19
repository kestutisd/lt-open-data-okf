---
type: Dataset
title: "VšĮ Klaipėdos būstai"
description: "Šiame rinkinyje pateikiama informacija apie Klaipėdos miesto savivaldybės nuomojamus savivaldybės ir socialinius būstus: būstų charakteristikos, nuomos sąlygos ir nuomininkai."
resource: "https://get.data.gov.lt/datasets/gov/kbu"
tags: [gov, kbu, deployed, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kbu/bustai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/kbu/bustai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3831/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kbu"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# VšĮ Klaipėdos būstai

- **Namespace:** `datasets/gov/kbu`[^manifest]
- **Manifest CSV:** [datasets/gov/kbu/bustai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kbu/bustai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kbu` (`deployed`)[^manifest]
- **Provider:** `kbu` — VšĮ Klaipėdos būstai *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3831/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/kbu`[^dcat]
- **Portal Title (`@lt`):** Klaipėdos miesto savivaldybės nuomojamų būstų registras[^dcat]
- **Portal Title (`@en`):** Klaipeda Municipality Rent Houses Register[^dcat]
- **Issued (`dct:issued`):** `2025-04-28`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL_2` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL_2`)[^dcat]
- **Distribution Date Span:** `2025-04-28` .. `2026-03-10`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Šiame rinkinyje pateikiama informacija apie Klaipėdos miesto savivaldybės nuomojamus savivaldybės ir socialinius būstus: būstų charakteristikos, nuomos sąlygos ir nuomininkai. Kiekviena lentelės eilutė atitinka vieną su Klaipėdos miesto savivaldybe sudarytą nuomos sutartį. Duomenų rinkinys yra nuolat atnaujinamas, apimantis laikotarpį nuo duomenų kaupimo pradžios iki dabar. Visi duomenys teikiami laikantis teisės aktuose numatytų duomenų atvėrimo reikalavimų, todėl tam tikros reikšmės, susijusios su asmens identifikavimu, yra užšifruotos. Duomenų teikėjas – VšĮ „Klaipėdos butai“. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

This package provides information about municipal and social housing rented by Klaipeda Municipality: housing characteristics, rental conditions and tenants. Each row of the table corresponds to one lease agreement concluded with Klaipeda Municipality. The dataset is kept up-to-date, covering the period from the start of the data collection to the present. All data shall be provided in accordance with the legal requirements for the opening of data and therefore certain values relating to the identification of the person shall be encrypted. Data provider – “Klaipėda apartments”. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Bustas](kbu/Bustas.md) | Klaipėdos miesto savivaldybės nuomojamų būstų registras | `4` | `vda_prime_key` | — | `19` | Rinkinys apie savivaldybės ir socialinio būsto nuomą Klaipėdos miesto savivaldybėje, kuriame pateikiama informacija apie būstų charakteristikas, nuomos... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kbu/bustai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kbu/bustai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kbu (https://data.gov.lt/datasets/3831/)
