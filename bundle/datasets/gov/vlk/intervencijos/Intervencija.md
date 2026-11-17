---
type: Table
title: "Intervencija — Medicininės intervencijos, atliktos taikant stacionarinį gydymą ar teikiant dienos chirurgijos paslaugas"
description: "Spinta table datasets/gov/vlk/intervencijos/Intervencija (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vlk/intervencijos/Intervencija"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/intervencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/intervencijos.csv#L19"
    last_modified: "2026-11-11T14:39:20Z"
---

# Intervencija — Medicininės intervencijos, atliktos taikant stacionarinį gydymą ar teikiant dienos chirurgijos paslaugas

- **Model:** `datasets/gov/vlk/intervencijos/Intervencija`[^manifest]
- **Dataset:** [datasets/gov/vlk/intervencijos](../intervencijos.md) (`datasets/gov/vlk/intervencijos`)
- **Manifest CSV:** [datasets/gov/vlk/intervencijos.csv#L19](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/intervencijos.csv#L19)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/intervencijos/Intervencija`
- **Primary Key (`ref`):** `ad_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `ref_sp_episode_id` | `ref` | [Etapas](Etapas.md) | `4` | `open` | — | Nuoroda į Etapas | Etapo unikalus numeris |
| `ref_sp_intervention_id` | `ref` | [/datasets/gov/vlk/achi/Intervencija](../achi/Intervencija.md) | `4` | `open` | — | ACHI kodas | Procedūros (ACHI) kodas pagal Australijos medicininių intervencijų klasifikaciją |
| `pagr_intervencija` | `integer` | — | `4` | `open` | — | Pagrindinė intervencija | Nurodoma ar intervencija etape pažymėta, kaip pagrindinė |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/intervencijos.csv
