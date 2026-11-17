---
type: Table
title: "JoniskioRajonas — Joniškio rajono savivaldybės kapinių kapaviečių duomenys"
description: "Spinta table datasets/gov/kapines/registras/kapavietes/JoniskioRajonas (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/kapines/registras/kapavietes/JoniskioRajonas"
tags: [gov, kapines, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kapines/kapavietes.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kapines/kapavietes.csv#L1070"
    last_modified: "2026-11-11T14:39:20Z"
---

# JoniskioRajonas — Joniškio rajono savivaldybės kapinių kapaviečių duomenys

- **Model:** `datasets/gov/kapines/registras/kapavietes/JoniskioRajonas`[^manifest]
- **Dataset:** [Duomenys apie kapavietes savivaldybių kapinėse](../kapavietes.md) (`datasets/gov/kapines/registras/kapavietes`)
- **Manifest CSV:** [datasets/gov/kapines/kapavietes.csv#L1070](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kapines/kapavietes.csv#L1070)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kapines/registras/kapavietes/JoniskioRajonas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `kapo_id` | `string` | — | `4` | `open` | — | Kapavietės identifikatorius | — |
| `kapavietes_dydis` | `number` | `m^2` | `4` | `open` | — | Kapavietės plotas | — |
| `matavimo_vnt` | `string` | — | `4` | `open` | — | Ploto matavimo vienetai | — |
| `kapines` | `string` | — | `4` | `open` | — | Kapavietės kapinių pavadinimas | — |
| `palaidotu_sk` | `integer` | `U` | `4` | `open` | — | Kapavietėje palaidotų velionių skaičius | — |
| `maks_velioniu_sk` | `integer` | `U` | `0` | `open` | — | Maksimalus leidžiamas kapavietėje laidoti velionių skaičius | — |
| `tipas` | `string` | — | `4` | `open` | — | Kapavietės tipas, nurodantis maksimalų laidojimo vietų skaičių. | — |
| `ilgis_m` | `number` | `m` | `4` | `open` | — | Kapavietės ilgis, nurodytas metrais. | — |
| `plotis_m` | `number` | `m` | `4` | `open` | — | Kapavietės plotis, nurodytas metrais | — |
| `geometrija` | `geometry(3857)` | — | `4` | `open` | — | Kapavietės koordinatės pagal WGS84 / Pseudo-Mercator koordinačių sistemą. | — |
| `ar_nestandartinis_dydis` | `boolean` | — | `4` | `open` | — | Požymis, ar kapavietė yra nestandartinio dydžio | — |
| `ar_kulturos_paveldas` | `boolean` | — | `4` | `open` | — | Požymis, ar kapavietė yra kultūros paveldo objektas | — |
| `paveldo_kodas` | `string` | — | `4` | `open` | — | Jei kapavietė yra kultūros paveldo objektas, nurodomas paveldo kodas. | — |
| `paveldo_aprasymas_lt` | `string` | — | `4` | `open` | — | Jei kapavietė yra kultūros paveldo objektas, nurodomas aprašymas. | — |
| `pastaba_lt` | `string` | — | `0` | `open` | — | Papildomos pastabos apie kapavietę | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"1"` | — | — | Vienvietis | — |
| `tipas` | `"2"` | — | — | Dvivietis | — |
| `tipas` | `"3"` | — | — | Trivietis | — |
| `tipas` | `"4"` | — | — | Keturvietis | — |
| `tipas` | `"5"` | — | — | Penkiavietis | — |
| `tipas` | `"6"` | — | — | Šešiavietis | — |
| `tipas` | `"7"` | — | — | Septynvietis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kapines/kapavietes.csv
