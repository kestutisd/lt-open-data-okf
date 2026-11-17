---
type: Table
title: "Istaiga — Panevėžio miesto ikimokyklinio ugdymo įstaigos"
description: "Informacija apie Panevėžio miesto ikimokyklinio ugdymo įstaigas"
resource: "https://get.data.gov.lt/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas/Istaiga"
tags: [gov, panevezio_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Istaiga — Panevėžio miesto ikimokyklinio ugdymo įstaigos

Informacija apie Panevėžio miesto ikimokyklinio ugdymo įstaigas

- **Model:** `datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas/Istaiga`[^manifest]
- **Dataset:** [Panevėžio miesto ikimokyklinio ugdymo įstaigų, grupių ir vaikų registracijos duomenys](../ikimokyklinis_ugdymas.md) (`datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas`)
- **Manifest CSV:** [datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas/Istaiga`
- **Primary Key (`ref`):** `istaigos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `istaigos_id` | `string` | — | `4` | `open` | — | Įstaigos ID numeris | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Įstaigos JAR kodas | — |
| `jar_validacija` | `string` | — | `4` | `open` | — | Įstaigos JAR kodo validacija | — |
| `istaigos_pavadinimas` | `string` | — | `4` | `open` | — | Įstaigos pavadinimas | — |
| `istaigos_vadovas` | `string` | — | `4` | `open` | — | Įstaigos vadovas | — |
| `istaigos_adresas` | `string` | — | `4` | `open` | — | Įstaigos adresas | — |
| `geometrija` | `geometry(point, 3346)` | — | `4` | `open` | — | Įstaigo vietos taško koordinatės | — |
| `istaigos_tel` | `string` | — | `4` | `open` | — | Įstaigos telefono numeris | — |
| `istaigos_el_pastas` | `string` | — | `4` | `open` | — | Įstaigos el. paštas | — |
| `istaigos_svetaine` | `string` | — | `4` | `open` | — | Įstaigos internetinės svetainės adresas | — |
| `mokymo_kalba` | `string` | — | `4` | `open` | — | Įstaigos bendravimo ir mokymo kalba | — |
| `grupiu_sk` | `integer` | — | `4` | `open` | — | Grupių skaičius įstaigoje | — |
| `vietu_sk` | `integer` | — | `4` | `open` | — | Vietų skaičius įstaigoje | — |
| `laisvu_vietu_sk` | `integer` | — | `4` | `open` | — | Laisvų vietų skaičius grupėje | — |
| `budinti_grupe` | `boolean` | — | `4` | `open` | — | Budinti grupė (yra / nėra) | — |
| `specialioji_grupe` | `boolean` | — | `4` | `open` | — | Specialioji grupė (yra / nėra) | — |
| `darbo_laikas` | `string` | — | `4` | `open` | — | Grupių darbo laikas įstaigoje | — |
| `veiklos_aprasymas` | `string` | — | `4` | `open` | — | Įstaigos veiklos aprašymas | — |
| `darbuotojai` | `string` | — | `4` | `open` | — | Įstaigos darbuotojai | — |
| `duomenys_gauti` | `datetime` | `L` | `4` | `open` | — | Duomenų gavimo data ir laikas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv
