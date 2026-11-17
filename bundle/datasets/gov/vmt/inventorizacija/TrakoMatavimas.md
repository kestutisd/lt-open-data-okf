---
type: Table
title: "TrakoMatavimas — Trakų matavimai"
description: "Lentelėje skelbiami trakų matavimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vmt/inventorizacija/TrakoMatavimas"
tags: [gov, vmt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmt/inventorizacija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmt/inventorizacija.csv#L120"
    last_modified: "2026-11-11T14:39:20Z"
---

# TrakoMatavimas — Trakų matavimai

Lentelėje skelbiami trakų matavimų duomenys. Anot Visuotinės Lietuvių Enciklopedijos, trakas - tai sumedėjusios augalijos žemutinis ardas; dažniausia tokie krūmai, kaip lazdynai, šaltekšniai, kadagiai, šermukšniai, serbentai ir kt., augantys po medžių danga. Viena lentelės eilutė identifikuoja trakto barelio sektoriaus vienos medelių rūšies inventorizacija vieno penkmečio laikotarpiu. Pateikiami agreguoti duomenys apie medelius pagal jų aukštį.

- **Model:** `datasets/gov/vmt/inventorizacija/TrakoMatavimas`[^manifest]
- **Dataset:** [Nacionalinės miškų inventorizacijos matavimų duomenys](../inventorizacija.md) (`datasets/gov/vmt/inventorizacija`)
- **Manifest CSV:** [datasets/gov/vmt/inventorizacija.csv#L120](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmt/inventorizacija.csv#L120)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmt/inventorizacija/TrakoMatavimas`
- **Primary Key (`ref`):** `matavimo_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `matavimo_id` | `string` | — | `4` | `open` | — | Trako matavimo identifikacinis numeris | — |
| `penkmetis` | `string` | — | `4` | `open` | — | Trako matavimo penkmetis | — |
| `trakto_id` | `string` | — | `4` | `open` | — | Trakto identifikacinis numeris | — |
| `barelio_id` | `string` | — | `4` | `open` | — | Barelio identifikacinis numeris | — |
| `sektoriaus_id` | `string` | — | `4` | `open` | — | Sektoriaus identifikacinis numeris | — |
| `atstumas` | `string` | — | `4` | `open` | — | Atstumas nuo trakto kraštinės | — |
| `rusis` | `string` | — | `4` | `open` | — | Medžio rūšies pavadinimas | — |
| `medeliu_sk_05` | `integer` | `U` | `4` | `open` | — | Trako medelių iki 0,5 m aukščio skaičius | — |
| `medeliu_sk_06_15` | `integer` | `U` | `4` | `open` | — | Trako medelių nuo 0,6 iki 1,5 m aukščio skaičius | — |
| `medeliu_sk_16_30` | `integer` | `U` | `4` | `open` | — | Trako medelių nuo 1,6 iki 3,0 m aukščio skaičius | — |
| `medeliu_sk_30` | `integer` | `U` | `4` | `open` | — | Trako medelių virš 3,0 m aukščio skaičius | — |
| `viso_medeliu` | `integer` | `U` | `4` | `open` | — | Trako medelių skaičius iš viso | — |
| `zveriu_pazeista_proc` | `number` | `%` | `4` | `open` | — | Žvėrių pažeistų medžių dalis, nurodyta procentais nuo visų sektoriaus rūšies medžių | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `atstumas` | `"Atstumas nuo trakto kraštinės pradžios 225 metrai"` | — | — | — | — |
| `atstumas` | `"Atstumas nuo trakto kraštinės pradžios 475 metrai"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmt/inventorizacija.csv
