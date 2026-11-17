---
type: Table
title: "Gavejas — Duomenys apie socialinės pašalpos gavėjus"
description: "Spinta table datasets/gov/sadm/charakteristikos/Gavejas (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/sadm/charakteristikos/Gavejas"
tags: [gov, sadm, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/sadm/charakteristikos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/charakteristikos.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Gavejas — Duomenys apie socialinės pašalpos gavėjus

- **Model:** `datasets/gov/sadm/charakteristikos/Gavejas`[^manifest]
- **Dataset:** [datasets/gov/sadm/charakteristikos](../charakteristikos.md) (`datasets/gov/sadm/charakteristikos`)
- **Manifest CSV:** [datasets/gov/sadm/charakteristikos.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/charakteristikos.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sadm/charakteristikos/Gavejas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Įrašo identifikatorius | — |
| `seimos_tipas` | `string` | — | `3` | `open` | — | Šeimos tipo identifikatorius | — |
| `sei_nariai` | `integer` | `U` | `4` | `open` | — | Asmenų, priklausančių šeimai, skaičius | — |
| `metai` | `integer` | — | `2` | `open` | — | Prašymo teikimo metai | — |
| `pasalpa` | `string` | — | `2` | `open` | — | Pašalpos tipas | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Gavėjo asmens amžiaus grupė | — |
| `lytis` | `string` | — | `3` | `open` | — | Gavėjo asmens lytis | — |
| `bedarbe` | `boolean` | — | `3` | `open` | — | Bedarbė šeima | Požymis ar šeimoje yra bedarbių |
| `darb_aktyvumas` | `string` | — | `3` | `open` | — | Gavėjo darbo aktyvumo identifikatorius | — |
| `soc_rizika` | `boolean` | — | `3` | `open` | — | Požymis ar šeimoje yra asmenų, priklausančių soc. rizikos įskaitai | — |
| `iskait_priezastis` | `string` | — | `3` | `open` | — | Šeimos įtraukimo į soc. riziką priežastis | — |
| `busto_bukle` | `string` | — | `3` | `open` | — | Busto turėjimo aplinkybių identifikatorius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "metai", ref: "Y")` | `type` | `4` | — | — | — | — |
| `pasalpa` | `"update(property: ""pasalpa[]"", type: ""array"", source: ""Pasalpa"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sadm/charakteristikos.csv
