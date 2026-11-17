---
type: Table
title: "MaitinimoParaiska — VšĮ K. Griniaus slaugos ir palaikomojo gydymo ligoninės pacientų maitinimo paraiškos"
description: "Šiame duomenų rinkinyje pateikiami VšĮ K."
resource: "https://get.data.gov.lt/datasets/gov/kgspgl/maitinimo_paraiskos/MaitinimoParaiska"
tags: [gov, kgspgl, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kgspgl/kgspgl_paraiska.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kgspgl/kgspgl_paraiska.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# MaitinimoParaiska — VšĮ K. Griniaus slaugos ir palaikomojo gydymo ligoninės pacientų maitinimo paraiškos

Šiame duomenų rinkinyje pateikiami VšĮ K. Griniaus slaugos ir palaikomojo gydymo ligoninės (Kauno miesto savivaldybė) pacientų maitinimo paraiškų duomenys, kaupiami apskaitos programoje Progra – Apskaita.

Rinkinys apima informaciją apie pacientams skirtą maitinimą pagal padalinius, dienas, valgymus, dietas, patiekalus, porcijų kiekius bei patiekalų savikainą. Pateikiami duomenys nuo 2022 metų kovo mėnesio.

- **Model:** `datasets/gov/kgspgl/maitinimo_paraiskos/MaitinimoParaiska`[^manifest]
- **Dataset:** [VšĮ K. Griniaus slaugos ir palaikomojo gydymo ligoninės pacientų maitinimo paraiškos](../maitinimo_paraiskos.md) (`datasets/gov/kgspgl/maitinimo_paraiskos`)
- **Manifest CSV:** [datasets/gov/kgspgl/kgspgl_paraiska.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kgspgl/kgspgl_paraiska.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kgspgl/maitinimo_paraiskos/MaitinimoParaiska`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `diena` | `date` | `D` | `4` | `open` | — | Maitinimo data | — |
| `porciju_kiekis` | `integer` | — | `4` | `open` | — | Porcijų kiekis | — |
| `valgymas` | `string` | — | `4` | `open` | — | Valgymo pavadinimas | — |
| `norma` | `number` | — | `4` | `open` | — | Norma | Įsakymu nustatyta ligonių visos dienos maitinimo piniginė norma. |
| `valgantis_padalinys` | `string` | — | `4` | `open` | — | Valgančio padalinio pavadinimas | — |
| `patiekalas` | `string` | — | `4` | `open` | — | Atsargos pavadinimas | — |
| `patiekalo_grupe` | `string` | — | `4` | `open` | — | Grupės pavadinimas | — |
| `patiekalo_savikaina` | `number` | — | `4` | `open` | — | Atsargos savikaina | — |
| `dietos_pavadinimas` | `string` | — | `4` | `open` | — | Dietos pavadinimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `valgymas` | `"Pusryčiai"` | — | — | Pusryčiai | — |
| `valgymas` | `"Priešpiečiai"` | — | — | Priešpiečiai | — |
| `valgymas` | `"Pietūs"` | — | — | Pietūs | — |
| `valgymas` | `"Pavakariai"` | — | — | Pavakariai | — |
| `valgymas` | `"Vakarienė"` | — | — | Vakarienė | — |
| `valgymas` | `"Nakčiai"` | — | — | Naktipiečiai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kgspgl/kgspgl_paraiska.csv
