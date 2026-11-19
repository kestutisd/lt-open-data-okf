---
type: Table
title: "ObjectInteraction — Sąveika su objektais"
description: "Spinta table datasets/gov/ivpk/registrai/ObjectInteraction (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/registrai/ObjectInteraction"
tags: [gov, ivpk, objectinteraction, deployed, level-4, cadence-other]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L151"
    title: "atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv#L151"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1196/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ivpk/registrai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# ObjectInteraction — Sąveika su objektais

- **Model:** `datasets/gov/ivpk/registrai/ObjectInteraction`[^manifest]
- **Dataset:** [Valstybės registrų ir informacinių sistemų registro duomenys](../registrai.md) (`datasets/gov/ivpk/registrai`)[^manifest]
- **Manifest CSV:** [datasets/gov/ivpk/registrai.csv#L151](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L151)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/registrai/ObjectInteraction` (`deployed`)[^manifest]
- **Provider:** `ivpk` — Valstybės skaitmeninių sprendimų agentūra (VSSA, buv. IVPK) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `OTHER`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `type` | `string` | — | `4` | `open` | — | Tipas | — |
| `object` | `ref` | [Object](Object.md) (`level=4 UUID`: `object._id`) | `4` | `open` | — | Objektas | — |
| `interaction_object` | `ref` | [Object](Object.md) (`level=4 UUID`: `interaction_object._id`) | `4` | `open` | — | Sąveika su objektu | — |
| `updated_at` | `datetime` | `S` | `4` | `open` | — | Atnaujinimo data | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `type` | `'S'` | — | — | Teikia duomenis | — |
| `type` | `'G'` | — | — | Gauna duomenis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv#L151 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L151)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ivpk/registrai (https://data.gov.lt/datasets/1196/)
