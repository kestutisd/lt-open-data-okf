---
type: Table
title: "Artefaktas — Seimo Kanceliarijos įvairialypės informacijos archyvų duomenys"
description: "Rinkinyje pateikiami duomenys apie Seimo Kanceliarijos archyvuose saugomus vaizdo, teksto ar garso artefaktus nuo XVI amžiaus iki šių dienų."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/archyviniai/Artefaktas"
tags: [gov, lrsk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lrsk/archyviniai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/archyviniai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Artefaktas — Seimo Kanceliarijos įvairialypės informacijos archyvų duomenys

Rinkinyje pateikiami duomenys apie Seimo Kanceliarijos archyvuose saugomus vaizdo, teksto ar garso artefaktus nuo XVI amžiaus iki šių dienų. Nurodoma artefakto vieta, kategorija, aprašymas, kalba, tema, pradžios ir pabaigos datos (jei taikoma) ir nuoroda, jei artefakto turinys prieinamas internete.

- **Model:** `datasets/gov/lrsk/archyviniai/Artefaktas`[^manifest]
- **Dataset:** [Seimo Kanceliarijos įvairialypės informacijos archyvų duomenys](../archyviniai.md) (`datasets/gov/lrsk/archyviniai`)
- **Manifest CSV:** [datasets/gov/lrsk/archyviniai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/archyviniai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/archyviniai/Artefaktas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Pilnas objekto pavadinimas. | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Objekto dalies aprašymas, pvz., kas ir kada kalbėjo posėdyje. | — |
| `nuo_lt` | `string` | — | `4` | `open` | — | Su objektu susijusio įvykio data, o ne saugojimo, įkėlimo ar pan. Gali būti pasirenkama iš kalendorius. Pilna reikšmė - data ir laikas, sekundžių tikslumu. Galima nurodyti ir nepilną datą (pavyzdžiui, tik metus). | — |
| `iki_lt` | `string` | — | `4` | `open` | — | Su objektu susijusio įvykio data, o ne saugojimo, įkėlimo ar pan. Gali būti pasirenkama iš kalendorius. Pilna reikšmė - data ir laikas, sekundžių tikslumu. Galima nurodyti ir nepilną datą (pavyzdžiui, tik metus). | — |
| `vieta` | `string` | — | `4` | `open` | — | Nurodoma objekto vieta. | — |
| `kategorija` | `string` | — | `4` | `open` | — | Pilnas objekto kategorijos pavadinimas. | — |
| `tipas` | `string` | — | `4` | `open` | — | Patikslintas kategorijos pavadinimas. | — |
| `potipis` | `string` | — | `4` | `open` | — | Objekto potipis. | — |
| `nuoroda_pav` | `string` | — | `4` | `open` | — | Nuorodos pavadinimas. | — |
| `nuoroda` | `string` | — | `4` | `open` | — | Nuoroda į objekto vietą LRS portale. | — |
| `kalba` | `string` | — | `4` | `open` | — | Nurodoma objekto kalba (-os). | — |
| `tema` | `string` | — | `4` | `open` | — | Klasifikatorius, naudojamas nurodyti objekto temas. | Temų hierarchija. Pastaba: Dalis objektų temų bus sudaromos ir patvirtinamos oficialiai (pvz., Fotodokumentų, saugomų seimo archyve, sisteminimo klasifikatorius, tvirtinamas Seimo kanclerio), tačiau dalį temų bus leidžiama įvesti laisvai (pvz., Parlamentarizmo istorijos ir įamžinimo skyriaus darbuotojams). |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `kategorija` | `"Vaizdas"` | — | — | — | — |
| `kategorija` | `"Tekstas"` | — | — | — | — |
| `kategorija` | `"Garso įrašas"` | — | — | — | — |
| `kategorija` | `"Vaizdo įrašas"` | — | — | — | — |
| `tipas` | `"Skaitmenintas popierinis dokumentas"` | — | — | — | — |
| `tipas` | `"Vaizdo įrašas"` | — | — | — | — |
| `tipas` | `"Garso įrašas"` | — | — | — | — |
| `tipas` | `"Fotodokumentas"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nuo_lt` | `update(property: "nuo_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `iki_lt` | `update(property: "iki_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `kalba` | `"update(property: ""kalba[]"", type: ""array"", source: ""Kalba"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/archyviniai.csv
