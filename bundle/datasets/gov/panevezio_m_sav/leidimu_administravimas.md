---
type: Dataset
title: "Panevėžio miesto savivaldybės išduotos licencijos ir jų apmokėjimai"
description: "Informacija apie Panevėžio miesto savivaldybės išduotas licencijas fiziniams ir juridiniams asmenims bei licencijų apmokėjimus"
resource: "https://get.data.gov.lt/datasets/gov/panevezio_m_sav/leidimu_administravimas"
tags: [gov, panevezio_m_sav, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/leidimu_administravimas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/panevezio_m_sav/leidimu_administravimas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4005/"
    title: "data.gov.lt DCAT-AP — datasets/gov/panevezio_m_sav/leidimu_administravimas"
    author: "team:vda"
    last_modified: "2026-11-11T00:00:00Z"
---

# Panevėžio miesto savivaldybės išduotos licencijos ir jų apmokėjimai

Informacija apie Panevėžio miesto savivaldybės išduotas licencijas fiziniams ir juridiniams asmenims bei licencijų apmokėjimus[^manifest]

- **Namespace:** `datasets/gov/panevezio_m_sav/leidimu_administravimas`[^manifest]
- **Manifest CSV:** [datasets/gov/panevezio_m_sav/leidimu_administravimas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/leidimu_administravimas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/panevezio_m_sav/leidimu_administravimas` (`deployed`)[^manifest]
- **Provider:** `panevezio_m_sav` — Panevėžio miesto savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/4005/`[^dcat]
- **Publisher (`dct:publisher`):** Panevėžio miesto savivaldybės administracija[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/panevezio_m_sav/leidimu_administravimas`[^dcat]
- **Portal Title (`@lt`):** Apmokėjimai už Panevėžio miesto savivaldybės išduodamus leidimus ir licencijas[^dcat]
- **Portal Title (`@en`):** Payments for permits and licences issued by Panevėžys City Municipality[^dcat]
- **Issued (`dct:issued`):** `2025-12-19`[^dcat]
- **Last Modified (`dct:modified`):** `2026-11-11`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-07` .. `2026-04-07`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiama informacija apie Panevėžio miesto savivaldybės išduotas licencijas juridiniams asmenims verstis mažmenine prekyba alkoholiniais gėrimais, vienkartines alkoholio prekybos licencijas ir licencijas verstis mažmenine prekyba tabako gaminiais. Rinkinyje taip pat nurodomi fizinių ir juridinių asmenų kasmetinių apmokėjimų į valstybės biudžetą už Panevėžio miesto savivaldybės išduodamus leidimus ir licencijas duomenys. Į rinkinį įtraukta nuo 1997 m. išduodamų alkoholio prekybos licencijų, nuo 2022 m. tabako prekybos licencijų ir nuo 2022 m. gautų apmokėjimų informacija. Duomenų teikėjas – Panevėžio miesto savivaldybė. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Licencija](leidimu_administravimas/Licencija.md) | Panevėžio miesto savivaldybės išduotos alkoholio ir tabako prekybos licencijas | `4` | `licencijos_id` | — | `14` | Informacija apie Panevėžio miesto savivaldybės išduotas alkoholio ir tabako prekybos licencijas |
| [LeidimoImoka](leidimu_administravimas/LeidimoImoka.md) | Įmokos už Panevėžio miesto savivaldybės išduodamus leidimus ir licencijas | `4` | `vda_prime_key` | — | `12` | Informacija apie imokas už Panevėžio miesto savivaldybės išduodamus leidimus ir licencijas |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/panevezio_m_sav/leidimu_administravimas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/leidimu_administravimas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/panevezio_m_sav/leidimu_administravimas (https://data.gov.lt/datasets/4005/)
