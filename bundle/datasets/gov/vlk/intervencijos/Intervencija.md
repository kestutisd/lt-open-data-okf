---
type: Table
title: "Intervencija — Medicininės intervencijos, atliktos taikant stacionarinį gydymą ar teikiant dienos chirurgijos paslaugas"
description: "Spinta table datasets/gov/vlk/intervencijos/Intervencija (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vlk/intervencijos/Intervencija"
tags: [gov, vlk, intervencija, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/intervencijos.csv#L19"
    title: "atviriduomenys/manifest — datasets/gov/vlk/intervencijos.csv#L19"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1509/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/intervencijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Intervencija — Medicininės intervencijos, atliktos taikant stacionarinį gydymą ar teikiant dienos chirurgijos paslaugas

- **Model:** `datasets/gov/vlk/intervencijos/Intervencija`[^manifest]
- **Dataset:** [Medicininės intervencijos, atliktos taikant stacionarinį gydymą ar teikiant dienos chirurgijos...](../intervencijos.md) (`datasets/gov/vlk/intervencijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/intervencijos.csv#L19](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/intervencijos.csv#L19)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/intervencijos/Intervencija` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ad_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `ref_sp_episode_id` | `ref` | [Etapas](Etapas.md) (`level=4 UUID`: `ref_sp_episode_id._id`) | `4` | `open` | — | Nuoroda į Etapas | Etapo unikalus numeris |
| `ref_sp_intervention_id` | `ref` | [Intervencija](../achi/Intervencija.md) (`level=4 UUID`: `ref_sp_intervention_id._id`) | `4` | `open` | — | ACHI kodas | Procedūros (ACHI) kodas pagal Australijos medicininių intervencijų klasifikaciją |
| `pagr_intervencija` | `integer` | — | `4` | `open` | — | Pagrindinė intervencija | Nurodoma ar intervencija etape pažymėta, kaip pagrindinė |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/intervencijos.csv#L19 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/intervencijos.csv#L19)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/intervencijos (https://data.gov.lt/datasets/1509/)
