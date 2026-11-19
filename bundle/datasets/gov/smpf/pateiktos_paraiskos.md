---
type: Dataset
title: "Švietimo mainų paramos fondo paraiškos ir lektorių programos"
description: "Rinkinyje pateikiami VšĮ Švietimo mainų paramos fondo nuo 2023 m. kaupiami ir saugomi pateiktų paraiškų ir lektorių programų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/smpf/pateiktos_paraiskos"
tags: [gov, smpf, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/smpf/pateiktos_paraiskos.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/smpf/pateiktos_paraiskos.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2825/"
    title: "data.gov.lt DCAT-AP — datasets/gov/smpf/pateiktos_paraiskos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Švietimo mainų paramos fondo paraiškos ir lektorių programos

Rinkinyje pateikiami VšĮ Švietimo mainų paramos fondo nuo 2023 m. kaupiami ir saugomi pateiktų paraiškų ir lektorių programų duomenys. Duomenų rinkinį sudaro dvi lentelės, sujungtos „paraiskos_nr“ stulpeliu. Vieną duomenų rinkinio lentelę sudaro į Lietuvoje organizuojamus renginius pateiktų paraiškų duomenys, o kitoje lentelėje pateikiamos Lietuvos dėstytojų / lektorių renginiams siūlomos programos. Viena duomenų rinkinio eilutė atitinka vieną paraišką arba vieną dėstytojo programą. Dėl techninių klausimų ar galimų klaidų galima kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/smpf/pateiktos_paraiskos`[^manifest]
- **Manifest CSV:** [datasets/gov/smpf/pateiktos_paraiskos.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/smpf/pateiktos_paraiskos.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/smpf/pateiktos_paraiskos` (`deployed`)[^manifest]
- **Provider:** `smpf` — VšĮ Švietimo mainų paramos fondas (SMPF) *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2825/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/smpf/pateiktos_paraiskos`[^dcat]
- **Portal Title (`@lt`):** Švietimo mainų paramos fondo paraiškos ir lektorių programos[^dcat]
- **Portal Title (`@en`):** Applications and lecturers' programmes of the Education Exchange Support Fund[^dcat]
- **Issued (`dct:issued`):** `2024-10-23`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-10-23` .. `2026-10-17`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami VšĮ Švietimo mainų paramos fondo nuo 2023 m. kaupiami ir saugomi pateiktų paraiškų ir lektorių programų duomenys. Duomenų rinkinį sudaro dvi lentelės, sujungtos „paraiskos_nr“ stulpeliu. Vieną duomenų rinkinio lentelę sudaro į Lietuvoje organizuojamus renginius pateiktų paraiškų duomenys, o kitoje lentelėje pateikiamos Lietuvos dėstytojų / lektorių renginiams siūlomos programos. Viena duomenų rinkinio eilutė atitinka vieną paraišką arba vieną dėstytojo programą. Duomenų teikėjas – VšĮ Švietimo mainų paramos fondas. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package contains data from applications submitted and programmes of lecturers compiled and stored by the Public Education Exchanges Support Foundation for Education Exchange from 2023. The dataset consists of two tables connected by a “paraiskos_nr” column. One dataset table consists of the data of applications submitted to events organised in Lithuania, while another table shows the programmes offered for events of Lithuanian lecturers/lecturers. One data set line corresponds to one application or one faculty program. Technical questions or possible errors may be referred to the atverimas@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Paraiska](pateiktos_paraiskos/Paraiska.md) | Švietimo mainų paramos fondo paraiškos | `4` | `vda_prime_key` | — | `16` | Rinkinyje pateikiami VšĮ Švietimo mainų paramos fondo nuo 2023 m. kaupiami ir saugomi pateiktų paraiškų duomenys. |
| [LektoriausPrograma](pateiktos_paraiskos/LektoriausPrograma.md) | Švietimo mainų paramos fondo lektorių siūlomos programos | `4` | `vda_prime_key` | `open` | `14` | Rinkinyje pateikiami VšĮ Švietimo mainų paramos fondo nuo 2023 m. kaupiami ir saugom lektorių siūlomų programų duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/smpf/pateiktos_paraiskos.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/smpf/pateiktos_paraiskos.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/smpf/pateiktos_paraiskos (https://data.gov.lt/datasets/2825/)
