---
type: Table
title: "ValiosPareiskimas"
description: "Spinta table datasets/gov/ntb/pacientu_valios_pareiskimai/ValiosPareiskimas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ntb/pacientu_valios_pareiskimai/ValiosPareiskimas"
tags: [gov, ntb, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ntb/pacientu_valios_pareiskimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# ValiosPareiskimas

- **Model:** `datasets/gov/ntb/pacientu_valios_pareiskimai/ValiosPareiskimas`[^manifest]
- **Dataset:** [datasets/gov/ntb/pacientu_valios_pareiskimai](../pacientu_valios_pareiskimai.md) (`datasets/gov/ntb/pacientu_valios_pareiskimai`)
- **Manifest CSV:** [datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntb/pacientu_valios_pareiskimai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ntb/pacientu_valios_pareiskimai/ValiosPareiskimas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tipas` | `string` | — | `4` | `open` | — | Paciento valios pareiškimo tipas | — |
| `uzpildymo_data` | `date` | `D` | `4` | `open` | — | Sutikimo užpildymo data | — |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Paciento amžiaus grupė | — |
| `lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `organo_pasirinkimo_tipas` | `string` | — | `4` | `open` | — | Audinių ir organų pasirinkimo tipas | Nurodo ryšį su susietais įrašais ‘SutikimuPoMirtiesOrganai’ lentelėje |
| `apskritis` | `ref` | [/datasets/gov/rc/ar/apskritis/Apskritis](../../rc/ar/apskritis/Apskritis.md) | `4` | `open` | — | Paciento gyvenamosios vietos apskritis | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Paciento gyvenamosios vietos savivaldybė | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/ntb/pacientu_valios_pareiskimai.csv
