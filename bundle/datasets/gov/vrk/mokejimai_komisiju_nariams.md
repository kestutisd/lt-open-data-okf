---
type: Dataset
title: "Rinkiminių komisijų nariams skirtas darbo užmokestis"
description: "Vyriausiosios rinkimų komisijos informacinė sistema kaupia informaciją apie rinkiminių komisijų nariams skirtą darbo užmokestį."
resource: "https://get.data.gov.lt/datasets/gov/vrk/mokejimai_komisiju_nariams"
tags: [gov, vrk, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/mokejimai_komisiju_nariams.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vrk/mokejimai_komisiju_nariams.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2807/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vrk/mokejimai_komisiju_nariams"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Rinkiminių komisijų nariams skirtas darbo užmokestis

- **Namespace:** `datasets/gov/vrk/mokejimai_komisiju_nariams`[^manifest]
- **Manifest CSV:** [datasets/gov/vrk/mokejimai_komisiju_nariams.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/mokejimai_komisiju_nariams.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vrk/mokejimai_komisiju_nariams` (`deployed`)[^manifest]
- **Provider:** `vrk` — Vyriausioji rinkimų komisija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2807/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vrk/mokejimai_komisiju_nariams`[^dcat]
- **Portal Title (`@lt`):** Rinkimų komisijų nariams skirtas darbo užmokestis[^dcat]
- **Portal Title (`@en`):** Salaries for members of election commissions[^dcat]
- **Issued (`dct:issued`):** `2024-11-28`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-09-20` .. `2025-04-10`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Vyriausiosios rinkimų komisijos informacinė sistema kaupia informaciją apie rinkiminių komisijų nariams skirtą darbo užmokestį. Duomenų rinkinyje „Rinkiminių komisijų nariams skirtas darbo užmokestis“ pateikiama mokėjimo, mokėjimo eilės, vykdomų rinkimų identifikacijos numeris, Rinkimų pavadinimas, mokėjimo ir mokėjimo eilės data, mokėjimo būsena, pseudonimizuotas komisijos nario identifikacijos numeris, apygardos identifikacijos numeris ir pavadinimas, komisijos nario pareigos ir mokėjimo suma (Eurais). Vienas įrašas atitinka vieno mokėjimo eilutę vienam asmeniui. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The information system of the Chief Electoral Commission collects information about the salary of the members of the electoral commissions. The data set "Salaries for members of election commissions" contains the identification number of the payment, order of payment, ongoing election, name of the election, date of payment and order of payment, payment status, pseudonymized identification number of the member of the commission, district identification number and name, responsibilities of the member of the commission and payment amount (in Euros). One entry corresponds to one payment line per person.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Uzmokestis](mokejimai_komisiju_nariams/Uzmokestis.md) | Rinkiminių komisijų nariams skirtas darbo užmokestis | `4` | `vda_prime_key` | — | `13` | Vyriausiosios rinkimų komisijos Sąmatų, darbo užmokesčio ir buhalterinės apskaitos posistemėje nuo 2011-12-19 kaupiami ir iki šiol atnaujinami rinkimų... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/mokejimai_komisiju_nariams.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/mokejimai_komisiju_nariams.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vrk/mokejimai_komisiju_nariams (https://data.gov.lt/datasets/2807/)
