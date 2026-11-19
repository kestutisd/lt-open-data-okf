---
type: Table
title: "AkcizoMokestis — Akcizų deklaracijų duomenys"
description: "Spinta table datasets/gov/vmi/akcizai/AkcizoMokestis (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/akcizai/AkcizoMokestis"
tags: [gov, vmi, akcizomokestis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/akcizai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vmi/akcizai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1176/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/akcizai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# AkcizoMokestis — Akcizų deklaracijų duomenys

- **Model:** `datasets/gov/vmi/akcizai/AkcizoMokestis`[^manifest]
- **Dataset:** [Duomenys apie akcizais apmokestinamas prekes](../akcizai.md) (`datasets/gov/vmi/akcizai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/akcizai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/akcizai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/akcizai/AkcizoMokestis` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `eiles_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/akcizai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/akcizai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/akcizai (https://data.gov.lt/datasets/1176/)
