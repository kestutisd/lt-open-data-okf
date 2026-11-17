---
type: Table
title: "Ataskaita — Ataskaita"
description: "Spinta table datasets/gov/vaspvt/priemones/Ataskaita (16 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/priemones/Ataskaita"
tags: [gov, vaspvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/medicinos_iranga.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_iranga.csv#L352"
    last_modified: "2026-11-11T14:39:20Z"
---

# Ataskaita — Ataskaita

- **Model:** `datasets/gov/vaspvt/priemones/Ataskaita`[^manifest]
- **Dataset:** [Sveikatos priežiūros technologijų, susijusių su medicinos prietaisais, vertinimo ir valdymo duomenys](../priemones.md) (`datasets/gov/vaspvt/priemones`)
- **Manifest CSV:** [datasets/gov/vaspvt/medicinos_iranga.csv#L352](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_iranga.csv#L352)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/priemones/Ataskaita`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikacinis kodas | — |
| `tipas` | `string` | — | `4` | `open` | — | Ataskaitos tipas | — |
| `ketvirtine_ataskaita` | `string` | — | `4` | `open` | — | Ketvirčio ataskaita | — |
| `pusmecio_ataskaita` | `string` | — | `4` | `open` | — | Pusės metų ataskaita | — |
| `ataskaitos_nr` | `string` | — | `4` | `open` | — | Ataskaitos numeris | — |
| `istaigos_kodas` | `string` | — | `4` | `open` | — | Įstaigos kodas | — |
| `istaiga` | `string` | — | `4` | `open` | — | Įstaiga | — |
| `skyrius` | `string` | — | `4` | `open` | — | Naudojimo vieta | — |
| `miestas` | `string` | — | `4` | `open` | — | Miestas | — |
| `iregistruota` | `date` | `D` | `4` | `open` | — | Įregistruotas | — |
| `statuso_data` | `date` | `D` | `4` | `open` | — | Ataskaitos atnaujinimo data | — |
| `ataskaitos_data` | `date` | `D` | `4` | `open` | — | Ataskaitos priėmimo data | — |
| `audituota` | `date` | `D` | `4` | `open` | — | Audito data | — |
| `audito_pakeitimai` | `date` | `D` | `4` | `open` | — | Audito pakeitimai | — |
| `naudotojo_tipas` | `string` | — | `4` | `open` | — | Naudotojo tipas | — |
| `filialas` | `string` | — | `1` | `open` | — | Filialas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"1"` | — | — | Medicinos priemones | Darbo su medicinos priemonemis ataskaita |
| `tipas` | `"2"` | — | — | Priemoniu i6laidu ataskaita | Medicinos priemoniu islaidu ataskaita |
| `ketvirtine_ataskaita` | `"1"` | — | — | Pirmasis ketvirtis | — |
| `ketvirtine_ataskaita` | `"2"` | — | — | Antrasis ketvirtis | — |
| `ketvirtine_ataskaita` | `"3"` | — | — | Treciasis ketvirtis | — |
| `ketvirtine_ataskaita` | `"4"` | — | — | Ketvirtasis ketvirtis | — |
| `pusmecio_ataskaita` | `"1"` | — | — | Pirmasis pusmetis | — |
| `pusmecio_ataskaita` | `"2"` | — | — | Antrasis pusmetis | — |
| `naudotojo_tipas` | `"1"` | — | — | Vidinis | Ataskaitas tikrina VASPVT |
| `naudotojo_tipas` | `"2"` | — | — | Isorinis | Ataskaita teikia istaigu atstovai |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/medicinos_iranga.csv
