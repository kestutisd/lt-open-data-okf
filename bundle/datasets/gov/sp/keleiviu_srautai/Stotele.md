---
type: Table
title: "Stotele"
description: "Lentelėje pateikiamas detalus keleivių skaičius kiekvienoje reiso stotelėje"
resource: "https://get.data.gov.lt/datasets/gov/sp/keleiviu_srautai/Stotele"
tags: [gov, sp, stotele, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sp/keleiviu_srautai.csv#L20"
    title: "atviriduomenys/manifest — datasets/gov/sp/keleiviu_srautai.csv#L20"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3901/"
    title: "data.gov.lt DCAT-AP — datasets/gov/sp/keleiviu_srautai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Stotele

Lentelėje pateikiamas detalus keleivių skaičius kiekvienoje reiso stotelėje[^manifest]

- **Model:** `datasets/gov/sp/keleiviu_srautai/Stotele`[^manifest]
- **Dataset:** [Vilniaus miesto viešojo transporto maršrutų keleivių srautų duomenys](../keleiviu_srautai.md) (`datasets/gov/sp/keleiviu_srautai`)[^manifest]
- **Manifest CSV:** [datasets/gov/sp/keleiviu_srautai.csv#L20](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sp/keleiviu_srautai.csv#L20)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sp/keleiviu_srautai/Stotele` (`deployed`)[^manifest]
- **Provider:** `sp` — Vilniaus miesto SĮ „Susisiekimo paslaugos“ *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `keliones_stoteles_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/sp/keleiviu_srautai.csv#L20 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sp/keleiviu_srautai.csv#L20)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/sp/keleiviu_srautai (https://data.gov.lt/datasets/3901/)
