---
type: Table
title: "SenGeoDuom2010 — Seniūnijų taškiniai geoerdviniai duomenys\",\" remiantis visuotiniu žemės ūkių sura"
description: "Spinta table datasets/gov/lsd/zemes_ukis/SenGeoDuom2010 (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/zemes_ukis/SenGeoDuom2010"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/zemes_ukio_surasymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/zemes_ukio_surasymai.csv#L47"
    last_modified: "2026-11-11T14:39:20Z"
---

# SenGeoDuom2010 — Seniūnijų taškiniai geoerdviniai duomenys"," remiantis visuotiniu žemės ūkių sura

- **Model:** `datasets/gov/lsd/zemes_ukis/SenGeoDuom2010`[^manifest]
- **Dataset:** [datasets/gov/lsd/zemes_ukis](../zemes_ukis.md) (`datasets/gov/lsd/zemes_ukis`)
- **Manifest CSV:** [datasets/gov/lsd/zemes_ukio_surasymai.csv#L47](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/zemes_ukio_surasymai.csv#L47)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/zemes_ukis/SenGeoDuom2010`
- **Primary Key (`ref`):** `objectid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `geo_koord` | `geometry(point, 4326)` | `m` | `4` | `open` | — | Ūkio koordinatė (WGS84) | — |
| `objectid` | `integer` | — | `4` | `open` | — | Objekto įdentifikatorius | — |
| `sav_pav` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |
| `sen_pav` | `string` | — | `2` | `open` | — | Seniūnijos pavadinimas | — |
| `galviju_sk` | `string` | — | `4` | `open` | — | Galvijų skaičius | — |
| `pauksc_sk` | `string` | — | `4` | `open` | — | Paukščių skaičius | — |
| `ariama_z` | `number` | — | `3` | `open` | — | Ariama žemė | — |
| `ukiu_sk` | `integer` | — | `4` | `open` | — | Ūkių skaičius | — |
| `znaudmenos` | `number` | — | `4` | `open` | — | Žemės naudmenos | — |
| `apskr_pav` | `string` | — | `2` | `open` | — | Apskrities pavadinimas | — |
| `kiauliu_sk` | `string` | — | `4` | `open` | — | Kiaulių skaičius | — |
| `darbuot_sk` | `string` | — | `4` | `open` | — | Darbuotojų skaičius | — |
| `karviu_sk` | `string` | — | `4` | `open` | — | Karvių skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/zemes_ukio_surasymai.csv
