---
type: Dataset
title: "Pinigų plovimo prevencijos apmokymų dalyvių duomenys"
description: "Pinigų plovimo prevencijos kompetencijų centro (PPPKC) administruojamoje organizuojamų mokymų dalyvių registracijos formoje (OMDRF) kaupiami į įstaigos vykdomus mokymus užsiregistravusiųjų dalyvių duomenys."
resource: "https://get.data.gov.lt/datasets/gov/pppkc/omdrf"
tags: [gov, pppkc, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pppkc/omdrf.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/pppkc/omdrf.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2743/"
    title: "data.gov.lt DCAT-AP — datasets/gov/pppkc/omdrf"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pinigų plovimo prevencijos apmokymų dalyvių duomenys

- **Namespace:** `datasets/gov/pppkc/omdrf`[^manifest]
- **Manifest CSV:** [datasets/gov/pppkc/omdrf.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pppkc/omdrf.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pppkc/omdrf` (`deployed`)[^manifest]
- **Provider:** `pppkc` — VšĮ Pinigų plovimo prevencijos kompetencijų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2743/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/pppkc/omdrf`[^dcat]
- **Portal Title (`@lt`):** Pinigų plovimo prevencijos apmokymų dalyvių duomenys[^dcat]
- **Portal Title (`@en`):** Data of participants in money laundering prevention training[^dcat]
- **Issued (`dct:issued`):** `2024-08-12`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2024-08-12` .. `2024-08-12`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pinigų plovimo prevencijos kompetencijų centro (PPPKC) administruojamoje organizuojamų mokymų dalyvių registracijos formoje (OMDRF) kaupiami į įstaigos vykdomus mokymus užsiregistravusiųjų dalyvių duomenys. Duomenys kaupiami nuo 2022 m. ir yra atnaujinami kas 3 mėnesius. Duomenų rinkinį sudaro dalyvio pseudonimizuotas, tiek maišos algoritmu, tiek raides pavertus žvaigždutėmis, vardas ir pavardė, pseudonimizuotas el. pašto adresas, atviras el. pašto teikėjas, organizacijos pavadinimas, rūšis ir mokymų tema. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Organised Training Participants Registration Form (OMDRF), administered by the Centre for Money Laundering Competencies (PPPKC), accumulates the data of registered participants in the training provided by the institution. Data have been collected since 2022 and are updated every 3 months. The dataset consists of a participant's pseudonymized name, a pseudonymized e-mail address, an open e-mail provider, an organization's name, type, and training topic, both in the bag algorithm and in the case of letters. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Dalyvis](omdrf/Dalyvis.md) | Pinigų plovimo prevencijos apmokymų dalyvių duomenys | `4` | `vda_id` | — | `8` | Pinigų plovimo prevencijos kompetencijų centro (PPPKC) administruojamoje Organizuojamų mokymų dalyvių registracijos formoje (OMDRF) kaupiami į įstaigos... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/pppkc/omdrf.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pppkc/omdrf.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/pppkc/omdrf (https://data.gov.lt/datasets/2743/)
