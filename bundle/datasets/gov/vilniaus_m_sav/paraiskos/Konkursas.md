---
type: Table
title: "Konkursas — Vilniaus miesto savivaldybės administracijos konkursų skelbimai"
description: "Pateikiami duomenys apie kiekvieną skelbtą konkursą, tikslus, aprašymą, programą, maksimalią finansavimo sumą, paraiškų teikimo pradžios ir pabaigos datas bei atsakingą savivaldybės skyrių."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/paraiskos/Konkursas"
tags: [gov, vilniaus_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/paraiskos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/paraiskos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Konkursas — Vilniaus miesto savivaldybės administracijos konkursų skelbimai

Pateikiami duomenys apie kiekvieną skelbtą konkursą, tikslus, aprašymą, programą, maksimalią finansavimo sumą, paraiškų teikimo pradžios ir pabaigos datas bei atsakingą savivaldybės skyrių.

- **Model:** `datasets/gov/vilniaus_m_sav/paraiskos/Konkursas`[^manifest]
- **Dataset:** [Vilniaus miesto savivaldybės skelbiamų konkursų paraiškų duomenys](../paraiskos.md) (`datasets/gov/vilniaus_m_sav/paraiskos`)
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/paraiskos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/paraiskos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/paraiskos/Konkursas`
- **Primary Key (`ref`):** `konkurso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `konkurso_id` | `string` | — | `4` | `open` | — | Konkurso identifikacinis numeris | — |
| `konkursas` | `string` | — | `4` | `open` | — | Konkurso pavadinimas | — |
| `tikslas_lt` | `string` | — | `4` | `open` | — | Konkurso tikslas | — |
| `aprasymas_lt` | `string` | — | `4` | `open` | — | Konkurso aprašymas | — |
| `programa` | `string` | — | `4` | `open` | — | Konkurso programos pavadinimas | — |
| `progr_aprasymas_lt` | `string` | — | `4` | `open` | — | Konkurso programos aprašymas | — |
| `programos_kodas` | `string` | — | `4` | `open` | — | Programos kodas | — |
| `finansavimas_lt` | `string` | — | `4` | `open` | — | Maksimali prašoma suma vienam projektui | — |
| `pradzia` | `date` | `D` | `4` | `open` | — | Konkurso pradžios data | — |
| `pabaiga` | `datetime` | `S` | `4` | `open` | — | Konkurso pabaigos laikas | — |
| `skyrius` | `string` | — | `4` | `open` | — | Savivaldybės skyrius, kuruojantis konkurso vykdymą | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tikslas_lt` | `update(property: "tikslas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `aprasymas_lt` | `update(property: "aprasymas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `progr_aprasymas_lt` | `update(property: "progr_aprasymas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `finansavimas_lt` | `update(property: "finansavimas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/paraiskos.csv
