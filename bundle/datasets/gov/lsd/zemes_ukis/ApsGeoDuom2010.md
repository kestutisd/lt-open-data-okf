---
type: Table
title: "ApsGeoDuom2010 — Apskričių taškiniai geoerdviniai duomenys\",\" remiantis visuotiniu žemės ūkių surašymu 2010 m."
description: "Spinta table datasets/gov/lsd/zemes_ukis/ApsGeoDuom2010 (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/zemes_ukis/ApsGeoDuom2010"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/zemes_ukio_surasymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/zemes_ukio_surasymai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# ApsGeoDuom2010 — Apskričių taškiniai geoerdviniai duomenys"," remiantis visuotiniu žemės ūkių surašymu 2010 m.

- **Model:** `datasets/gov/lsd/zemes_ukis/ApsGeoDuom2010`[^manifest]
- **Dataset:** [datasets/gov/lsd/zemes_ukis](../zemes_ukis.md) (`datasets/gov/lsd/zemes_ukis`)
- **Manifest CSV:** [datasets/gov/lsd/zemes_ukio_surasymai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/zemes_ukio_surasymai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/zemes_ukis/ApsGeoDuom2010`
- **Primary Key (`ref`):** `objectid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `geo_koord` | `geometry(point, 4326)` | `m` | `4` | `open` | — | Ūkio koordinatė (WGS84) | — |
| `galviju_sk` | `integer` | — | `4` | `open` | — | Galvijų skaičius | — |
| `pauksc_sk` | `integer` | — | `4` | `open` | — | Paukščių skaičius | — |
| `ariama_z` | `number` | — | `3` | `open` | — | Ariama žemė | — |
| `ukiu_sk` | `integer` | — | `4` | `open` | — | Ūkių skaičius | — |
| `znaudmenos` | `integer` | — | `4` | `open` | — | Žemės naudmenos | — |
| `apskr_pav` | `string` | — | `2` | `open` | — | Apskrities pavadinimas | — |
| `kiauliu_sk` | `integer` | — | `4` | `open` | — | Kiaulių skaičius apskrityje | — |
| `darbuot_sk` | `integer` | — | `4` | `open` | — | Darbuotojų skaičius apskrityje | — |
| `karviu_sk` | `integer` | — | `4` | `open` | — | Karvių skaičius apskrityje | — |
| `objectid` | `integer` | — | `4` | `open` | — | Objekto įdentifikatorius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/zemes_ukio_surasymai.csv
