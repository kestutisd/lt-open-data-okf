---
type: Table
title: "SkiepytiVakcina — Pasiskiepiję asmenys pagal laikotarpį, ligą, vakciną ir įstaigą"
description: "Spinta table datasets/gov/lsd/sveikata/skiepai/SkiepytiVakcina (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/skiepai/SkiepytiVakcina"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/skiepai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/skiepai.csv#L30"
    last_modified: "2026-11-11T14:39:20Z"
---

# SkiepytiVakcina — Pasiskiepiję asmenys pagal laikotarpį, ligą, vakciną ir įstaigą

- **Model:** `datasets/gov/lsd/sveikata/skiepai/SkiepytiVakcina`[^manifest]
- **Dataset:** [Asmenys, paskiepyti įvairių ligų skiepais](../skiepai.md) (`datasets/gov/lsd/sveikata/skiepai`)
- **Manifest CSV:** [datasets/gov/lsd/sveikata/skiepai.csv#L30](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/skiepai.csv#L30)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/skiepai/SkiepytiVakcina`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `sezonas` | `integer` | — | `4` | `open` | — | Sezono pradžios metai | Sezonas prasideda nuo rugsėjo mėn. Pvz., "2023" sezonas apima periodą nuo 2023 rugsėjo 1 d. iki 2024 rugpjūčio 31 d. |
| `laikotarpis` | `string` | — | `2` | `open` | — | Laikotarpis | Mėnuo, kai buvo paskiepyta, arba "Visas sezonas" |
| `liga` | `string` | — | `2` | `open` | — | Liga, nuo kurios skiepijama | — |
| `sukelejas` | `string` | — | `2` | `open` | — | Ligos sukėlėjas | — |
| `n_asm_ligoje` | `integer` | — | `4` | `open` | — | Asmenų skaičius pagal ligą | Unikalių asmenų skaičius, paskiepytų nuo šios ligos per nurodytą laikotarpį. Gali būti mažesnis viso sezono laikotarpyje, negu suma pamėnesiui, jei žmogus skiepijasi kelis kartus per sezoną |
| `medication_name` | `string` | — | `2` | `open` | — | Vakcinos, kuria skiepijama, pavadinimas | — |
| `n_asm_vaiste` | `integer` | — | `4` | `open` | — | Asmenų skaičius pagal ligą ir vakciną | Suma gali būti didesnė nei skaičius pagal ligą, jei asmuo gavo kelias skirtingas vakcinas |
| `espbi_ist_pav` | `string` | — | `3` | `open` | — | Skiepijančios įstaigos pavadinimas | — |
| `n_asm_istaigoje` | `integer` | — | `4` | `open` | — | Asmenų skaičius pagal ligą, vakciną ir įstaigą | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/skiepai.csv
