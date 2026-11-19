---
type: Table
title: "ObjectStatus — Objekto statusas"
description: "Spinta table datasets/gov/miskai/sekline/ObjectStatus (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/sekline/ObjectStatus"
tags: [gov, miskai, objectstatus, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sekline.csv#L11"
    title: "atviriduomenys/manifest — datasets/gov/miskai/sekline.csv#L11"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/739/"
    title: "data.gov.lt DCAT-AP — datasets/gov/miskai/sekline"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# ObjectStatus — Objekto statusas

- **Model:** `datasets/gov/miskai/sekline/ObjectStatus`[^manifest]
- **Dataset:** [Lietuvos sėklinės miško bazės objektų sąrašai](../sekline.md) (`datasets/gov/miskai/sekline`)[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/sekline.csv#L11](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sekline.csv#L11)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/sekline/ObjectStatus` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `value` | `string` | — | `3` | `open` | — | Objekto statuso kodas | — |
| `namelt` | `string` | — | `3` | `open` | — | Objekto statuso pavadinimas | — |
| `namelt_plural` | `string` | — | `3` | `open` | — | Objekto statuso pavadinimas daugiskaita | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/sekline.csv#L11 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sekline.csv#L11)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/miskai/sekline (https://data.gov.lt/datasets/739/)
