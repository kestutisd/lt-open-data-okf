---
type: Table
title: "Klausimas — Vilniaus miesto tarybos posėdžių duomenys ir apibendrinti rezultatai"
description: "Spinta table datasets/gov/vilniaus_m_sav/balsavimai/Klausimas (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/balsavimai/Klausimas"
tags: [gov, vilniaus_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/balsavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/balsavimai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Klausimas — Vilniaus miesto tarybos posėdžių duomenys ir apibendrinti rezultatai

- **Model:** `datasets/gov/vilniaus_m_sav/balsavimai/Klausimas`[^manifest]
- **Dataset:** [Vilniaus miesto tarybos balsavimai](../balsavimai.md) (`datasets/gov/vilniaus_m_sav/balsavimai`)
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/balsavimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/balsavimai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/balsavimai/Klausimas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `posedis` | `string` | — | `4` | `open` | — | Tarybos posėdžio pavadinimas | — |
| `posedzio_statusas` | `string` | — | `4` | `open` | — | Posėdžio statusas | — |
| `pirmininkas` | `string` | — | `4` | `open` | — | Posėdžio pirmininkas | — |
| `sekretorius` | `string` | — | `4` | `open` | — | Posėdžio sekretorius | — |
| `prasidejo` | `datetime` | `S` | `4` | `open` | — | Posėdžio pradžios laiko žyma | — |
| `baigesi` | `datetime` | `S` | `4` | `open` | — | Posėdžio pabaigos laiko žyma | — |
| `klausimo_id` | `string` | — | `4` | `open` | — | Svarstyto klausimo identifikacinis numeris | — |
| `klausimas_lt` | `string` | — | `2` | `open` | — | Svarstytas klausimas | — |
| `svarstymas` | `string` | — | `4` | `open` | — | Svarstymas | — |
| `svarstymo_tvarka` | `string` | — | `4` | `open` | — | Klausimo svarstymo tvarka | — |
| `balsavimo_id` | `string` | — | `4` | `open` | — | Balsavimo identifikacinis numeris | — |
| `balsavo` | `integer` | `U` | `4` | `open` | — | Bendras Tarybos narių, dalyvavusių balsavime, skaičius | — |
| `nebalsavo` | `integer` | `U` | `4` | `open` | — | Bendras Tarybos narių, nedalyvavusių balsavime, skaičius | — |
| `dalyvavo` | `integer` | `U` | `4` | `open` | — | Bendras Tarybos narių, dalyvavusių posėdyje, skaičius | — |
| `reikia_daugumai` | `integer` | `U` | `4` | `open` | — | Minimalus kriterijus kvorumui pasiekti (50% dalyvavusių posėdyje) | — |
| `sprendimas` | `string` | — | `4` | `open` | — | Balsavime priimtas sprendimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `posedzio_statusas` | `"Baigta"` | — | — | — | — |
| `posedzio_statusas` | `"Vyksta"` | — | — | — | — |
| `posedzio_statusas` | `"Parengta"` | — | — | — | — |
| `posedzio_statusas` | `"Įvykęs"` | — | — | — | — |
| `posedzio_statusas` | `"Užbaigta/Tvarkoma"` | — | — | — | — |
| `svarstymo_tvarka` | `"Bendra tvarka"` | — | — | — | — |
| `svarstymo_tvarka` | `"Skubos tvarka"` | — | — | — | — |
| `svarstymo_tvarka` | `"Viena stadija"` | — | — | — | — |
| `svarstymo_tvarka` | `"Skubos tvarka arba ne"` | — | — | — | — |
| `svarstymo_tvarka` | `"Skubos tvarka, jei bus komiteto pritarimas"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `klausimas_lt` | `update(property: "klausimas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/balsavimai.csv
