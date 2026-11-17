---
type: Table
title: "LovuFondas — VšĮ Rokiškio psichiatrijos ligoninės pacientų ir lovų fondo skaičiaus dinamika"
description: "Spinta table datasets/gov/rpl/lovu_fondas/LovuFondas (18 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rpl/lovu_fondas/LovuFondas"
tags: [gov, rpl, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rpl/lovu_fondas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rpl/lovu_fondas.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# LovuFondas — VšĮ Rokiškio psichiatrijos ligoninės pacientų ir lovų fondo skaičiaus dinamika

- **Model:** `datasets/gov/rpl/lovu_fondas/LovuFondas`[^manifest]
- **Dataset:** [datasets/gov/rpl/lovu_fondas](../lovu_fondas.md) (`datasets/gov/rpl/lovu_fondas`)
- **Manifest CSV:** [datasets/gov/rpl/lovu_fondas.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rpl/lovu_fondas.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rpl/lovu_fondas/LovuFondas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `data` | `date` | `D` | `4` | `open` | — | Formos pildymo data | — |
| `skyr_pav` | `string` | — | `4` | `open` | — | Skyriaus pavadinimas | — |
| `fakt_lovos` | `integer` | — | `4` | `open` | — | Faktinis naudojamų lovų skaičius, įskaitant remontuojamas lovas | — |
| `ligoniu_viso_vakar` | `integer` | — | `4` | `open` | — | Ligonių skaičius praėjusios paros pradžioje iš viso | — |
| `ligoniu_kaimo_vakar` | `integer` | — | `4` | `open` | — | Ligonių kaimo gyventojų skaičius praėjusios paros pradžioje | — |
| `atvyko` | `integer` | — | `4` | `open` | — | Atvyko iš viso (be perkeltų pačioje ligoninėje) | — |
| `atvyko_kaimo` | `integer` | — | `4` | `open` | — | Atvyko kaimo gyventojų | — |
| `atkelta` | `integer` | — | `4` | `open` | — | Atkelta pacientų iš kitų skyrių pačioje ligoninėje | — |
| `atkelta_kaimo` | `integer` | — | `4` | `open` | — | Atkelta pacientų iš kitų skyrių pačioje ligoninėje kaimo gyventojų | — |
| `iskelta` | `integer` | — | `4` | `open` | — | Iškelta pacientų į kitus skyrius pačioje ligoninėje | — |
| `iskelta_kaimo` | `integer` | — | `4` | `open` | — | Iškelta pacientų į kitus skyrius pačioje ligoninėje kaimo gyventojų | — |
| `israsyta_viso` | `integer` | — | `4` | `open` | — | Išrašyta pacientų iš viso | — |
| `israsyta_stacionar` | `integer` | — | `4` | `open` | — | Išrašyti iš ligoninės pacientai, kurie perkelti į kitus stacionarus | — |
| `israsyta_kaimo` | `integer` | — | `4` | `open` | — | Išrašyta kaimo gyventojų | — |
| `mire_viso` | `integer` | — | `4` | `open` | — | Mirė pacientų iš viso | — |
| `mire_kaimo` | `integer` | — | `4` | `open` | — | Mirė kaimo gyventojų | — |
| `ligoniu_viso` | `integer` | — | `4` | `open` | — | Ligonių skaičius šios dienos pradžioje | — |
| `ligoniu_viso_kaimo` | `integer` | — | `4` | `open` | — | Iš jų šios dienos pradžioje yra kaimo gyventojų | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rpl/lovu_fondas.csv
