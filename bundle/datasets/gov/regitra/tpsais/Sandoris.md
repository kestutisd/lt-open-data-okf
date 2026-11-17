---
type: Table
title: "Sandoris — Transporto priemonių sandorių duomenys"
description: "AB „Regitra“ Transporto priemonių savininkų apskaitos informacinė sistema kaupia transporto priemonių (toliau TP) savininkų bei jų vykdytų sandorių duomenis."
resource: "https://get.data.gov.lt/datasets/gov/regitra/tpsais/Sandoris"
tags: [gov, regitra, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/regitra/tpsais.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/tpsais.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sandoris — Transporto priemonių sandorių duomenys

AB „Regitra“ Transporto priemonių savininkų apskaitos informacinė sistema kaupia transporto priemonių (toliau TP) savininkų bei jų vykdytų sandorių duomenis. Duomenys kaupiami nuo 2021-05-01 ir yra atnaujinami. Duomenų rinkinys sudarytas iš pseudonimizuotų dokumento identifikatoriaus bei išorinio rakto į sisteminę veiklą, iš dokumento rūšies, nurodančios santorio pobūdį, dokumento išdavimo datos, sandorio šalies, sumos, valiutos, atsiskaitymo būdo bei įrašo modifikavimo laiko. Vienas įrašas rinkinyje atitinka vieną sandorio dokumentą.

- **Model:** `datasets/gov/regitra/tpsais/Sandoris`[^manifest]
- **Dataset:** [Transporto priemonių sandorių duomenys](../tpsais.md) (`datasets/gov/regitra/tpsais`)
- **Manifest CSV:** [datasets/gov/regitra/tpsais.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/tpsais.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/regitra/tpsais/Sandoris`
- **Primary Key (`ref`):** `dok_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dok_id` | `string` | — | `4` | `open` | — | Pseudonimizuotas sandorio dokumento identifikatorius | — |
| `veiklos_id` | `string` | — | `4` | `open` | — | Pseudonimizuotas išorinis raktas į sisteminę veiklą | — |
| `dok_rusis` | `string` | — | `4` | `open` | — | Sandorio dokumento rūšis | — |
| `isd_data` | `datetime` | `D` | `4` | `open` | — | Dokumento išdavimo data | — |
| `salis` | `string` | — | `4` | `open` | — | Sandorio šalis | — |
| `suma` | `number` | — | `4` | `open` | — | Sandorio suma | — |
| `valiuta` | `string` | — | `4` | `open` | — | Sandorio valiuta | — |
| `mokejimo_budas` | `string` | — | `4` | `open` | — | Atsiskaitymo būdas sandoryje | — |
| `iraso_mod_data` | `datetime` | `S` | `4` | `open` | — | Įrašo modifikavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/regitra/tpsais.csv
