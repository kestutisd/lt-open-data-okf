---
type: Table
title: "Prasymas — Prašymai į Panevėžio miesto ikimokyklinio ugdymo įstaigas"
description: "Informacija apie prašymus į Panevėžio miesto ikimokyklinio ugdymo įstaigas"
resource: "https://get.data.gov.lt/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas/Prasymas"
tags: [gov, panevezio_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L41"
    last_modified: "2026-11-11T14:39:20Z"
---

# Prasymas — Prašymai į Panevėžio miesto ikimokyklinio ugdymo įstaigas

Informacija apie prašymus į Panevėžio miesto ikimokyklinio ugdymo įstaigas

- **Model:** `datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas/Prasymas`[^manifest]
- **Dataset:** [Panevėžio miesto ikimokyklinio ugdymo įstaigų, grupių ir vaikų registracijos duomenys](../ikimokyklinis_ugdymas.md) (`datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas`)
- **Manifest CSV:** [datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L41](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L41)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas/Prasymas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Prašymo numerio ID | — |
| `prasymo_nr` | `string` | — | `4` | `open` | — | Unikalus prašymo numeris | — |
| `prasymo_data` | `datetime` | `L` | `4` | `open` | — | Prašymo pateikimo data ir laikas | — |
| `vaiko_ak` | `string` | — | `4` | `open` | — | Vaiko asmens kodas | — |
| `vaiko_ak_validacija` | `string` | — | `4` | `open` | — | Vaiko asmens kodo validacija | — |
| `gim_metai_vaiko_ak` | `date` | `Y` | `4` | `open` | — | Vaiko gimimo metai, nustatyti iš asmens kodo | — |
| `lytis_vaiko_ak` | `string` | — | `4` | `open` | — | Vaiko lytis, nustatyta iš asmens kodo | — |
| `pageidauja_lankyti_nuo` | `date` | `D` | `4` | `open` | — | Data nuo kada ageidauja lankyti | — |
| `prasymo_busena` | `string` | — | `4` | `open` | — | Prašymo būsena | — |
| `informavimo_budas` | `string` | — | `4` | `open` | — | Informavimo būdas | — |
| `prioritetu_sk` | `integer` | — | `4` | `open` | — | Prioritetų skaičius | — |
| `sukurta` | `datetime` | `L` | `4` | `open` | — | Įrašo sukūrimo data | — |
| `atnaujinta` | `datetime` | `L` | `4` | `open` | — | Įrašo atnaujinimo data | — |
| `inst_id` | `string` | — | `4` | `open` | — | Įstaigos ID numeris | — |
| `duomenys_gauti` | `datetime` | `L` | `4` | `open` | — | Duomenų gavimo data ir laikas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis_vaiko_ak` | `"Moteris"` | — | — | Moteris | — |
| `lytis_vaiko_ak` | `"Vyras"` | — | — | Vyras | — |
| `informavimo_budas` | `"Trumpąja SMS žinute"` | — | — | Trumpąja SMS žinute | — |
| `informavimo_budas` | `"El. pašto laišku"` | — | — | El. pašto laišku | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv
