---
type: Table
title: "SakiuRajonas — Šakių rajono savivaldybės kapinių kapaviečių duomenys"
description: "Spinta table datasets/gov/kapines/registras/kapavietes/SakiuRajonas (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/kapines/registras/kapavietes/SakiuRajonas"
tags: [gov, kapines, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kapines/kapavietes.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kapines/kapavietes.csv#L955"
    last_modified: "2026-11-11T14:39:20Z"
---

# SakiuRajonas — Šakių rajono savivaldybės kapinių kapaviečių duomenys

- **Model:** `datasets/gov/kapines/registras/kapavietes/SakiuRajonas`[^manifest]
- **Dataset:** [Duomenys apie kapavietes savivaldybių kapinėse](../kapavietes.md) (`datasets/gov/kapines/registras/kapavietes`)
- **Manifest CSV:** [datasets/gov/kapines/kapavietes.csv#L955](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kapines/kapavietes.csv#L955)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kapines/registras/kapavietes/SakiuRajonas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `kapines` | `string` | — | `4` | `open` | — | Kapavietės kapinių pavadinimas | — |
| `kapo_id` | `string` | — | `4` | `open` | — | Kapavietės identifikatorius | — |
| `kapavietes_dydis` | `number` | `m^2` | `4` | `open` | — | Kapavietės plotas | — |
| `matavimo_vnt` | `string` | — | `3` | `open` | — | Ploto matavimo vienetai | — |
| `palaidotu_sk` | `integer` | `U` | `4` | `open` | — | Kapavietėje palaidotų velionių skaičius | — |
| `maks_velioniu_sk` | `integer` | `U` | `4` | `open` | — | Maksimalus leidžiamas kapavietėje laidoti velionių skaičius | — |
| `tipas` | `string` | — | `4` | `open` | — | Kapavietės tipas | Gali būti kapavietė arba kolumbariumas |
| `ilgis_m` | `number` | `m` | `4` | `open` | — | Kapavietės ilgis, nurodytas metrais. | Kai kapavietės tipas kolumbariumas, stulpelis įgija reikšmę "1". |
| `plotis_m` | `number` | `m` | `4` | `open` | — | Kapavietės plotis, nurodytas metrais | — |
| `geometrija` | `geometry(3857)` | — | `4` | `open` | — | Kapavietės vietos taško koordinatės pagal WGS84 / Pseudo-Mercator koordinačių sistemą. | — |
| `ar_nestandartinis_dydis` | `boolean` | — | `4` | `open` | — | Požymis, ar kapavietė yra nestandartinio dydžio | — |
| `ar_kulturos_paveldas` | `boolean` | — | `4` | `open` | — | Požymis, ar kapavietė yra kultūros paveldo objektas | — |
| `paveldo_kodas` | `string` | — | `4` | `open` | — | Jei kapavietė yra kultūros paveldo objektas, nurodomas paveldo kodas. | — |
| `paveldo_aprasymas_lt` | `string` | — | `2` | `open` | — | Jei kapavietė yra kultūros paveldo objektas, nurodomas aprašymas. | — |
| `pastaba_lt` | `string` | — | `2` | `open` | — | Papildomos pastabos apie kapavietę | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"kapavietė"` | — | — | — | — |
| `tipas` | `"kolumbariumas"` | — | — | Kolumbariumo niša | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paveldo_aprasymas_lt` | `update(property: "paveldo_aprasymas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `pastaba_lt` | `update(property: "pastaba_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kapines/kapavietes.csv
