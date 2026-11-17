---
type: Table
title: "WeatherConditionRetro"
description: "Spinta table datasets/gov/lakd/keliu_oro_stoteles/WeatherConditionRetro (25 columns)."
tags: [gov, lakd, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lakd/keliu_oro_stoteles.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliu_oro_stoteles.csv#L48"
    last_modified: "2026-11-11T14:39:20Z"
---

# WeatherConditionRetro

- **Model:** `datasets/gov/lakd/keliu_oro_stoteles/WeatherConditionRetro`[^manifest]
- **Dataset:** [datasets/gov/lakd/keliu_oro_stoteles](../keliu_oro_stoteles.md) (`datasets/gov/lakd/keliu_oro_stoteles`)
- **Manifest CSV:** [datasets/gov/lakd/keliu_oro_stoteles.csv#L48](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliu_oro_stoteles.csv#L48)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **URI:** `vadovas:dsa/dimensijos.html#model.ref`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `surinkimo_data_unix` | `datetime` | `S` | `2` | `open` | — | Surinkimo data unix formatu | — |
| `surinkimo_data` | `temporal` | `T` | `5` | `open` | `dct:temporal` | Surinkimo data | — |
| `id` | `integer` | — | `4` | `open` | — | Įrenginio identifikacinis numeris | — |
| `irenginys` | `string` | — | `3` | `open` | — | Įrenginio pavadinimas | — |
| `numeris` | `string` | — | `2` | `open` | — | Kelio numeris | — |
| `pavadinimas` | `string` | — | `2` | `open` | — | Kelio pavadinimas | — |
| `kilometras` | `number` | — | `3` | `open` | — | Vieta | kilometras |
| `oro_temperatura` | `number` | `°C` | `4` | `open` | — | Oro temperatūra | — |
| `vejo_greitis_vidut` | `number` | `m/s` | `4` | `open` | — | Vidutinis vėjo greitis | — |
| `krituliu_tipas` | `string` | — | `4` | `open` | — | Kritulių tipas | — |
| `krituliu_kiekis` | `number` | — | `3` | `open` | — | Kritulių kiekis | — |
| `dangos_temperatura` | `number` | `°C` | `4` | `open` | — | Dangos temperatūra | — |
| `matomumas` | `string` | — | `3` | `open` | — | Matomumas | — |
| `rasos_taskas` | `number` | — | `3` | `open` | — | Rasos taškas | — |
| `kelio_danga` | `string` | — | `4` | `open` | — | Kelio dangos būklė | — |
| `uzsalimo_taskas` | `number` | `°C` | `4` | `open` | — | Užšalimo taškas | — |
| `vejo_greitis_maks` | `number` | `m/s` | `4` | `open` | — | Maksimalus vėjo greitis | — |
| `vejo_kryptis` | `string` | — | `3` | `open` | — | Vėjo kryptis | — |
| `sukibimo_koeficientas` | `number` | — | `3` | `open` | — | Sukibimo koeficientas | — |
| `ilguma` | `integer` | — | `3` | `open` | — | Ilguma | LKS-94 |
| `platuma` | `integer` | — | `3` | `open` | — | Platuma | LKS-94 |
| `vieta_lks94` | `geometry(point, 3346)` | `m` | — | — | — | — | — |
| `lat` | `number` | — | `3` | `open` | — | Platuma | WGS-84 |
| `lng` | `number` | — | `3` | `open` | — | Ilguma | WGS-84 |
| `vieta_wgs84` | `geometry(point, 4326)` | `m` | — | — | — | — | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `krituliu_tipas` | `"Lietus, silpnas"` | — | — | Silpnas lietus | — |
| `krituliu_tipas` | `"Lietus, vidutinis"` | — | — | Vidutinio stiprumo lietus | — |
| `krituliu_tipas` | `"Nėra"` | — | — | Kritulių nėra | — |
| `krituliu_tipas` | `"Krituliai"` | — | — | Kritulių yra | — |
| `krituliu_tipas` | `"Dulksna"` | — | — | Dulksna | — |
| `kelio_danga` | `"Šlapia"` | — | — | Šlapia | — |
| `kelio_danga` | `"Sausa"` | — | — | Sausa | — |
| `kelio_danga` | `"Drėgna"` | — | — | Drėgna | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |
| `dct` | `http://purl.org/dc/terms/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `numeris` | `create(property: "kelias", type: "ref", ref: "/datasets/gov/lakd/keliai/StateRoad[kelionr]")` | `type` | `4` | — | — | — | — |
| `numeris` | `update(property: "kelias.numeris", type: "")` | `property` | `4` | — | — | — | — |
| `pavadinimas` | `update(property: "kelias.pavadinimas", type: "")` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/keliu_oro_stoteles.csv
