---
type: Dataset
title: "Utenos rajono savivaldybės administracijos georeferencinių duomenų sistema"
description: "Utenos rajono savivaldybės administracijos georeferencinių duomenų rinkinį sudaro Utenos rajono savivaldybės pildomi Geodezinių darbų duomenys, 18 skirtingų darbų tipų apjungti su prašymais ir Utenos raj."
resource: "https://get.data.gov.lt/datasets/gov/utenos_r_sav/infoera"
tags: [gov, utenos_r_sav, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/utenos_r_sav/infoera.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/utenos_r_sav/infoera.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4115/"
    title: "data.gov.lt DCAT-AP — datasets/gov/utenos_r_sav/infoera"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Utenos rajono savivaldybės administracijos georeferencinių duomenų sistema

- **Namespace:** `datasets/gov/utenos_r_sav/infoera`[^manifest]
- **Manifest CSV:** [datasets/gov/utenos_r_sav/infoera.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/utenos_r_sav/infoera.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/utenos_r_sav/infoera` (`deployed`)[^manifest]
- **Provider:** `utenos_r_sav` — Utenos rajono savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/4115/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/utenos_r_sav/infoera`[^dcat]
- **Portal Title (`@lt`):** Utenos rajono savivaldybės administracijos geodezinių duomenų sistemos INFOERA duomenys[^dcat]
- **Portal Title (`@en`):** INFOERA data from THE geodetic data system OF THE municipal administration of Utena district[^dcat]
- **Issued (`dct:issued`):** `2026-01-27`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-01-27` .. `2026-09-28`[^dcat]

### Portal Description (`@lt`)

Utenos rajono savivaldybės administracijos georeferencinių duomenų rinkinį sudaro Utenos rajono savivaldybės pildomi Geodezinių darbų duomenys, 18 skirtingų darbų tipų apjungti su prašymais ir Utenos raj. savivaldybėje nuo 2007 metų išduotais leidimais. Darbai atliekami įvairaus pobūdžio objektuose – gatvėse, gręžiniuose, žemės sklypuose, pastatuose ir t. t. Į duomenų rinkinį taip pat įtraukta Geodezinių darbų archyvinė lentelė, apimanti 2007–2022 metais atliktus trijų tipų darbus – topografines nuotraukas, kontrolines geodezines nuotraukas ir sklypo planus. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Archyvas](infoera/Archyvas.md) | Utenos rajono savivaldybės administracijos georeferencinių duomenų archyvas | — | `id` | — | `8` | — |
| [Darbas](infoera/Darbas.md) | Utenos rajono savivaldybės administracijos georeferenciniai duomenys | — | `vda_prime_key` | — | `15` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/utenos_r_sav/infoera.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/utenos_r_sav/infoera.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/utenos_r_sav/infoera (https://data.gov.lt/datasets/4115/)
