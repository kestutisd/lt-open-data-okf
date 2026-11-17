---
type: Table
title: "Pavyzdys — Saugiųjų dokumentų ir blankų pavyzdžių sąrašas"
description: "Valstybės saugiųjų dokumentų ir saugiųjų dokumentų blankų, tokių kaip tokių kaip pasai, asmens tapatybės kortelės, kelionės dokumentai, vairuotojo pažymėjimai, akcizais apmokestinamų prekių banderolės, aukštojo mokslo diplomai ir kt...."
resource: "https://get.data.gov.lt/datasets/gov/vdtat/saugiuju_dokumentu_registras/Pavyzdys"
tags: [gov, vdtat, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vdtat/saugiuju_dokumentu_registras.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L32"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pavyzdys — Saugiųjų dokumentų ir blankų pavyzdžių sąrašas

Valstybės saugiųjų dokumentų ir saugiųjų dokumentų blankų, tokių kaip tokių kaip pasai, asmens tapatybės kortelės, kelionės dokumentai, vairuotojo pažymėjimai, akcizais apmokestinamų prekių banderolės, aukštojo mokslo diplomai ir kt., pavyzdžių sąrašas

- **Model:** `datasets/gov/vdtat/saugiuju_dokumentu_registras/Pavyzdys`[^manifest]
- **Dataset:** [Saugiųjų dokumentų ir saugiųjų dokumentų blankų registro duomenys](../saugiuju_dokumentu_registras.md) (`datasets/gov/vdtat/saugiuju_dokumentu_registras`)
- **Manifest CSV:** [datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L32](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L32)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vdtat/saugiuju_dokumentu_registras/Pavyzdys`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Eilutės identifikatorius | — |
| `pavyzdzio_id` | `string` | — | `4` | `open` | — | Dokumento blanko ar pavyzdžio identifikatorius | — |
| `dokumento_ar_blanko_id` | `string` | — | `4` | `open` | — | Dokumento ar blanko identifikatorius | — |
| `dokumento_pavadinimas` | `string` | — | `4` | `open` | — | Dokumento ar blanko pavadinimas | — |
| `istaigos_isleidziancios_dokumenta_pavadinimas` | `string` | — | `4` | `open` | — | Įstaigos išleidžiančios dokumentą ar blanką pavadinimas | — |
| `nuoroda_i_dokumento_pavyzdi` | `string` | — | `4` | `open` | — | Nuoroda į dokumento pavyzdį | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vdtat/saugiuju_dokumentu_registras.csv
