---
type: Table
title: "Object — Sėklinės bazės objektas"
description: "Spinta table datasets/gov/miskai/sekline/Object (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/sekline/Object"
tags: [gov, miskai, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/miskai/sekline.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sekline.csv#L42"
    last_modified: "2026-11-11T14:39:20Z"
---

# Object — Sėklinės bazės objektas

- **Model:** `datasets/gov/miskai/sekline/Object`[^manifest]
- **Dataset:** [datasets/gov/miskai/sekline](../sekline.md) (`datasets/gov/miskai/sekline`)
- **Manifest CSV:** [datasets/gov/miskai/sekline.csv#L42](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sekline.csv#L42)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/sekline/Object`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | — | `3` | `open` | — | Kodas | — |
| `seed_base_type` | `ref` | [SeedBaseType](SeedBaseType.md) | `4` | `open` | — | Sėklinės bazės tipas | — |
| `object_status` | `ref` | [ObjectStatus](ObjectStatus.md) | `4` | `open` | — | Objekto statusas | — |
| `name` | `string` | — | `3` | `open` | — | Objekto pavadinimas | — |
| `mdm_category` | `ref` | [MDMCategory](MDMCategory.md) | `4` | `open` | — | MDM kategorija | — |
| `mdm_distribution_opportunity` | `ref` | [MDMDistributionOpportunity](MDMDistributionOpportunity.md) | `4` | `open` | — | MDM platinimo galimybė | — |
| `origin_district` | `ref` | [OriginDistrict](OriginDistrict.md) | `4` | `open` | — | Kilmės rajonas | — |
| `owner` | `ref` | [Owner](Owner.md) | `4` | `open` | — | Valdytojas | — |
| `forestry` | `ref` | [Forestry](Forestry.md) | `4` | `open` | — | Girininkija | — |
| `quarter` | `string` | — | `3` | `open` | — | Kvartalai | — |
| `parcel` | `string` | — | `3` | `open` | — | Sklypai | — |
| `north_latitude` | `string` | — | `3` | `open` | — | Šiaurės platuma | Geografinės koordinatės |
| `east_longitude` | `string` | — | `3` | `open` | — | Rytų ilguma | Geografinės koordinatės |
| `altitude` | `number` | `m` | `4` | `open` | — | Aukštis virš jūros lygio (m.) | — |
| `foundation_date` | `date` | `Y` | `4` | `open` | — | Įkūrimo/įveisimo data | — |
| `tree_type` | `ref` | [TreeType](TreeType.md) | `4` | `open` | — | Medžio tipas | — |
| `area` | `number` | `ha` | `4` | `open` | — | Plotas (ha) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/sekline.csv
