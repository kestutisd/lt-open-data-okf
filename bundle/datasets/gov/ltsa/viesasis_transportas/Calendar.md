---
type: Table
title: "Calendar — Viešojo transporto paslaugų tvarkaraščiai"
description: "Viešojo transporto tvarkaraščiai pagal savaitės dienas."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/Calendar"
tags: [gov, ltsa, calendar, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L68"
    title: "atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L68"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1929/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ltsa/viesasis_transportas"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Calendar — Viešojo transporto paslaugų tvarkaraščiai

Viešojo transporto tvarkaraščiai pagal savaitės dienas. GTFS formato duomenys iš Lietuvos transporto saugos administracijos VINTRA sistemos (https://www.visimarsrutai.lt/gtfs/)[^manifest]

- **Model:** `datasets/gov/ltsa/viesasis_transportas/Calendar`[^manifest]
- **Dataset:** [Lietuvos transporto saugos administracijos viešojo transporto kelionių duomenys](../viesasis_transportas.md) (`datasets/gov/ltsa/viesasis_transportas`)[^manifest]
- **Manifest CSV:** [datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L68](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L68)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/Calendar` (`deployed`)[^manifest]
- **Provider:** `ltsa` — Lietuvos transporto saugos administracija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `service_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-10-20`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L68 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L68)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ltsa/viesasis_transportas (https://data.gov.lt/datasets/1929/)
