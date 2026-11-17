---
type: Table
title: "ElRysiaiPastasTeikejas — Elektroninių ryšių bei pašto paslaugų teikėjai ir jų pateiktų periodinių ataskaitų statistika"
description: "Lentelėje pateikiama Lietuvos Respublikos ryšių reguliavimo tarnybai pateiktų pašto paslaugų ir elektroninių ryšių ataskaitų statistika."
resource: "https://get.data.gov.lt/datasets/gov/rrt/el_rysiu_ir_pasto_teikejai/ElRysiaiPastasTeikejas"
tags: [gov, rrt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rrt/el_rysiu_ir_pasto_teikejai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/el_rysiu_ir_pasto_teikejai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# ElRysiaiPastasTeikejas — Elektroninių ryšių bei pašto paslaugų teikėjai ir jų pateiktų periodinių ataskaitų statistika

Lentelėje pateikiama Lietuvos Respublikos ryšių reguliavimo tarnybai pateiktų pašto paslaugų ir elektroninių ryšių ataskaitų statistika. Duomenys pateikiami nuo 2021 metų. Metai ir ketvirtis nurodo periodą, už kurį pateikta ataskaita, bet ne ataskaitos pateikimo laiką. Vienam ketvirčiui yra pateikiama viena ataskaita. Jei įmonė tuo pačiu metu teikia ir pašto, ir elektroninių ryšių paslaugas ji gali pateikti dvi skirtingas ataskaitas tam pačiam ketvirčiui. Stulpelyje „jar_kodas“ taip pat pateikiami ir užsienio įmonių kodai. Duomenys atnaujinami kas 3 mėnesius.

- **Model:** `datasets/gov/rrt/el_rysiu_ir_pasto_teikejai/ElRysiaiPastasTeikejas`[^manifest]
- **Dataset:** [Elektroninių ryšių bei pašto paslaugų teikėjai ir jų pateiktų periodinių ataskaitų statistika](../el_rysiu_ir_pasto_teikejai.md) (`datasets/gov/rrt/el_rysiu_ir_pasto_teikejai`)
- **Manifest CSV:** [datasets/gov/rrt/el_rysiu_ir_pasto_teikejai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/el_rysiu_ir_pasto_teikejai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rrt/el_rysiu_ir_pasto_teikejai/ElRysiaiPastasTeikejas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai, už kuriuos pateikta ataskaita | — |
| `ketvirtis` | `string` | — | `4` | `open` | — | Ketvirtis, už kurį pateikta ataskaita | — |
| `ataskaitos_tipas` | `string` | — | `4` | `open` | — | Ataskaitos tipas | — |
| `imones_pavadinimas` | `string` | — | `4` | `open` | — | Įmonės pavadinimas | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Juridinių asmenų registro kodas | — |
| `el_pastas` | `string` | — | `4` | `open` | — | Elektroninio pašto adresas | — |
| `internetine_svetaine` | `url` | — | `4` | `open` | — | Internetinė svetainė | — |
| `pirma_ataskaita_pateikta` | `date` | `D` | `4` | `open` | — | Pirmos ataskaitos pateikimo data | — |
| `paskutine_ataskaita_pateikta` | `date` | `D` | `4` | `open` | — | Paskutinės ataskaitos pateikimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ketvirtis` | `"I"` | — | — | Pirmas ketvirtis | — |
| `ketvirtis` | `"II"` | — | — | Antras ketvirtis | — |
| `ketvirtis` | `"III"` | — | — | Trečias ketvirtis | — |
| `ketvirtis` | `"IV"` | — | — | Ketvirtas ketvirtis | — |
| `ataskaitos_tipas` | `"Pašto paslaugos ataskaita"` | — | — | Pašto paslaugos ataskaita | — |
| `ataskaitos_tipas` | `"Elektroninių ryšių ataskaita"` | — | — | Elektroninių ryšių ataskaita | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/el_rysiu_ir_pasto_teikejai.csv
