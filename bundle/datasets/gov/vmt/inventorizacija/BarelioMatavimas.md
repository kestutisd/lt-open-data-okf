---
type: Table
title: "BarelioMatavimas — Barelių matavimai"
description: "Lentelėje skelbiami barelių matavimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vmt/inventorizacija/BarelioMatavimas"
tags: [gov, vmt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmt/inventorizacija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmt/inventorizacija.csv#L12"
    last_modified: "2026-11-11T14:39:20Z"
---

# BarelioMatavimas — Barelių matavimai

Lentelėje skelbiami barelių matavimų duomenys. Viena eilutė - vienas barelio matavimas. Pateikiama barelio lokacija trakte, matavimo data, penkerių metų ciklas, būsena ir konfidencialumo tikslais "triukšmintos" barelių centrų koordinatės.

- **Model:** `datasets/gov/vmt/inventorizacija/BarelioMatavimas`[^manifest]
- **Dataset:** [Nacionalinės miškų inventorizacijos matavimų duomenys](../inventorizacija.md) (`datasets/gov/vmt/inventorizacija`)
- **Manifest CSV:** [datasets/gov/vmt/inventorizacija.csv#L12](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmt/inventorizacija.csv#L12)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmt/inventorizacija/BarelioMatavimas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `trakto_id` | `string` | — | `4` | `open` | — | Trakto identifikacinis numeris | — |
| `barelio_id` | `string` | — | `4` | `open` | — | Barelio identifikacinis numeris | — |
| `bar_tipas` | `string` | — | `4` | `open` | — | Barelio tipas | — |
| `bar_padetis` | `string` | — | `4` | `open` | — | Barelio padėtis trakte | — |
| `matavimo_data` | `date` | `D` | `4` | `open` | — | Barelio matavimo data | — |
| `penkmetis` | `string` | — | `4` | `open` | — | Barelio matavimo penkmetis | — |
| `geometrija` | `geometry(point, 3346)` | — | `4` | `open` | — | Barelių centrų taškų LKS94 koordinatės. Dėl konfidencialumo pateiktos koordinatės yra "triukšmintos" ir neatspindi tikslių barelių centrų taškų. | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `bar_tipas` | `"Pastovus 1 kartą"` | — | — | — | — |
| `bar_tipas` | `"Pastovus 2 kartą"` | — | — | — | — |
| `bar_tipas` | `"Pastovus 3 kartą"` | — | — | — | — |
| `bar_tipas` | `"Pastovus 4 kartą"` | — | — | — | — |
| `bar_tipas` | `"Pastovus 5 kartą"` | — | — | — | — |
| `bar_tipas` | `"Laikinas 1 kartą"` | — | — | — | — |
| `bar_padetis` | `"Barelis yra šiaurinėje trakto kraštinėje"` | — | — | — | — |
| `bar_padetis` | `"Barelis yra vakarinėje trakto kraštinėje"` | — | — | — | — |
| `bar_padetis` | `"Barelis yra rytinėje trakto kraštinėje"` | — | — | — | — |
| `bar_padetis` | `"Barelis yra pietinėje trakto kraštinėje"` | — | — | — | — |
| `penkmetis` | `"1998_02t"` | — | — | — | — |
| `penkmetis` | `"2003_07t"` | — | — | — | — |
| `penkmetis` | `"2008_12"` | — | — | — | — |
| `penkmetis` | `"2013_17"` | — | — | — | — |
| `penkmetis` | `"2018-2022"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmt/inventorizacija.csv
