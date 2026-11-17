---
type: Table
title: "InstitucijosDarbuotojas — Rokiškio savivaldybės darbuotojai"
description: "Spinta table datasets/gov/rokiskio_r_sav/institucijos_darbuotojai/InstitucijosDarbuotojas (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rokiskio_r_sav/institucijos_darbuotojai/InstitucijosDarbuotojas"
tags: [gov, rokiskio_r_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rokiskio_r_sav/institucijos_darbuotojai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rokiskio_r_sav/institucijos_darbuotojai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# InstitucijosDarbuotojas — Rokiškio savivaldybės darbuotojai

- **Model:** `datasets/gov/rokiskio_r_sav/institucijos_darbuotojai/InstitucijosDarbuotojas`[^manifest]
- **Dataset:** [Rokiškio savivaldybės darbuotojai](../institucijos_darbuotojai.md) (`datasets/gov/rokiskio_r_sav/institucijos_darbuotojai`)
- **Manifest CSV:** [datasets/gov/rokiskio_r_sav/institucijos_darbuotojai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rokiskio_r_sav/institucijos_darbuotojai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rokiskio_r_sav/institucijos_darbuotojai/InstitucijosDarbuotojas`
- **Primary Key (`ref`):** `tabelio_nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tabelio_nr` | `string` | — | `4` | `open` | — | Darbuotojo unikalus tabelio numeris | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Asmens kodas unikaliai šfruotas šiam rinkiniui (su kitais rinkiniais nesijungia) | — |
| `ak_validacija` | `string` | — | `4` | `open` | — | Ar asmens kodas validus | — |
| `lytis_ak` | `string` | — | `4` | `open` | — | Asmens lytis iš asmens kodo | — |
| `gim_desimtm_ak` | `date` | `Y` | `4` | `open` | — | Asmens gimimo metai iš asmens kodo | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `gim_desimtm` | `date` | `Y` | `4` | `open` | — | Gimimo metai | — |
| `darbo_pradzia` | `date` | `D` | `4` | `open` | — | Darbo pradžios data | — |
| `darbo_pabaiga` | `date` | `D` | `4` | `open` | — | Darbo pabaigos data | — |
| `skyrius` | `string` | — | `4` | `open` | — | Skyriaus pavadinimas | — |
| `institucija` | `string` | — | `4` | `open` | — | Institucijos pavadinimas | — |
| `imones_kodas` | `string` | — | `4` | `open` | — | Įmonės kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rokiskio_r_sav/institucijos_darbuotojai.csv
