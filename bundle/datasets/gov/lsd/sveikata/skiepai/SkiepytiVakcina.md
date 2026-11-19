---
type: Table
title: "SkiepytiVakcina — Pasiskiepiję asmenys pagal laikotarpį, ligą, vakciną ir įstaigą"
description: "Spinta table datasets/gov/lsd/sveikata/skiepai/SkiepytiVakcina (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/skiepai/SkiepytiVakcina"
tags: [gov, lsd, skiepytivakcina, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/skiepai.csv#L30"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/skiepai.csv#L30"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2777/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/skiepai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# SkiepytiVakcina — Pasiskiepiję asmenys pagal laikotarpį, ligą, vakciną ir įstaigą

- **Model:** `datasets/gov/lsd/sveikata/skiepai/SkiepytiVakcina`[^manifest]
- **Dataset:** [Asmenys, paskiepyti įvairių ligų skiepais](../skiepai.md) (`datasets/gov/lsd/sveikata/skiepai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/skiepai.csv#L30](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/skiepai.csv#L30)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/skiepai/SkiepytiVakcina` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/skiepai.csv#L30 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/skiepai.csv#L30)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/skiepai (https://data.gov.lt/datasets/2777/)
