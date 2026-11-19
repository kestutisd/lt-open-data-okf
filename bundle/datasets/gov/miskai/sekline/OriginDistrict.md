---
type: Table
title: "OriginDistrict — Kilmės rajonas"
description: "Spinta table datasets/gov/miskai/sekline/OriginDistrict (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/sekline/OriginDistrict"
tags: [gov, miskai, origindistrict, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sekline.csv#L37"
    title: "atviriduomenys/manifest — datasets/gov/miskai/sekline.csv#L37"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/739/"
    title: "data.gov.lt DCAT-AP — datasets/gov/miskai/sekline"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# OriginDistrict — Kilmės rajonas

- **Model:** `datasets/gov/miskai/sekline/OriginDistrict`[^manifest]
- **Dataset:** [Lietuvos sėklinės miško bazės objektų sąrašai](../sekline.md) (`datasets/gov/miskai/sekline`)[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/sekline.csv#L37](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sekline.csv#L37)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/sekline/OriginDistrict` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tree_type` | `ref` | [TreeType](TreeType.md) (`level=4 UUID`: `tree_type._id`) | `4` | `open` | — | Medžio tipas | — |
| `name` | `string` | — | `3` | `open` | — | Kilmės rajono pavadinimas | — |
| `teritory` | `string` | — | `3` | `open` | — | Kilmės rajono teritorija | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/sekline.csv#L37 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sekline.csv#L37)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/miskai/sekline (https://data.gov.lt/datasets/739/)
