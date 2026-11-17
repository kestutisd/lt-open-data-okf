---
type: Table
title: "Sutartis — Bendrojo ugdymo įstaigų maitinimo paslaugų viešųjų pirkimų sutarčių duomenys"
description: "Spinta table datasets/gov/lsd/vpt/maitinimo_sutartys/Sutartis (25 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/vpt/maitinimo_sutartys/Sutartis"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/vpt/maitinimo_sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/maitinimo_sutartys.csv#L15"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sutartis — Bendrojo ugdymo įstaigų maitinimo paslaugų viešųjų pirkimų sutarčių duomenys

- **Model:** `datasets/gov/lsd/vpt/maitinimo_sutartys/Sutartis`[^manifest]
- **Dataset:** [Ugdymo įstaigų maitinimo sutarčių duomenys](../maitinimo_sutartys.md) (`datasets/gov/lsd/vpt/maitinimo_sutartys`)
- **Manifest CSV:** [datasets/gov/lsd/vpt/maitinimo_sutartys.csv#L15](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/maitinimo_sutartys.csv#L15)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/vpt/maitinimo_sutartys/Sutartis`
- **Primary Key (`ref`):** `sutarties_id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sutarties_id` | `string` | — | `4` | `open` | — | Sutarties identifikacinis numeris | — |
| `registracijos_id` | `string` | — | `4` | `open` | — | Sutarties registracijos identifikacinis numeris | — |
| `tev_registracijos_id` | `string` | — | `4` | `open` | — | Tėvinės sutarties identifikacinis numeris, susijęs su registracijos_id. | — |
| `sutarties_issiuntimas` | `date` | `D` | `4` | `open` | — | Sutarties išsiuntimo pasirašymui data | — |
| `sutarties_pradzia` | `datetime` | `S` | `4` | `open` | — | Sutarties galiojimo pradžios laiko žyma | — |
| `sutarties_pabaiga` | `datetime` | `S` | `4` | `open` | — | Sutarties galiojimo termino laiko žyma | — |
| `ar_sutartis_galioja` | `boolean` | — | `4` | `open` | — | Požymis, ar sutartis galioja paskutinio rinkinio atnaujinimo metu | — |
| `duomenu_atnaujinimas` | `datetime` | `S` | `4` | `open` | — | Sutarties duomenų atnaujinimo data | — |
| `sutarties_nr` | `string` | — | `4` | `open` | — | Sutarties registracijos numeris | — |
| `sutarties_objektas` | `string` | — | `4` | `open` | — | Sutarties objekto pavadinimas | — |
| `verte_eur` | `number` | — | `4` | `open` | — | Sutarties vertė, nurodyta eurais | — |
| `sutarties_tipas` | `string` | — | `4` | `open` | — | Sutarties tipas | — |
| `pirkimo_budas` | `string` | — | `4` | `open` | — | Viešojo pirkimo konkurse skelbto pirkimo būdas | — |
| `pirkimo_nr` | `string` | — | `4` | `open` | — | Viešojo pirkimo numeris | — |
| `bvpz_kodas` | `string` | — | `4` | `open` | — | Bendrojo viešųjų pirkimų žodyno kodas, naudotas viešajam pirkimui | — |
| `bvpz_pavadinimas` | `string` | — | `4` | `open` | — | Bendrojo viešųjų pirkimų žodyno kodo aprašumas, naudotas viešajam pirkimui | — |
| `tiekeju_grupe` | `string` | — | `4` | `open` | — | Nurodoma tiekėjų grupė, jeigu sutartį pasirašė keli tiekėjai | — |
| `tiekejas` | `string` | — | `4` | `open` | — | Tiekėjo pavadinimas | — |
| `tiekejo_jar` | `string` | — | `4` | `open` | — | Tiekėjo juridinio asmens kodas | — |
| `tiekejo_valstybe` | `string` | — | `4` | `open` | — | Tiekėjo valstybės pavadinimas | — |
| `tiek_adresas` | `string` | — | `4` | `open` | — | Tiekėjo adresas | — |
| `po` | `string` | — | `4` | `open` | — | Perkančiosios organizacijos pavadinimas | Perkančioji organizacija maitinimui organizuoti gali būti ne tik mokykla, bet ir savivaldybė. |
| `po_jar` | `string` | — | `4` | `open` | — | Perkančiosios organizacijos juridinio asmens kodas | — |
| `po_adresas` | `string` | — | `4` | `open` | — | Perkančiosios organizacijos adresas | — |
| `po_geometrija` | `geometry(3346)` | — | `4` | `open` | — | Perkančiosios organizacijos vietos koordinatės (LKS) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tiekejo_valstybe` | `"Lietuva"` | — | — | — | — |
| `tiekejo_valstybe` | `"Lenkija"` | — | — | — | — |
| `tiekejo_valstybe` | `"Slovėnija"` | — | — | — | — |
| `tiekejo_valstybe` | `"Latvija"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/vpt/maitinimo_sutartys.csv
