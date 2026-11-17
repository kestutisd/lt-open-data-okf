---
type: Table
title: "ValiosPareiskimoOrganas"
description: "Spinta table datasets/gov/ntb/pacientu_valios_pareiskimai/ValiosPareiskimoOrganas (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ntb/pacientu_valios_pareiskimai/ValiosPareiskimoOrganas"
tags: [gov, ntb, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ntb/pacientu_valios_pareiskimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L33"
    last_modified: "2026-11-11T14:39:20Z"
---

# ValiosPareiskimoOrganas

- **Model:** `datasets/gov/ntb/pacientu_valios_pareiskimai/ValiosPareiskimoOrganas`[^manifest]
- **Dataset:** [datasets/gov/ntb/pacientu_valios_pareiskimai](../pacientu_valios_pareiskimai.md) (`datasets/gov/ntb/pacientu_valios_pareiskimai`)
- **Manifest CSV:** [datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L33](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L33)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ntb/pacientu_valios_pareiskimai/ValiosPareiskimoOrganas`
- **Primary Key (`ref`):** `sutikimas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sutikimas` | `ref` | [ValiosPareiskimas](ValiosPareiskimas.md) | `4` | `open` | — | Susietas sutikimas | — |
| `organas` | `ref` | [Organas](Organas.md) | `4` | `open` | — | Susietas audinys ar organas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ntb/pacientu_valios_pareiskimai.csv
