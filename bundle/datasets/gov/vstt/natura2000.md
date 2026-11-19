---
type: Dataset
title: "Natura 2000 teritorijų apsaugos tikslų duomenys"
description: "Steigiant „Natura 2000“ tinklą Lietuvoje ir užtikrinant jo vertybių apsaugą, inventorizuojamos pagal ES Buveinių ir Paukščių direktyvas saugomos buveinės ir rūšys, nustatoma jų buveinių būklė, išskiriamos jų apsaugai svarbios teritorijos ir joms nustatomi konkretūs apsaugos..."
resource: "https://get.data.gov.lt/datasets/gov/vstt/natura2000"
tags: [gov, vstt, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/natura2000.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vstt/natura2000.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2270/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vstt/natura2000"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Natura 2000 teritorijų apsaugos tikslų duomenys

- **Namespace:** `datasets/gov/vstt/natura2000`[^manifest]
- **Manifest CSV:** [datasets/gov/vstt/natura2000.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/natura2000.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/natura2000` (`deployed`)[^manifest]
- **Provider:** `vstt` — Valstybinė saugomų teritorijų tarnyba prie Aplinkos ministerijos *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2270/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vstt/natura2000`[^dcat]
- **Portal Title (`@lt`):** Natura 2000 teritorijų apsaugos tikslų duomenys[^dcat]
- **Portal Title (`@en`):** Data on conservation targets for Natura 2000 sites[^dcat]
- **Issued (`dct:issued`):** `2023-03-23`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2023-03-23` .. `2026-09-21`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Steigiant „Natura 2000“ tinklą Lietuvoje ir užtikrinant jo vertybių apsaugą, inventorizuojamos pagal ES Buveinių ir Paukščių direktyvas saugomos buveinės ir rūšys, nustatoma jų buveinių būklė, išskiriamos jų apsaugai svarbios teritorijos ir joms nustatomi konkretūs apsaugos tikslai, laikantis palankios apsaugos būklės kriterijų Bendrijos svarbos buveinėms ir rūšims. Apsaugos tikslai nustatomi siekiant kuo tiksliau apibrėžti pageidaujamą tam tikroje teritorijoje siektiną išsaugojimo būklę arba lygį. Jie nustatomi kiekvienam buveinių tipui ir rūšims, esančioms toje teritorijoje. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The establishment of the Natura 2000 network in Lithuania and the protection of its values involves inventorying habitats and species protected under the EU Habitats and Birds Directives, determining their habitat status, identifying sites of conservation importance, and setting specific conservation targets for them, in line with the criteria for favourable conservation status for habitats and species of Community importance. The conservation targets shall be set in order to define as precisely as possible the desired conservation status or level to be achieved in a given area. They shall be set for each habitat type and species present in the area.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [VietovesVertybe](natura2000/VietovesVertybe.md) | Natura 2000 teritorijų vietovių sąrašo duomenys | `4` | `id` | — | `11` | — |
| [ApsaugosTikslas](natura2000/ApsaugosTikslas.md) | Natura 2000 teritorijų apsaugos tikslų duomenys | `4` | — | — | `13` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/natura2000.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/natura2000.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vstt/natura2000 (https://data.gov.lt/datasets/2270/)
