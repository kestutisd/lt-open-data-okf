---
type: Table
title: "ValiosPareiskimas"
description: "Spinta table datasets/gov/ntb/pacientu_valios_pareiskimai/ValiosPareiskimas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ntb/pacientu_valios_pareiskimai/ValiosPareiskimas"
tags: [gov, ntb, valiospareiskimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1210/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ntb/pacientu_valios_pareiskimai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# ValiosPareiskimas

- **Model:** `datasets/gov/ntb/pacientu_valios_pareiskimai/ValiosPareiskimas`[^manifest]
- **Dataset:** [Pacientų valios pareiškimo duomenys](../pacientu_valios_pareiskimai.md) (`datasets/gov/ntb/pacientu_valios_pareiskimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ntb/pacientu_valios_pareiskimai/ValiosPareiskimas` (`deployed`)[^manifest]
- **Provider:** `ntb` — Nacionalinis transplantacijos biuras prie Sveikatos apsaugos ministerijos *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tipas` | `string` | — | `4` | `open` | — | Paciento valios pareiškimo tipas | — |
| `uzpildymo_data` | `date` | `D` | `4` | `open` | — | Sutikimo užpildymo data | — |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Paciento amžiaus grupė | — |
| `lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `organo_pasirinkimo_tipas` | `string` | — | `4` | `open` | — | Audinių ir organų pasirinkimo tipas | Nurodo ryšį su susietais įrašais ‘SutikimuPoMirtiesOrganai’ lentelėje |
| `apskritis` | `ref` | [Apskritis](../../rc/ar/apskritis/Apskritis.md) (`level=4 UUID`: `apskritis._id`) | `4` | `open` | — | Paciento gyvenamosios vietos apskritis | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Paciento gyvenamosios vietos savivaldybė | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"sutikimas"` | `consent` | — | Sutikimas transplantacijai po mirties | — |
| `tipas` | `"nesutikimas"` | `refusal` | — | Nesutikimas transplantacijai po mirties | — |
| `amziaus_grupe` | `"00-13"` | — | — | — | — |
| `amziaus_grupe` | `"14-17"` | — | — | — | — |
| `amziaus_grupe` | `"18-24"` | — | — | — | — |
| `amziaus_grupe` | `"25-29"` | — | — | — | — |
| `amziaus_grupe` | `"30-34"` | — | — | — | — |
| `amziaus_grupe` | `"35-39"` | — | — | — | — |
| `amziaus_grupe` | `"40-44"` | — | — | — | — |
| `amziaus_grupe` | `"45-49"` | — | — | — | — |
| `amziaus_grupe` | `"50-54"` | — | — | — | — |
| `amziaus_grupe` | `"55-59"` | — | — | — | — |
| `amziaus_grupe` | `"60-64"` | — | — | — | — |
| `amziaus_grupe` | `"65-69"` | — | — | — | — |
| `amziaus_grupe` | `"70+"` | — | — | — | — |
| `lytis` | `"vyras"` | — | — | — | — |
| `lytis` | `"moteris"` | — | — | — | — |
| `organo_pasirinkimo_tipas` | `"visi"` | `1` | — | Bet kurie audiniai ir organai | — |
| `organo_pasirinkimo_tipas` | `"tik_pasirinkti"` | `2` | — | Tik nurodyti audiniai ir / ar organai | — |
| `organo_pasirinkimo_tipas` | `"isskyrus_pasirinktus"` | `3` | — | Visi audiniai ir organai išskyrus | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ntb/pacientu_valios_pareiskimai (https://data.gov.lt/datasets/1210/)
