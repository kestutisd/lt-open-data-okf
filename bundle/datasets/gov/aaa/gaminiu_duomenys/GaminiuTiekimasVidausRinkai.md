---
type: Table
title: "GaminiuTiekimasVidausRinkai — Gaminių tiekimo vidaus rinkai apskaitos duomenys"
description: "Spinta table datasets/gov/aaa/gaminiu_duomenys/GaminiuTiekimasVidausRinkai (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/gaminiu_duomenys/GaminiuTiekimasVidausRinkai"
tags: [gov, aaa, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/gaminiu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/gaminiu_duomenys.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# GaminiuTiekimasVidausRinkai — Gaminių tiekimo vidaus rinkai apskaitos duomenys

- **Model:** `datasets/gov/aaa/gaminiu_duomenys/GaminiuTiekimasVidausRinkai`[^manifest]
- **Dataset:** [datasets/gov/aaa/gaminiu_duomenys](../gaminiu_duomenys.md) (`datasets/gov/aaa/gaminiu_duomenys`)
- **Manifest CSV:** [datasets/gov/aaa/gaminiu_duomenys.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/gaminiu_duomenys.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/gaminiu_duomenys/GaminiuTiekimasVidausRinkai`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilės nr. | — |
| `metai` | `date` | `Y` | `4` | `open` | — | Metai | — |
| `srautas` | `string` | — | `2` | `open` | — | Gaminių srautas | Pagal Gamintojų ir importuotojų registravimo taisyklių, patvirtintų Lietuvos Respublikos aplinkos ministro 2009-05-27 Nr. D1-291, priedą. Apibrėžta gaminių srautų klasifikacija naudojama ir Vieningos gaminių, pakuočių ir atliekų apskaitos informacinėje sistemoje (GPAIS). |
| `rusis` | `string` | — | `2` | `open` | — | Gaminio rūšis | Pagal Gamintojų ir importuotojų registravimo taisyklių, patvirtintų Lietuvos Respublikos aplinkos ministro 2009-05-27 Nr. D1-291, priedą. Apibrėžta gaminių rūšių klasifikacija naudojama ir Vieningos gaminių, pakuočių ir atliekų apskaitos informacinėje sistemoje (GPAIS). |
| `imoniu_sk` | `integer` | `U` | `4` | `open` | — | Įmonių, pateikusių ataskaitas, skaičius, vnt. | Skaičiuojamos įmonės, kurios GPAIS patvirtino ketvirčių suvestines, kurių metinės ataskaitos yra suformuotos ar vertinamos bei įmonės, pateikusios VMI deklaracijas FR0523 |
| `kiekis` | `integer` | `t` | `4` | `open` | — | Patiekta vidaus rinkai, t | Kiekis tonomis |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/gaminiu_duomenys.csv
