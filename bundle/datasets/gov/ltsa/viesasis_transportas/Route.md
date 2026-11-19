---
type: Table
title: "Route — Viešojo transporto maršrutai"
description: "Viešojo transporto maršrutų informacija, linijų pavadinimai ir tipai (autobusai, traukiniai)."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/Route"
tags: [gov, ltsa, route, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L34"
    title: "atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L34"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1929/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ltsa/viesasis_transportas"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Route — Viešojo transporto maršrutai

Viešojo transporto maršrutų informacija, linijų pavadinimai ir tipai (autobusai, traukiniai). GTFS formato duomenys iš Lietuvos transporto saugos administracijos VINTRA sistemos (https://www.visimarsrutai.lt/gtfs/)[^manifest]

- **Model:** `datasets/gov/ltsa/viesasis_transportas/Route`[^manifest]
- **Dataset:** [Lietuvos transporto saugos administracijos viešojo transporto kelionių duomenys](../viesasis_transportas.md) (`datasets/gov/ltsa/viesasis_transportas`)[^manifest]
- **Manifest CSV:** [datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L34](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L34)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/Route` (`deployed`)[^manifest]
- **Provider:** `ltsa` — Lietuvos transporto saugos administracija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `route_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-10-20`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `agency_id` | `string` | — | `4` | `open` | — | Agentūros, kuriai priklauso maršrutas, ID | — |
| `route_id` | `string` | — | `4` | `open` | — | Maršruto unikalus identifikatorius | — |
| `route_short_name` | `string` | — | `4` | `open` | — | Trumpoji maršruto pavadinimo forma | — |
| `route_long_name` | `string` | — | `3` | `open` | — | Pilnas maršruto pavadinimas | — |
| `route_type` | `string` | — | `4` | `open` | — | Transporto tipo kodas: 0 - tramvajus, 1 - metro, 2 - traukinys, 3 - autobusas, 4 - keltai, 5 - troleibusas | — |
| `route_desc` | `string` | — | `3` | `open` | — | Maršruto aprašymas | — |
| `route_url` | `string` | — | `3` | `open` | — | Maršruto svetainės URL | — |
| `route_color` | `string` | — | `4` | `open` | — | Maršruto spalvos šešioliktainis kodas (be #, pvz., FF0000) | — |
| `route_text_color` | `string` | — | `4` | `open` | — | Teksto spalvos šešioliktainis kodas maršruto fone | — |
| `network_id` | `string` | — | `4` | `open` | — | Tinklo identifikatorius, grupuojantis kelis maršrutus | — |
| `eligibility_restricted` | `string` | — | `4` | `open` | — | Indikatorius, ar maršrutas skirtas tik tam tikroms keleivių grupėms (pvz., studentams, senjorams) | — |
| `bikes_allowed` | `string` | — | `4` | `open` | — | Pažymi, ar konkrečiame maršrute leidžiama vežtis dviračius | — |
| `route_sort_order` | `integer` | — | `4` | `open` | — | Nustato, kokia tvarka maršrutai turi būti pateikiami naudotojo sąsajoje (mažesnės vertės rodomos pirmiau) | — |
| `regional_fare_card` | `string` | — | `4` | `open` | — | Indikatorius, ar maršrutui taikoma regioninė bilietų sistema | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L34 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L34)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ltsa/viesasis_transportas (https://data.gov.lt/datasets/1929/)
