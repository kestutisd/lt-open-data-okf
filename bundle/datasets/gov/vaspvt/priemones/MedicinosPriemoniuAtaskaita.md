---
type: Table
title: "MedicinosPriemoniuAtaskaita — Ataskaitų Apie Brangias Priemones Sąrašas"
description: "Spinta table datasets/gov/vaspvt/priemones/MedicinosPriemoniuAtaskaita (18 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/priemones/MedicinosPriemoniuAtaskaita"
tags: [gov, vaspvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/medicinos_iranga.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_iranga.csv#L315"
    last_modified: "2026-11-11T14:39:20Z"
---

# MedicinosPriemoniuAtaskaita — Ataskaitų Apie Brangias Priemones Sąrašas

- **Model:** `datasets/gov/vaspvt/priemones/MedicinosPriemoniuAtaskaita`[^manifest]
- **Dataset:** [Sveikatos priežiūros technologijų, susijusių su medicinos prietaisais, vertinimo ir valdymo duomenys](../priemones.md) (`datasets/gov/vaspvt/priemones`)
- **Manifest CSV:** [datasets/gov/vaspvt/medicinos_iranga.csv#L315](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_iranga.csv#L315)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/priemones/MedicinosPriemoniuAtaskaita`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Id | — |
| `irenginys` | `ref` | [MedicinosPriemone](MedicinosPriemone.md) | `4` | `open` | — | Medicinos Priemone | — |
| `ataskaita` | `ref` | [Ataskaita](Ataskaita.md) | `4` | `open` | — | Ataskaita | — |
| `modelis` | `string` | — | `4` | `open` | — | Tipas/Modelis | — |
| `serijos_nr` | `string` | — | `4` | `open` | — | Priemonės Nr. | — |
| `priemones_rusis` | `string` | — | `4` | `open` | — | Priemones tipas | — |
| `pirkimas` | `date` | `D` | `4` | `open` | — | Įsigijimo Data: | — |
| `kaina_su_pvm` | `number` | — | `2` | `open` | — | Priemonės Įsigijimo Kaina Su Priedais | — |
| `kaina_be_pvm` | `number` | — | `2` | `open` | — | Priemonės Įsigijimo Kaina Be Priedų | — |
| `instaliacijos_kaina` | `number` | — | `2` | `open` | — | Priemones Instaliavimo Kaina | — |
| `eksploatacines_islaidos` | `number` | — | `2` | `open` | — | Priemones Naudojimo Vidutines Menesio Islaidos | — |
| `apmokymo_islaidos` | `number` | — | `2` | `open` | — | Priemones Personalo Mokymai | — |
| `nusidevejimas` | `number` | — | `2` | `open` | — | Priemones Sukauptas Nusidevejimas | — |
| `likutine_verte` | `number` | — | `2` | `open` | — | Priemones Likutine Verte | — |
| `grazintina_suma` | `number` | `U` | `2` | `open` | — | Su St-Mp Atliekamų Procedūrų/Tyrimų Skaičius Per Einamuosius Metus | — |
| `gamintojas` | `string` | — | `4` | `open` | — | Gamintojo Pavadinimas | — |
| `filialas` | `string` | — | `1` | `open` | — | Filialas | — |
| `gedimo_laikas` | `integer` | `U` | `4` | `open` | — | Prastovos Dėl Gedimo Skaičius Dienomis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `priemones_rusis` | `"1"` | — | — | Angiografas | — |
| `priemones_rusis` | `"2"` | — | — | Diagnostinė rentgeno įranga | — |
| `priemones_rusis` | `"3"` | — | — | Diagnostinis ultragarsinis prietaisas | — |
| `priemones_rusis` | `"4"` | — | — | Gama kamera | — |
| `priemones_rusis` | `"5"` | — | — | Kompiuterinis tomografas | — |
| `priemones_rusis` | `"6"` | — | — | Linijinis greitintuvas | — |
| `priemones_rusis` | `"7"` | — | — | Magnetinio rezonanso tomografas | — |
| `priemones_rusis` | `"8"` | — | — | Mamografas | — |
| `priemones_rusis` | `"9"` | — | — | Pozitronų emisijos tomografas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kaina_su_pvm` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `kaina_be_pvm` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `instaliacijos_kaina` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `eksploatacines_islaidos` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `apmokymo_islaidos` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `nusidevejimas` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `likutine_verte` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `grazintina_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/medicinos_iranga.csv
