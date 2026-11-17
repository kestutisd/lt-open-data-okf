---
type: Table
title: "Iskvietimas — Alytaus šilumos tinklų iškvietimų, nusiskundimų ir konsultacijų registras"
description: "Duomenų rininyje pateikiami nuo 2024 m. kaupiami Alytaus šilumos tinklų klientų nusiskundimų, konsultacijų ir iškvietimų žurnalo duomenys."
resource: "https://get.data.gov.lt/datasets/gov/ast/registras/Iskvietimas"
tags: [gov, ast, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ast/konsultacijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/konsultacijos.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Iskvietimas — Alytaus šilumos tinklų iškvietimų, nusiskundimų ir konsultacijų registras

Duomenų rininyje pateikiami nuo 2024 m. kaupiami Alytaus šilumos tinklų klientų nusiskundimų, konsultacijų ir iškvietimų žurnalo duomenys. Rinkinio objektas – įmonės kliento kreipimasis į Alytaus šilumos tinklus. Rinkinyje nurodoma iškvietimo informacija – gatvė, namo numeris ir iškvietimo priežastis. Taip pat pateikiama pagal iškvietimą vykdytų darbų informacija: darbus atlikusio asmens identifikatorius (sudarytas užšifravus atsakingo darbuotojo vardą ir pavardę), darbų trukmė valandos ir minučių tikslumu, pabaigos žyma, identifikuota gedimo priežastis ir bendra darbų trukmė nuo iškvietimo momento iki darbų užbaigimo.

- **Model:** `datasets/gov/ast/registras/Iskvietimas`[^manifest]
- **Dataset:** [Alytaus šilumos tinklų iškvietimų, nusiskundimų ir konsultacijų registras](../registras.md) (`datasets/gov/ast/registras`)
- **Manifest CSV:** [datasets/gov/ast/konsultacijos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/konsultacijos.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ast/registras/Iskvietimas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `registracija` | `datetime` | `S` | `4` | `open` | — | Registracijos laiko žyma | — |
| `gatve` | `string` | — | `3` | `open` | — | Objekto gatvė | — |
| `namo_nr` | `string` | — | `3` | `open` | — | Objekto namo numeris | — |
| `iskvietimo_priezastis` | `string` | — | `4` | `open` | — | Iškvietimo priežastis | — |
| `darbus_atliko` | `string` | — | `4` | `open` | — | Darbus atlikęs asmuo. | Stulpelis sudarytas, užšifravus darbuotojo vardą ir pavardę. |
| `darbu_trukme_h` | `integer` | `h` | `4` | `open` | — | Darbų trukmė valandų tikslumu | — |
| `darbu_trukme_min` | `integer` | `min` | `4` | `open` | — | Darbų trukmė minučių tikslumu | — |
| `darbu_pabaiga` | `datetime` | `S` | `4` | `open` | — | Darbų pabaigos laiko žyma | — |
| `bendra_trukme_h` | `integer` | `h` | `4` | `open` | — | Bendra darbų tvarkymo trukmė valandomis, nurodanti skirtumą tarp darbų pabaigos ir pranešimo registracijos laiko žymų. | — |
| `gedimo_priezastis` | `string` | — | `4` | `open` | — | Gedimo priežastis, identifikuojama darbus atlikusio darbuotojo | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `iskvietimo_priezastis` | `"K.V.skaitiklio plombavimas"` | — | — | — | — |
| `iskvietimo_priezastis` | `"Sugedęs KV skaitiklis"` | — | — | — | — |
| `iskvietimo_priezastis` | `"KITA"` | — | — | — | — |
| `iskvietimo_priezastis` | `"K.V.skaitiklio keitimas (montavimas)"` | — | — | — | — |
| `iskvietimo_priezastis` | `"Nutekėjimai KV sistemoje"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ast/konsultacijos.csv
