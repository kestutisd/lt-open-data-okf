---
type: Dataset
title: "Gyventojų pajamos"
description: "Agreguoti duomenys apie gyventojų deklaruotas pajamas pagal rūšis šalies miestuose, savivaldybėse ir apskrityse."
resource: "https://get.data.gov.lt/datasets/gov/vmi/gyventoju_pajamos"
tags: [gov, vmi, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/gyventoju_pajamos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmi/gyventoju_pajamos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1181/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/gyventoju_pajamos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Gyventojų pajamos

- **Namespace:** `datasets/gov/vmi/gyventoju_pajamos`[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/gyventoju_pajamos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/gyventoju_pajamos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/gyventoju_pajamos` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1181/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė mokesčių inspekcija prie Finansų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmi/gyventoju_pajamos`[^dcat]
- **Portal Title (`@lt`):** Gyventojų pajamos[^dcat]
- **Portal Title (`@en`):** Income[^dcat]
- **Issued (`dct:issued`):** `2022-03-15`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2022-03-08` .. `2026-06-08`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Agreguoti duomenys apie gyventojų deklaruotas pajamas pagal rūšis šalies miestuose, savivaldybėse ir apskrityse. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Aggregate data on declared income of the population by species in the country&#39;s cities, municipalities and counties[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [GyventojuPajamos](gyventoju_pajamos/GyventojuPajamos.md) | Duomenys apie mokėtojo deklaruotas pajamas | — | — | — | `9` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/gyventoju_pajamos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/gyventoju_pajamos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/gyventoju_pajamos (https://data.gov.lt/datasets/1181/)
