---
type: Table
title: "CalendarDate — Viešojo transporto išimtinės paslaugų datos"
description: "Viešojo transporto išimtinės paslaugų datos (pridėtos ar atšauktos, pvz., šventinės dienos)."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/CalendarDate"
tags: [gov, ltsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L28"
    last_modified: "2026-11-11T14:39:20Z"
---

# CalendarDate — Viešojo transporto išimtinės paslaugų datos

Viešojo transporto išimtinės paslaugų datos (pridėtos ar atšauktos, pvz., šventinės dienos). GTFS formato duomenys iš Lietuvos transporto saugos administracijos VINTRA sistemos (https://www.visimarsrutai.lt/gtfs/)

- **Model:** `datasets/gov/ltsa/viesasis_transportas/CalendarDate`[^manifest]
- **Dataset:** [Lietuvos transporto saugos administracijos viešojo transporto kelionių duomenys](../viesasis_transportas.md) (`datasets/gov/ltsa/viesasis_transportas`)
- **Manifest CSV:** [datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L28](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L28)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/CalendarDate`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros unikalus įrašo identifikatorius | — |
| `service_id` | `string` | — | `4` | `open` | — | Paslaugos unikalus identifikatorius | — |
| `date` | `date` | `D` | `4` | `open` | — | Išimties data | — |
| `exception_type` | `string` | — | `4` | `open` | — | Išimties tipas (1 - pridėta paslauga, 2 - atšaukta paslauga) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv
