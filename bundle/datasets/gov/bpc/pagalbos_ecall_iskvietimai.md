---
type: Dataset
title: "Transporto priemonių pagalbos iškvietimo skambučių „eCall“ duomenys"
description: "Lentelėje pateikti Bendrosios pagalbos centro (BPC) registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, duomenys, kai transporto priemonėje įrengta sistema suaktyvinama automatiškai (transporto priemonėje įrengtais jutikliais) arba rankiniu būdu ir per..."
resource: "https://get.data.gov.lt/datasets/gov/bpc/pagalbos_ecall_iskvietimai"
tags: [gov, bpc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_ecall_iskvietimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/bpc/pagalbos_ecall_iskvietimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2761/"
    title: "data.gov.lt DCAT-AP — datasets/gov/bpc/pagalbos_ecall_iskvietimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Transporto priemonių pagalbos iškvietimo skambučių „eCall“ duomenys

- **Namespace:** `datasets/gov/bpc/pagalbos_ecall_iskvietimai`[^manifest]
- **Manifest CSV:** [datasets/gov/bpc/pagalbos_ecall_iskvietimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_ecall_iskvietimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/bpc/pagalbos_ecall_iskvietimai` (`deployed`)[^manifest]
- **Provider:** `bpc` — Bendrasis pagalbos centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2761/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/bpc/pagalbos_ecall_iskvietimai`[^dcat]
- **Portal Title (`@lt`):** Transporto priemonių pagalbos iškvietimo skambučių „eCall“ duomenys[^dcat]
- **Portal Title (`@en`):** Vehicle emergency call eCall data[^dcat]
- **Issued (`dct:issued`):** `2024-08-23`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-08-22` .. `2026-03-05`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lentelėje pateikti Bendrosios pagalbos centro (BPC) registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, duomenys, kai transporto priemonėje įrengta sistema suaktyvinama automatiškai (transporto priemonėje įrengtais jutikliais) arba rankiniu būdu ir per mobiliojo ryšio tinklą užmezgamas ryšys tarp į eismo ar kitokį įvykį patekusios transporto priemonės ir Bendrojo pagalbos centro. Svarbu atkreipti dėmesį, kad lentelėje pateikiamos ne tikslios, o "grindų" (angl. floor) funkcija į 1 km dydžio kvadratinę gardelę suapvalintos koordinatės: pavyzdžiui, vietoj koordinatės "582964, 6061791" (LKS-94), pateikiama "582000, 6061000" (LKS-94) koordinatė, kuri atspindi kairįjį 1 km kvadratinės gardelės kampą. Duomenys kaupiami nuo 2003 m. ir yra atnaujinami kas mėnesį. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

: The table contains data on accidents registered by the General Emergency Centre (PSAP) and reported by 112 when the system installed on the vehicle is activated automatically (on-board sensors) or manually and a connection is established via the mobile network between the vehicle involved in the traffic or other incident and the General Emergency Centre. Data have been collected since 2003 and are updated monthly. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [EcallSkambutis](pagalbos_ecall_iskvietimai/EcallSkambutis.md) | Transporto priemonių pagalbos iškvietimo skambučių „eCall“ duomenys | `4` | `iraso_id` | — | `17` | Lentelėje pateikti Bendrosios pagalbos centro (BPC) registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, duomenys, kai transporto... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/bpc/pagalbos_ecall_iskvietimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_ecall_iskvietimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/bpc/pagalbos_ecall_iskvietimai (https://data.gov.lt/datasets/2761/)
