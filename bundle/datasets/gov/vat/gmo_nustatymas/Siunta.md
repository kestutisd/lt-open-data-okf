---
type: Table
title: "Siunta — Pateikiama informacija apie ŪS pavadinimą, mėginio eilės Nr., veislę, kategoriją / klasę, siuntos Nr., siuntos svorį (kg) / vnt., pasėlio plotą, ha, mėginio ėmimo datą, tyrimų rezultatų išvadą."
description: "Spinta table datasets/gov/vat/gmo_nustatymas/Siunta (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/gmo_nustatymas/Siunta"
tags: [gov, vat, siunta, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r32_gmo_nustatymas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/r32_gmo_nustatymas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1888/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/gmo_nustatymas"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Siunta — Pateikiama informacija apie ŪS pavadinimą, mėginio eilės Nr., veislę, kategoriją / klasę, siuntos Nr., siuntos svorį (kg) /...

- **Model:** `datasets/gov/vat/gmo_nustatymas/Siunta`[^manifest]
- **Dataset:** [Informacija apie paimtus mėginius iš siuntų dėl genetinės modifikacijos nustatymo](../gmo_nustatymas.md) (`datasets/gov/vat/gmo_nustatymas`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r32_gmo_nustatymas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r32_gmo_nustatymas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/gmo_nustatymas/Siunta` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `eil_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r32_gmo_nustatymas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r32_gmo_nustatymas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/gmo_nustatymas (https://data.gov.lt/datasets/1888/)
