---
type: Table
title: "Attribution — Viešojo transporto duomenų priskyrimai"
description: "Organizacijos, susijusios su viešojo transporto duomenų kūrimu, teikimu, priežiūra ar eksploatavimu."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/Attribution"
tags: [gov, ltsa, attribution, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L143"
    title: "atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L143"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1929/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ltsa/viesasis_transportas"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Attribution — Viešojo transporto duomenų priskyrimai

Organizacijos, susijusios su viešojo transporto duomenų kūrimu, teikimu, priežiūra ar eksploatavimu. GTFS formato duomenys iš Lietuvos transporto saugos administracijos VINTRA sistemos (https://www.visimarsrutai.lt/gtfs/)[^manifest]

- **Model:** `datasets/gov/ltsa/viesasis_transportas/Attribution`[^manifest]
- **Dataset:** [Lietuvos transporto saugos administracijos viešojo transporto kelionių duomenys](../viesasis_transportas.md) (`datasets/gov/ltsa/viesasis_transportas`)[^manifest]
- **Manifest CSV:** [datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L143](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L143)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/Attribution` (`deployed`)[^manifest]
- **Provider:** `ltsa` — Lietuvos transporto saugos administracija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-10-20`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L143 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L143)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ltsa/viesasis_transportas (https://data.gov.lt/datasets/1929/)
