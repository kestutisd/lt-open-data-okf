---
type: Dataset
title: "Sveikatos priežiūros įstaigų laboratorijos rezultatų duomenys (Rokiškio psichiatrijos ligoninė)"
description: "Duomenys iš Ligoninės klinikinės diagnostinės laboratorijos informacinės sistemos (KDLIS)."
resource: "https://get.data.gov.lt/datasets/gov/rpl/laboratorijos"
tags: [gov, rpl, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rpl/laboratorijos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rpl/laboratorijos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2723/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rpl/laboratorijos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sveikatos priežiūros įstaigų laboratorijos rezultatų duomenys (Rokiškio psichiatrijos ligoninė)

- **Namespace:** `datasets/gov/rpl/laboratorijos`[^manifest]
- **Manifest CSV:** [datasets/gov/rpl/laboratorijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rpl/laboratorijos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rpl/laboratorijos` (`deployed`)[^manifest]
- **Provider:** `rpl` — Rokiškio psichiatrijos ligoninė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2723/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rpl/laboratorijos`[^dcat]
- **Portal Title (`@lt`):** Sveikatos priežiūros įstaigos laboratorijos tyrimų rezultatų duomenys (Rokiškio psichiatrijos ligoninė)[^dcat]
- **Portal Title (`@en`):** Results of the laboratory of health care institutions (Rokiškis Psychiatric Hospital)[^dcat]
- **Issued (`dct:issued`):** `2024-08-29`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-07-26` .. `2026-10-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys iš Ligoninės klinikinės diagnostinės laboratorijos informacinės sistemos (KDLIS). Pateikiama informacija apie pacientus (gimimo metai, lytis) ir atliktų tyrimų informacija (tyrimo data, laikas, tyrimo grupė, tyrimo analitė, rezultatai, normos bei matavimo vienetai). Atveriami duomenys nuo 2023 m. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data from the Information System of the Hospital Clinical Diagnostic Laboratory (KDLIS). Information on patients (year of birth, sex) and information on the studies carried out (date, time, study group, study analyte, results, rates and units of measure) shall be provided. Data shall be collected from 2008 onwards.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Rezultatas](laboratorijos/Rezultatas.md) | Sveikatos priežiūros įstaigų laboratorijos rezultatų duomenys (Rokiškio psichiatrijos ligoninė) | `4` | `vda_id` | — | `18` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rpl/laboratorijos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rpl/laboratorijos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rpl/laboratorijos (https://data.gov.lt/datasets/2723/)
