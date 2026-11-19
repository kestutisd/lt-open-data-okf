---
type: Dataset
title: "Nuotekų kiekiai pagal rodiklius po valymo"
description: "Alytaus rajono savivaldybės įmonės „Simno komunalininkas“ Nuotekų valymo registre kaupiamos užterštumo rodiklių reikšmės po valymo."
resource: "https://get.data.gov.lt/datasets/gov/simno_komun/tersalai_po_valymo"
tags: [gov, simno_komun, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/nvr_po.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/simno_komun/nvr_po.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2788/"
    title: "data.gov.lt DCAT-AP — datasets/gov/simno_komun/tersalai_po_valymo"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Nuotekų kiekiai pagal rodiklius po valymo

- **Namespace:** `datasets/gov/simno_komun/tersalai_po_valymo`[^manifest]
- **Manifest CSV:** [datasets/gov/simno_komun/nvr_po.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/nvr_po.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/simno_komun/tersalai_po_valymo` (`deployed`)[^manifest]
- **Provider:** `simno_komun` — Alytaus rajono savivaldybės įmonė „Simno komunalininkas“ *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2788/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/simno_komun/tersalai_po_valymo`[^dcat]
- **Portal Title (`@lt`):** Alytaus rajono savivaldybės įmonės "Simno Komunalininko" Nuotekų kiekiai pagal rodiklius po valymo[^dcat]
- **Portal Title (`@en`):** Quantities of waste water from the Municipality of Alytus “Simno Komunalininko” according to the indicators after treatment[^dcat]
- **Issued (`dct:issued`):** `2024-09-13`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2024-09-12` .. `2024-09-13`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Alytaus rajono savivaldybės įmonės „Simno komunalininkas“ Nuotekų valymo registre kaupiamos užterštumo rodiklių reikšmės po valymo. Duomenų rinkinys apima duomenis nuo 2018 m. Duomenų rinkinį sudaro: valymo įrenginio pavadinimas, užterštumo rodiklių pavadinimai ir rodiklių reikšmės bei pirmųjų pusmečių dienų datos, kada buvo matuotas užterštumas. Duomenų rinkinys yra ilgo formato, todėl vieno valymo įrenginio duomenys išdėstyti vertikaliai. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The waste water treatment register of Simno komunalistas, a municipal enterprise in Alytus district, accumulates the values of the pollution indicators after treatment. The dataset includes data from 2018. The dataset includes: the name of the treatment plant, the names of the contamination indicators and the values of the indicators and the dates of the first six months when the contamination was measured. The data set is in a long format, so the data for one cleaning plant is arranged vertically. If you have any questions about the dataset, please contact the State Data Control Opening Team by e-mail atverimas@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TersaluKiekis](tersalai_po_valymo/TersaluKiekis.md) | Nuotekų kiekiai pagal rodiklius po valymo | `4` | `vda_prime_key` | — | `5` | Alytaus rajono savivaldybės įmonės „Simno komunalininkas“ Nuotekų valymo registre kaupiamos užterštumo rodiklių reikšmės po valymo. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/simno_komun/nvr_po.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/nvr_po.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/simno_komun/tersalai_po_valymo (https://data.gov.lt/datasets/2788/)
