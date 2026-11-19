---
type: Table
title: "Organas"
description: "Spinta table datasets/gov/ntb/pacientu_valios_pareiskimai/Organas (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ntb/pacientu_valios_pareiskimai/Organas"
tags: [gov, ntb, organas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L37"
    title: "atviriduomenys/manifest — datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L37"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1210/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ntb/pacientu_valios_pareiskimai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Organas

- **Model:** `datasets/gov/ntb/pacientu_valios_pareiskimai/Organas`[^manifest]
- **Dataset:** [Pacientų valios pareiškimo duomenys](../pacientu_valios_pareiskimai.md) (`datasets/gov/ntb/pacientu_valios_pareiskimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L37](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L37)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ntb/pacientu_valios_pareiskimai/Organas` (`deployed`)[^manifest]
- **Provider:** `ntb` — Nacionalinis transplantacijos biuras prie Sveikatos apsaugos ministerijos *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `grupe` | `string` | — | `4` | `open` | — | Audinio ar organo grupė/pogrupis | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L37 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L37)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ntb/pacientu_valios_pareiskimai (https://data.gov.lt/datasets/1210/)
