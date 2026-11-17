---
type: Table
title: "GyvVietTaskas2010 — Gyvenamųjų vietovių taškiniai geoerdviniai duomenys\",\" remiantis visuotiniu žemės ūkių surašymu 2010 m."
description: "Spinta table datasets/gov/lsd/zemes_ukis/GyvVietTaskas2010 (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/zemes_ukis/GyvVietTaskas2010"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/zemes_ukio_surasymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/zemes_ukio_surasymai.csv#L17"
    last_modified: "2026-11-11T14:39:20Z"
---

# GyvVietTaskas2010 — Gyvenamųjų vietovių taškiniai geoerdviniai duomenys"," remiantis visuotiniu žemės ūkių surašymu 2010 m.

- **Model:** `datasets/gov/lsd/zemes_ukis/GyvVietTaskas2010`[^manifest]
- **Dataset:** [datasets/gov/lsd/zemes_ukis](../zemes_ukis.md) (`datasets/gov/lsd/zemes_ukis`)
- **Manifest CSV:** [datasets/gov/lsd/zemes_ukio_surasymai.csv#L17](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/zemes_ukio_surasymai.csv#L17)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/zemes_ukis/GyvVietTaskas2010`
- **Primary Key (`ref`):** `objectid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `geo_koord` | `geometry(point, 4326)` | `m` | `4` | `open` | — | Ūkio koordinatė (WGS84) | — |
| `sen_pav` | `string` | — | `2` | `open` | — | Seniūnijos pavadinimas | — |
| `kiauliu_sk` | `string` | — | `4` | `open` | — | Kiaulių skaičius seniūnijoje | — |
| `darbuot_sk` | `string` | — | `4` | `open` | — | Darbuotojų skaičius | — |
| `objectid` | `integer` | — | `4` | `open` | — | Objekto įdentifikatorius | — |
| `gyv_pav` | `string` | — | `2` | `open` | — | Gyvenvietės pavadinimas | — |
| `sav_pav` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |
| `galviju_sk` | `string` | — | `4` | `open` | — | Galvijų skaičius | — |
| `pauksc_sk` | `string` | — | `4` | `open` | — | Paukščių skaičius | — |
| `ariama_z` | `number` | — | `3` | `open` | — | Ariama žemė | — |
| `ukiu_sk` | `integer` | — | `4` | `open` | — | Ūkių skaičius | — |
| `znaudmenos` | `number` | — | `4` | `open` | — | Žemės naudmenos | — |
| `apskr_pav` | `string` | — | `2` | `open` | — | Apskrities pavadinimas | — |
| `karviu_sk` | `string` | — | `4` | `open` | — | Karvių skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/zemes_ukio_surasymai.csv
