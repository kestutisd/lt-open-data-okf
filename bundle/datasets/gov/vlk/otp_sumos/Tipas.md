---
type: Table
title: "Tipas — Ortopedijos techninių ir medicinos priemonių tipai"
description: "Informacija apie ortopedijos techninių ir medicinos priemonių tipus"
resource: "https://get.data.gov.lt/datasets/gov/vlk/otp_sumos/Tipas"
tags: [gov, vlk, tipas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/otp_sumos.csv#L14"
    title: "atviriduomenys/manifest — datasets/gov/vlk/otp_sumos.csv#L14"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1800/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/otp_sumos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Tipas — Ortopedijos techninių ir medicinos priemonių tipai

Informacija apie ortopedijos techninių ir medicinos priemonių tipus[^manifest]

- **Model:** `datasets/gov/vlk/otp_sumos/Tipas`[^manifest]
- **Dataset:** [Mokamos sumos už ortopedijos technines ir medicinos priemones](../otp_sumos.md) (`datasets/gov/vlk/otp_sumos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/otp_sumos.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/otp_sumos.csv#L14)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/otp_sumos/Tipas` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ad_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `grupe` | `ref` | [Grupe](Grupe.md) (`level=4 UUID`: `grupe._id`) | `4` | `open` | — | Nuoroda į Grupė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/otp_sumos.csv#L14 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/otp_sumos.csv#L14)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/otp_sumos (https://data.gov.lt/datasets/1800/)
