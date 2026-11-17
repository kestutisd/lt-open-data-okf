---
type: Table
title: "Shape — Viešojo transporto maršrutų geografinės trajektorijos"
description: "Viešojo transporto maršrutų geografinės trajektorijos (linijos žemėlapyje)."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/Shape"
tags: [gov, ltsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L50"
    last_modified: "2026-11-11T14:39:20Z"
---

# Shape — Viešojo transporto maršrutų geografinės trajektorijos

Viešojo transporto maršrutų geografinės trajektorijos (linijos žemėlapyje). GTFS formato duomenys iš Lietuvos transporto saugos administracijos VINTRA sistemos (https://www.visimarsrutai.lt/gtfs/)

- **Model:** `datasets/gov/ltsa/viesasis_transportas/Shape`[^manifest]
- **Dataset:** [Lietuvos transporto saugos administracijos viešojo transporto kelionių duomenys](../viesasis_transportas.md) (`datasets/gov/ltsa/viesasis_transportas`)
- **Manifest CSV:** [datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L50](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L50)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/Shape`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros unikalus įrašo identifikatorius | — |
| `shape_id` | `string` | — | `4` | `open` | — | Maršruto formos identifikatorius | — |
| `shape_pt_sequence` | `integer` | — | `4` | `open` | — | Maršruto taškų seka | — |
| `shape_pt_lat` | `number` | — | `4` | `open` | — | Maršruto formos taško platuma | — |
| `shape_pt_lon` | `number` | — | `4` | `open` | — | Maršruto formos taško ilguma | — |
| `shape_dist_traveled` | `number` | — | `4` | `open` | — | Atstumas nuo maršruto pradžios iki taško | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv
