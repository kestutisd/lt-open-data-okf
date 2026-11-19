---
type: Table
title: "MDMCategory — Miško dauginamosios medžiagos kategorija"
description: "Spinta table datasets/gov/miskai/sekline/MDMCategory (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/sekline/MDMCategory"
tags: [gov, miskai, mdmcategory, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sekline.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/miskai/sekline.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/739/"
    title: "data.gov.lt DCAT-AP — datasets/gov/miskai/sekline"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# MDMCategory — Miško dauginamosios medžiagos kategorija

- **Model:** `datasets/gov/miskai/sekline/MDMCategory`[^manifest]
- **Dataset:** [Lietuvos sėklinės miško bazės objektų sąrašai](../sekline.md) (`datasets/gov/miskai/sekline`)[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/sekline.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sekline.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/sekline/MDMCategory` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `value` | `string` | — | `3` | `open` | — | MDM kategorijos kodas | — |
| `name` | `string` | — | `3` | `open` | — | MDM kategorijos pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/sekline.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sekline.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/miskai/sekline (https://data.gov.lt/datasets/739/)
