---
type: Dataset
title: "VšĮ Rokiškio psichiatrijos ligoninėje gydytų pacientų duomenys"
description: "Paciento gyvenamosios vietos regionas (miesto ar rajono pavadinimas), atsiuntusi įstaiga, diagnozė, amžius, lytis, gydymosi laikotarpis, gydymo rezultatas."
resource: "https://get.data.gov.lt/datasets/gov/rpl/gydyti_pacientai"
tags: [gov, rpl, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rpl/gydyti_pacientai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rpl/gydyti_pacientai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2029/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rpl/gydyti_pacientai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# VšĮ Rokiškio psichiatrijos ligoninėje gydytų pacientų duomenys

- **Namespace:** `datasets/gov/rpl/gydyti_pacientai`[^manifest]
- **Manifest CSV:** [datasets/gov/rpl/gydyti_pacientai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rpl/gydyti_pacientai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rpl/gydyti_pacientai` (`deployed`)[^manifest]
- **Provider:** `rpl` — Rokiškio psichiatrijos ligoninė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2029/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rpl/gydyti_pacientai`[^dcat]
- **Portal Title (`@lt`):** VšĮ Rokiškio psichiatrijos ligoninėje gydytų pacientų duomenys[^dcat]
- **Portal Title (`@en`):** Data of patients treated at the Rokiškis Psychiatric Hospital of VšĮ[^dcat]
- **Issued (`dct:issued`):** `2022-09-29`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-04-22` .. `2026-10-15`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Paciento gyvenamosios vietos regionas (miesto ar rajono pavadinimas), atsiuntusi įstaiga, diagnozė, amžius, lytis, gydymosi laikotarpis, gydymo rezultatas. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Region of the patient&#39;s residence (name of the city or district), referring institution, diagnosis, age, gender, period of treatment, result of treatment[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Pacientai](gydyti_pacientai/Pacientai.md) | VšĮ Rokiškio psichiatrijos ligoninėje gydytų pacientų duomenys | `4` | `vda_id` | — | `16` | Paciento gyvenamosios vietos regionas (miesto ar rajono pavadinimas), atsiuntusi įstaiga, diagnozė, amžius, lytis, gydymosi laikotarpis, gydymo rezultatas |

[^manifest]: atviriduomenys/manifest — datasets/gov/rpl/gydyti_pacientai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rpl/gydyti_pacientai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rpl/gydyti_pacientai (https://data.gov.lt/datasets/2029/)
