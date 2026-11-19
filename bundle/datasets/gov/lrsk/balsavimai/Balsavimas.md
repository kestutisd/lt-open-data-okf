---
type: Table
title: "Balsavimas — Balsavimai"
description: "Spinta table datasets/gov/lrsk/balsavimai/Balsavimas (18 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/balsavimai/Balsavimas"
tags: [gov, lrsk, balsavimas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/balsavimai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/lrsk/balsavimai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/6101/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrsk/balsavimai"
    author: "team:vda"
    last_modified: "2026-10-27T00:00:00Z"
---

# Balsavimas — Balsavimai

- **Model:** `datasets/gov/lrsk/balsavimai/Balsavimas`[^manifest]
- **Dataset:** [Balsavimai](../balsavimai.md) (`datasets/gov/lrsk/balsavimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lrsk/balsavimai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/balsavimai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/balsavimai/Balsavimas` (`deployed`)[^manifest]
- **Provider:** `lrsk` — Lietuvos Respublikos Seimo Kanceliarija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `balsavimo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-10-27`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `balsavimo_id` | `string` | — | `4` | `open` | — | Balsavimo identifikatorius | — |
| `kadencijos_id` | `string` | — | `4` | `open` | — | Kadencijos identifikatorius | — |
| `sesijos_id` | `string` | — | `4` | `open` | — | Sesijos identifikatorius | — |
| `sesija` | `string` | — | `4` | `open` | — | Sesija | — |
| `posedzio_tipas` | `string` | — | `4` | `open` | — | Posėdžio tipas | — |
| `posedzio_nr` | `integer` | — | `4` | `open` | — | Posėdžio numeris | — |
| `balsavimo_pradzia` | `datetime` | `S` | `4` | `open` | — | Balsavimo pradžios data ir laikas | — |
| `balsavimo_pabaiga` | `datetime` | `S` | `4` | `open` | — | Balsavimo pabaigos data ir laikas | — |
| `klausimo_nr` | `string` | — | `4` | `open` | — | Klausimo numeris | — |
| `darb_klausimas` | `string` | — | `4` | `open` | — | Darbotvarkės klausimas | — |
| `balsavimo_tipas` | `string` | — | `4` | `open` | — | Balsavimo tipas | — |
| `balsavimo_klausimas` | `string` | — | `4` | `open` | — | Balsavimo klausimas | — |
| `balsavimo_klausimas_alt` | `string` | — | `4` | `open` | — | Alternatyvus balsavimo klausimas | — |
| `suvestine` | `string` | — | `4` | `open` | — | Suvestinė | — |
| `uz` | `integer` | — | `4` | `open` | — | Balsų „už“ skaičius | — |
| `pries` | `integer` | — | `4` | `open` | — | Balsų „prieš“ skaičius | — |
| `susilaike` | `integer` | — | `4` | `open` | — | Susilaikiusių skaičius | — |
| `verdiktas` | `string` | — | `4` | `open` | — | Verdiktas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/balsavimai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/balsavimai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrsk/balsavimai (https://data.gov.lt/datasets/6101/)
