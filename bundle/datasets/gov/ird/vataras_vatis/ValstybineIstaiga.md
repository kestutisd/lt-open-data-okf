---
type: Table
title: "ValstybineIstaiga — Valstybės ir savivaldybių institucijos bei įstaigos, jų pavaldumas"
description: "Aktualus ir išsamus valstybės ir savivaldybių institucijų bei įstaigų sąrašas, šių įstaigų pavaldumas viena kitai."
resource: "https://get.data.gov.lt/datasets/gov/ird/vataras_vatis/ValstybineIstaiga"
tags: [gov, ird, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ird/vataras_vatis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/vataras_vatis.csv#L33"
    last_modified: "2026-11-11T14:39:20Z"
---

# ValstybineIstaiga — Valstybės ir savivaldybių institucijos bei įstaigos, jų pavaldumas

Aktualus ir išsamus valstybės ir savivaldybių institucijų bei įstaigų sąrašas, šių įstaigų pavaldumas viena kitai. Duomenų šaltinis - VATIS ir VATARAS. Pateikiamos tik šiuo metu egzistuojančios įstaigos.

- **Model:** `datasets/gov/ird/vataras_vatis/ValstybineIstaiga`[^manifest]
- **Dataset:** [Valstybės tarnautojų registras, Valstybės tarnybos valdymo informacinė sistema](../vataras_vatis.md) (`datasets/gov/ird/vataras_vatis`)
- **Manifest CSV:** [datasets/gov/ird/vataras_vatis.csv#L33](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/vataras_vatis.csv#L33)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/vataras_vatis/ValstybineIstaiga`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `2` | `open` | — | Unikalus įstaigos identifikatorius | — |
| `pavaldumas_id` | `string` | — | `2` | `open` | — | Įstaigos, kuriai pavaldi šį įstaiga, identifikatorius | — |
| `jar_kodas` | `string` | — | `2` | `open` | — | Įstaigos Juridinių asmenų registro (JAR) kodas | — |
| `pavadinimas` | `string` | — | `2` | `open` | — | Įstaigos pavadinimas | — |
| `sutrumpintas_pavadinimas` | `string` | — | `4` | `open` | — | Įstaigos sutrumpintas pavadinimas | — |
| `istaigu_grupe` | `string` | — | `3` | `open` | — | Įstaigų grupė, kuriai priklauso šį įstaiga | — |
| `adresas` | `string` | — | `2` | `open` | — | Įstaigos adresas | — |
| `web` | `url` | — | `4` | `open` | — | Įstaigos interneto svetainės adresas | — |
| `el_pastas` | `string` | — | `4` | `open` | — | Įstaigos elektroninio pašto adresas | — |
| `isteigta` | `date` | `D` | `2` | `open` | — | Įstaigos įsteigimo data | — |
| `atnaujinimas` | `date` | `D` | `4` | `open` | — | Naujausio įrašo arba modifikacijos data gaunamuose duomenyse | Paruošiamas imant naujausio įrašo originaliuose duomenyse datą |

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/vataras_vatis.csv
