---
type: Table
title: "VietovesAugalas — Vietovės dirvožemio augalai"
description: "Informacija apie Lietuvos teritorijos vietovėse, kuriose Gamtos Tyrimų Centro moksliniai darbuotojai tiria dirvožemio temperatūrą ir drėgmę, augalus augančius."
resource: "https://get.data.gov.lt/datasets/gov/gtc/dirvozemio_temperatura/VietovesAugalas"
tags: [gov, gtc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/gtc/dirvozemio_temperatura.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/gtc/dirvozemio_temperatura.csv#L24"
    last_modified: "2026-11-11T14:39:20Z"
---

# VietovesAugalas — Vietovės dirvožemio augalai

Informacija apie Lietuvos teritorijos vietovėse, kuriose Gamtos Tyrimų Centro moksliniai darbuotojai tiria dirvožemio temperatūrą ir drėgmę, augalus augančius.

- **Model:** `datasets/gov/gtc/dirvozemio_temperatura/VietovesAugalas`[^manifest]
- **Dataset:** [Dirvožemio temperatūra ir drėgmė bei dirvožemyje augantys augalai](../dirvozemio_temperatura.md) (`datasets/gov/gtc/dirvozemio_temperatura`)
- **Manifest CSV:** [datasets/gov/gtc/dirvozemio_temperatura.csv#L24](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/gtc/dirvozemio_temperatura.csv#L24)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/gtc/dirvozemio_temperatura/VietovesAugalas`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Įrašo unikalus identifikatorius | — |
| `vietoves_registratoriaus_id` | `string` | — | `4` | `open` | — | Vietovės registratoriaus identifikatorius | — |
| `augalo_pavadinimas_la` | `string` | — | `4` | `open` | — | Augalo pavadinimas lotynų kalba | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `augalo_pavadinimas_la` | `update(property: "augalo_pavadinimas@la", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/gtc/dirvozemio_temperatura.csv
