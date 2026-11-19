---
type: Table
title: "VidausVandenuLaivas — Vidaus vandenų laivai"
description: "Spinta table datasets/gov/ltsa/vidaus_vandenu_laivai/VidausVandenuLaivas (19 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/vidaus_vandenu_laivai/VidausVandenuLaivas"
tags: [gov, ltsa, vidausvandenulaivas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/vidaus_vandenu_laivai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/ltsa/vidaus_vandenu_laivai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2091/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ltsa/vidaus_vandenu_laivai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# VidausVandenuLaivas — Vidaus vandenų laivai

- **Model:** `datasets/gov/ltsa/vidaus_vandenu_laivai/VidausVandenuLaivas`[^manifest]
- **Dataset:** [Vidaus vandenų laivų duomenys](../vidaus_vandenu_laivai.md) (`datasets/gov/ltsa/vidaus_vandenu_laivai`)[^manifest]
- **Manifest CSV:** [datasets/gov/ltsa/vidaus_vandenu_laivai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/vidaus_vandenu_laivai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/vidaus_vandenu_laivai/VidausVandenuLaivas` (`deployed`)[^manifest]
- **Provider:** `ltsa` — Lietuvos transporto saugos administracija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ship_id,own_le`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/vidaus_vandenu_laivai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/vidaus_vandenu_laivai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ltsa/vidaus_vandenu_laivai (https://data.gov.lt/datasets/2091/)
