---
type: Table
title: "Patvirtinimas — Profesinės patirties patvirtinimas"
description: "Informacija apie piliečių išvykstančių dirbti kitose ES valstybėse profesinės patirties patvirtinimą."
resource: "https://get.data.gov.lt/datasets/gov/eimin/prof_patirt_patvirtinimas/Patvirtinimas"
tags: [gov, eimin, patvirtinimas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eimin/prof_patirt_patvirtinimas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/eimin/prof_patirt_patvirtinimas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2309/"
    title: "data.gov.lt DCAT-AP — datasets/gov/eimin/prof_patirt_patvirtinimas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Patvirtinimas — Profesinės patirties patvirtinimas

Informacija apie piliečių išvykstančių dirbti kitose ES valstybėse profesinės patirties patvirtinimą.[^manifest]

- **Model:** `datasets/gov/eimin/prof_patirt_patvirtinimas/Patvirtinimas`[^manifest]
- **Dataset:** [Profesinės patirties patvirtinimas](../prof_patirt_patvirtinimas.md) (`datasets/gov/eimin/prof_patirt_patvirtinimas`)[^manifest]
- **Manifest CSV:** [datasets/gov/eimin/prof_patirt_patvirtinimas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eimin/prof_patirt_patvirtinimas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/eimin/prof_patirt_patvirtinimas/Patvirtinimas` (`deployed`)[^manifest]
- **Provider:** `eimin` — Lietuvos Respublikos ekonomikos ir inovacijų ministerija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Sugeneruotas tikrinimo numeris | — |
| `dokumento_numeris` | `string` | — | `4` | `open` | — | Dokumento numeris | — |
| `gavimo_data` | `date` | `D` | `4` | `open` | — | Prašymo išduoti dokumentą gavimo data | — |
| `isdavimo_data` | `date` | `D` | `4` | `open` | — | Dokumento išdavimo data | — |
| `salis` | `string` | — | `4` | `open` | — | Šalis į kurią išvykstama dirbti | — |
| `sarasas` | `string` | — | `4` | `open` | — | Dokumentų sąrašo numeris | — |
| `grupe` | `string` | — | — | — | — | Profesinės veiklos grupės numeris pagal direktyvą 2005/36/EB | — |
| `grupes_pavadinimas` | `string` | — | — | — | — | Profesinės veiklos grupės pavadinimas | — |
| `pogrupis` | `string` | — | `4` | `open` | — | Profesinės veiklos pogrupio numeris pagal direktyvą 2005/36/EB | — |
| `pogrupio_pavadinimas` | `string` | — | `4` | `open` | — | Profesinės veiklos pogrupio pavadinimas | — |
| `lytis` | `string` | — | `4` | `open` | — | Piliečio lytis | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Piliečio gimimo metai | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | — | `"Vyras"` | — | — | — |
| `lytis` | — | `"Moteris"` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/eimin/prof_patirt_patvirtinimas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eimin/prof_patirt_patvirtinimas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/eimin/prof_patirt_patvirtinimas (https://data.gov.lt/datasets/2309/)
