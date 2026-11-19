---
type: Table
title: "AsmenuNeigalumas — Asmenų neįgalumo lygis"
description: "Spinta table datasets/gov/ndnt/neigalumo_lygis/AsmenuNeigalumas (9 columns)."
tags: [gov, ndnt, asmenuneigalumas, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ndnt/neigalumo_lygis.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/ndnt/neigalumo_lygis.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# AsmenuNeigalumas — Asmenų neįgalumo lygis

- **Model:** `datasets/gov/ndnt/neigalumo_lygis/AsmenuNeigalumas`[^manifest]
- **Dataset:** [Asmenų neįgalumo lygio duomenys](../neigalumo_lygis.md) (`datasets/gov/ndnt/neigalumo_lygis`)[^manifest]
- **Manifest CSV:** [datasets/gov/ndnt/neigalumo_lygis.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ndnt/neigalumo_lygis.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `ndnt` — Asmens su negalia teisių apsaugos agentūra (buv. NDNT) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `gimimo_metai, tlk10am`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nl_lygis` | `string` | — | `4` | `open` | — | Neįgalumo lygis | — |
| `reg_data` | `date` | `D` | `4` | `open` | — | Registracijos data | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) (`level=3`: `savivaldybe.sav_kodas`) | `3` | `open` | — | Savivaldybė | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `gimimo_metai` | `date` | `D` | `4` | `open` | — | Gimimo metai | — |
| `galiojimo_data_nuo` | `date` | `D` | `4` | `open` | — | Galiojimo data nuo | — |
| `galiojimo_data_iki` | `date` | `D` | `4` | `open` | — | Galiojimo data iki | — |
| `terminas` | `string` | — | `3` | `open` | — | Terminas | — |
| `tlk10am` | `ref` | [Tlk10am](../../vlk/tlk10am/Tlk10am.md) (`level=3`: `tlk10am.code`) | `3` | `open` | — | Ligos kodas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `nl_lygis` | `"vidutinis"` | — | — | — | — |
| `nl_lygis` | `"lengvas"` | — | — | — | — |
| `nl_lygis` | `"sunkus"` | — | — | — | — |
| `lytis` | `"v"` | — | — | Vyras | — |
| `lytis` | `"m"` | — | — | Moteris | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/ndnt/neigalumo_lygis.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ndnt/neigalumo_lygis.csv#L5)
