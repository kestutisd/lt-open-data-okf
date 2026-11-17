---
type: Table
title: "Sankcija — Ekonominės sankcijos"
description: "Juridinių asmenų įrašai, turintys požymius: priimtas sprendimas, apmokejimo_data"
resource: "https://get.data.gov.lt/datasets/gov/ntakd/ekonomines_sankcijos/Sankcija"
tags: [gov, ntakd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ntakd/ekonomines_sankcijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/ekonomines_sankcijos.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sankcija — Ekonominės sankcijos

Juridinių asmenų įrašai, turintys požymius: priimtas sprendimas, apmokejimo_data

- **Model:** `datasets/gov/ntakd/ekonomines_sankcijos/Sankcija`[^manifest]
- **Dataset:** [Duomenys apie ūkio subjektams taikytas ekonomines sankcijas už Alkoholio kontrolės įstatymo ir Tabako, tabako gaminių ir su jais susijusių gaminių kontrolės įstatymo pažeidimus](../ekonomines_sankcijos.md) (`datasets/gov/ntakd/ekonomines_sankcijos`)
- **Manifest CSV:** [datasets/gov/ntakd/ekonomines_sankcijos.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/ekonomines_sankcijos.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ntakd/ekonomines_sankcijos/Sankcija`
- **Primary Key (`ref`):** `eil_nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `pavadinimas` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Įmonės pavadinimas | — |
| `kodas` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Įmonės kodas | — |
| `nutarimas` | `string` | — | `2` | `open` | — | Nutarimo numeris | — |
| `nutarimo_priemimas` | `date` | `D` | `4` | `open` | — | Nutarimo priėmimo data | — |
| `pazeistas_aki_tki` | `string` | — | `4` | `open` | — | Pažeistas AKĮ ar TKĮ straipsnis | — |
| `sprendimas` | `number` | — | `2` | `open` | — | Priimtas sprendimas | — |
| `ar_apmoketa` | `string` | — | `2` | `open` | — | Požymis nurodantis, ar apmokėta | — |
| `apmoketa` | `date` | `D` | `4` | `open` | — | Apmokėjimo data | — |
| `suma` | `number` | — | `2` | `open` | — | Apmokėjimo suma | — |
| `apskundimas` | `string` | — | `2` | `open` | — | Apskundimas | — |
| `vaat` | `string` | — | `2` | `open` | — | VAAT sprendimas | — |
| `lvat` | `string` | — | `2` | `open` | — | LVAT sprendimas | — |
| `antstolis` | `string` | — | `4` | `open` | — | Antstolių kontora | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sprendimas` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ntakd/ekonomines_sankcijos.csv
