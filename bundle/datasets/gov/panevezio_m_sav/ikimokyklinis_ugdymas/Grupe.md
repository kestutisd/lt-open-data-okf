---
type: Table
title: "Grupe — Panevėžio miesto ikimokyklinio ugdymo įstaigų grupės"
description: "Informacija apie Panevėžio miesto ikimokyklinio ugdymo įstaigų grupes"
resource: "https://get.data.gov.lt/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas/Grupe"
tags: [gov, panevezio_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L29"
    last_modified: "2026-11-11T14:39:20Z"
---

# Grupe — Panevėžio miesto ikimokyklinio ugdymo įstaigų grupės

Informacija apie Panevėžio miesto ikimokyklinio ugdymo įstaigų grupes

- **Model:** `datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas/Grupe`[^manifest]
- **Dataset:** [Panevėžio miesto ikimokyklinio ugdymo įstaigų, grupių ir vaikų registracijos duomenys](../ikimokyklinis_ugdymas.md) (`datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas`)
- **Manifest CSV:** [datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L29](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L29)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas/Grupe`
- **Primary Key (`ref`):** `gr_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gr_id` | `string` | — | `4` | `open` | — | Grupės ID numeris | — |
| `istaigos_id` | `string` | — | `4` | `open` | — | Įstaigos ID numeris | — |
| `gr_pavadinimas` | `string` | — | `4` | `open` | — | Grupės pavadinimas | — |
| `programos_tipas` | `string` | — | `4` | `open` | — | Grupės tipas pagal veiklą (bendrojo ugdymo ar specialioji) | — |
| `vietu_grupeje` | `integer` | — | `4` | `open` | — | Vietų skaičius grupėje | — |
| `laisvu_vietu_grupeje` | `integer` | — | `4` | `open` | — | Laisvų vietų skaičius grupėje | — |
| `amziaus_ribos` | `string` | — | `4` | `open` | — | Amžiaus ribos grupėje | — |
| `duomenys_gauti` | `datetime` | `L` | `4` | `open` | — | Duomenų gavimo data ir laikas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `programos_tipas` | `"Bendrojo ugdymo"` | — | — | Bendrojo ugdymo | — |
| `programos_tipas` | `"Specialioji"` | — | — | Specialioji | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv
