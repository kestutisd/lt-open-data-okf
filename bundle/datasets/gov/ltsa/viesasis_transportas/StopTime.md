---
type: Table
title: "StopTime — Viešojo transporto sustojimų laikai ir seka"
description: "Viešojo transporto sustojimų laikai ir jų seka kiekvienam maršruto reisui."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/StopTime"
tags: [gov, ltsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L121"
    last_modified: "2026-11-11T14:39:20Z"
---

# StopTime — Viešojo transporto sustojimų laikai ir seka

Viešojo transporto sustojimų laikai ir jų seka kiekvienam maršruto reisui. GTFS formato duomenys iš Lietuvos transporto saugos administracijos VINTRA sistemos (https://www.visimarsrutai.lt/gtfs/)

- **Model:** `datasets/gov/ltsa/viesasis_transportas/StopTime`[^manifest]
- **Dataset:** [Lietuvos transporto saugos administracijos viešojo transporto kelionių duomenys](../viesasis_transportas.md) (`datasets/gov/ltsa/viesasis_transportas`)
- **Manifest CSV:** [datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L121](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L121)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/StopTime`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros unikalus įrašo identifikatorius | — |
| `pickup_booking_rule_id` | `string` | — | `4` | `open` | — | Įlaipinimo užsakymo taisyklės ID | — |
| `drop_off_booking_rule_id` | `string` | — | `4` | `open` | — | Išlaipinimo užsakymo taisyklės ID | — |
| `note_id` | `string` | — | `4` | `open` | — | Nuoroda į pastabų lentelę, suteikianti papildomą informaciją apie reisą | — |
| `trip_id` | `string` | — | `4` | `open` | — | Kelionės unikalus identifikatorius | — |
| `stop_id` | `string` | — | `4` | `open` | — | Stotelės identifikatorius, kurioje įvyksta atvykimas ar išvykimas | — |
| `location_id` | `string` | — | `4` | `open` | — | Unikalus vietos ID, naudojamas stotelių grupavimui ar alternatyvioms vietoms nurodyti | — |
| `location_group_id` | `string` | — | `4` | `open` | — | ID, jungiantis kelias susijusias vietas į grupę | — |
| `arrival_time` | `string` | — | `4` | `open` | — | Atvykimo laikas formatu HH:MM:SS | — |
| `departure_time` | `string` | — | `4` | `open` | — | Išvykimo laikas formatu HH:MM:SS | — |
| `start_pickup_drop_off_window` | `string` | — | `4` | `open` | — | Laiko intervalo pradžia, kai leidžiamas įlaipinimas ar išlaipinimas | — |
| `end_pickup_drop_off_window` | `string` | — | `4` | `open` | — | Laiko intervalo pabaiga, kai leidžiamas įlaipinimas ar išlaipinimas | — |
| `timepoint` | `string` | — | `4` | `open` | — | Laiko tikslumas: 1 - tikslus, 0 - apytikslis | — |
| `stop_sequence` | `integer` | — | `4` | `open` | — | Stotelės seka maršrute | — |
| `stop_headsign` | `string` | — | `4` | `open` | — | Stotelės kryptis | — |
| `pickup_type` | `string` | — | `4` | `open` | — | Įlaipinimo tipas: 0 - reguliarus, 1 - nėra įlaipinimo, 2 - reikia užsakyti, 3 - susitarti su vairuotoju | — |
| `drop_off_type` | `string` | — | `4` | `open` | — | Išlaipinimo tipas: 0 - reguliarus, 1 - nėra išlaipinimo, 2 - reikia užsakyti, 3 - susitarti su vairuotoju | — |
| `shape_dist_traveled` | `string` | — | `4` | `open` | — | Atstumas nuo kelionės pradžios iki stotelės | — |
| `continuous_pickup` | `string` | — | `4` | `open` | — | Nenurodyto (nenustatyto grafike) įlaipinimo galimybė po šios stotelės iki kitos​(0 – galima įlipti bet kurioje maršruto vietoje tarp šios ir kitos stotelės, 1 arba tuščia – negalima (tik stotelėse), 2 – galima įlipti tarp stotelių, bet būtina paskambinti iš anksto, 3 – galima, bet reikia susitarti su vairuotoju iš anksto​) | — |
| `continuous_drop_off` | `string` | — | `4` | `open` | — | Nenurodyto išlaipinimo galimybė nuo šios stotelės iki kitos | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv
