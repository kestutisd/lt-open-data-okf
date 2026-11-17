---
type: Table
title: "SulaikytaPreke — Akcizinių prekių sulaikymų duomenys"
description: "Muitinės departamento duomenų apie akcizinių prekių nelegalios apyvartos užkardymo rezultatus kaupimo ir apdorojimo sistemoje nuo 2017 m. kaupiami ir iki šiol atnaujinami akcizinių prekių sulaikymo duomenys."
resource: "https://get.data.gov.lt/datasets/gov/muitine/stebesena/SulaikytaPreke"
tags: [gov, muitine, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/stebesena.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/stebesena.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# SulaikytaPreke — Akcizinių prekių sulaikymų duomenys

Muitinės departamento duomenų apie akcizinių prekių nelegalios apyvartos užkardymo rezultatus kaupimo ir apdorojimo sistemoje nuo 2017 m. kaupiami ir iki šiol atnaujinami akcizinių prekių sulaikymo duomenys. Duomenų rinkinį sudaro: atitinkamos medžiagos siuntą sulaikiusi aukštesnė institucija, metų ketvirčio periodo pradžia ir pabaiga, atitinkamos prekės siuntos sulaikymo data, sulaikytos prekės ir jos grupės pavadinimai, atitinkamu laikotarpiu sulaikytos prekės bendra vertė ir kiekis. Vienas įrašas atitinka vieną aukštesnės institucijos, laikotarpio ir prekės kombinaciją. Duomenų teikėjas – Muitinės departamentas prie Lietuvos Respublikos finansų ministerijos.

- **Model:** `datasets/gov/muitine/stebesena/SulaikytaPreke`[^manifest]
- **Dataset:** [Akcizinių prekių sulaikymų duomenys](../stebesena.md) (`datasets/gov/muitine/stebesena`)
- **Manifest CSV:** [datasets/gov/muitine/stebesena.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/stebesena.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/stebesena/SulaikytaPreke`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `aukstesne_institucija` | `string` | — | `4` | `open` | — | Institucija, pranešusi apie sulaikytas prekes | — |
| `laikotarpio_pradzia` | `date` | `M` | `4` | `open` | — | Metų ketvirčio, kada sulaikyta prekė, pradžia | — |
| `laikotarpio_pabaiga` | `date` | `M` | `4` | `open` | — | Metų ketvirčio, kada sulaikyta prekė, pabaiga | — |
| `preke` | `string` | — | `4` | `open` | — | Sulaikyta prekė | — |
| `prekes_grupe` | `string` | — | `4` | `open` | — | Sulaikytos prekės grupė | — |
| `bendras_prekes_kiekis` | `number` | — | `4` | `open` | — | Bendras esamu laikotarpiu sulaikytos prekės kiekis | — |
| `kiekio_matavimo_vienetas` | `string` | — | `4` | `open` | — | Sulaikytos prekės kiekio matavimo vienetas | — |
| `bendra_prekes_verte` | `number` | — | `4` | `open` | — | Bendra esamu laikotarpiu sulaikytos prekės vertė | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `aukstesne_institucija` | — | `"Valstybės sienos apsaugos tarnyba"` | — | Valstybės sienos apsaugos tarnyba | — |
| `aukstesne_institucija` | — | `"Lietuvos Respublikos muitinė"` | — | Lietuvos Respublikos muitinė | — |
| `aukstesne_institucija` | — | `"Policijos departamentas"` | — | Policijos departamentas | — |
| `aukstesne_institucija` | — | `"Valstybinė mokesčių inspekcija"` | — | Valstybinė mokesčių inspekcija | — |
| `kiekio_matavimo_vienetas` | — | `"Kilogramas"` | — | Kilogramas | — |
| `kiekio_matavimo_vienetas` | — | `"Litras"` | — | Litras | — |
| `kiekio_matavimo_vienetas` | — | `"Vienetas"` | — | Vienetas | — |
| `kiekio_matavimo_vienetas` | — | `"Tona"` | — | Tona | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/stebesena.csv
