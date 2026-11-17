---
type: Table
title: "Paraiska — Švietimo mainų paramos fondo paraiškos"
description: "Rinkinyje pateikiami VšĮ Švietimo mainų paramos fondo nuo 2023 m. kaupiami ir saugomi pateiktų paraiškų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/smpf/pateiktos_paraiskos/Paraiska"
tags: [gov, smpf, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/smpf/pateiktos_paraiskos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/smpf/pateiktos_paraiskos.csv#L9"
    last_modified: "2026-11-11T14:39:20Z"
---

# Paraiska — Švietimo mainų paramos fondo paraiškos

Rinkinyje pateikiami VšĮ Švietimo mainų paramos fondo nuo 2023 m. kaupiami ir saugomi pateiktų paraiškų duomenys. Rinkinio lentelę sudaro į Lietuvoje organizuojamus renginius pateiktų paraiškų duomenys. Viena eilutė atitinka vieną paraišką.

- **Model:** `datasets/gov/smpf/pateiktos_paraiskos/Paraiska`[^manifest]
- **Dataset:** [Švietimo mainų paramos fondo paraiškos ir lektorių programos](../pateiktos_paraiskos.md) (`datasets/gov/smpf/pateiktos_paraiskos`)
- **Manifest CSV:** [datasets/gov/smpf/pateiktos_paraiskos.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/smpf/pateiktos_paraiskos.csv#L9)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/smpf/pateiktos_paraiskos/Paraiska`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `paraiskos_nr` | `string` | — | `4` | `open` | — | Paraiškos numeris | — |
| `prasymas_pateiktas` | `date` | `D` | `4` | `open` | — | Prašymo pateikimo data | — |
| `prasymas_patvirtintas` | `date` | `D` | `4` | `open` | — | Prašymo patvirtinimo data | — |
| `prasymo_statusas` | `string` | — | `4` | `open` | — | Prašymo statusas | — |
| `komentaras_lt` | `string` | — | `2` | `open` | — | Kometaras | — |
| `vardas_pavarde` | `string` | — | `4` | `open` | — | Pareiškėjo vardas pavardė | — |
| `pareiskejo_institucija` | `string` | — | `4` | `open` | — | Pareiškėjo įstaiga | — |
| `pareiskejo_pareigos` | `string` | — | `4` | `open` | — | Pareiškėjo pareigos | — |
| `kvietimo_pav_lt` | `string` | — | `2` | `open` | — | Kvietimo/šaukimo pavadinimas | — |
| `vietos_tipas` | `string` | — | `4` | `open` | — | Renginio vietos tipas | — |
| `renginio_salis` | `string` | — | `4` | `open` | — | Renginio šalis | — |
| `renginio_miestas` | `string` | — | `4` | `open` | — | Renginio miestas | — |
| `renginio_pradzia` | `date` | `D` | `4` | `open` | — | Renginio pradžios data | — |
| `renginio_pabaiga` | `date` | `D` | `4` | `open` | — | Renginio pabaigosdata | — |
| `duomenu_atnaujinimas` | `date` | `D` | `4` | `open` | — | Paskutinio duomenų atnaujinimo data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `komentaras_lt` | `update(property: "komentaras_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `kvietimo_pav_lt` | `update(property: "kvietimo_pav_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/smpf/pateiktos_paraiskos.csv
