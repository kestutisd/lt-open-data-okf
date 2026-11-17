---
type: Table
title: "VeikliojiMedziaga — Produktų veikliosios medžiagos"
description: "Lentelė „Produktų veikliosios medžiagos“."
resource: "https://get.data.gov.lt/datasets/gov/lsd/nvsc/bpdb/VeikliojiMedziaga"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/nvsc/bpdb.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nvsc/bpdb.csv#L14"
    last_modified: "2026-11-11T14:39:20Z"
---

# VeikliojiMedziaga — Produktų veikliosios medžiagos

Lentelė „Produktų veikliosios medžiagos“. Lentelę sudaro: negrįžtamai šifruoti produkto ir medžiagos identifikatoriai, medžiagos CAS numeris, pavadinimas ir koncentracija. Vienas įrašas atitinka vieną produkto ir vienos veikliosios medžiagos kombinaciją. Kadangi viename produkte gali būti kelios veikliosios medžiagos, to paties produkto įrašas kartojasi tiek kartų, kiek jame yra veikliųjų medžiagų, ir kiekvienas to paties produkto įrašas atitinka to paties produkto ir skirtingos veikliosios medžiagos kombinaciją. Pvz., jeigu produkte yra 3 veikliosios medžiagos, to paties produkto įrašas kartotis atitinkamai 3 kartus.

- **Model:** `datasets/gov/lsd/nvsc/bpdb/VeikliojiMedziaga`[^manifest]
- **Dataset:** [Biocidinių produktų duomenys](../bpdb.md) (`datasets/gov/lsd/nvsc/bpdb`)
- **Manifest CSV:** [datasets/gov/lsd/nvsc/bpdb.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nvsc/bpdb.csv#L14)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/nvsc/bpdb/VeikliojiMedziaga`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `produkto_id` | `string` | — | `4` | `open` | — | Išorinis raktas į produktą | — |
| `medziagos_id` | `string` | — | `4` | `open` | — | Išorinis raktas į veikliąją medžiagą | — |
| `medziagos_cas_nr` | `string` | — | `4` | `open` | — | Veikliosios medžiagos CAS numeris | — |
| `medziagos_pav` | `string` | — | `3` | `open` | — | Veikliosios medžiagos pavadinimas | — |
| `medziagos_konc` | `number` | `%` | `4` | `open` | — | Veikliosios medžiagos koncentracija produkte | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/nvsc/bpdb.csv
