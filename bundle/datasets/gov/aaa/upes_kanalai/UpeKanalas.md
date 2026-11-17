---
type: Table
title: "UpeKanalas — Upės ir kanalai"
description: "Pagal Upių, ežerų ir tvenkinių kadastro nuostatus, patvirtintų Lietuvos Respublikos Vyriausybės 2000-09-19 nutarimu Nr. 1114, kadastre kaupiama informacija apie upes, kurių ilgis ne mažesnis kaip 3 kilometrai arba baseino plotas ne..."
resource: "https://get.data.gov.lt/datasets/gov/aaa/upes_kanalai/UpeKanalas"
tags: [gov, aaa, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/upes_kanalai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/upes_kanalai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# UpeKanalas — Upės ir kanalai

Pagal Upių, ežerų ir tvenkinių kadastro nuostatus, patvirtintų Lietuvos Respublikos Vyriausybės 2000-09-19 nutarimu Nr. 1114, kadastre kaupiama informacija apie upes, kurių ilgis ne mažesnis kaip 3 kilometrai arba baseino plotas ne mažesnis kaip 5 kv. kilometrai ir (ar) valstybinės reikšmės vidaus vandens telkiniams priskirtas upes ar kanalus, ir (ar) upes ar kanalus, kuriuose vykdomas valstybinis aplinkos monitoringas.

- **Model:** `datasets/gov/aaa/upes_kanalai/UpeKanalas`[^manifest]
- **Dataset:** [datasets/gov/aaa/upes_kanalai](../upes_kanalai.md) (`datasets/gov/aaa/upes_kanalai`)
- **Manifest CSV:** [datasets/gov/aaa/upes_kanalai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/upes_kanalai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/upes_kanalai/UpeKanalas`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Upės unikalus identifikatorius | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Upės, kanalo pavadinimas | — |
| `kadastroid` | `string` | — | `4` | `open` | — | Objekto kadastro identifikavimo kodas | — |
| `registruota` | `date` | `D` | `4` | `open` | — | Kadastro objekto registravimo data | Metai, mėnuo, diena, laikas |
| `redaguota` | `date` | `D` | `4` | `open` | — | Kadastro objekto redagavimo data | Metai, mėnuo, diena, laikas |
| `kategorija` | `integer` | — | `4` | `open` | — | Vandens objekto kategorijos pavadinimo kodas | Įsakymu Nr. D1-752 patvirtintas PAVIRŠINIŲ VANDENS TELKINIŲ KATEGORIJŲ KLASIFIKATORIUS https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/TAIS.361485 |
| `ubr_kodas` | `string` | — | `4` | `open` | — | Upės pabaseinio arba baseino, kuriame yra vandens objektas, kodas | — |
| `vyrupes_uid` | `string` | — | `4` | `open` | — | Vyresniosios upės, į kurią įteka upės, unikalus identifikatorius | — |
| `koord` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Žiočių centro koordinatės | LKS 94 koordinačių sistemoje |
| `krantas` | `integer` | — | `4` | `open` | — | Įtekėjimo į vyresniąją upę krantas | — |
| `eiliskumas` | `integer` | — | `3` | `open` | — | Upės įtekėjimo eiliškumas | Upės, įtekančios į Baltijos jūrą ar Kuršių marias, atžvilgiu. |
| `ilgis` | `number` | `km` | `4` | `open` | — | Upės ilgis | Geografinis Lietuvos teritorijoje |
| `debitas` | `number` | `m^3/s` | `4` | `open` | — | Vidutinis daugiametis vandens debitas upės žiotyse | — |
| `shape` | `geometry(3346)` | — | `4` | `open` | — | Geometrinis primityvas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `kategorija` | `1` | — | — | Upė | — |
| `kategorija` | `2` | — | — | Kanalas | — |
| `kategorija` | `3` | — | — | Natūralus ežeras | — |
| `kategorija` | `4` | — | — | Užtvenktas ežeras | — |
| `kategorija` | `5` | — | — | Tvenkinys | — |
| `kategorija` | `6` | — | — | Dirbtinis nepratekamas paviršinio vandens telkinys | — |
| `kategorija` | `7` | — | — | Tarpinis vandens telkinys | — |
| `kategorija` | `8` | — | — | Pakrantės vandens telkinys | — |
| `kategorija` | `9` | — | — | Teritorinis vandens telkinys | — |
| `krantas` | `0` | — | — | kairys | — |
| `krantas` | `1` | — | — | dešinys | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/upes_kanalai.csv
