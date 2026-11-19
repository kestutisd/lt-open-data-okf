---
type: Table
title: "Object — Sėklinės bazės objektas"
description: "Spinta table datasets/gov/miskai/sekline/Object (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/sekline/Object"
tags: [gov, miskai, object, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sekline.csv#L42"
    title: "atviriduomenys/manifest — datasets/gov/miskai/sekline.csv#L42"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/739/"
    title: "data.gov.lt DCAT-AP — datasets/gov/miskai/sekline"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Object — Sėklinės bazės objektas

- **Model:** `datasets/gov/miskai/sekline/Object`[^manifest]
- **Dataset:** [Lietuvos sėklinės miško bazės objektų sąrašai](../sekline.md) (`datasets/gov/miskai/sekline`)[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/sekline.csv#L42](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sekline.csv#L42)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/sekline/Object` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | — | `3` | `open` | — | Kodas | — |
| `seed_base_type` | `ref` | [SeedBaseType](SeedBaseType.md) (`level=4 UUID`: `seed_base_type._id`) | `4` | `open` | — | Sėklinės bazės tipas | — |
| `object_status` | `ref` | [ObjectStatus](ObjectStatus.md) (`level=4 UUID`: `object_status._id`) | `4` | `open` | — | Objekto statusas | — |
| `name` | `string` | — | `3` | `open` | — | Objekto pavadinimas | — |
| `mdm_category` | `ref` | [MDMCategory](MDMCategory.md) (`level=4 UUID`: `mdm_category._id`) | `4` | `open` | — | MDM kategorija | — |
| `mdm_distribution_opportunity` | `ref` | [MDMDistributionOpportunity](MDMDistributionOpportunity.md) (`level=4 UUID`: `mdm_distribution_opportunity._id`) | `4` | `open` | — | MDM platinimo galimybė | — |
| `origin_district` | `ref` | [OriginDistrict](OriginDistrict.md) (`level=4 UUID`: `origin_district._id`) | `4` | `open` | — | Kilmės rajonas | — |
| `owner` | `ref` | [Owner](Owner.md) (`level=4 UUID`: `owner._id`) | `4` | `open` | — | Valdytojas | — |
| `forestry` | `ref` | [Forestry](Forestry.md) (`level=4 UUID`: `forestry._id`) | `4` | `open` | — | Girininkija | — |
| `quarter` | `string` | — | `3` | `open` | — | Kvartalai | — |
| `parcel` | `string` | — | `3` | `open` | — | Sklypai | — |
| `north_latitude` | `string` | — | `3` | `open` | — | Šiaurės platuma | Geografinės koordinatės |
| `east_longitude` | `string` | — | `3` | `open` | — | Rytų ilguma | Geografinės koordinatės |
| `altitude` | `number` | `m` | `4` | `open` | — | Aukštis virš jūros lygio (m.) | — |
| `foundation_date` | `date` | `Y` | `4` | `open` | — | Įkūrimo/įveisimo data | — |
| `tree_type` | `ref` | [TreeType](TreeType.md) (`level=4 UUID`: `tree_type._id`) | `4` | `open` | — | Medžio tipas | — |
| `area` | `number` | `ha` | `4` | `open` | — | Plotas (ha) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/sekline.csv#L42 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sekline.csv#L42)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/miskai/sekline (https://data.gov.lt/datasets/739/)
