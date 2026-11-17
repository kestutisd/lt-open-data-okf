---
type: Table
title: "Tyrimas — Tyrimai"
description: "Spinta table datasets/gov/aaa/oro_monitoringo_matavimai/Tyrimas (15 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/oro_monitoringo_matavimai/Tyrimas"
tags: [gov, aaa, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/oro_monitoringo_matavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_monitoringo_matavimai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Tyrimas — Tyrimai

- **Model:** `datasets/gov/aaa/oro_monitoringo_matavimai/Tyrimas`[^manifest]
- **Dataset:** [datasets/gov/aaa/oro_monitoringo_matavimai](../oro_monitoringo_matavimai.md) (`datasets/gov/aaa/oro_monitoringo_matavimai`)
- **Manifest CSV:** [datasets/gov/aaa/oro_monitoringo_matavimai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_monitoringo_matavimai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/oro_monitoringo_matavimai/Tyrimas`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tad_laikotarpis_nuo` | `date` | `D` | `4` | `open` | — | Tyrimo laikotarpis nuo | — |
| `tad_laikotarpis_iki` | `date` | `D` | `4` | `open` | — | Tyrimo laikotarpis iki | — |
| `tad_tiriamas_objektas` | `string` | — | `3` | `open` | — | Tiriamas objektas | — |
| `tad_gis_taskas` | `geometry(point, 3346)` | — | `3` | `open` | — | Tyrimo vieta | — |
| `tsd_tyrimo_tipas` | `string` | — | `3` | `open` | — | Tyrimo sudedamosios tipas | CHE - Cheminiai tyrimai |
| `trz_neapibr` | `number` | — | `3` | `open` | — | Parametras, apibrėžiantis tyrimo rezultato tikslumą | — |
| `trz_rez_skaitinis` | `number` | — | `3` | `open` | — | Skaitinis tyrimo rezultatas | — |
| `mvn_kodas` | `string` | — | `3` | `open` | — | Matavimo vieneto kodas | — |
| `mvn_pavad` | `string` | — | `3` | `open` | — | Matavimo vieneto pavadinimas | — |
| `ptm_kodas` | `string` | — | `2` | `open` | — | Parametro kodas | Gali būti sutrumpintas parametro pavadinimas |
| `ptm_pavad` | `string` | — | `2` | `open` | — | Parametro pavadinimas | Matavimo vienetai švinui - µg/m3 (mikrogramai), kitiems – ng/m3 (nanogramai) |
| `mtd_standartas` | `string` | — | `2` | `open` | — | Standartas, reglamentuojantis tyrimo atlikimą. | — |
| `mtd_metodo_principas` | `string` | — | `2` | `open` | — | Principo, kuriuo pagrįstas metodas, įvardinimas | — |
| `vkl_pavad` | `string` | — | `3` | `open` | — | Veiklos pavadinimas | — |
| `ttr_pavad` | `string` | — | `4` | `open` | — | Tyrimų terpės pavadinimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ttr_pavad` | `"Aplinkos oras"` | — | — | Aplinkos oras | — |
| `ttr_pavad` | `"Išorinė spinduliuotė"` | — | — | Išorinė spinduliuotė | — |
| `ttr_pavad` | `"Aerozolinis filtras (stiklo pluošto)"` | — | — | Aerozolinis filtras (stiklo pluošto) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/oro_monitoringo_matavimai.csv
