---
type: Table
title: "ApsaugosPriemone — Saugiųjų dokumentų ir blankų apsaugos priemonių sąrašas"
description: "Valstybės saugiųjų dokumentų ir saugiųjų dokumentų blankų, tokių kaip tokių kaip pasai, asmens tapatybės kortelės, kelionės dokumentai, vairuotojo pažymėjimai, akcizais apmokestinamų prekių banderolės, aukštojo mokslo diplomai ir kt...."
resource: "https://get.data.gov.lt/datasets/gov/vdtat/saugiuju_dokumentu_registras/ApsaugosPriemone"
tags: [gov, vdtat, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vdtat/saugiuju_dokumentu_registras.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L40"
    last_modified: "2026-11-11T14:39:20Z"
---

# ApsaugosPriemone — Saugiųjų dokumentų ir blankų apsaugos priemonių sąrašas

Valstybės saugiųjų dokumentų ir saugiųjų dokumentų blankų, tokių kaip tokių kaip pasai, asmens tapatybės kortelės, kelionės dokumentai, vairuotojo pažymėjimai, akcizais apmokestinamų prekių banderolės, aukštojo mokslo diplomai ir kt., apsaugos priemonių sąrašas

- **Model:** `datasets/gov/vdtat/saugiuju_dokumentu_registras/ApsaugosPriemone`[^manifest]
- **Dataset:** [Saugiųjų dokumentų ir saugiųjų dokumentų blankų registro duomenys](../saugiuju_dokumentu_registras.md) (`datasets/gov/vdtat/saugiuju_dokumentu_registras`)
- **Manifest CSV:** [datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L40](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L40)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vdtat/saugiuju_dokumentu_registras/ApsaugosPriemone`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Eilutės identifikatorius | — |
| `priemones_id` | `string` | — | `4` | `open` | — | Dokumento ar blanko apsaugos priemonės identifikatorius | — |
| `dokumento_ar_blanko_id` | `string` | — | `4` | `open` | — | Dokumento ar blanko identifikatorius | — |
| `dokumento_pavadinimas` | `string` | — | `4` | `open` | — | Dokumento ar blanko pavadinimas | — |
| `istaigos_isleidziancios_dokumenta_pavadinimas` | `string` | — | `4` | `open` | — | Įstaigos išleidžiančios dokumentą ar blanką pavadinimas | — |
| `nuoroda_i_apsaugos_priemones_pavyzdi` | `string` | — | `4` | `open` | — | Nuoroda į apsaugos priemonės pavyzdį | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vdtat/saugiuju_dokumentu_registras.csv
