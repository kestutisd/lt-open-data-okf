---
type: Table
title: "Calendar — Viešojo transporto paslaugų tvarkaraščiai"
description: "Viešojo transporto tvarkaraščiai pagal savaitės dienas."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/Calendar"
tags: [gov, ltsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L68"
    last_modified: "2026-11-11T14:39:20Z"
---

# Calendar — Viešojo transporto paslaugų tvarkaraščiai

Viešojo transporto tvarkaraščiai pagal savaitės dienas. GTFS formato duomenys iš Lietuvos transporto saugos administracijos VINTRA sistemos (https://www.visimarsrutai.lt/gtfs/)

- **Model:** `datasets/gov/ltsa/viesasis_transportas/Calendar`[^manifest]
- **Dataset:** [Lietuvos transporto saugos administracijos viešojo transporto kelionių duomenys](../viesasis_transportas.md) (`datasets/gov/ltsa/viesasis_transportas`)
- **Manifest CSV:** [datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L68](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L68)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/Calendar`
- **Primary Key (`ref`):** `service_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `service_id` | `string` | — | `4` | `open` | — | Paslaugos unikalus identifikatorius | — |
| `monday` | `boolean` | — | `4` | `open` | — | Ar paslauga veikia pirmadieniais (1 - taip, 0 - ne) | — |
| `tuesday` | `boolean` | — | `4` | `open` | — | Ar paslauga veikia antradieniais (1 - taip, 0 - ne) | — |
| `wednesday` | `boolean` | — | `4` | `open` | — | Ar paslauga veikia trečiadieniais (1 - taip, 0 - ne) | — |
| `thursday` | `boolean` | — | `4` | `open` | — | Ar paslauga veikia ketvirtadieniais (1 - taip, 0 - ne) | — |
| `friday` | `boolean` | — | `4` | `open` | — | Ar paslauga veikia penktadieniais (1 - taip, 0 - ne) | — |
| `saturday` | `boolean` | — | `4` | `open` | — | Ar paslauga veikia šeštadieniais (1 - taip, 0 - ne) | — |
| `sunday` | `boolean` | — | `4` | `open` | — | Ar paslauga veikia sekmadieniais (1 - taip, 0 - ne) | — |
| `start_date` | `date` | `D` | `4` | `open` | — | Paslaugos pradžios data | — |
| `end_date` | `date` | `D` | `4` | `open` | — | Paslaugos pabaigos data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv
