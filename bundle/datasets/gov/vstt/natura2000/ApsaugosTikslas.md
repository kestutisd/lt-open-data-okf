---
type: Table
title: "ApsaugosTikslas — Natura 2000 teritorijų apsaugos tikslų duomenys"
description: "Spinta table datasets/gov/vstt/natura2000/ApsaugosTikslas (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vstt/natura2000/ApsaugosTikslas"
tags: [gov, vstt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vstt/natura2000.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/natura2000.csv#L18"
    last_modified: "2026-11-11T14:39:20Z"
---

# ApsaugosTikslas — Natura 2000 teritorijų apsaugos tikslų duomenys

- **Model:** `datasets/gov/vstt/natura2000/ApsaugosTikslas`[^manifest]
- **Dataset:** [datasets/gov/vstt/natura2000](../natura2000.md) (`datasets/gov/vstt/natura2000`)
- **Manifest CSV:** [datasets/gov/vstt/natura2000.csv#L18](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/natura2000.csv#L18)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/natura2000/ApsaugosTikslas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `kodas` | `ref` | [/datasets/gov/vstt/teritorijos/BuveiniuApsaugaiSvarbiTeritorija[bast_kodas]](../teritorijos/BuveiniuApsaugaiSvarbiTeritorija.md) | `4` | `open` | — | Buveinės kodas | Buveinių apsaugai svarbios teritorijos kodas |
| `kodas.pavadinimas` | `string` | — | `4` | `open` | — | Pavadinimas | Buveinių apsaugai svarbios teritorijos pavadinimas |
| `rusis` | `string` | — | `4` | `open` | — | Rūšis | Rūšies lotyniškas pavadinimas |
| `buveine` | `string` | — | `4` | `open` | — | Buveinės pavadinimas | — |
| `tipas` | `string` | — | `4` | `open` | — | Buveinių ekosistemos grupė | — |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Geometrija | Geometrijos tipas, koordinačių sistemos kodas |
| `data` | `date` | `D` | `4` | `open` | — | Inventorizacijos data | — |
| `plotas` | `number` | `ha` | `4` | `open` | — | Plotas | Plotas hektarais |
| `bukle` | `string` | — | `4` | `open` | — | Vertybės būklė | — |
| `tikslas` | `string` | — | `4` | `open` | — | Vertybės išsaugojimo tikslas | — |
| `sluoksnis` | `string` | — | `4` | `open` | — | Sluoksnis | Geometrijos tipas, sluoksnis iš kurio suformuoti duomenys |
| `statusas` | `string` | — | `4` | `open` | — | Objekto teisinis statusas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/natura2000.csv
