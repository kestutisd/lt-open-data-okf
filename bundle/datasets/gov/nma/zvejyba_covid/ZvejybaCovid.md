---
type: Table
title: "ZvejybaCovid — Lietuvos žuvininkystės sektoriaus 2014–2020 metų veiksmų priemonės „Laikinas žvejybos veiklos nutraukimas“ veiklos sritis „Laikinas žvejybos veiklos nutraukimas dėl COVID-19“"
description: "Spinta table datasets/gov/nma/zvejyba_covid/ZvejybaCovid (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nma/zvejyba_covid/ZvejybaCovid"
tags: [gov, nma, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nma/zvejyba_covid.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/zvejyba_covid.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# ZvejybaCovid — Lietuvos žuvininkystės sektoriaus 2014–2020 metų veiksmų priemonės „Laikinas žvejybos veiklos nutraukimas“ veiklos sritis „Laikinas žvejybos veiklos nutraukimas dėl COVID-19“

- **Model:** `datasets/gov/nma/zvejyba_covid/ZvejybaCovid`[^manifest]
- **Dataset:** [datasets/gov/nma/zvejyba_covid](../zvejyba_covid.md) (`datasets/gov/nma/zvejyba_covid`)
- **Manifest CSV:** [datasets/gov/nma/zvejyba_covid.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/zvejyba_covid.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nma/zvejyba_covid/ZvejybaCovid`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pavadinimas` | `string` | — | `3` | `open` | — | Priemonės pavadinimas | — |
| `tipas` | `string` | — | `4` | `open` | — | Pareiškėjo tipas | — |
| `lytis` | `string` | — | `4` | `open` | — | Pareiškėjo lytis | — |
| `rajonas` | `string` | — | `3` | `open` | — | Rajonas | — |
| `suma_eur` | `number` | — | `2` | `open` | — | Išmokėta suma | — |

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

[^manifest]: atviriduomenys/manifest — datasets/gov/nma/zvejyba_covid.csv
