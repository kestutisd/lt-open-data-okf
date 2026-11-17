---
type: Table
title: "KonteinerioIsvezimas"
description: "Spinta table datasets/gov/vilniaus_m_sav/atlieku_tvarkymas/KonteinerioIsvezimas (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas/KonteinerioIsvezimas"
tags: [gov, vilniaus_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L12"
    last_modified: "2026-11-11T14:39:20Z"
---

# KonteinerioIsvezimas

- **Model:** `datasets/gov/vilniaus_m_sav/atlieku_tvarkymas/KonteinerioIsvezimas`[^manifest]
- **Dataset:** [Vilniaus atliekų sistemos administratoriaus atliekų tvarkymas](../atlieku_tvarkymas.md) (`datasets/gov/vilniaus_m_sav/atlieku_tvarkymas`)
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L12](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L12)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas/KonteinerioIsvezimas`
- **Primary Key (`ref`):** `pickup_history_id`
- **Level:** `4`
- **URI:** `Faktinių atliekų surinkimo operacijų žurnalas`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pickup_history_id` | `string` | — | `4` | `open` | — | Konteinerių išvežimai | Atliekų surinkimo archyvinis identifikatorius |
| `dumpster_id` | `string` | — | `4` | `open` | — | Konteinerio identifikatorius | — |
| `inventorinis_nr` | `string` | — | `4` | `open` | — | Inventoriaus numeris | — |
| `konteinerio_turis` | `number` | — | `4` | `open` | — | Tūris | — |
| `papildomas_turis` | `number` | — | `4` | `open` | — | Papildomas tūris | — |
| `apskaiciuotas_svoris` | `number` | — | `4` | `open` | — | Apskaičiuotos atliekos | — |
| `veiksmo_data` | `datetime` | — | `4` | `open` | — | Veiksmo data | — |
| `veiksmas` | `string` | — | `4` | `open` | — | Veiksmas | — |
| `aptarnavimas` | `string` | — | `4` | `open` | — | Aptarnavimo tipas | — |
| `komentaras` | `string` | — | `4` | `open` | — | Komentaras | — |
| `tvarkytojas` | `string` | — | `4` | `open` | — | Atliekų tvarkytojo pavadinimas | — |
| `geometrija` | `geometry(point, 4326)` | — | `4` | `open` | — | Geometrija | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `veiksmas` | `"Ištuštinti"` | — | — | Ištuštinti | — |
| `veiksmas` | `"Pastatyti"` | — | — | Pastatyti | — |
| `veiksmas` | `"Nuimti"` | — | — | Nuimti | — |
| `veiksmas` | `"Informacinis užsakymas"` | — | — | Informacinis užsakymas | — |
| `veiksmas` | `"Pakeisti"` | — | — | Pakeisti | — |
| `aptarnavimas` | `"Aptarnautas"` | — | — | Aptarnautas | — |
| `aptarnavimas` | `"Neaptarnautas"` | — | — | Neaptarnautas | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv
