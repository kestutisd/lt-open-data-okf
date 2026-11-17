---
type: Table
title: "AdminZodis — Administracinės lietuvių kalbos žodžiai ir kiti reiškiniai"
description: "Lentelėje pateikta dalis lietuvių administracinėje kalboje aptinkamų probleminių žodžių ir kitų kalbos reiškinių su jų vartosenos paaiškinimais iš Lietuvių kalbos instituto (LKI) Administracinės kalbos aktualijų duomenų bazės, kuriai..."
resource: "https://get.data.gov.lt/datasets/gov/lki/zodziai_administracineje_kalboje/AdminZodis"
tags: [gov, lki, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lki/zodziai_administracineje_kalboje.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/zodziai_administracineje_kalboje.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# AdminZodis — Administracinės lietuvių kalbos žodžiai ir kiti reiškiniai

Lentelėje pateikta dalis lietuvių administracinėje kalboje aptinkamų probleminių žodžių ir kitų kalbos reiškinių su jų vartosenos paaiškinimais iš Lietuvių kalbos instituto (LKI) Administracinės kalbos aktualijų duomenų bazės, kuriai duomenys rinkti iš verstinių Europos Sąjungos dokumentų.

Pirmą kartą duomenys surinkti 2014 m. Kiti šių duomenų atnaujinimai galimi ateityje, Lietuvių kalbos institutui vykdant papildomus duomenų rinkimo projektus.

- **Model:** `datasets/gov/lki/zodziai_administracineje_kalboje/AdminZodis`[^manifest]
- **Dataset:** [Administracinės lietuvių kalbos žodžiai ir kiti reiškiniai](../zodziai_administracineje_kalboje.md) (`datasets/gov/lki/zodziai_administracineje_kalboje`)
- **Manifest CSV:** [datasets/gov/lki/zodziai_administracineje_kalboje.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/zodziai_administracineje_kalboje.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lki/zodziai_administracineje_kalboje/AdminZodis`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `zodis` | `string` | — | `4` | `open` | — | Žodis ar kitas kalbos reiškinys | — |
| `paaiskinimas_lt` | `string` | — | `4` | `open` | — | Žodžio ar kito kalbos reiškinio vartosenos paaiškinimas (pateiktas grynojo teksto formatu) | — |
| `paaiskinimas_html_lt` | `string` | — | `4` | `open` | — | Žodžio ar kito kalbos reiškinio vartosenos paaiškinimas (pateiktas html formatu) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paaiskinimas_lt` | `update(property: "paaiskinimas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `paaiskinimas_html_lt` | `update(property: "paaiskinimas_html_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lki/zodziai_administracineje_kalboje.csv
