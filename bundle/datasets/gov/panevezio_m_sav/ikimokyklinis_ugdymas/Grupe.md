---
type: Table
title: "Grupe — Panevėžio miesto ikimokyklinio ugdymo įstaigų grupės"
description: "Informacija apie Panevėžio miesto ikimokyklinio ugdymo įstaigų grupes"
resource: "https://get.data.gov.lt/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas/Grupe"
tags: [gov, panevezio_m_sav, grupe, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L29"
    title: "atviriduomenys/manifest — datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L29"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3843/"
    title: "data.gov.lt DCAT-AP — datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Grupe — Panevėžio miesto ikimokyklinio ugdymo įstaigų grupės

Informacija apie Panevėžio miesto ikimokyklinio ugdymo įstaigų grupes[^manifest]

- **Model:** `datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas/Grupe`[^manifest]
- **Dataset:** [Panevėžio miesto ikimokyklinio ugdymo įstaigų, grupių ir vaikų registracijos duomenys](../ikimokyklinis_ugdymas.md) (`datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas`)[^manifest]
- **Manifest CSV:** [datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L29](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L29)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas/Grupe` (`deployed`)[^manifest]
- **Provider:** `panevezio_m_sav` — Panevėžio miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `gr_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `programos_tipas` | `"Bendrojo ugdymo"` | — | — | Bendrojo ugdymo | — |
| `programos_tipas` | `"Specialioji"` | — | — | Specialioji | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L29 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L29)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas (https://data.gov.lt/datasets/3843/)
