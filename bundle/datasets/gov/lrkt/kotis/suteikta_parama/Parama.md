---
type: Table
title: "Parama — Suteiktos valstybės pagalbos ir nereikšmingos (de minimis) pagalbos registro duomenys"
description: "Spinta table datasets/gov/lrkt/kotis/suteikta_parama/Parama (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lrkt/kotis/suteikta_parama/Parama"
tags: [gov, lrkt, parama, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrkt/suteikta_parama.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lrkt/suteikta_parama.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3803/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrkt/kotis/suteikta_parama"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Parama — Suteiktos valstybės pagalbos ir nereikšmingos (de minimis) pagalbos registro duomenys

- **Model:** `datasets/gov/lrkt/kotis/suteikta_parama/Parama`[^manifest]
- **Dataset:** [Suteiktos valstybės pagalbos ir nereikšmingos (de minimis) pagalbos registro duomenys](../suteikta_parama.md) (`datasets/gov/lrkt/kotis/suteikta_parama`)[^manifest]
- **Manifest CSV:** [datasets/gov/lrkt/suteikta_parama.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrkt/suteikta_parama.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrkt/kotis/suteikta_parama/Parama` (`deployed`)[^manifest]
- **Provider:** `lrkt` — Lietuvos Respublikos Konkurencijos Taryba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `paramos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paramos_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `paramos_suma` | `number` | — | `4` | `open` | — | Suteiktos paramos suma | — |
| `paramos_gavimo_data` | `date` | `D` | `4` | `open` | — | Paramos gavimo data | — |
| `paramos_tipas` | `string` | — | `4` | `open` | — | Paramos tipas | — |
| `paramos_tipo_pavad` | `string` | — | `4` | `open` | — | Pilnas paramos tipo pavadinimas | — |
| `teisinis_pagrindas` | `string` | — | `4` | `open` | — | Paramos gavimo teisinis pagrindas | — |
| `prasymo_busena` | `string` | — | `4` | `open` | — | Prašymo gauti paramą būsena | — |
| `gavejas` | `string` | — | `4` | `open` | — | Paramos gavėjas | — |
| `gavejo_tipas` | `string` | — | `4` | `open` | — | Paramos gavėjo tipas | — |
| `ar_gavej_uzsieniet` | `boolean` | — | `4` | `open` | — | Požymis ar paramos gavėjas užsienietis | — |
| `gavejo_kodas` | `string` | — | `4` | `open` | — | Paramos gavėjo kodas | — |
| `atnaujinimo_data` | `date` | `D` | `4` | `open` | — | Duomenų atnaujinimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrkt/suteikta_parama.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrkt/suteikta_parama.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrkt/kotis/suteikta_parama (https://data.gov.lt/datasets/3803/)
