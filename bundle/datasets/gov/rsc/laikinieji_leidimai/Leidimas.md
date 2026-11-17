---
type: Table
title: "Leidimas — Laikinieji leidimai vykdyti veiklą su jonizuojančiosios spinduliuotės šaltiniais"
description: "Spinta table datasets/gov/rsc/laikinieji_leidimai/Leidimas (15 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rsc/laikinieji_leidimai/Leidimas"
tags: [gov, rsc, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rsc/laikinieji_leidimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/laikinieji_leidimai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Leidimas — Laikinieji leidimai vykdyti veiklą su jonizuojančiosios spinduliuotės šaltiniais

- **Model:** `datasets/gov/rsc/laikinieji_leidimai/Leidimas`[^manifest]
- **Dataset:** [datasets/gov/rsc/laikinieji_leidimai](../laikinieji_leidimai.md) (`datasets/gov/rsc/laikinieji_leidimai`)
- **Manifest CSV:** [datasets/gov/rsc/laikinieji_leidimai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/laikinieji_leidimai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rsc/laikinieji_leidimai/Leidimas`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `leid_nr` | `string` | — | `4` | `open` | — | Laikinojo leidimo numeris | — |
| `isduota` | `date` | `D` | `4` | `open` | — | Laikinojo leidimo išdavimo data | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Laikinojo leidimo galiojimo pabaigos data | — |
| `busena` | `string` | — | `4` | `open` | — | Laikinojo leidimo būsenos pavadinimas | — |
| `galiojimas` | `string` | — | `4` | `open` | — | Laikinojo leidimo galiojimo statusas | — |
| `paslauga` | `string` | — | `3` | `open` | — | Laikinojo leidimo paslaugos pavadinimas | — |
| `turetojo_kodas` | `string` | — | `1` | `open` | — | Laikinojo leidimo turėtojo juridinis kodas | — |
| `turetojas` | `string` | — | `1` | `open` | — | Turėtojo pavadinimas | — |
| `turetojo_uzs_adr` | `string` | — | `1` | `open` | — | Adresas užsienio šalyse | — |
| `turetojo_salis` | `string` | — | `4` | `open` | — | Valstybės pavadinimas | — |
| `turetojo_koord` | `geometry(point, 4326)` | — | `3` | `open` | — | Juridinio asmens koordinatės užsienio šalyse | — |
| `gavejo_kodas` | `string` | — | `2` | `open` | — | Laikinojo leidimo gavėjo juridinis kodas | — |
| `gavejas` | `string` | — | `1` | `open` | — | Gavėjo pavadinimas | — |
| `gavejo_salis` | `string` | — | `4` | `open` | — | Valstybės pavadinimas | — |
| `gavejo_koord` | `geometry(point, 3346)` | — | `3` | `open` | — | Leidimą gaunančio juridinio asmens koordinatės | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `busena` | `"Neišduotas"` | — | — | Neišduotas | — |
| `busena` | `"Išduotas"` | — | — | Išduotas | — |
| `galiojimas` | `"galioja"` | — | — | Leidimas galioja | — |
| `galiojimas` | `"negalioja"` | — | — | Leidimas negalioja | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gavejo_kodas` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `base` | `4` | `open` | — | — | — |
| `gavejo_kodas` | `update(type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rsc/laikinieji_leidimai.csv
