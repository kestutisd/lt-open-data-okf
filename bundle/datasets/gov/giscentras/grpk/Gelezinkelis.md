---
type: Table
title: "Gelezinkelis — Sluoksnyje saugoma informacija apie geležinkelio vėžės ašines linijas"
description: "Spinta table datasets/gov/giscentras/grpk/Gelezinkelis (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/giscentras/grpk/Gelezinkelis"
tags: [gov, giscentras, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/giscentras/grpk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L71"
    last_modified: "2026-11-11T14:39:20Z"
---

# Gelezinkelis — Sluoksnyje saugoma informacija apie geležinkelio vėžės ašines linijas

- **Model:** `datasets/gov/giscentras/grpk/Gelezinkelis`[^manifest]
- **Dataset:** [Georeferencinio pagrindo kadastro erdviniai duomenys](../grpk.md) (`datasets/gov/giscentras/grpk`)
- **Manifest CSV:** [datasets/gov/giscentras/grpk.csv#L71](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L71)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/giscentras/grpk/Gelezinkelis`
- **Primary Key (`ref`):** `top_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `top_id` | `string` | — | `4` | `open` | — | Objekto identifikavimo kodas (reikšmė yra privaloma) | — |
| `gkodas` | `string` | — | `4` | `open` | — | Erdvinio objekto kodas (reikšmė yra privaloma) | — |
| `meta` | `string` | — | `4` | `open` | — | Raktas į GRPK rinkinio sluoksnio metaduomenų lenteles | — |
| `red_priezastis` | `string` | — | `4` | `open` | — | Objekto duomenų ir informacijos sukūrimo ar paskutinio pakeitimo priežastis (reikšmė yra privaloma įvedus naują ar patikslinus esamo objekto duomenis ir informaciją) | — |
| `red_saltinis` | `string` | — | `4` | `open` | — | Objekto duomenims sukurti, nustatyti ar pakeisti naudotas duomenų šaltinis. Galimos reikšmės | — |
| `suk_data` | `datetime` | `L` | `4` | `open` | — | Objekto įregistravimo (sukūrimo) data (reikšmė yra privaloma) | — |
| `red_data` | `datetime` | `L` | `4` | `open` | — | Objekto duomenų ir informacijos keitimo data (reikšmė yra privaloma patikslinus esamo objekto duomenis ir informaciją) | — |
| `info` | `string` | — | `4` | `open` | — | Paaiškinamoji informacija | — |
| `lygmuo` | `integer` | — | `4` | `open` | — | Geležinkelio lygis žemės paviršiaus atžvilgiu | — |
| `tipas` | `integer` | — | `4` | `open` | — | Stoties geležinkelio kelio tipas | — |
| `gkategor` | `integer` | — | `4` | `open` | — | Geležinkelio bėgių kelio svarba geležinkelių tinkle | — |
| `shape_length` | `number` | `m` | `4` | `open` | — | Objekto perimetro ilgis | — |
| `shape` | `geometry(multilinestring, 3346)` | — | `4` | `open` | — | Objekto geometrijos tipas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gkodas` | `"gz1"` | — | — | Europinio standarto geležinkelio ašinė linija – per vidurį išilgai europinio standarto geležinkelio bėgių kelio einanti menama linija | — |
| `gkodas` | `"gz2"` | — | — | Plačios vėžės geležinkelio ašinė linija – per vidurį išilgai plačios vėžės geležinkelio bėgių kelio einanti menama linija | — |
| `gkodas` | `"gz4"` | — | — | Siaurojo geležinkelio ar funikulieriaus ašinė linija – per vidurį išilgai siauros vėžės geležinkelio ar funikulieriaus bėgių kelio einanti menama linija | — |
| `gkodas` | `"sgz1"` | — | — | Statomo europinio standarto geležinkelio ašinė linija – per vidurį išilgai europinio standarto geležinkelio bėgių kelio einanti menama linija | — |
| `gkodas` | `"sgz2"` | — | — | Statomo plačios vėžės geležinkelio ašinė linija – per vidurį išilgai plačios vėžės geležinkelio bėgių kelio einanti menama linija | — |
| `gkodas` | `"sgz4"` | — | — | Statomo siaurojo geležinkelio ar funikulieriaus ašinė linija – per vidurį išilgai siauros vėžės geležinkelio ar funikulieriaus bėgių kelio einanti menama linija | — |
| `gkodas` | `"gz10"` | — | — | Grįžratis – ratas su geležinkelio bėgiais riedmenims apgręžti ar paleisti į kitą kelią | — |
| `info` | `"neveik."` | — | — | neveikiantis | — |
| `info` | `"E"` | — | — | elektrifikuotas | — |
| `info` | `"funik."` | — | — | funikulierius | — |
| `info` | `"KT"` | — | — | kai netinka nė viena iš reikšmių | — |
| `lygmuo` | `1` | — | — | 1-ame lygyje aukščiau žemės paviršiaus | — |
| `lygmuo` | `0` | — | — | žemės paviršiuje | — |
| `lygmuo` | `-1` | — | — | 1-ame lygyje žemiau žemės paviršiaus (po žeme) | — |
| `lygmuo` | `-9999` | — | — | kai netinka nė viena iš reikšmių | — |
| `tipas` | `0` | — | — | stoties kelias | — |
| `tipas` | `1` | — | — | pagrindinis kelias | — |
| `tipas` | `-9999` | — | — | kai netinka nė viena iš reikšmių | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/giscentras/grpk.csv
