---
type: Table
title: "Istaiga — Įstaigų sąrašas"
description: "Spinta table datasets/gov/vlk/otp_sumos/Istaiga (1 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vlk/otp_sumos/Istaiga"
tags: [gov, vlk, istaiga, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/otp_sumos.csv#L29"
    title: "atviriduomenys/manifest — datasets/gov/vlk/otp_sumos.csv#L29"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1800/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/otp_sumos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Istaiga — Įstaigų sąrašas

- **Model:** `datasets/gov/vlk/otp_sumos/Istaiga`[^manifest]
- **Dataset:** [Mokamos sumos už ortopedijos technines ir medicinos priemones](../otp_sumos.md) (`datasets/gov/vlk/otp_sumos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/otp_sumos.csv#L29](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/otp_sumos.csv#L29)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/otp_sumos/Istaiga` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `istg_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `istg_id` | `ref` | [Istaiga](../istaigos/Istaiga.md) (`level=4 UUID`: `istg_id._id`) | `4` | `open` | — | Įstaigos ID | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/otp_sumos.csv#L29 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/otp_sumos.csv#L29)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/otp_sumos (https://data.gov.lt/datasets/1800/)
