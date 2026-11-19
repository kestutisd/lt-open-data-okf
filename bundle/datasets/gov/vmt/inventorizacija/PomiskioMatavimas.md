---
type: Table
title: "PomiskioMatavimas — Pomiškių matavimai"
description: "Lentelėje skelbiami pomiškių matavimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vmt/inventorizacija/PomiskioMatavimas"
tags: [gov, vmt, pomiskiomatavimas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmt/inventorizacija.csv#L95"
    title: "atviriduomenys/manifest — datasets/gov/vmt/inventorizacija.csv#L95"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2830/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmt/inventorizacija"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PomiskioMatavimas — Pomiškių matavimai

Lentelėje skelbiami pomiškių matavimų duomenys. Pomiškis - miško vertikaliosios struktūros dalis, kurią sudaro krūmai, jauni medeliai ir medžiai, nepasiekę viršutinio ardo. Viena eilutė identifikuoja trakto barelio sektoriaus medžių rūšies inventorizaciją vieno penkmečio laikotarpiu. Pateikiami medžio rūšies surašymo duomenys: vidutinis amžius, medžių skaičius pagal aukščio kategorijas ir perspektyvumą.[^manifest]

- **Model:** `datasets/gov/vmt/inventorizacija/PomiskioMatavimas`[^manifest]
- **Dataset:** [Nacionalinės miškų inventorizacijos matavimų duomenys](../inventorizacija.md) (`datasets/gov/vmt/inventorizacija`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmt/inventorizacija.csv#L95](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmt/inventorizacija.csv#L95)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmt/inventorizacija/PomiskioMatavimas` (`deployed`)[^manifest]
- **Provider:** `vmt` — Valstybinė Miškų Tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `matavimo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `matavimo_id` | `string` | — | `4` | `open` | — | Pomiškio matavimo identifikacinis numeris | — |
| `penkmetis` | `string` | — | `4` | `open` | — | Pomiškio matavimo penkmetis | — |
| `trakto_id` | `string` | — | `4` | `open` | — | Trakto identifikacinis numeris | — |
| `barelio_id` | `string` | — | `4` | `open` | — | Barelio identifikacinis numeris | — |
| `sektoriaus_id` | `string` | — | `4` | `open` | — | Sektoriaus identifikacinis numeris | — |
| `atstumas` | `string` | — | `4` | `open` | — | Atstumas nuo trakto kraštinės | — |
| `rusis_lot` | `string` | — | `4` | `open` | — | Lotyniškas medžio rūšies pavadinimas | — |
| `rusis_lt` | `string` | — | `4` | `open` | — | Lietuviškas rūšies pavadinimas | — |
| `amzius` | `integer` | — | `4` | `open` | — | Vidutinis sektoriaus medžių rūšies amžius | — |
| `zveriu_pazeista_proc` | `number` | `%` | `4` | `open` | — | Žvėrių pažeistų medžių dalis, nurodyta procentais nuo visų sektoriaus rūšies medžių | — |
| `medeliu_sk_05` | `integer` | `U` | `4` | `open` | — | Medelių iki 0,5 m aukščio skaičius | — |
| `medeliu_sk_06_15` | `integer` | `U` | `4` | `open` | — | Medelių nuo 0,6 iki 1,5 m aukščio skaičius | — |
| `medeliu_sk_16_30` | `integer` | `U` | `4` | `open` | — | Medelių nuo 1,6 iki 3,0 m aukščio skaičius | — |
| `medeliu_sk_30` | `integer` | `U` | `4` | `open` | — | Medelių virš 3,0 m aukščio skaičius | — |
| `viso_medeliu` | `integer` | `U` | `4` | `open` | — | Medelių skaičius iš viso | — |
| `neperspektyviu_05` | `integer` | `U` | `4` | `open` | — | Neperspektyvių medelių iki 0,5 m aukščio skaičius | — |
| `neperspektyviu_15` | `integer` | `U` | `4` | `open` | — | Neperspektyvių medelių nuo 0,6 iki 1,5 m aukščio skaičius | — |
| `neperspektyviu_30` | `integer` | `U` | `4` | `open` | — | Neperspektyvių medelių nuo 1,6 iki 3,0 m aukščio skaičius | — |
| `neperspektyviu_31` | `integer` | `U` | `4` | `open` | — | Neperspektyvių medelių virš 3,0 m aukščio skaičius | — |
| `neperspektyviu_proc` | `number` | `%` | `4` | `open` | — | Neperspektyvių medelių žvėrių pažeidimas, % | — |
| `viso_neperspektyviu` | `integer` | `U` | `4` | `open` | — | Bendras neperspektyvių medelių skaičius | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `atstumas` | `"Atstumas nuo trakto kraštinės pradžios 225 metrai"` | — | — | — | — |
| `atstumas` | `"Atstumas nuo trakto kraštinės pradžios 475 metrai"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmt/inventorizacija.csv#L95 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmt/inventorizacija.csv#L95)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmt/inventorizacija (https://data.gov.lt/datasets/2830/)
