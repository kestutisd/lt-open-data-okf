---
type: Table
title: "Kelias — Sluoksnyje saugoma informacija apie kelių ir gatvių ašines linijas"
description: "Spinta table datasets/gov/giscentras/grpk/Kelias (18 columns)."
resource: "https://get.data.gov.lt/datasets/gov/giscentras/grpk/Kelias"
tags: [gov, giscentras, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/giscentras/grpk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Kelias — Sluoksnyje saugoma informacija apie kelių ir gatvių ašines linijas

- **Model:** `datasets/gov/giscentras/grpk/Kelias`[^manifest]
- **Dataset:** [Georeferencinio pagrindo kadastro erdviniai duomenys](../grpk.md) (`datasets/gov/giscentras/grpk`)
- **Manifest CSV:** [datasets/gov/giscentras/grpk.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/giscentras/grpk/Kelias`
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
| `enumeris` | `string` | — | `4` | `open` | — | Kelio ar gatvės, sutampančios su Europine magistrale, numeris | — |
| `numeris` | `string` | — | `4` | `open` | — | Valstybinės reikšmės kelio ar gatvės, sutampančios su valstybinės reikšmės keliu, numeris | — |
| `vardas` | `string` | — | `4` | `open` | — | Gatvės pavadinimas (jei nustatytas) | — |
| `danga` | `string` | — | `4` | `open` | — | Kelio, gatvės, taip pat tilto, viršutinės dangos medžiaga | — |
| `jplotis` | `number` | `m` | `4` | `open` | — | Važiuojamosios kelio dangos plotis | — |
| `plotis` | `number` | `m` | `4` | `open` | — | Bendras kelio plotis (su kelkraščiais) | — |
| `kategor` | `string` | — | `4` | `open` | — | Valstybinės ar vietinės reikšmės kelio ar gatvės, sutampančios su valstybinės ar vietinės reikšmės keliu, kategorija (jei nustatyta) | — |
| `lygmuo` | `integer` | — | `4` | `open` | — | Kelio lygis žemės paviršiaus atžvilgiu | — |
| `paskirtis` | `string` | — | `4` | `open` | — | Kelio, gatvės tipas, paskirtis | — |
| `shape_length` | `number` | `m` | `4` | `open` | — | Objekto perimetro ilgis | — |
| `shape` | `geometry(multilinestring, 3346)` | — | `4` | `open` | — | Objekto geometrijos tipas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gkodas` | `"gc2"` | — | — | Gatvės ašinė linija – per vidurį išilgai gatvės važiuojamosios dalies einanti menama linija | — |
| `gkodas` | `"gc12"` | — | — | Kelio su danga ašinė linija – per vidurį išilgai važiuojamosios kelio su danga dalies einanti menama linija | — |
| `gkodas` | `"gc14"` | — | — | Kelio su danga be rišiklių ašinė linija – per vidurį išilgai kelio su danga be rišiklių važiuojamosios dalies einanti menama linija | — |
| `gkodas` | `"gc15"` | — | — | Gruntkelio ašinė linija – per vidurį išilgai važiuojamosios gruntkelio dalies einanti menama linija | — |
| `gkodas` | `"gc16"` | — | — | Lauko ir miško kelio ašinė linija – per vidurį išilgai lauko ar miško kelio einanti menama linija | — |
| `gkodas` | `"gc3"` | — | — | Kelio, esančio uždarose teritorijose ir nepatenkančio į visuomeninio ar viešojo transporto tinklą, ašinė linija – per vidurį išilgai kelio važiuojamosios dalies einanti menama linija | — |
| `gkodas` | `"dc2"` | — | — | Pėsčiųjų, dviračių ar apžvalginio tako, takelio ašinė linija – per vidurį išilgai pėsčiųjų, dviračių ar apžvalginio tako, takelio, esančio miestų parkuose ar lankytinuose objektuose, einanti menama linija | — |
| `gkodas` | `"zs22"` | — | — | Kelto, perkėlos ašinė linija – sąlyginė linija, jungianti du kelius, nurodanti, kad automobilių transportą ir (ar) pėsčiuosius per vandens telkinį gali perkelti keltas ar kitas perkėlos įrenginys | — |
| `danga` | `"A"` | — | — | asfaltas | — |
| `danga` | `"C"` | — | — | cementbetonis | — |
| `danga` | `"G"` | — | — | grindinys, trinkelės | — |
| `danga` | `"Sk"` | — | — | skalda | — |
| `danga` | `"Ž"` | — | — | žvyras | — |
| `danga` | `"Md"` | — | — | medis | — |
| `danga` | `"KT"` | — | — | kai netinka nė viena iš reikšmių | — |
| `kategor` | `"AM"` | — | — | Automagistralė | — |
| `kategor` | `"1"` | — | — | pirmos kategorijos kelias | — |
| `kategor` | `"2"` | — | — | antros kategorijos kelias | — |
| `kategor` | `"3"` | — | — | trečios kategorijos kelias | — |
| `kategor` | `"4"` | — | — | ketvirtos kategorijos kelias | — |
| `kategor` | `"5"` | — | — | penktos kategorijos kelias | — |
| `kategor` | `"1V"` | — | — | pirmos kategorijos vietinis kelias | — |
| `kategor` | `"2V"` | — | — | antros kategorijos vietinis kelias | — |
| `kategor` | `"3V"` | — | — | trečios kategorijos vietinis kelias | — |
| `kategor` | `"KT"` | — | — | kai netinka nė viena iš reikšmių | — |
| `lygmuo` | `3` | — | — | 3-ame lygyje aukščiau žemės paviršiaus | — |
| `lygmuo` | `2` | — | — | 2-ame lygyje aukščiau žemės paviršiaus | — |
| `lygmuo` | `1` | — | — | 1-ame lygyje aukščiau žemės paviršiaus | — |
| `lygmuo` | `0` | — | — | žemės paviršiuje | — |
| `lygmuo` | `-1` | — | — | 1-ame lygyje žemiau žemės paviršiaus (po žeme) | — |
| `lygmuo` | `-9999` | — | — | kai netinka nė viena iš reikšmių | — |
| `paskirtis` | `"LEGR"` | — | — | greitėjimo, lėtėjimo juosta | — |
| `paskirtis` | `"PAGR"` | — | — | pagrindinė gatvė ar kelias | — |
| `paskirtis` | `"ZIED"` | — | — | žiedinė sankryža | — |
| `paskirtis` | `"JUNG"` | — | — | jungiamasis kelias | — |
| `paskirtis` | `"PESC"` | — | — | pėsčiųjų takas | — |
| `paskirtis` | `"DVIR"` | — | — | dviračių takas | — |
| `paskirtis` | `"P/J"` | — | — | pagrindinė gatvė ir jungiamasis kelias | — |
| `paskirtis` | `"P/L"` | — | — | pagrindinė gatvė ir jungiamasis kelias | — |
| `paskirtis` | `"P/Z"` | — | — | pagrindinė gatvė ir žiedinė sankryža | — |
| `paskirtis` | `"PZ/J"` | — | — | pagrindinė gatvė žiede arba jungiamasis kelias | — |
| `paskirtis` | `"Z/J"` | — | — | žiedinė sankryža arba jungiamasis kelias | — |
| `paskirtis` | `"KT"` | — | — | kai netinka nė viena iš reikšmių | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vardas` | `update(property: "vardas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/giscentras/grpk.csv
