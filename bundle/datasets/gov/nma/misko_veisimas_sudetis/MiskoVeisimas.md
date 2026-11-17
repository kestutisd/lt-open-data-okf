---
type: Table
title: "MiskoVeisimas — Lietuvos kaimo plėtros programos 2014-2020 priemonė \"Miško veisimas\" - miško sudėtis"
description: "Spinta table datasets/gov/nma/misko_veisimas_sudetis/MiskoVeisimas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nma/misko_veisimas_sudetis/MiskoVeisimas"
tags: [gov, nma, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nma/misko_veisimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/misko_veisimas.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# MiskoVeisimas — Lietuvos kaimo plėtros programos 2014-2020 priemonė "Miško veisimas" - miško sudėtis

- **Model:** `datasets/gov/nma/misko_veisimas_sudetis/MiskoVeisimas`[^manifest]
- **Dataset:** [datasets/gov/nma/misko_veisimas_sudetis](../misko_veisimas_sudetis.md) (`datasets/gov/nma/misko_veisimas_sudetis`)
- **Manifest CSV:** [datasets/gov/nma/misko_veisimas.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/misko_veisimas.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nma/misko_veisimas_sudetis/MiskoVeisimas`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `programa` | `string` | — | `3` | `open` | — | Priemonės pavadinimas | — |
| `veiklos_sritis` | `string` | — | `3` | `open` | — | Veiklos sritis | — |
| `pareiskejo_tipas` | `string` | — | `4` | `open` | — | Pareiškėjo tipas | — |
| `pareiskejo_lytis` | `string` | — | `4` | `open` | — | Pareiškėjo lytis | — |
| `paraiskos_pateikimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos pateikimo data | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Projekto įgyvendinimo vieta | — |
| `medzio_rusis` | `string` | — | `3` | `open` | — | Medžio rūšies pavadinimas | — |
| `medziu_kiekis` | `number` | `U` | `4` | `open` | — | Medžių kiekis, vnt. | — |
| `bylos_numeris` | `string` | — | `4` | `open` | — | Projektas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pareiskejo_tipas` | `"Fizinis"` | — | — | Fizinis asmuo | — |
| `pareiskejo_tipas` | `"Juridinis"` | — | — | Juridinis asmuo | — |
| `pareiskejo_lytis` | `"V"` | — | — | Vyras | — |
| `pareiskejo_lytis` | `"M"` | — | — | Moteris | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `update(type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nma/misko_veisimas.csv
