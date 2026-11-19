---
type: Table
title: "Lygmuo"
description: "Spinta table datasets/gov/lsd/cl/evrk/Lygmuo (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/cl/evrk/Lygmuo"
tags: [gov, lsd, lygmuo, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/cl/evrk.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lsd/cl/evrk.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1927/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/cl/evrk"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Lygmuo

- **Model:** `datasets/gov/lsd/cl/evrk/Lygmuo`[^manifest]
- **Dataset:** [Ekonominės veiklos klasifikatorius](../evrk.md) (`datasets/gov/lsd/cl/evrk`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/cl/evrk.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/cl/evrk.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/cl/evrk/Lygmuo` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pavadinimas_lt` | `string` | — | `2` | `open` | — | Pavadinimas | — |
| `pavadinimas_en` | `string` | — | `2` | `open` | — | Pavadinimas | — |
| `lygmuo` | `integer` | — | `4` | `open` | — | Lygmuo | — |

# Related References

- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/cl/evrk.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/cl/evrk.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/cl/evrk (https://data.gov.lt/datasets/1927/)
