---
type: Table
title: "Nusiskundimas — VVTAT vartotojų nusiskundimo pobūdžių klasifikatorius"
description: "Rinkinyje pateikiami duomenys apie Valstybinės vartotojų teisių apsaugos tarnybos naudojamus klasifikatorius"
resource: "https://get.data.gov.lt/datasets/gov/vvtat/klasifikatoriai/Nusiskundimas"
tags: [gov, vvtat, nusiskundimas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/klasifikatoriai.csv#L50"
    title: "atviriduomenys/manifest — datasets/gov/vvtat/klasifikatoriai.csv#L50"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2682/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vvtat/klasifikatoriai"
    author: "team:vda"
    last_modified: "2026-08-17T00:00:00Z"
---

# Nusiskundimas — VVTAT vartotojų nusiskundimo pobūdžių klasifikatorius

**Dataset Context:** Rinkinyje pateikiami duomenys apie Valstybinės vartotojų teisių apsaugos tarnybos naudojamus klasifikatorius[^manifest]

- **Model:** `datasets/gov/vvtat/klasifikatoriai/Nusiskundimas`[^manifest]
- **Dataset:** [Duomenys apie VVTAT klasifikatorius](../klasifikatoriai.md) (`datasets/gov/vvtat/klasifikatoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vvtat/klasifikatoriai.csv#L50](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/klasifikatoriai.csv#L50)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvtat/klasifikatoriai/Nusiskundimas` (`deployed`)[^manifest]
- **Provider:** `vvtat` — Valstybinė vartotojų teisių apsaugos tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-08-17`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `string` | — | `4` | `open` | — | Pobūdžio kodas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Nusiskundimo pobūdis | — |
| `galioja_nuo` | `date` | `D` | `4` | `open` | — | Klasifikatoriaus galiojimo pradžia | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Klasifikatoriaus galiojimo pabaiga | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvtat/klasifikatoriai.csv#L50 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/klasifikatoriai.csv#L50)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vvtat/klasifikatoriai (https://data.gov.lt/datasets/2682/)
