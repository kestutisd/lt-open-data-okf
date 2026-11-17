---
type: Table
title: "Siunta — Pateikiama informacija apie ŪS pavadinimą, mėginio eilės Nr., veislę, kategoriją / klasę, siuntos Nr., siuntos svorį (kg) / vnt., pasėlio plotą, ha, mėginio ėmimo datą, tyrimų rezultatų..."
description: "Spinta table datasets/gov/vat/gmo_nustatymas/Siunta (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/gmo_nustatymas/Siunta"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/r32_gmo_nustatymas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r32_gmo_nustatymas.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Siunta — Pateikiama informacija apie ŪS pavadinimą, mėginio eilės Nr., veislę, kategoriją / klasę, siuntos Nr., siuntos svorį (kg) / vnt., pasėlio plotą, ha, mėginio ėmimo datą, tyrimų rezultatų...

- **Model:** `datasets/gov/vat/gmo_nustatymas/Siunta`[^manifest]
- **Dataset:** [datasets/gov/vat/gmo_nustatymas](../gmo_nustatymas.md) (`datasets/gov/vat/gmo_nustatymas`)
- **Manifest CSV:** [datasets/gov/vat/r32_gmo_nustatymas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r32_gmo_nustatymas.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/gmo_nustatymas/Siunta`
- **Primary Key (`ref`):** `eil_nr`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `ukio_subjektas` | `string` | — | `2` | `open` | — | Ūkio subjekto pavadinimas | — |
| `veisle` | `string` | — | `4` | `open` | — | Veislė | — |
| `kategorija` | `string` | — | `2` | `open` | — | Kategorija ir klasė | — |
| `siunta` | `string` | — | `1` | `open` | — | Siuntos numeris | — |
| `apimtis` | `string` | — | `2` | `open` | — | Siuntos svoris (kg) / vnt. pasėlio plotas (ha) | — |
| `data` | `date` | `D` | `4` | `open` | — | Mėginio ėmimo data | — |
| `isvada` | `string` | — | `4` | `open` | — | Tyrimų rezultatų išvada | — |
| `kultura` | `string` | — | `4` | `open` | — | Kultūra | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `kultura` | `"Žieminiai rapsai"` | — | — | — | — |
| `kultura` | `"Sėklinės bulvės"` | — | — | — | — |
| `kultura` | `"Sėjamasis linas (sėmenims)"` | — | — | — | — |
| `kultura` | `"Paprastieji kukurūzai"` | — | — | — | — |
| `kultura` | `"Paprastasis kukurūzas"` | — | — | — | — |
| `kultura` | `"Sėmeniniai linai"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ukio_subjektas` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo", type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r32_gmo_nustatymas.csv
