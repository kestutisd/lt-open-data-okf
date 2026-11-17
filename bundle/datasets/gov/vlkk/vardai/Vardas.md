---
type: Table
title: "Vardas — Vardų lingvistiniai duomenys"
description: "Valstybinė lietuvių kalbos komisijos (VLKK) Lietuvos Respublikos piliečių vardų sąvadas, kaip duomenų rinkinio šaltinis, yra sukurtas Gyventojų registro 2006 m. pilietybę turėjusių asmenų vardų duomenimis ir toliau yra pildomas..."
resource: "https://get.data.gov.lt/datasets/gov/vlkk/vardai/Vardas"
tags: [gov, vlkk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlkk/vardai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlkk/vardai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Vardas — Vardų lingvistiniai duomenys

Valstybinė lietuvių kalbos komisijos (VLKK) Lietuvos Respublikos piliečių vardų sąvadas, kaip duomenų rinkinio šaltinis, yra sukurtas Gyventojų registro 2006 m. pilietybę turėjusių asmenų vardų duomenimis ir toliau yra pildomas naujagimių vardais. Rinkinyje duomenys kaupiami nuo 2010 m. ir yra atnaujinami kas 3 mėnesius. Duomenys apima pilną vardą, sudarančių vardų skaičių (komponentiškumą), vardo lytį, normiškumą, ar tai yra šventojo vardas, vardo įvedimo datą, vėliausias atnaujinimo bei paieškos datas, paieškų skaičių ir iki po 5 vardų kilmės grupes, pogrupius ir poskyrius.

- **Model:** `datasets/gov/vlkk/vardai/Vardas`[^manifest]
- **Dataset:** [Vardų lingvistiniai duomenys](../vardai.md) (`datasets/gov/vlkk/vardai`)
- **Manifest CSV:** [datasets/gov/vlkk/vardai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlkk/vardai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlkk/vardai/Vardas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `pilnas_vardas` | `string` | — | `4` | `open` | — | Pilnas vardas su sudėtiniais vardais | — |
| `vardu_sk` | `integer` | `U` | `4` | `open` | — | Sudėtinių vardų skaičius | — |
| `lytis` | `string` | — | `4` | `open` | — | Vardo turėtojo lytis | — |
| `normiskumas` | `string` | — | `4` | `open` | — | Vardo normiškumo būsena | — |
| `ar_sventojo_vardas` | `boolean` | — | `4` | `open` | — | Ar vardas yra šventojo vardas | — |
| `sukurimo_data` | `datetime` | `S` | `4` | `open` | — | Vardo įvedimo sistemoje data ir laikas sekundės tikslumu | — |
| `atnaujinimo_data` | `datetime` | `S` | `4` | `open` | — | Vardo paskutinio atnaujinimo data ir laikas sekundės tikslumu | — |
| `veliausia_paieskos_data` | `datetime` | `S` | `4` | `open` | — | Vardo vėliausios paieškos data ir laikas sekundės tikslumu | — |
| `paiesku_sk` | `integer` | `U` | `4` | `open` | — | Vardo paieškų skaičius | — |
| `kilmes_grupe_1` | `string` | — | `4` | `open` | — | Vardo kilmės grupės pirmas variantas | — |
| `kilmes_pogrupis_1` | `string` | — | `4` | `open` | — | Vardo kilmės pogrupio pirmas variantas | — |
| `kilmes_poskyris_1` | `string` | — | `4` | `open` | — | Vardo kilmės poskyrio pirmas variantas | — |
| `kilmes_grupe_2` | `string` | — | `4` | `open` | — | Vardo kilmės grupės antras variantas | — |
| `kilmes_pogrupis_2` | `string` | — | `4` | `open` | — | Vardo kilmės pogrupio antras variantas | — |
| `kilmes_poskyris_2` | `string` | — | `4` | `open` | — | Vardo kilmės poskyrio antras variantas | — |
| `kilmes_grupe_3` | `string` | — | `4` | `open` | — | Vardo kilmės grupės trečias variantas | — |
| `kilmes_pogrupis_3` | `string` | — | `4` | `open` | — | Vardo kilmės pogrupio trečias variantas | — |
| `kilmes_poskyris_3` | `string` | — | `4` | `open` | — | Vardo kilmės poskyrio trečias variantas | — |
| `kilmes_grupe_4` | `string` | — | `4` | `open` | — | Vardo kilmės grupės ketvirtas variantas | — |
| `kilmes_pogrupis_4` | `string` | — | `4` | `open` | — | Vardo kilmės pogrupio ketvirtas variantas | — |
| `kilmes_poskyris_4` | `string` | — | `4` | `open` | — | Vardo kilmės poskyrio ketvirtas variantas | — |
| `kilmes_grupe_5` | `string` | — | `4` | `open` | — | Vardo kilmės grupės penktas variantas | — |
| `kilmes_pogrupis_5` | `string` | — | `4` | `open` | — | Vardo kilmės pogrupio penktas variantas | — |
| `kilmes_poskyris_5` | `string` | — | `4` | `open` | — | Vardo kilmės poskyrio penktas variantas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Vyras"` | `vyro` | — | Vyras | — |
| `lytis` | `"Moteris"` | `moters` | — | Moteris | — |
| `normiskumas` | `"Nepasirinkta"` | `nepasirinkta` | — | Nepasirinkta | — |
| `normiskumas` | `"Teiktinas"` | `teiktinas` | — | Teiktinas | — |
| `normiskumas` | `"Vengtinas"` | `vengtinas` | — | Vengtinas | — |
| `normiskumas` | `"Neteiktinas"` | `neteiktinas` | — | Neteiktinas | — |
| `kilmes_grupe_1` | `"Baltiška kilmė"` | `baltiškos kilmės` | — | Baltiška kilmė | — |
| `kilmes_grupe_1` | `"Svetima kilmė"` | `svetimos kilmės` | — | Svetima kilmė | — |
| `kilmes_grupe_2` | `"Baltiška kilmė"` | `baltiškos kilmės` | — | Baltiška kilmė | — |
| `kilmes_grupe_2` | `"Svetima kilmė"` | `svetimos kilmės` | — | Svetima kilmė | — |
| `kilmes_grupe_3` | `"Baltiška kilmė"` | `baltiškos kilmės` | — | Baltiška kilmė | — |
| `kilmes_grupe_3` | `"Svetima kilmė"` | `svetimos kilmės` | — | Svetima kilmė | — |
| `kilmes_grupe_4` | `"Baltiška kilmė"` | `baltiškos kilmės` | — | Baltiška kilmė | — |
| `kilmes_grupe_4` | `"Svetima kilmė"` | `svetimos kilmės` | — | Svetima kilmė | — |
| `kilmes_grupe_5` | `"Baltiška kilmė"` | `baltiškos kilmės` | — | Baltiška kilmė | — |
| `kilmes_grupe_5` | `"Svetima kilmė"` | `svetimos kilmės` | — | Svetima kilmė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlkk/vardai.csv
