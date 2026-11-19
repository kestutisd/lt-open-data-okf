---
type: Table
title: "STRUKPadalinys — Struktūriniai padaliniai"
description: "Spinta table datasets/gov/miskai/leidimai/STRUKPadalinys (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/leidimai/STRUKPadalinys"
tags: [gov, miskai, strukpadalinys, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/leidimai.csv#L16"
    title: "atviriduomenys/manifest — datasets/gov/miskai/leidimai.csv#L16"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2121/"
    title: "data.gov.lt DCAT-AP — datasets/gov/miskai/leidimai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# STRUKPadalinys — Struktūriniai padaliniai

- **Model:** `datasets/gov/miskai/leidimai/STRUKPadalinys`[^manifest]
- **Dataset:** [Leidimų kirsti mišką statistika](../leidimai.md) (`datasets/gov/miskai/leidimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/leidimai.csv#L16](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/leidimai.csv#L16)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/leidimai/STRUKPadalinys` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pavadinimas` | `string` | — | `3` | `open` | — | Poskyris | Teritorinio miškų kontrolės poskyrio pavadinimas |
| `tmkp` | `ref` | [TMKPadalinys](TMKPadalinys.md) (`level=4 UUID`: `tmkp._id`) | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/leidimai.csv#L16 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/leidimai.csv#L16)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/miskai/leidimai (https://data.gov.lt/datasets/2121/)
