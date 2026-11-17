---
type: Table
title: "NuotekuDebitas — Nuotekų debitas"
description: "Alytaus rajono savivaldybės įmonės „Simno komunalininkas“ vedamoje nuotekų debitų apskaitoje fiksuojamas kiekviename valymo įrenginyje išvalytų buitinių nuotekų kiekis, skaičiuojamas kubiniais metrais per dieną."
resource: "https://get.data.gov.lt/datasets/gov/simno_komun/nuotekos/NuotekuDebitas"
tags: [gov, simno_komun, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/simno_komun/nuotekos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/nuotekos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# NuotekuDebitas — Nuotekų debitas

Alytaus rajono savivaldybės įmonės „Simno komunalininkas“ vedamoje nuotekų debitų apskaitoje fiksuojamas kiekviename valymo įrenginyje išvalytų buitinių nuotekų kiekis, skaičiuojamas kubiniais metrais per dieną. Duomenys nuo 2018 iki 2023 metų.

- **Model:** `datasets/gov/simno_komun/nuotekos/NuotekuDebitas`[^manifest]
- **Dataset:** [Nuotekų debitas](../nuotekos.md) (`datasets/gov/simno_komun/nuotekos`)
- **Manifest CSV:** [datasets/gov/simno_komun/nuotekos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/nuotekos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/simno_komun/nuotekos/NuotekuDebitas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `irenginys` | `string` | — | `4` | `open` | — | Įrenginys | — |
| `data` | `date` | `D` | `4` | `open` | — | Laikotarpis | — |
| `debitas_m3` | `number` | `m^3/d` | `4` | `open` | — | Atitekėjusių (ištekėjusių) nuotekų kiekis per dieną | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/simno_komun/nuotekos.csv
