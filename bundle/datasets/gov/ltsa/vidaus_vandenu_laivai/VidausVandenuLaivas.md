---
type: Table
title: "VidausVandenuLaivas — Vidaus vandenų laivai"
description: "Spinta table datasets/gov/ltsa/vidaus_vandenu_laivai/VidausVandenuLaivas (19 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/vidaus_vandenu_laivai/VidausVandenuLaivas"
tags: [gov, ltsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ltsa/vidaus_vandenu_laivai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/vidaus_vandenu_laivai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# VidausVandenuLaivas — Vidaus vandenų laivai

- **Model:** `datasets/gov/ltsa/vidaus_vandenu_laivai/VidausVandenuLaivas`[^manifest]
- **Dataset:** [datasets/gov/ltsa/vidaus_vandenu_laivai](../vidaus_vandenu_laivai.md) (`datasets/gov/ltsa/vidaus_vandenu_laivai`)
- **Manifest CSV:** [datasets/gov/ltsa/vidaus_vandenu_laivai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/vidaus_vandenu_laivai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/vidaus_vandenu_laivai/VidausVandenuLaivas`
- **Primary Key (`ref`):** `ship_id,own_le`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ship_call_sign` | `string` | — | `4` | `open` | — | Laivo šaukiniai | — |
| `own_le` | `string` | — | `2` | `open` | — | Savininkas JA | Savininko juridinio asmens kodas |
| `shipyard_location` | `string` | — | `4` | `open` | — | Laivo statybos vieta | — |
| `ship_constructed` | `string` | — | `2` | `open` | — | Laivo pastatymo metai | — |
| `created` | `string` | — | `2` | `open` | — | Įrašo sukūrimo data | — |
| `ship_freeboard` | `string` | — | `2` | `open` | — | Minimalus borto aukštis virš vandens | — |
| `ship_height` | `string` | — | `2` | `open` | — | Laivo gabaritinis aukštis | — |
| `ship_hull_material` | `string` | — | `3` | `open` | — | Laivo korpuso medžiaga | — |
| `ship_length` | `string` | — | `2` | `open` | — | Laivo gabaritinis ilgis | — |
| `ship_max_drght` | `string` | — | `2` | `open` | — | Laivo grimzlė | — |
| `ship_net_tg` | `string` | — | `2` | `open` | — | Laivo grynoji talpa | — |
| `ship_max_psg` | `string` | — | `2` | `open` | — | Laivo keleivių skaičius | — |
| `ship_recon` | `string` | — | `2` | `open` | — | Laivo rekonstrukcijos metai | — |
| `ship_brand` | `string` | — | `4` | `open` | — | Laivo markė | — |
| `ship_type` | `string` | — | `3` | `open` | — | Laivo tipas | — |
| `ship_use` | `string` | — | `3` | `open` | — | Laivo paskirtis | — |
| `shipyard_title` | `string` | — | `2` | `open` | — | Statyklos pavadinimas | — |
| `ship_id` | `string` | — | `4` | `open` | — | Laivo ID | — |
| `ship_width` | `string` | — | `2` | `open` | — | Laivo gabaritinis plotis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/vidaus_vandenu_laivai.csv
