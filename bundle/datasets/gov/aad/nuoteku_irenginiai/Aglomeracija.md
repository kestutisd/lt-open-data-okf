---
type: Table
title: "Aglomeracija — Preliminarios nuotekų tvarkymo sistemų aglomeracijų ribos"
description: "Duomenys pateikiami iš aplinkos apsaugos departamento nuotekų tvarkymo informacinės sistemos."
resource: "https://get.data.gov.lt/datasets/gov/aad/nuoteku_irenginiai/Aglomeracija"
tags: [gov, aad, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aad/nuoteku_irenginiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aad/nuoteku_irenginiai.csv#L42"
    last_modified: "2026-11-11T14:39:20Z"
---

# Aglomeracija — Preliminarios nuotekų tvarkymo sistemų aglomeracijų ribos

Duomenys pateikiami iš aplinkos apsaugos departamento nuotekų tvarkymo informacinės sistemos. Šioje lentelėje pateikiamos preliminarios nuotekų tvarkymo sistemų aglomeracijų ribos. Lentelėje galima rasti ne tik aglomeracijų ribas, bet ir jos dydi, gyventojų skaičių, gyventojų tankumą. Aglomeracijų lentelėje viena eilutė atitinka vieną preliminarią aglomeraciją. Duomenų aprėptis – visa Lietuva.

Duomenų teikėjas: Aplinkos apsaugos departamentas prie Aplinkos ministerijos

- **Model:** `datasets/gov/aad/nuoteku_irenginiai/Aglomeracija`[^manifest]
- **Dataset:** [Nuotekų valymo įrenginiai bei jų kokacijos](../nuoteku_irenginiai.md) (`datasets/gov/aad/nuoteku_irenginiai`)
- **Manifest CSV:** [datasets/gov/aad/nuoteku_irenginiai.csv#L42](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aad/nuoteku_irenginiai.csv#L42)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aad/nuoteku_irenginiai/Aglomeracija`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `aglomeracijos_id` | `string` | — | `4` | `open` | — | Aglomeracijos Identifikatorius | — |
| `teritorijos_pavadinimas` | `string` | — | `4` | `open` | — | Teritorijos pavadinimas | — |
| `gyventoju_sk` | `integer` | — | `4` | `open` | — | Gyventojų skaičius | — |
| `gyventoju_tankumas` | `integer` | — | `4` | `open` | — | Gyventojų tankumas | — |
| `plotas` | `number` | `km^2` | `4` | `open` | — | Aglomeracijos plotas | — |
| `geometrija` | `geometry(multipolygon, 3346)` | — | `4` | `open` | — | Geometrija (teritorija) | — |
| `informacijos_aktualumas` | `string` | — | `4` | `open` | — | Informacijos aktualumas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aad/nuoteku_irenginiai.csv
