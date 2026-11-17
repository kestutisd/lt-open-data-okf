---
type: Table
title: "Attribution — Viešojo transporto duomenų priskyrimai"
description: "Organizacijos, susijusios su viešojo transporto duomenų kūrimu, teikimu, priežiūra ar eksploatavimu."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/Attribution"
tags: [gov, ltsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L143"
    last_modified: "2026-11-11T14:39:20Z"
---

# Attribution — Viešojo transporto duomenų priskyrimai

Organizacijos, susijusios su viešojo transporto duomenų kūrimu, teikimu, priežiūra ar eksploatavimu. GTFS formato duomenys iš Lietuvos transporto saugos administracijos VINTRA sistemos (https://www.visimarsrutai.lt/gtfs/)

- **Model:** `datasets/gov/ltsa/viesasis_transportas/Attribution`[^manifest]
- **Dataset:** [Lietuvos transporto saugos administracijos viešojo transporto kelionių duomenys](../viesasis_transportas.md) (`datasets/gov/ltsa/viesasis_transportas`)
- **Manifest CSV:** [datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L143](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L143)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/Attribution`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `agency_id` | `string` | — | `4` | `open` | — | Nurodo, kad ši atribucija taikoma konkrečiai transporto agentūrai | — |
| `route_id` | `string` | — | `4` | `open` | — | Nurodo, kad atribucija taikoma konkrečiam maršrutui | — |
| `id` | `string` | — | `4` | `open` | — | Unikalus atribucijos identifikatorius. Naudojamas, kai norima išskirti atskiras atribucijas ar versti jų pavadinimus | — |
| `trip_id` | `string` | — | `4` | `open` | — | Nurodo, kad atribucija taikoma konkrečiam reisui | — |
| `organization_name` | `string` | — | `3` | `open` | — | Organizacijos pavadinimas, kuriam taikoma atribucija. Privalomas, nes tai pagrindinė informacija apie subjektą | — |
| `is_producer` | `boolean` | — | `4` | `open` | — | Žymi, ar organizacija yra duomenų gamintojas (parengė GTFS rinkinį) | — |
| `is_operator` | `boolean` | — | `4` | `open` | — | Žymi, ar organizacija yra transporto operatorius (faktiškai vykdo transporto paslaugas) | — |
| `is_authority` | `boolean` | — | `4` | `open` | — | Žymi, ar organizacija yra viešojo transporto reguliavimo, planavimo ar administravimo institucija | — |
| `attribution_url` | `string` | — | `4` | `open` | — | Organizacijos tinklalapio adresas. Naudojama dokumentacijai, licencijoms ar viešinimo taisyklėms | — |
| `attribution_email` | `string` | — | `4` | `open` | — | Kontaktinis organizacijos el. paštas | — |
| `attribution_phone` | `string` | — | `2` | `open` | — | Kontaktinis organizacijos telefono numeris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv
