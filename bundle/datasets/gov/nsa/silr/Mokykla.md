---
type: Table
title: "Mokykla — \"Mokinių lankomumo duomenų mokyklos\""
description: "Spinta table datasets/gov/nsa/silr/Mokykla (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/silr/Mokykla"
tags: [gov, nsa, mokykla, deployed, level-4, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/silr/silr.csv#L21"
    title: "atviriduomenys/manifest — datasets/gov/nsa/silr/silr.csv#L21"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2910/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nsa/silr"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Mokykla — "Mokinių lankomumo duomenų mokyklos"

- **Model:** `datasets/gov/nsa/silr/Mokykla`[^manifest]
- **Dataset:** [Švietimo įstaigų lankomumo rodikliai](../silr.md) (`datasets/gov/nsa/silr`)[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/silr/silr.csv#L21](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/silr/silr.csv#L21)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/silr/Mokykla` (`deployed`)[^manifest]
- **Provider:** `nsa` — Nacionalinė švietimo agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_2`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | "Unikalus identifikatorius" | — |
| `ins_kodas` | `string` | — | `4` | `open` | — | "Švietimo įstaigos (mokyklos) kodas Juridinių asmenų registre" | — |
| `pad_kodas` | `string` | — | `4` | `open` | — | Švietimo ir mokslo institucijų registro institucijos padalinio kodas | — |
| `ins_pav` | `string` | — | `4` | `open` | — | Švietimo įstaigos (mokyklos) pavadinimas Juridinių asmenų registre | — |
| `pad_pav` | `string` | — | `4` | `open` | — | Švietimo ir mokslo institucijų registro institucijos padalinio pavadinimas | — |
| `sav_kodas` | `string` | — | `4` | `open` | — | Savivaldybės kodas | — |
| `sav_pav` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/silr/silr.csv#L21 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/silr/silr.csv#L21)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nsa/silr (https://data.gov.lt/datasets/2910/)
