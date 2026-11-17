---
type: Table
title: "Revise — Projekto patikros vietoje"
description: "Spinta table datasets/gov/finmin/kontroles_veiksmai/Revise (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/kontroles_veiksmai/Revise"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/kontroles_veiksmai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kontroles_veiksmai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Revise — Projekto patikros vietoje

- **Model:** `datasets/gov/finmin/kontroles_veiksmai/Revise`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų kontrolės veiksmų duomenys](../kontroles_veiksmai.md) (`datasets/gov/finmin/kontroles_veiksmai`)
- **Manifest CSV:** [datasets/gov/finmin/kontroles_veiksmai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kontroles_veiksmai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/kontroles_veiksmai/Revise`
- **Primary Key (`ref`):** `revise_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `revise_id` | `string` | — | `4` | `open` | — | Patikros vietoje identifikatorius | — |
| `project_hash_id` | `string` | — | `4` | `open` | — | Projekto pseudonimas | Jungimui tik šio rinkinio viduje |
| `number` | `string` | — | `4` | `open` | — | Patikros vietoje numeris | — |
| `from` | `date` | `D` | `4` | `open` | — | Patikros vietoje atlikimo data nuo | — |
| `till` | `date` | `D` | `4` | `open` | — | Patikros vietoje atlikimo data iki | — |
| `type` | `string` | — | `3` | `open` | — | Patikros vietoje tipas | — |
| `full` | `boolean` | — | `4` | `open` | — | Patikra vietoje atlikta pilna apimtimi | — |
| `correction_deadline` | `date` | `D` | `4` | `open` | — | Neatitikimų ištaisymo termino data | — |
| `correction_found` | `boolean` | — | `4` | `open` | — | Požymis, ar užfiksuota neatitikimų | — |
| `correction_fixed` | `date` | `D` | `4` | `open` | — | Neatitikimų ištaisymo data, jei neatitikimai ištaisyti | — |
| `state` | `string` | — | `3` | `open` | — | Patikros vietoje būsena | — |
| `state_updated` | `date` | `D` | `4` | `open` | — | Patikros vietoje būsenos data | — |
| `remark_types` | `string` | — | `2` | `open` | — | Pastebėjimų tipai | Kiekvieno atskiro pastebėjimo tipas atskirtas kabliataškiu |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `remark_types` | `"update(property: ""remark_types[]"", type: ""array"", source: ""Remark_types"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/kontroles_veiksmai.csv
