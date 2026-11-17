---
type: Table
title: "Stotele"
description: "Lentelėje pateikiamas detalus keleivių skaičius kiekvienoje reiso stotelėje"
resource: "https://get.data.gov.lt/datasets/gov/sp/keleiviu_srautai/Stotele"
tags: [gov, sp, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/sp/keleiviu_srautai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sp/keleiviu_srautai.csv#L20"
    last_modified: "2026-11-11T14:39:20Z"
---

# Stotele

Lentelėje pateikiamas detalus keleivių skaičius kiekvienoje reiso stotelėje

- **Model:** `datasets/gov/sp/keleiviu_srautai/Stotele`[^manifest]
- **Dataset:** [Vilniaus miesto viešojo transporto maršrutų keleivių srautų duomenys](../keleiviu_srautai.md) (`datasets/gov/sp/keleiviu_srautai`)
- **Manifest CSV:** [datasets/gov/sp/keleiviu_srautai.csv#L20](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sp/keleiviu_srautai.csv#L20)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sp/keleiviu_srautai/Stotele`
- **Primary Key (`ref`):** `keliones_stoteles_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `keliones_stoteles_id` | `string` | — | `4` | `open` | — | Stotelės kelionėje identifikatorius | — |
| `reiso_id` | `string` | — | `4` | `open` | — | Reiso identifikatorius | — |
| `stoteles_seka` | `integer` | — | `4` | `open` | — | Stotelės eilės numeris kelionėje | — |
| `stoteles_id` | `string` | — | `4` | `open` | — | Stotelės identifikatorius | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Stotelės pavadinimas | — |
| `koord_id` | `string` | — | `4` | `open` | — | Stotelės koordinatės identifikatorius | — |
| `geometrija_wkt` | `geometry(point, 3346)` | — | `4` | `open` | — | Stotelės geometrija (lokacija) WKT formatu | — |
| `atvykimo_laikas` | `datetime` | `S` | `4` | `open` | — | Atvykimo į stotelę laikas | — |
| `atvykimo_velavimas_s` | `integer` | — | `4` | `open` | — | Atvykimo į stotelę vėlavimo trukmė sekundėmis | — |
| `isvykimo_laikas` | `datetime` | `S` | `4` | `open` | — | Išvykimo iš stotelės laikas | — |
| `isvykimo_velavimas_s` | `integer` | — | `4` | `open` | — | Išvykimo iš stotelės vėlavimo trukmė sekundėmis | — |
| `keliones_trukme_s` | `integer` | — | `4` | `open` | — | Kelionės trukmė nuo išvykimo iš stotelės iki atvykimo į sekančią stotelę sekundėmis | — |
| `stovejimo_trukme_s` | `integer` | — | `4` | `open` | — | Keleivių įlipimo ir išlipimo trukmė sekundėmis | — |
| `ilipusiu_sk` | `integer` | — | `4` | `open` | — | Įlipusių keleivių skaičius | — |
| `islipusiu_sk` | `integer` | — | `4` | `open` | — | Išlipusių keleivių skaičius | — |
| `keleiviu_sk` | `integer` | — | `4` | `open` | — | Keleivių kiekis maršrute | — |
| `ilipusiu_sk_perskaiciuotas` | `integer` | — | `4` | `open` | — | Perskaičiuotas (patikslintas), pagal DILAX integruotus algoritmus, įlipusių keleivių kiekis | — |
| `islipusiu_sk_perskaiciuotas` | `integer` | — | `4` | `open` | — | Perskaičiuotas (patikslintas), pagal DILAX integruotus algoritmus, išlipusių keleivių kiekis | — |
| `keleiviu_sk_perskaiciuotas` | `integer` | — | `4` | `open` | — | Perskaičiuotas (patikslintas), pagal DILAX integruotus algoritmus, keleivių kiekis | — |
| `transporto_sustojimas` | `boolean` | — | `4` | `open` | — | Stotelėje sustojusios transporto priemonės požymis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sp/keleiviu_srautai.csv
