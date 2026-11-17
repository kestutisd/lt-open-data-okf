---
type: Table
title: "Trip — Viešojo transporto reisai"
description: "Viešojo transporto konkretūs reisai pagal maršrutus, kryptis ir tvarkaraščius."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/Trip"
tags: [gov, ltsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L80"
    last_modified: "2026-11-11T14:39:20Z"
---

# Trip — Viešojo transporto reisai

Viešojo transporto konkretūs reisai pagal maršrutus, kryptis ir tvarkaraščius. GTFS formato duomenys iš Lietuvos transporto saugos administracijos VINTRA sistemos (https://www.visimarsrutai.lt/gtfs/)

- **Model:** `datasets/gov/ltsa/viesasis_transportas/Trip`[^manifest]
- **Dataset:** [Lietuvos transporto saugos administracijos viešojo transporto kelionių duomenys](../viesasis_transportas.md) (`datasets/gov/ltsa/viesasis_transportas`)
- **Manifest CSV:** [datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L80](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L80)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/Trip`
- **Primary Key (`ref`):** `trip_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `route_id` | `string` | — | `4` | `open` | — | Maršruto identifikatorius | — |
| `note_id` | `string` | — | `4` | `open` | — | Nuoroda į pastabų lentelę, suteikianti papildomą informaciją apie reisą | — |
| `trip_id` | `string` | — | `4` | `open` | — | Kelionės unikalus identifikatorius | — |
| `service_id` | `string` | — | `4` | `open` | — | Paslaugos identifikatorius | — |
| `trip_short_name` | `string` | — | `4` | `open` | — | Trumpas kelionės pavadinimas | — |
| `trip_headsign` | `string` | — | `4` | `open` | — | Kelionės kryptis | — |
| `direction_id` | `string` | — | `4` | `open` | — | Reiso kryptis: 0 - pirmyn (arba pagal laikrodžio rodyklę), 1 - atgal (arba prieš laikrodžio rodyklę) | — |
| `block_id` | `string` | — | `4` | `open` | — | Bloko ID, nurodantis reisų seką, kurią aptarnauja ta pati transporto priemonė | — |
| `shape_id` | `string` | — | `4` | `open` | — | Maršruto formos identifikatorius | — |
| `wheelchair_accessible` | `string` | — | `4` | `open` | — | Pritaikymas neįgaliesiems: 0 - nėra informacijos, 1 - pritaikyta, 2 - nepritaikyta | — |
| `bikes_allowed` | `string` | — | `4` | `open` | — | Dviračių leidimas: 0 - nėra informacijos, 1 - leidžiama, 2 - neleidžiama | — |
| `mean_duration_factor` | `string` | — | `4` | `open` | — | Vidutinės kelionės trukmės korekcijos koeficientas | — |
| `mean_duration_offset` | `string` | — | `4` | `open` | — | Vidutinės kelionės trukmės korekcijos poslinkis sekundėmis | — |
| `safe_duration_factor` | `string` | — | `4` | `open` | — | Saugios kelionės trukmės korekcijos koeficientas | — |
| `safe_duration_offset` | `string` | — | `4` | `open` | — | Saugios kelionės trukmės korekcijos poslinkis sekundėmis | — |
| `cars_allowed` | `string` | — | `4` | `open` | — | Indikatorius, ar reise leidžiama gabenti automobilius | — |
| `peak_offpeak` | `string` | — | `4` | `open` | — | Indikatorius, ar reisas priklauso piko ar ne piko laikui | — |
| `mta_trip_id` | `string` | — | `4` | `open` | — | Reiso identifikatorius pagal MTA sistemą | — |
| `boarding_type` | `string` | — | `4` | `open` | — | Apibrėžia, kaip vykdomas įlaipinimas reise | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv
