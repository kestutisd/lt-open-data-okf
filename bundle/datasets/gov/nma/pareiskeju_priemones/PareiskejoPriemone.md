---
type: Table
title: "PareiskejoPriemone — Pareiškėjų dalyvavimas NMA priemonėse"
description: "Spinta table datasets/gov/nma/pareiskeju_priemones/PareiskejoPriemone (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nma/pareiskeju_priemones/PareiskejoPriemone"
tags: [gov, nma, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nma/pareiskeju_priemones.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/pareiskeju_priemones.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# PareiskejoPriemone — Pareiškėjų dalyvavimas NMA priemonėse

- **Model:** `datasets/gov/nma/pareiskeju_priemones/PareiskejoPriemone`[^manifest]
- **Dataset:** [datasets/gov/nma/pareiskeju_priemones](../pareiskeju_priemones.md) (`datasets/gov/nma/pareiskeju_priemones`)
- **Manifest CSV:** [datasets/gov/nma/pareiskeju_priemones.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/pareiskeju_priemones.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nma/pareiskeju_priemones/PareiskejoPriemone`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pareiskejo_kodas` | `string` | — | `3` | `open` | — | Pareiškėjo kodas | — |
| `pareiskejo_tipas` | `string` | — | `4` | `open` | — | Pareiškėjo tipas | — |
| `pareiskejo_lytis` | `string` | — | `4` | `open` | — | Pareiškėjo lytis | — |
| `priemones_kodas` | `string` | — | `3` | `open` | — | Priemonės kodas | — |
| `priemones_pavadinimas` | `string` | — | `3` | `open` | — | Priemonės pavadinimas | — |
| `paraiskos_pateikimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos pateikimo data | — |
| `projekto_busena` | `string` | — | `3` | `open` | — | Projekto būsena | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pareiskejo_tipas` | `"Fizinis"` | — | — | Fizinis asmuo | — |
| `pareiskejo_tipas` | `"Juridinis"` | — | — | Juridinis asmuo | — |
| `pareiskejo_lytis` | `"V"` | — | — | Vyras | — |
| `pareiskejo_lytis` | `"M"` | — | — | Moteris | — |
| `projekto_busena` | `"Autorizuota"` | — | — | Autorizuota | — |
| `projekto_busena` | `"Nebeaktuali"` | — | — | Nebeaktuali | — |
| `projekto_busena` | `"Pateikta"` | — | — | Pateikta | — |
| `projekto_busena` | `"Vertinama"` | — | — | Vertinama | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nma/pareiskeju_priemones.csv
