---
type: Table
title: "LietuvosVardasDomenas — Domenai su Lietuvos vardu"
description: "Lentelėje pateikiami Lietuvos Respublikos ryšių reguliavimo tarnybos duomenys apie prašymus registruoti domenus su Lietuvos vardu."
resource: "https://get.data.gov.lt/datasets/gov/rrt/domenai_su_lt_vardu/LietuvosVardasDomenas"
tags: [gov, rrt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rrt/domenai_su_lt_vardu.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/domenai_su_lt_vardu.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# LietuvosVardasDomenas — Domenai su Lietuvos vardu

Lentelėje pateikiami Lietuvos Respublikos ryšių reguliavimo tarnybos duomenys apie prašymus registruoti domenus su Lietuvos vardu. Tai galioja domenams, kurie varduose prieš aukščiausiojo lygio domeną „.lt“ turi Lietuvos vardą. Šiems domenams reikalingas atskiras leidimas. Visos taisyklės yra apibrėžtos Lietuvos Respublikos Vyriausybės nutarime „Dėl Lietuvos vardo vartojimo interneto domenų varduose taisyklių patvirtinimo“. Laiko aprėptis nuo 2009 m. spalio mėn. Fizinių asmenų vardai yra nuasmeninti paliekant tik inicialus. Atnaujinimo dažnis - kasdien.

- **Model:** `datasets/gov/rrt/domenai_su_lt_vardu/LietuvosVardasDomenas`[^manifest]
- **Dataset:** [Domenai su Lietuvos vardu](../domenai_su_lt_vardu.md) (`datasets/gov/rrt/domenai_su_lt_vardu`)
- **Manifest CSV:** [datasets/gov/rrt/domenai_su_lt_vardu.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/domenai_su_lt_vardu.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rrt/domenai_su_lt_vardu/LietuvosVardasDomenas`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `domenas` | `string` | — | `4` | `open` | — | Domeno pavadinimas | — |
| `prasymo_tipas` | `string` | — | `4` | `open` | — | Domeno prašymo tipas | — |
| `domeno_savininko_tipas` | `string` | — | `4` | `open` | — | Domeno savininko tipas | — |
| `domeno_savininko_pavadinimas` | `string` | — | `4` | `open` | — | Domeno savininko pavadinimas | — |
| `prasymo_data` | `date` | `D` | `4` | `open` | — | Prašymo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `prasymo_tipas` | `"Prašymas įregistruoti domeną"` | — | — | Prašymas įregistruoti domeną | — |
| `prasymo_tipas` | `"Prašymas išregistruoti domeną"` | — | — | Prašymas išregistruoti domeną | — |
| `domeno_savininko_tipas` | `"Fizinis asmuo"` | — | — | Fizinis asmuo | — |
| `domeno_savininko_tipas` | `"Juridinis asmuo"` | — | — | Juridinis asmuo | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/domenai_su_lt_vardu.csv
