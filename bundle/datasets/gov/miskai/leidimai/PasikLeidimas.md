---
type: Table
title: "PasikLeidimas — Išduoti leidimai"
description: "Spinta table datasets/gov/miskai/leidimai/PasikLeidimas (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/leidimai/PasikLeidimas"
tags: [gov, miskai, pasikleidimas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/leidimai.csv#L48"
    title: "atviriduomenys/manifest — datasets/gov/miskai/leidimai.csv#L48"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2121/"
    title: "data.gov.lt DCAT-AP — datasets/gov/miskai/leidimai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PasikLeidimas — Išduoti leidimai

- **Model:** `datasets/gov/miskai/leidimai/PasikLeidimas`[^manifest]
- **Dataset:** [Leidimų kirsti mišką statistika](../leidimai.md) (`datasets/gov/miskai/leidimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/leidimai.csv#L48](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/leidimai.csv#L48)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/leidimai/PasikLeidimas` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `leidimas` | `ref` | [Leidimas](Leidimas.md) (`level=4 UUID`: `leidimas._id`) | `4` | `open` | — | — | — |
| `prat_data` | `datetime` | `D` | `4` | `open` | — | Leidimo išdavimo/pratęsimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/leidimai.csv#L48 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/leidimai.csv#L48)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/miskai/leidimai (https://data.gov.lt/datasets/2121/)
