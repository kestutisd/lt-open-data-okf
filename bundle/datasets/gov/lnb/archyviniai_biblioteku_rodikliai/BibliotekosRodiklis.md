---
type: Table
title: "BibliotekosRodiklis — Archyviniai bibliotekų statistikos rodikliai"
description: "Rinkinyje pateikiami pagrindiniai šalies bibliotekų veiklos rezultatai ir rodikliai nuo 2007 iki 2023 metų pagal savivaldybę, rajoną, biblioteką."
resource: "https://get.data.gov.lt/datasets/gov/lnb/archyviniai_biblioteku_rodikliai/BibliotekosRodiklis"
tags: [gov, lnb, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lnb/archyviniai_biblioteku_rodikliai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/archyviniai_biblioteku_rodikliai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# BibliotekosRodiklis — Archyviniai bibliotekų statistikos rodikliai

Rinkinyje pateikiami pagrindiniai šalies bibliotekų veiklos rezultatai ir rodikliai nuo 2007 iki 2023 metų pagal savivaldybę, rajoną, biblioteką.

- **Model:** `datasets/gov/lnb/archyviniai_biblioteku_rodikliai/BibliotekosRodiklis`[^manifest]
- **Dataset:** [Archyviniai bibliotekų statistikos rodikliai](../archyviniai_biblioteku_rodikliai.md) (`datasets/gov/lnb/archyviniai_biblioteku_rodikliai`)
- **Manifest CSV:** [datasets/gov/lnb/archyviniai_biblioteku_rodikliai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/archyviniai_biblioteku_rodikliai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lnb/archyviniai_biblioteku_rodikliai/BibliotekosRodiklis`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `metai` | `integer` | — | `4` | `open` | — | Rodiklio statistikos metai | — |
| `biblioteka` | `string` | — | `4` | `open` | — | Bibliotekos pavadinimas | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Teritorijos pavadinimas | — |
| `apskritis` | `string` | — | `2` | `open` | — | Apskrities pavadinimas | — |
| `rodiklio_grupe` | `string` | — | `4` | `open` | — | Rodiklio grupė, jungianti kelis rodiklius | — |
| `rodiklio_kodas` | `string` | — | `4` | `open` | — | Rodiklio sutrumpintas kodas | — |
| `rodiklio_aprasymas` | `string` | — | `4` | `open` | — | Rodiklio aprašymas | — |
| `reiksme` | `integer` | — | `4` | `open` | — | Rodiklio reikšmė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lnb/archyviniai_biblioteku_rodikliai.csv
