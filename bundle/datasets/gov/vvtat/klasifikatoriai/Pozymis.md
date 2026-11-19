---
type: Table
title: "Pozymis — VVTAT patikrinimų metu nustatytų pažeidimų požymių klasifikatorius"
description: "Rinkinyje pateikiami duomenys apie Valstybinės vartotojų teisių apsaugos tarnybos naudojamus klasifikatorius"
resource: "https://get.data.gov.lt/datasets/gov/vvtat/klasifikatoriai/Pozymis"
tags: [gov, vvtat, pozymis, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/klasifikatoriai.csv#L56"
    title: "atviriduomenys/manifest — datasets/gov/vvtat/klasifikatoriai.csv#L56"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2682/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vvtat/klasifikatoriai"
    author: "team:vda"
    last_modified: "2026-08-17T00:00:00Z"
---

# Pozymis — VVTAT patikrinimų metu nustatytų pažeidimų požymių klasifikatorius

**Dataset Context:** Rinkinyje pateikiami duomenys apie Valstybinės vartotojų teisių apsaugos tarnybos naudojamus klasifikatorius[^manifest]

- **Model:** `datasets/gov/vvtat/klasifikatoriai/Pozymis`[^manifest]
- **Dataset:** [Duomenys apie VVTAT klasifikatorius](../klasifikatoriai.md) (`datasets/gov/vvtat/klasifikatoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vvtat/klasifikatoriai.csv#L56](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/klasifikatoriai.csv#L56)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvtat/klasifikatoriai/Pozymis` (`deployed`)[^manifest]
- **Provider:** `vvtat` — Valstybinė vartotojų teisių apsaugos tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-08-17`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo unikalus identifikatorius | — |
| `pavadinimas_lt` | `string` | — | `4` | `open` | — | Požymio pavadinimas | — |
| `galioja_nuo` | `date` | `D` | `4` | `open` | — | Klasifikatoriaus galiojimo pradžia | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Klasifikatoriaus galiojimo pabaiga | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvtat/klasifikatoriai.csv#L56 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/klasifikatoriai.csv#L56)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vvtat/klasifikatoriai (https://data.gov.lt/datasets/2682/)
