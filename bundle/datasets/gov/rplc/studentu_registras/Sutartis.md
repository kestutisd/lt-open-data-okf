---
type: Table
title: "Sutartis — Pateikiami Respublikinio Priklausomybės Ligų Centro Vilniaus, Kauno, Klaipėdos, Šiaulių ir Panevėžio filialų studentų, atlikusių praktiką, rezidentūrą, tyrimą ar užsiėmusių kita veikla..."
description: "Spinta table datasets/gov/rplc/studentu_registras/Sutartis (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rplc/studentu_registras/Sutartis"
tags: [gov, rplc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rplc/studentu_registras.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rplc/studentu_registras.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sutartis — Pateikiami Respublikinio Priklausomybės Ligų Centro Vilniaus, Kauno, Klaipėdos, Šiaulių ir Panevėžio filialų studentų, atlikusių praktiką, rezidentūrą, tyrimą ar užsiėmusių kita veikla...

- **Model:** `datasets/gov/rplc/studentu_registras/Sutartis`[^manifest]
- **Dataset:** [datasets/gov/rplc/studentu_registras](../studentu_registras.md) (`datasets/gov/rplc/studentu_registras`)
- **Manifest CSV:** [datasets/gov/rplc/studentu_registras.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rplc/studentu_registras.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rplc/studentu_registras/Sutartis`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `mokymo_istaiga` | `string` | — | `4` | `open` | — | Asmens mokymo įstaiga | Jei asmuo atlieka praktiką kaip savanoris, įraše žymima "Savanoris" |
| `praktikos_pradzia` | `date` | `D` | `4` | `open` | — | Praktikos pradžios data | — |
| `sutarties_rusis` | `string` | — | `3` | `open` | — | Sutarties rūšis | — |
| `komentaras` | `string` | — | `4` | `open` | — | Papildomas komentaras apie sutartį | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rplc/studentu_registras.csv
