---
type: Table
title: "FareAttribute — Viešojo transporto bilietų kainos"
description: "Viešojo transporto bilietų kainos, valiuta ir persėdimų taisyklės."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/FareAttribute"
tags: [gov, ltsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L11"
    last_modified: "2026-11-11T14:39:20Z"
---

# FareAttribute — Viešojo transporto bilietų kainos

Viešojo transporto bilietų kainos, valiuta ir persėdimų taisyklės. GTFS formato duomenys iš Lietuvos transporto saugos administracijos VINTRA sistemos (https://www.visimarsrutai.lt/gtfs/)

- **Model:** `datasets/gov/ltsa/viesasis_transportas/FareAttribute`[^manifest]
- **Dataset:** [Lietuvos transporto saugos administracijos viešojo transporto kelionių duomenys](../viesasis_transportas.md) (`datasets/gov/ltsa/viesasis_transportas`)
- **Manifest CSV:** [datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L11](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L11)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/FareAttribute`
- **Primary Key (`ref`):** `fare_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `agency_id` | `string` | — | `4` | `open` | — | Agentūros ID, kuriai taikomas šis tarifas | — |
| `fare_id` | `string` | — | `4` | `open` | — | Unikalus tarifo (bilieto) identifikatorius | — |
| `price` | `number` | — | `4` | `open` | — | Bilieto kaina | — |
| `currency_type` | `string` | — | `4` | `open` | — | Valiutos kodas ISO 4217 formatu (pvz., EUR) | — |
| `payment_method` | `string` | — | `4` | `open` | — | Mokėjimo metodas: 0 - mokama transporto priemonėje, 1 - mokama iš anksto | — |
| `transfers` | `integer` | — | `4` | `open` | — | Leidžiamų persėdimų skaičius: 0 - negalimi, 1 - vienas, 2 - du, tuščia - neriboti | — |
| `transfer_duration` | `integer` | — | `4` | `open` | — | Persėdimo galiojimo trukmė sekundėmis​. Nurodo, kiek laiko (nuo pirmo važiavimo pradžios) galioja persėdimai su šiuo bilietu | — |
| `journey_duration` | `integer` | — | `4` | `open` | — | Kelionės galiojimo trukmė sekundėmis​. Nurodo, kiek laiko galioja kelionė su šiuo bilietu | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv
