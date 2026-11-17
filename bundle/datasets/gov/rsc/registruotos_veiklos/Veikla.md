---
type: Table
title: "Veikla — Registruota veikla su jonizuojančios spinduliuotės šaltiniais"
description: "Spinta table datasets/gov/rsc/registruotos_veiklos/Veikla (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rsc/registruotos_veiklos/Veikla"
tags: [gov, rsc, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rsc/registruotos_veiklos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/registruotos_veiklos.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Veikla — Registruota veikla su jonizuojančios spinduliuotės šaltiniais

- **Model:** `datasets/gov/rsc/registruotos_veiklos/Veikla`[^manifest]
- **Dataset:** [datasets/gov/rsc/registruotos_veiklos](../registruotos_veiklos.md) (`datasets/gov/rsc/registruotos_veiklos`)
- **Manifest CSV:** [datasets/gov/rsc/registruotos_veiklos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/registruotos_veiklos.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rsc/registruotos_veiklos/Veikla`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `leid_nr` | `string` | — | `4` | `open` | — | Registruotos veiklos numeris | — |
| `isduota` | `date` | `D` | `4` | `open` | — | Registruotos veiklos išdavimo data | — |
| `busena` | `string` | — | `4` | `open` | — | Registruotos veiklos būsena | — |
| `ja_kodas` | `string` | — | `2` | `open` | — | Juridinio asmens kodas | — |
| `org_pav` | `string` | — | `1` | `open` | — | Juridinio asmens pavadinimas | — |
| `adresas` | `string` | — | `2` | `open` | — | Pilnas adresas | — |
| `miesto_pozymis` | `boolean` | — | `4` | `open` | — | Miesto požymis | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |
| `salis` | `string` | — | `4` | `open` | — | Valstybės pavadinimas | — |
| `koord` | `geometry(point, 3346)` | — | `3` | `open` | — | Juridinio asmens koordinatės | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `busena` | `"Neregistruota"` | — | — | Neregistruota | — |
| `busena` | `"Registruota"` | — | — | Registruota | — |
| `busena` | `"Panaikintas registravimas"` | — | — | Panaikintas registravimas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ja_kodas` | `create(property: "ja_kodas", type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rsc/registruotos_veiklos.csv
