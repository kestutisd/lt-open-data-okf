---
type: Table
title: "VeikliojiMedziaga — Produktų veikliosios medžiagos"
description: "Lentelė „Produktų veikliosios medžiagos“."
resource: "https://get.data.gov.lt/datasets/gov/lsd/nvsc/bpdb/VeikliojiMedziaga"
tags: [gov, lsd, veikliojimedziaga, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nvsc/bpdb.csv#L14"
    title: "atviriduomenys/manifest — datasets/gov/lsd/nvsc/bpdb.csv#L14"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2917/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/nvsc/bpdb"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# VeikliojiMedziaga — Produktų veikliosios medžiagos

Lentelė „Produktų veikliosios medžiagos“. Lentelę sudaro: negrįžtamai šifruoti produkto ir medžiagos identifikatoriai, medžiagos CAS numeris, pavadinimas ir koncentracija. Vienas įrašas atitinka vieną produkto ir vienos veikliosios medžiagos kombinaciją. Kadangi viename produkte gali būti kelios veikliosios medžiagos, to paties produkto įrašas kartojasi tiek kartų, kiek jame yra veikliųjų medžiagų, ir kiekvienas to paties produkto įrašas atitinka to paties produkto ir skirtingos veikliosios medžiagos kombinaciją. Pvz., jeigu produkte yra 3 veikliosios medžiagos, to paties produkto įrašas kartotis atitinkamai 3 kartus.[^manifest]

- **Model:** `datasets/gov/lsd/nvsc/bpdb/VeikliojiMedziaga`[^manifest]
- **Dataset:** [Biocidinių produktų duomenys](../bpdb.md) (`datasets/gov/lsd/nvsc/bpdb`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/nvsc/bpdb.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nvsc/bpdb.csv#L14)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/nvsc/bpdb/VeikliojiMedziaga` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `produkto_id` | `string` | — | `4` | `open` | — | Išorinis raktas į produktą | — |
| `medziagos_id` | `string` | — | `4` | `open` | — | Išorinis raktas į veikliąją medžiagą | — |
| `medziagos_cas_nr` | `string` | — | `4` | `open` | — | Veikliosios medžiagos CAS numeris | — |
| `medziagos_pav` | `string` | — | `3` | `open` | — | Veikliosios medžiagos pavadinimas | — |
| `medziagos_konc` | `number` | `%` | `4` | `open` | — | Veikliosios medžiagos koncentracija produkte | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/nvsc/bpdb.csv#L14 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nvsc/bpdb.csv#L14)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/nvsc/bpdb (https://data.gov.lt/datasets/2917/)
