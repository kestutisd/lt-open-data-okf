---
type: Table
title: "UpeKanalas — Upės ir kanalai"
description: "Pagal Upių, ežerų ir tvenkinių kadastro nuostatus, patvirtintų Lietuvos Respublikos Vyriausybės 2000-09-19 nutarimu Nr. 1114, kadastre kaupiama informacija apie upes, kurių ilgis ne mažesnis kaip 3 kilometrai arba baseino plotas ne mažesnis kaip 5 kv."
resource: "https://get.data.gov.lt/datasets/gov/aaa/upes_kanalai/UpeKanalas"
tags: [gov, aaa, upekanalas, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/upes_kanalai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/aaa/upes_kanalai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1779/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/upes_kanalai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# UpeKanalas — Upės ir kanalai

Pagal Upių, ežerų ir tvenkinių kadastro nuostatus, patvirtintų Lietuvos Respublikos Vyriausybės 2000-09-19 nutarimu Nr. 1114, kadastre kaupiama informacija apie upes, kurių ilgis ne mažesnis kaip 3 kilometrai arba baseino plotas ne mažesnis kaip 5 kv. kilometrai ir (ar) valstybinės reikšmės vidaus vandens telkiniams priskirtas upes ar kanalus, ir (ar) upes ar kanalus, kuriuose vykdomas valstybinis aplinkos monitoringas.[^manifest]

- **Model:** `datasets/gov/aaa/upes_kanalai/UpeKanalas`[^manifest]
- **Dataset:** [Upių, kanalų duomenys](../upes_kanalai.md) (`datasets/gov/aaa/upes_kanalai`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/upes_kanalai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/upes_kanalai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/upes_kanalai/UpeKanalas` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/upes_kanalai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/upes_kanalai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/upes_kanalai (https://data.gov.lt/datasets/1779/)
