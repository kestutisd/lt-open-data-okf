---
type: Table
title: "Stop — Viešojo transporto sustojimo taškai"
description: "Viešojo transporto sustojimo taškų (stotelių, stočių) duomenys su pavadinimais ir koordinatėmis."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/Stop"
tags: [gov, ltsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L101"
    last_modified: "2026-11-11T14:39:20Z"
---

# Stop — Viešojo transporto sustojimo taškai

Viešojo transporto sustojimo taškų (stotelių, stočių) duomenys su pavadinimais ir koordinatėmis. GTFS formato duomenys iš Lietuvos transporto saugos administracijos VINTRA sistemos (https://www.visimarsrutai.lt/gtfs/)

- **Model:** `datasets/gov/ltsa/viesasis_transportas/Stop`[^manifest]
- **Dataset:** [Lietuvos transporto saugos administracijos viešojo transporto kelionių duomenys](../viesasis_transportas.md) (`datasets/gov/ltsa/viesasis_transportas`)
- **Manifest CSV:** [datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L101](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L101)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/Stop`
- **Primary Key (`ref`):** `stop_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `stop_id` | `string` | — | `4` | `open` | — | Stotelės unikalus identifikatorius | — |
| `stop_name` | `string` | — | `4` | `open` | — | Stotelės pavadinimas | — |
| `stop_lat` | `number` | — | `4` | `open` | — | Stotelės platuma | — |
| `stop_lon` | `number` | — | `4` | `open` | — | Stotelės ilguma | — |
| `stop_code` | `string` | — | `4` | `open` | — | Stotelės kodas | — |
| `stop_desc` | `string` | — | `4` | `open` | — | Stotelės aprašymas | — |
| `zone_id` | `string` | — | `4` | `open` | — | Zonos, kurioje yra stotelė, ID | — |
| `stop_url` | `string` | — | `3` | `open` | — | Stotelės svetainės URL | — |
| `location_type` | `string` | — | `4` | `open` | — | Vietos tipas: 0 - stotelė, 1 - stotis, 2 - įėjimas/išėjimas, 3 - mazgas, 4 - įlaipinimo platforma | — |
| `parent_station` | `string` | — | `4` | `open` | — | Pagrindinė stotelė, su kuria yra susijusi stotelė | — |
| `wheelchair_boarding` | `string` | — | `4` | `open` | — | Pritaikymas neįgaliesiems: 0 - nėra informacijos, 1 - pritaikyta, 2 - nepritaikyta | — |
| `stop_timezone` | `string` | — | `4` | `open` | — | Stotelės laiko juosta | — |
| `vehicle_type` | `string` | — | `4` | `open` | — | Transporto priemonės tipas, aptarnaujantis stotelę | — |
| `platform_code` | `string` | — | `4` | `open` | — | Perono kodas, naudojamas nurodyti, iš kurio perono vyksta išvykimai | — |
| `level_id` | `string` | — | `4` | `open` | — | Aukšto (lygmens) ID, kuriame yra ši vieta | — |
| `mta_stop_id` | `string` | — | `4` | `open` | — | Stotelės identifikatorius pagal MTA (Metropolitan Transportation Authority) sistemą | — |
| `regional_fare_card` | `string` | — | `4` | `open` | — | Indikatorius, ar stotelė priklauso regioninei bilietų sistemai | — |
| `tts_stop_name` | `string` | — | `4` | `open` | — | Stotelės pavadinimo versija, skirta automatinio perskaitymo sistemoms (tekstą į kalbą) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv
