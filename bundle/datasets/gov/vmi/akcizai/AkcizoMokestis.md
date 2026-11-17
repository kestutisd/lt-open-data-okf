---
type: Table
title: "AkcizoMokestis — Akcizų deklaracijų duomenys"
description: "Spinta table datasets/gov/vmi/akcizai/AkcizoMokestis (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/akcizai/AkcizoMokestis"
tags: [gov, vmi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/akcizai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/akcizai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# AkcizoMokestis — Akcizų deklaracijų duomenys

- **Model:** `datasets/gov/vmi/akcizai/AkcizoMokestis`[^manifest]
- **Dataset:** [datasets/gov/vmi/akcizai](../akcizai.md) (`datasets/gov/vmi/akcizai`)
- **Manifest CSV:** [datasets/gov/vmi/akcizai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/akcizai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/akcizai/AkcizoMokestis`
- **Primary Key (`ref`):** `eiles_nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eiles_nr` | `string` | — | `4` | `open` | — | Rinkinio eilės numeris | — |
| `moketojas` | `integer` | — | `2` | `open` | — | Mokesčių mokėtojas (kvaziidentifikatorius) | — |
| `data_nuo` | `date` | `D` | `4` | `open` | — | Data periodo pradžia | — |
| `data_iki` | `date` | `D` | `4` | `open` | — | Data periodo pabaiga | — |
| `grupe` | `integer` | — | `2` | `open` | — | Tarifinės grupės kodas | — |
| `suma` | `number` | — | `2` | `open` | — | Sumokėta suma | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/akcizai.csv
