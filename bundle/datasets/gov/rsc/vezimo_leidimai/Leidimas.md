---
type: Table
title: "Leidimas — Vežimo leidimai"
description: "Spinta table datasets/gov/rsc/vezimo_leidimai/Leidimas (15 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rsc/vezimo_leidimai/Leidimas"
tags: [gov, rsc, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rsc/vezimo_leidimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/vezimo_leidimai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Leidimas — Vežimo leidimai

- **Model:** `datasets/gov/rsc/vezimo_leidimai/Leidimas`[^manifest]
- **Dataset:** [datasets/gov/rsc/vezimo_leidimai](../vezimo_leidimai.md) (`datasets/gov/rsc/vezimo_leidimai`)
- **Manifest CSV:** [datasets/gov/rsc/vezimo_leidimai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/vezimo_leidimai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rsc/vezimo_leidimai/Leidimas`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `leid_nr` | `string` | — | `4` | `open` | — | Vežimo leidimo numeris | — |
| `isduota` | `date` | `D` | `4` | `open` | — | Vežimo leidimo išdavimo data | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Vežimo leidimo galiojimo data | — |
| `galiojimas` | `string` | — | `4` | `open` | — | Vežimo leidimų galiojimo statusas | — |
| `turetojo_kodas` | `string` | — | `1` | `open` | — | Radioaktyviųjų medžiagų turėtojo juridinio asmens kodas | — |
| `turetojas` | `string` | — | `1` | `open` | — | Radioaktyviųjų medžiagų turėtojo pavadinimas | — |
| `turetojo_koord` | `geometry(point, 4326)` | — | `3` | `open` | — | Juridinio asmens koordinatės | — |
| `vezejo_kodas` | `string` | — | `1` | `open` | — | Radioaktyviųjų medžiagų vežėjo juridinio asmens kodas | — |
| `vezejas` | `string` | — | `1` | `open` | — | Radioaktyviųjų medžiagų vežėjo pavadinimas | — |
| `gavejo_kodas` | `string` | — | `1` | `open` | — | Radioaktyviųjų medžiagų gavėjo juridinio asmens kodas | — |
| `gavejas` | `string` | — | `1` | `open` | — | Radioaktyviųjų medžiagų gavėjo pavadinimas | — |
| `gavejo_koord` | `geometry(point, 3346)` | — | `3` | `open` | — | Juridinio asmens koordinatės | — |
| `krovinio_rus_id` | `string` | — | `4` | `open` | — | Krovinio rūšies identifikatorius | — |
| `leid_tipo_id` | `string` | — | `4` | `open` | — | Vežimo leidimo tipo identifikatorius | — |
| `leid_rus_id` | `string` | — | `4` | `open` | — | Leidimo rūšies identifikatorius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `galiojimas` | `"galioja"` | — | — | Leidimas galioja | — |
| `galiojimas` | `"negalioja"` | — | — | Leidimas negalioja | — |
| `krovinio_rus_id` | `"1"` | — | — | Radioaktyviosios medžiagos | — |
| `krovinio_rus_id` | `"2"` | — | — | Radioaktyviosios atliekos | — |
| `leid_tipo_id` | `"1"` | — | — | Lietuvoje | — |
| `leid_tipo_id` | `"2"` | — | — | Tarp ES narių | — |
| `leid_tipo_id` | `"3"` | — | — | Tarp ne ES narių | — |
| `leid_rus_id` | `"1"` | — | — | Vienkartinis | — |
| `leid_rus_id` | `"2"` | — | — | Daugkartinis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rsc/vezimo_leidimai.csv
