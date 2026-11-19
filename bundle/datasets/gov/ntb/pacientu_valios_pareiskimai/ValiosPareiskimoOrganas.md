---
type: Table
title: "ValiosPareiskimoOrganas"
description: "Spinta table datasets/gov/ntb/pacientu_valios_pareiskimai/ValiosPareiskimoOrganas (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ntb/pacientu_valios_pareiskimai/ValiosPareiskimoOrganas"
tags: [gov, ntb, valiospareiskimoorganas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L33"
    title: "atviriduomenys/manifest — datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L33"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1210/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ntb/pacientu_valios_pareiskimai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# ValiosPareiskimoOrganas

- **Model:** `datasets/gov/ntb/pacientu_valios_pareiskimai/ValiosPareiskimoOrganas`[^manifest]
- **Dataset:** [Pacientų valios pareiškimo duomenys](../pacientu_valios_pareiskimai.md) (`datasets/gov/ntb/pacientu_valios_pareiskimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L33](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L33)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ntb/pacientu_valios_pareiskimai/ValiosPareiskimoOrganas` (`deployed`)[^manifest]
- **Provider:** `ntb` — Nacionalinis transplantacijos biuras prie Sveikatos apsaugos ministerijos *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `sutikimas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sutikimas` | `ref` | [ValiosPareiskimas](ValiosPareiskimas.md) (`level=4 UUID`: `sutikimas._id`) | `4` | `open` | — | Susietas sutikimas | — |
| `organas` | `ref` | [Organas](Organas.md) (`level=4 UUID`: `organas._id`) | `4` | `open` | — | Susietas audinys ar organas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L33 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L33)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ntb/pacientu_valios_pareiskimai (https://data.gov.lt/datasets/1210/)
