---
type: Dataset
title: "Akcizinių prekių sulaikymų duomenys"
description: "Muitinės departamento duomenų apie akcizinių prekių nelegalios apyvartos užkardymo rezultatus kaupimo ir apdorojimo sistemoje nuo 2017 m. kaupiami ir iki šiol atnaujinami akcizinių prekių sulaikymo duomenys."
resource: "https://get.data.gov.lt/datasets/gov/muitine/stebesena"
tags: [gov, muitine, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/stebesena.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/muitine/stebesena.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2874/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/stebesena"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Akcizinių prekių sulaikymų duomenys

- **Namespace:** `datasets/gov/muitine/stebesena`[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/stebesena.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/stebesena.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/stebesena` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2874/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/muitine/stebesena`[^dcat]
- **Portal Title (`@lt`):** Akcizinių prekių sulaikymų duomenys[^dcat]
- **Portal Title (`@en`):** Excise goods detention data[^dcat]
- **Issued (`dct:issued`):** `2024-11-28`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-11-28` .. `2026-10-15`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Muitinės departamento duomenų apie akcizinių prekių nelegalios apyvartos užkardymo rezultatus kaupimo ir apdorojimo sistemoje nuo 2017 m. kaupiami ir iki šiol atnaujinami akcizinių prekių sulaikymo duomenys. Duomenų rinkinį sudaro: atitinkamos medžiagos prekę sulaikiusi aukštesnė institucija, metų ketvirčio periodo pradžia ir pabaiga, atitinkamos prekės sulaikymo data, sulaikytos prekės ir jos grupės pavadinimai, atitinkamu laikotarpiu sulaikytos prekės bendra vertė ir kiekis. Vienas įrašas atitinka vieną aukštesnės institucijos, laikotarpio ir prekės kombinaciją. Duomenų teikėjas – Muitinės departamentas prie Lietuvos Respublikos finansų ministerijos. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

In the system of accumulation and processing of data of the Customs Department on the results of the prevention of illegal circulation of excise goods, data on the detention of excise goods shall be accumulated and updated as of 2017. The dataset shall comprise: the higher authority holding the item in question, the beginning and end of the quarterly period of the year, the date of detention of the item concerned, the names of the goods detained and its group, the total value and quantity of the item detained during the relevant period. One entry corresponds to one combination of a higher institution, period, and item. Data provider shall mean the Customs Department under the Ministry of Finance of the Republic of Lithuania. Technical questions or possible errors can be contacted by the atverimas@stat.gov.lt[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SulaikytaPreke](stebesena/SulaikytaPreke.md) | Akcizinių prekių sulaikymų duomenys | `4` | `vda_prime_key` | — | `9` | Muitinės departamento duomenų apie akcizinių prekių nelegalios apyvartos užkardymo rezultatus kaupimo ir apdorojimo sistemoje nuo 2017 m. kaupiami ir iki... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/stebesena.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/stebesena.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/stebesena (https://data.gov.lt/datasets/2874/)
