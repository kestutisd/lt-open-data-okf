---
type: Table
title: "IsimtineParama — Lietuvos kaimo plėtros programos 2014-2020 priemonė \"Išimtinė laikina parama ūkininkams ir MVĮ\""
description: "Spinta table datasets/gov/nma/isimtine_parama/IsimtineParama (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nma/isimtine_parama/IsimtineParama"
tags: [gov, nma, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nma/isimtine_parama.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/isimtine_parama.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# IsimtineParama — Lietuvos kaimo plėtros programos 2014-2020 priemonė "Išimtinė laikina parama ūkininkams ir MVĮ"

- **Model:** `datasets/gov/nma/isimtine_parama/IsimtineParama`[^manifest]
- **Dataset:** [datasets/gov/nma/isimtine_parama](../isimtine_parama.md) (`datasets/gov/nma/isimtine_parama`)
- **Manifest CSV:** [datasets/gov/nma/isimtine_parama.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/isimtine_parama.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nma/isimtine_parama/IsimtineParama`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pavadinimas` | `string` | — | `3` | `open` | — | Priemonės pavadinimas | — |
| `tipas` | `string` | — | `4` | `open` | — | Pareiškėjo tipas | — |
| `lytis` | `string` | — | `4` | `open` | — | Pareiškėjo lytis | — |
| `rajonas` | `string` | — | `3` | `open` | — | Rajonas | — |
| `suma_eur` | `number` | — | `4` | `open` | — | Išmokėta suma | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Fizinis"` | — | — | Fizinis asmuo | — |
| `tipas` | `"Juridinis"` | — | — | Juridinis asmuo | — |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `suma_eur` | `update(type: "money, ref: "EUR")"` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nma/isimtine_parama.csv
