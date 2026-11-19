---
type: Dataset
title: "Nuotekų debitas"
description: "Alytaus rajono savivaldybės įmonės „Simno komunalininkas“ vedamoje nuotekų debitų apskaitoje fiksuojamas kiekviename valymo įrenginyje išvalytų buitinių nuotekų kiekis, skaičiuojamas kubiniais metrais per dieną."
resource: "https://get.data.gov.lt/datasets/gov/simno_komun/nuotekos"
tags: [gov, simno_komun, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/nuotekos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/simno_komun/nuotekos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2783/"
    title: "data.gov.lt DCAT-AP — datasets/gov/simno_komun/nuotekos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Nuotekų debitas

Alytaus rajono savivaldybės įmonės „Simno komunalininkas“ vedamoje nuotekų debitų apskaitoje fiksuojamas kiekviename valymo įrenginyje išvalytų buitinių nuotekų kiekis, skaičiuojamas kubiniais metrais per dieną. Duomenys nuo 2018 iki 2023 metų.[^manifest]

- **Namespace:** `datasets/gov/simno_komun/nuotekos`[^manifest]
- **Manifest CSV:** [datasets/gov/simno_komun/nuotekos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/nuotekos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/simno_komun/nuotekos` (`deployed`)[^manifest]
- **Provider:** `simno_komun` — Alytaus rajono savivaldybės įmonė „Simno komunalininkas“ *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2783/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/simno_komun/nuotekos`[^dcat]
- **Portal Title (`@lt`):** Alytaus rajono savivaldybės įmonės "Simno Komunalininko" nuotekų debitas[^dcat]
- **Portal Title (`@en`):** Wastewater debit of Simno Komunalistas, Municipality of Alytus District Municipality[^dcat]
- **Issued (`dct:issued`):** `2024-09-13`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2024-09-09` .. `2024-09-12`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Alytaus rajono savivaldybės įmonės „Simno komunalininkas“ vedamoje nuotekų debitų apskaitoje fiksuojamas kiekviename valymo įrenginyje išvalytų buitinių nuotekų kiekis, skaičiuojamas kubiniais metrais per dieną. Duomenys nuo 2018 iki 2023 metų. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The metering of sewage debits conducted by Simnas komunalininkai, a municipal enterprise in Alytus District Municipality district, records the amount of domestic waste water treated at each treatment plant, calculated in cubic meters per day. Data from 2023. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NuotekuDebitas](nuotekos/NuotekuDebitas.md) | Nuotekų debitas | `4` | `vda_prime_key` | — | `4` | Alytaus rajono savivaldybės įmonės „Simno komunalininkas“ vedamoje nuotekų debitų apskaitoje fiksuojamas kiekviename valymo įrenginyje išvalytų buitinių... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/simno_komun/nuotekos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/nuotekos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/simno_komun/nuotekos (https://data.gov.lt/datasets/2783/)
