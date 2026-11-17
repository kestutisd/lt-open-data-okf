---
type: Table
title: "Agency — Viešojo transporto paslaugų teikėjai"
description: "Viešojo transporto operatorių (autobusų, traukinių) duomenys."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/Agency"
tags: [gov, ltsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L58"
    last_modified: "2026-11-11T14:39:20Z"
---

# Agency — Viešojo transporto paslaugų teikėjai

Viešojo transporto operatorių (autobusų, traukinių) duomenys. GTFS formato duomenys iš Lietuvos transporto saugos administracijos VINTRA sistemos (https://www.visimarsrutai.lt/gtfs/)

- **Model:** `datasets/gov/ltsa/viesasis_transportas/Agency`[^manifest]
- **Dataset:** [Lietuvos transporto saugos administracijos viešojo transporto kelionių duomenys](../viesasis_transportas.md) (`datasets/gov/ltsa/viesasis_transportas`)
- **Manifest CSV:** [datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L58](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L58)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/Agency`
- **Primary Key (`ref`):** `agency_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `agency_id` | `string` | — | `3` | `open` | — | Agentūros unikalus identifikatorius | — |
| `agency_name` | `string` | — | `3` | `open` | — | Agentūros pavadinimas | — |
| `agency_url` | `string` | — | `4` | `open` | — | Agentūros svetainės URL | — |
| `agency_timezone` | `string` | — | `4` | `open` | — | Agentūros laiko juosta | — |
| `agency_lang` | `string` | — | `4` | `open` | — | Agentūros kalbos kodas ISO 639-1 formatu | — |
| `agency_phone` | `string` | — | `4` | `open` | — | Agentūros telefono numeris | — |
| `agency_fare_url` | `string` | — | `4` | `open` | — | Bilietų kainos informacijos svetainės URL | — |
| `agency_email` | `string` | — | `4` | `open` | — | Agentūros kontaktinis el. paštas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv
