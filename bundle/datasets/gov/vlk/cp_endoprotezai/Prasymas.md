---
type: Table
title: "Prasymas — Endoprotezavimo prašymų lentelė"
description: "Endoprotezavimo prašymų lentelė"
resource: "https://get.data.gov.lt/datasets/gov/vlk/cp_endoprotezai/Prasymas"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/cp_endoprotezai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/cp_endoprotezai.csv#L28"
    last_modified: "2026-11-11T14:39:20Z"
---

# Prasymas — Endoprotezavimo prašymų lentelė

Endoprotezavimo prašymų lentelė

- **Model:** `datasets/gov/vlk/cp_endoprotezai/Prasymas`[^manifest]
- **Dataset:** [datasets/gov/vlk/cp_endoprotezai](../cp_endoprotezai.md) (`datasets/gov/vlk/cp_endoprotezai`)
- **Manifest CSV:** [datasets/gov/vlk/cp_endoprotezai.csv#L28](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/cp_endoprotezai.csv#L28)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/cp_endoprotezai/Prasymas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `operacijos_tipo_id` | `ref` | [Tipas](Tipas.md) | `4` | `open` | — | Nuoroda į Tipas | Operacijos tipo unikalus numeris |
| `protezo_tipo_id` | `ref` | [ProtezoTipas](ProtezoTipas.md) | `4` | `open` | — | Nuoroda į ProtezoTipas | Endoprotezo tipo unikalus numeris |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/cp_endoprotezai.csv
