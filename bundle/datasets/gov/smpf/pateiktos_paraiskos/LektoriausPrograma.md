---
type: Table
title: "LektoriausPrograma — Švietimo mainų paramos fondo lektorių siūlomos programos"
description: "Rinkinyje pateikiami VšĮ Švietimo mainų paramos fondo nuo 2023 m. kaupiami ir saugom lektorių siūlomų programų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/smpf/pateiktos_paraiskos/LektoriausPrograma"
tags: [gov, smpf, lektoriausprograma, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/smpf/pateiktos_paraiskos.csv#L29"
    title: "atviriduomenys/manifest — datasets/gov/smpf/pateiktos_paraiskos.csv#L29"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2825/"
    title: "data.gov.lt DCAT-AP — datasets/gov/smpf/pateiktos_paraiskos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# LektoriausPrograma — Švietimo mainų paramos fondo lektorių siūlomos programos

Rinkinyje pateikiami VšĮ Švietimo mainų paramos fondo nuo 2023 m. kaupiami ir saugom lektorių siūlomų programų duomenys. Lentelę sudaro į Lietuvoje organizuojamus renginius Lietuvos dėstytojų / lektorių siūlomos programos. Viena duomenų rinkinio eilutė atitinka vieną dėstytojo programą.[^manifest]

- **Model:** `datasets/gov/smpf/pateiktos_paraiskos/LektoriausPrograma`[^manifest]
- **Dataset:** [Švietimo mainų paramos fondo paraiškos ir lektorių programos](../pateiktos_paraiskos.md) (`datasets/gov/smpf/pateiktos_paraiskos`)[^manifest]
- **Manifest CSV:** [datasets/gov/smpf/pateiktos_paraiskos.csv#L29](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/smpf/pateiktos_paraiskos.csv#L29)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/smpf/pateiktos_paraiskos/LektoriausPrograma` (`deployed`)[^manifest]
- **Provider:** `smpf` — VšĮ Švietimo mainų paramos fondas (SMPF) *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `paraiskos_nr` | `string` | — | `4` | `open` | — | Paraiškos numeris | — |
| `vardas_pavarde` | `string` | — | `4` | `open` | — | Lektoriaus vardas pavardė | — |
| `salis` | `string` | — | `4` | `open` | — | Lektoriaus šalis | — |
| `pareigos` | `string` | — | `4` | `open` | — | Lektoriaus pareigos | — |
| `istaiga` | `string` | — | `4` | `open` | — | Lektoriaus įstaiga | — |
| `destomas_dalykas` | `string` | — | `4` | `open` | — | lektoriaus dėstomas dalykas/modulis | — |
| `programos_aprasymas` | `string` | — | `2` | `open` | — | Programos aprašymas | — |
| `valstybinis_prog_kodas` | `string` | — | `4` | `open` | — | Programos valstybinis kodas | — |
| `veiklos_aprasymas` | `string` | — | `2` | `open` | — | Veiklos aprašymas | — |
| `veiklos_trukme` | `integer` | — | `4` | `open` | — | Veiklos trukmė | — |
| `eksperto_ivertinimas` | `integer` | — | `4` | `open` | — | Lektoriaus programos įvertinimas (vertina ekspertas) | — |
| `statusas` | `string` | — | `4` | `open` | — | Įvertinimo statusas | — |
| `duomenu_atnaujinimas` | `date` | `D` | `4` | `open` | — | Paskutinio duomenų atnaujinimo data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `valstybinis_prog_kodas` | `update(property: "valstybinis_prog_kodas[]", type: "array", source: "valstybinis_prog_kodas")` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/smpf/pateiktos_paraiskos.csv#L29 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/smpf/pateiktos_paraiskos.csv#L29)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/smpf/pateiktos_paraiskos (https://data.gov.lt/datasets/2825/)
